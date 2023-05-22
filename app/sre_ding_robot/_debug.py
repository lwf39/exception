class Debugger():
	def __init__(self):
		pass

	@staticmethod
	def printRsp(rsp):
		print('rsp.status_code: %s' % rsp.status_code)
		print('rsp.content: %s' % rsp.content)