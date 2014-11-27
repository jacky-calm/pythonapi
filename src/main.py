import json
import __builtin__
import inspect

class main(object):
	"""docstring for main"""
	def __init__(self):
		super(main, self).__init__()
	
	def dumpBuildInFunctions(self):
		docUrl = "https://docs.python.org/2/library/functions.html#%s"
		functions = [name for name, function in sorted(vars(__builtin__).items()) \
 				if inspect.isbuiltin(function) or inspect.isfunction(function)]
		open('build_in_functions.json', 'w').write(json.dumps(functions))
		
	def generateHtml(self):
		pass

if __name__ == '__main__':
	main = main()
	main.dumpBuildInFunctions()