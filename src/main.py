import json
import __builtin__
import inspect
import types

class main(object):
	"""dump build_in_functions"""
	def __init__(self):
		super(main, self).__init__()
	
	def dumpBuildInFunctions(self):
		docUrl = "https://docs.python.org/2/library/functions.html#%s"
		functions = [name for name, function in sorted(vars(__builtin__).items()) \
 				if inspect.isbuiltin(function) or inspect.isfunction(function)]
		open('build_in_functions.json', 'w').write(json.dumps(functions))

	def dumpBuildInTypes(self):
		typeList = [t for t in vars(types)  ]
		print typeList
		open('build_in_types.json', 'w').write(json.dumps(typeList))
		
	def generateHtml(self):
		pass

if __name__ == '__main__':
	main = main()
	# help(main)
	# main.dumpBuildInFunctions()
	main.dumpBuildInTypes()