from sre_ding_robot.alert import AlertRobot
class Ding_ding():
    def __init__(self,txt):
        self.url = 'http://ops.h3yun.com:30001/dingrobotapi'
        self.txt = txt
        self.title = '新增异常'
    def ding_proxy(self,exceptioncontent):
        # * 创建报警Robot
        robot = AlertRobot(title=self.title, url=self.url)
        # * 发送报警
        rsp = robot.alert(endpoint='NewExceptionContent', metric='新增异常', trigger=exceptioncontent, desc=self.txt)

        # * 正常返回rsp -- requests.post()返回的Response对象
        return 200