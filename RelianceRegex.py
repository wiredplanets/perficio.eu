"""

# RelianceRegex.py

## Regex

### Constants
* REGEX_EXPRESSION_TELEPHONE: String
* REGEX_EXCEPTION_TELEPHONE: String

### Methods
* evaluate: field (String), format (String)

"""

class Regex:

	# Constants

	REGEX_EXPRESSION_TELEPHONE="\\([1-9]\\d{2}\\)+-[1-9]\\d{2}-\\d{4}"
	REGEX_EXCEPTION_TELEPHONE="Invalid format for Telephone. Expected (999)-999-999."

	# Methods

	def evaluate(self,arguments,field,format):
		from java.lang import String
		flag=true
		values=field.getValues()
		for value in values:
			argument=String(value)
			arguments.append(argument)
			if not argument.matches(format):
				flag=false
		return flag
