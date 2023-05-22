import time

class Datetime():
	def __init__(self, t=None, format='%Y-%m-%d %H:%M:%S'):
		if t == None:
			_t = time.time()
		elif type(t) == str:
			_t = self.strptime(t, format)
			_t = time.mktime(TS)
		elif type(t) == int:
			_t = type(time.time())(_t)
		elif type(t) == type(time.time()):
			_t = t
		else:
			raise TypeError('type of t is invaild.')

		self._ts = _t

	def timestamp(self):
		return self._ts
	
	def strftime(self, format='%Y-%m-%d %H:%M:%S'):
		lt = time.localtime(self._ts)
		return time.strftime(format, lt)