"""

# RelianceForum.py

## Forum

### Constants
* THREAD_APPEND: Boolean

### Constructors
* init: document (RelianceDocument), subform (RelianceSubform), user (RelianceUser)

### Methods
* add: fields (dictionary)

"""

class Forum():

	# Constants

	THREAD_APPEND=true

	# Constructors

	def __init__(self,document,subform,user):
		self._document=document
		self._subform=subform
		self._user=user

	# Methods

	def add(self,fields):
		attachment=self._document.getField(fields["ThreadAttachment"])
		comment=self._document.getField(fields["ThreadMessage"])
		if comment.getValue() or attachment.getValues():
			if self.THREAD_APPEND:
				record=self._subform.newRecord()
			else:
				record=self._subform.newRecord(0)
			record.getField(fields["ForumAttachment"]).copy(attachment)
			discussion=Discussion(record.getField(fields["ForumMessage"]),self._user)
			discussion.add(comment.getValue())
			attachment.clear()
			comment.clear()
