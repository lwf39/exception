from enum import Enum
from enum import unique as unique

from .base import DingRobot
from ._datetime import Datetime

StateColors = {
    'PROBLEM': '#FF0000', # red
    'OK': '#008000' # green
}

LevelColors = {
    'P0': '#DF7401', # orange
    'P1': '#A901DB', # magenta
    'P2': '#0080FF', # blue
    'P3': '#000000' # black
}

class AlertRobot(DingRobot):
    """用于报警的DingRobot，主要格式化了报警内容。

    Parameters
    ----------
    title: str
        设置报警标题。具体可看 `Example`
        Note: 不同于 `DingRobot.sendMarkdown` 的title，:meth:`alert` 中的subtitle才是 `DingRobot.sendMarkdown` 的title。

    url: str
        设置DingRobot的Webhook url。    

    **kwargs
        会传给 `DingRobot` 进行初始化

    Attributes
    ----------
    title: str
        同 ``param: title``
    """
    def __init__(self, title, url, **kwargs):
        super().__init__(url, **kwargs)
        self.title = title

    def alert(self, endpoint, metric, trigger, desc='', *, count=1, state='PROBLEM', subtitle=None, title=None, level='P1', datetime=None, **kwargs):
        """用于监控报警

        Parameters
        -----------
        endpoint: str
            监控的对象(或端点)

        metric: str
            监控对象(或端点)的Metric(数据)因什么触发了报警

        trigger: str
            监控对象(或端点)的Metric(指标)因什么触发了报警

        desc: str
            description的简写，用于详细描述报警说明

        subtitle: str, defaults to None
            用于显示钉钉信息的小标题。if None, ``subtitle = level.capitalize() + ' - ' + trigger``

        title: str, defaults to None
            报警标题。 if None, 会使用实例化时传入的title。

        level: str, defaults to 'PROBLEM'
            报警等级。目前可设置 ``CRITICAL`` ``PROBLEM`` ``WARNING`` ``INFO`` 4个等级

        datetime: str, defaults to None
            报警事件。 if None, 等于当前事件

        level_color: str, defaults to None
            报警等级的颜色。 if None, 会使用 `Level` 的默认颜色。 注意: 使用的是颜色编码，类似 `#FF0000`

        to_color_level: bool, defaults to True
            报警等级是否使用颜色。

        extra_text: str
            附加的markdown。详情请看 `Example`

        **kwargs
            会传给 :meth:`sendMarkdown`

        Returns
        -------
        requests.models.Response
            rsp -- ``request.post()`` 返回的 ``Response``

        Notes
        -----
        desc(description)应具有快速解读，完整信息点的特征

        """
        if '登陆失败' in desc:
            level = 'P0'
        if title == None:
            title = self.title

        if subtitle == None:
            subtitle =  state + ' - ' + title

        if datetime == None:
            datetime = Datetime().strftime()

        state_color = StateColors[state]
        state = '<font color=%s>%s</font>' % (state_color, state)

        level_color = LevelColors[level]
        level = '<font color=%s>%s</font>' % (level_color, level)

        text = []
        text.append('### %s' % title) # title
        text.append('---')
        text.append('#### 告警等级: %s' % level) # level
        text.append('#### 告警状态: %s' % state) # level
        text.append('#### 告警时间: %s' % datetime) # datetime
        text.append('#### 告警端点: %s' % endpoint) # endpoint
        text.append('#### 告警指标: %s' % metric) # metric
        text.append('#### 告警条件: %s' % trigger) # trigger 
        text.append('#### 告警次数: %s' % count) # trigger 
        text.append('#### 告警说明: %s' % desc) # description
        text.append('#### 告警方案: 1' )

        text = '\n'.join(text)

        rsp = self.sendMarkdown(subtitle, text, **kwargs)
        return rsp