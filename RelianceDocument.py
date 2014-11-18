"""

# RelianceDocument.py

## Document

### Constants
* FIELD_PARENT_FORM: String
* FIELD_PARENT_ID: String
* FIELD_PARENT_WORKFLOW: String

### Constructors
* init: application (RelianceApplication), document (RelianceDocument)

### Methods
* _secure: field (String), userids (List), usernames (List)
* _secureEditors
* _secureManagers
* _secureReaders
* inherit
* secure
* validate

"""

class Document:

	# Constants

	FIELD_PARENT_FORM="APPLICATION_FORM_PARENT_FORM"
	FIELD_PARENT_ID="APPLICATION_FORM_PARENT_ID"
	FIELD_PARENT_WORKFLOW="APPLICATION_FORM_PARENT_WORKFLOW"

	# Constructors

	def __init__(self,application,document):
		self._application=application
		self._document=document
		self.toolkit=Toolkit()

	# Methods

	def _secure(self,field,userids,usernames):
		if not usernames==[]:
			userids.extend(self.toolkit.getUserIdsByUsernames(usernames))
		if DEBUG:self._document.addError(Rlist.toString(userids))
		self._document.setFieldValues(field,userids)

	def _secureEditors(self):
		userids=[]
		#!!! Append/extend with userids
		usernames=[]
		#!!! Append/extend with usernames
		self._secure(FIELD_SYSTEM_EDITORS,userids,usernames)

	def _secureManagers(self):
		userids=[]
		#!!! Append/extend with userids
		usernames=[]
		#!!! Append/extend with usernames
		self._secure(FIELD_SYSTEM_MANAGERS,userids,usernames)

	def _secureReaders(self):
		userids=[]
		#!!! Append/extend with userids
		usernames=[]
		#!!! Append/extend with usernames
		self._secure(FIELD_SYSTEM_READERS,userids,usernames)

	def inherit(self):
		isParentDocumentOpened=self._document.isParentDocumentOpened()
		parent=self._document.getParentDocument()
		if parent:
			self._document.setFieldValue(self.FIELD_PARENT_FORM,parent.getFormName())
			self._document.setFieldValue(self.FIELD_PARENT_ID,parent.getID())
			self._document.setFieldValue(self.FIELD_PARENT_WORKFLOW,parent.getPhase().getWorkflowDesignName())
			inheritance=Inheritance(parent,self._document)
			inheritance.copy("SOURCE_FIELD_NAME","TARGET_FIELD_NAME")
			if not isParentDocumentOpened:
				parent.close()

	def initiate(self):
		self._document.setFieldValue("FIELD_NAME","FIELD_VALUE")

	def secure(self):
		self._secureEditors()
		self._secureManagers()
		self._secureReaders()

	def validate(self):
		return
