"""

# RelianceInheritance.py

## Inheritance

### Constructors
* init: sourceDocument (RelianceDocument), targetDocument (RelianceDocument)

### Methods
* copy: sourceFieldName (String), targetFieldName (String)

"""

class Inheritance:

	# Constructors

	def __init__(self,sourceDocument,targetDocument=None):
		if not targetDocument:
			targetDocument=sourceDocument
		self._sourceDocument=sourceDocument
		self._targetDocument=targetDocument

	# Methods

	def copy(self,sourceFieldName,targetFieldName=None):
		if not targetFieldName:
			targetName=sourceFieldName
		sourceField=self._sourceDocument.getField(sourceFieldName)
		targetField=self._targetDocument.getField(targetFieldName)
		settings=targetField.getSetting()
		type=settings.getFieldType()
		if sourceField.getSetting().getFieldType()==type:
			if type in [PublicFieldSetting.FIELD_TYPE_ATTACHMENT,PublicFieldSetting.FIELD_TYPE_LINK]:
				targetField.copy(sourceField)
			else:
				if settings.isMultiValue():
					targetField.setValues(sourceField.getValues())
				else:
					targetField.setValue(sourceField.getValue())
		else:
			if settings.isMultiValue():
				targetField.setValues(sourceField.getValues())
			else:
				targetField.setValue(sourceField.getDisplayText())
