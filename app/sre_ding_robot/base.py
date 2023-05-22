import requests
import json
from .exceptions import DingStatusCodeError, DingErrCodeError

class DingRobot():
    """封装了最基本的钉钉机器人发消息接口 – text和markdown

    Parameters
    ----------
    url: str
        钉钉机器人的Webhook
    timeout: int, defaults to 7
        配置调用钉钉的连接超时和读取超时

    Attributes
    ----------
    url: str
        等于 param `url`
    timeout: int
        等于 param `timout`

    """
    def __init__(self, url, *, timeout=7):
        
        self.url = url
        self.headers = {
            'Content-Type': 'application/json'
        }
        self.timeout = timeout

    def send(self, data):
        """执行requests.port，调用钉钉接口

        Parameters
        ----------
        data: dict
            data的格式可参考钉钉开发文档

        Returns
        -------
        requests.models.Response
            rsp -- ``request.post()`` 返回的 ``Response``

        Raises
        ------
        DingStatusCodeError
            访问钉钉接口后，返回http状态码不为200。有可能是初始化类时，填错了Webhook地址；或钉钉服务端的错误；有时候也有可能是因为http网关层拦截了。

        DingContentError
            访问钉钉接口成功，但返回的不是json或不符合规范。有可能是初始化类时，填错了Webhook地址；或钉钉服务端的错误；或钉钉接口规范改了。

        DingErrCodeError
            访问钉钉接口成功，解析json也成功，但返回的errcode不为0。详情可查 `钉钉开发文档` 。

        """
        rsp = requests.post(self.url, headers=self.headers, data=json.dumps(data), timeout=self.timeout)
        _checkRsp(rsp)
        return rsp

    def sendText(self, content, *, atMobiles=[], isAtAll=False):
        """
        Parameters
        ----------
        content: str
            需要发送的内容

        atMobiles: list(int), defaults to [ ]
            list of 手机, 配合content，@特定某个人。详情请看 `Example` 或 `钉钉开发文档`

        isAtAll: bool, defaults to False
            用于@所有人. if True, @所有人; otherwise, nothing will happen. 详情请看 `Example` 或 `钉钉开发文档`

        Returns
        -------
        requests.models.Response
            rsp -- ``request.post()`` 返回的 ``Response``

        Raises
        ------
        TypeError
            当content类型不为str时触发

        ValueError
            当content值为空字符串时触发

        Others
            因为调用的 :meth:`send` 的接口，所以会有可能触发 :meth:`send` 的异常。详情请看 :meth:`send` 。
        """
        if type(content) is not str:
            raise TypeError('content is not a string')
        content = content.strip()
        if len(content) == 0:
            raise ValueError('content is null')

        data = {
            "msgtype": "text",
            "text": {
                "content": content
            },
            "at": {
                "atMobiles": atMobiles, 
                "isAtAll": isAtAll
            }
        }

        rsp = self.send(data)
        
        return rsp


    def sendMarkdown(self, title, text, *, atMobiles=[], isAtAll=False):
        """
        Parameters
        ----------
        content: str
            需要发送的内容

        atMobiles: list(int), defaults to [ ]
            list of 手机, 配合content，@特定某个人。详情请看 `Example` 或 `钉钉开发文档`

        isAtAll: bool, defaults to False
            用于@所有人. if True, @所有人; otherwise, nothing will happen. 详情请看 `Example` 或 `钉钉开发文档`

        Returns
        -------
        requests.models.Response
            rsp -- ``request.post()`` 返回的 ``Response``

        Raises
        ------
        TypeError
            当content类型不为str时触发

        ValueError
            当content值为空字符串时触发

        Others
            因为调用的 :meth:`send` 的接口，所以会有可能触发 :meth:`send` 的异常。详情请看 :meth:`send` 。
        """
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": text
            },
            "at": {
                "atMobiles": atMobiles, 
                "isAtAll": isAtAll
            }
        }
        rsp = self.send(data)
        return rsp

    def print(self, msg):
        """用于简单的使用 :meth:`sendText` 。

        Parameters
        ----------
        msg: str
            同 :meth:`sendText` 的 `content`, 只是用msg代表简单信息。

        Returns
        -------
        requests.models.Response
            rsp -- ``request.post()`` 返回的 ``Response``

        """
        rsp = self.sendText(msg)
        return rsp


def _checkRsp(rsp):
    if rsp.status_code != 200:
        raise DingStatusCodeError(rsp)
    else:
        try:
            r = rsp.json()
        except ValueError:
            raise DingContentError(rsp)
        if r['errcode'] != 0:
            raise DingErrCodeError(rsp)

