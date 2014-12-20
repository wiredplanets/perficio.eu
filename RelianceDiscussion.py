"""

# RelianceDiscussion.py

## Discussion

### Constants
* THREAD_APPEND: Boolean
* THREAD_STAMP_FORMAT: String
* THREAD_STAMP_MONTHS: List

### Constructors
* init: field (RelianceField), user (RelianceUser)

### Methods
* _getExistingThread
* _getNewPost: message (String)
* add: message (String)

"""

class Discussion:

	# Constants

	THREAD_APPEND=true
	THREAD_STAMP_FORMAT="%(name)s, %(day)s-%(month)s-%(year)s %(time)s:"
	THREAD_STAMP_MONTHS=["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

	# Constuctors

	def __init__(self,field,user):
		self._field=field
		self._user=user

	# Methods

	def _getExistingThread(self):
		thread=self._field.getValue()
		if thread:
			arguments={"thread":thread,"line":Rstring.newLine()}
			if self.THREAD_APPEND:
				thread="%(thread)s%(line)s%(line)s"%arguments
			else:
				thread="%(line)s%(line)s%(thread)s"%arguments
		return thread

	def _getNewPost(self,message):
		now=Rdate.now()
		post=self.THREAD_STAMP_FORMAT%{"day":Rdate.getDay(now),"month":self.THREAD_STAMP_MONTHS[Rdate.getMonth(now)],"name":self._user.getDisplayName(),"time":Rdate.getTimeOnly(now,2,self._user),"year":Rdate.getYear(now)}
		post+=Rstring.newLine()
		post+=message
		return post

	def add(self,message):
		arguments={"post":self._getNewPost(message),"thread":self._getExistingThread()}
		if self.THREAD_APPEND:
			self._field.setValue("%(thread)s%(post)s"%arguments)
		else:
			self._field.setValue("%(post)s%(thread)s"%arguments)
