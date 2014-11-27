import json
import __builtin__
import inspect



class main(object):
	"""docstring for main"""
	def __init__(self):
		super(main, self).__init__()
	
	def dumpBuildInFunctions(self):
		functions = [name for name, function in sorted(vars(__builtin__).items()) \
 				if inspect.isbuiltin(function) or inspect.isfunction(function)]
		open('build_in_functions.json', 'w').write(json.dumps(functions))

		

if __name__ == '__main__':
	main = main()
	main.dumpBuildInFunctions()