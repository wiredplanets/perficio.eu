"""

# RelianceToolkit.py

## Toolkit

### Constants
* ABBREVIATE_TEXT_DELIMITER: Integer
* ABBREVIATE_TEXT_FORMAT: String
* ABBREVIATE_TEXT_LENGTH: Integer
* DEBUG_DATABASE_VENDOR: String
* DEBUG_HELLO_WORLD: String

### Methods
* abbreviateText: text (String)
* addDocumentLink: applicationName (String), document (RelianceDocument), documentId (Integer), fieldName (String), formName (String)		
* addSubformRecord: document (RelianceDocument), subformName (String)
* debugDatabaseVendor: document (RelianceDocument)
* debugHelloWorld: document (RelianceDocument)
* getUserIdsByUsernames: application (RelianceApplication), usernames (List)
* getWorkflowPhase: document (RelianceDocument)
* isGroupMember: group (String), id (Integer)

"""

class Toolkit:

	# Constants

	ABBREVIATE_TEXT_DELIMITER=3
	ABBREVIATE_TEXT_FORMAT="%(text)s..."
	ABBREVIATE_TEXT_LENGTH=50
	DEBUG_DATABASE_VENDOR="Debug Database Vendor %(vendor)s"
	DEBUG_HELLO_WORLD="Hello world"

	# Methods

	def abbreviateText(self,text):
		if Rstring.length(text)>self.ABBREVIATE_TEXT_DELIMITER:
			text=self.ABBREVIATE_TEXT_FORMAT%{"text":Rstring.left(self.ABBREVIATE_TEXT_LENGTH-self.ABBREVIATE_TEXT_DELIMITER,text)}
		return text

	def addDocumentLink(self,applicationName,document,documentId,fieldName,formName):		
		document.getField(fieldName).addDocLink(PublicDocLink.createDocLink(applicationName,formName,documentId))

	def addSubformRecord(self,document,subformName):
		document.getSubform(subformName).newRecord()

	def debugDatabaseVendor(self,document):
		document.addError(self.DEBUG_DATABASE_VENDOR%{"vendor":PublicEngineConfig.getEngineDatabaseVendor()})

	def debugHelloWorld(self,document):
		document.addError(self.DEBUG_HELLO_WORLD)

	def getUserIdsByUsernames(self,application,usernames):
		ids=[]
		select="SELECT USER_SETTINGS.USER_ID"
		select+=" FROM ENGINE.USER_SETTINGS"
		select+=" WHERE USER_SETTINGS.USER_NAME IN ('%(usernames)s')"%{"usernames":Rlist.toString(usernames,"','")}
		dao=application.executeQueryFromDatasource(DATASOURCE_NAME,{DATASOURCE_MAPPING:select})
		if dao:
			while dao.next():
				ids.append(dao.getValue("USER_ID"))
		return ids

	def getWorkflowPhase(self,document):
		phase=document.getPhase()
		if phase.isSendingBackward() or phase.isSendingForward():
			try:
				phase=phase.getNextPhase()
			except:
				phase=document.getPhase()
		return phase

	def isGroupMember(self,group,id):
		flag=false
		if id in PublicUserManager().convertToUsers([group]):
			flag=true
		return flag
