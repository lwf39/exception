class DingRobotError(Exception):
	pass


class DingStatusCodeError(DingRobotError):
	def __init__(self, rsp, msg='StatusCode of ding response is not 200.'):
		self.rsp = rsp
		self.msg = msg

	def __str__(self):
		return self.msg

class DingErrCodeError(DingRobotError):
	def __init__(self, rsp, msg='ErrCode of ding return is not 0.'):
		self.rsp = rsp
		self.msg = msg

	def __str__(self):
		return self.msg


class DingContentError(DingRobotError):
	def __init__(self, rsp, msg='Content of ding response is not a json.'):
		self.rsp = rsp
		self.msg = msg

	def __str__(self):
		return self.msg
