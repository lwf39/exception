import etcd3
import time
import datetime
from config import etcd_host



def get_etcd_data():
    # 先获得时间数组格式的日期
    OneMinuteAgo = (datetime.datetime.now() - datetime.timedelta(minutes = 1))
    # 转换为时间戳
    timeStamp = int(time.mktime(OneMinuteAgo.timetuple()) * 1000)

    # 创建etcd3客户端对象并连接到etcd服务器
    etcd = etcd3.client(host=etcd_host, port=2379)

    data_exception = []
    # 获取指定前缀的所有键值对
    prefix = '/exception-mining/exception-class/data/content/'
    for data, path in etcd.get_prefix(prefix):
            # 判断value是否为None，如果不为None，则将二进制数据解码为字符串（假设采用UTF-8编码）
        if path is not None:
            decoded_data = data.decode('utf-8')
            decoded_path = path.key.decode('utf-8').split('/')[5]
            ctime_data,_ = etcd.get(f'/exception-mining/exception-class/data/ctime/{decoded_path}')
            if int(ctime_data.decode('utf-8')) > timeStamp:
                data_exception.append(decoded_data)
    return data_exception
