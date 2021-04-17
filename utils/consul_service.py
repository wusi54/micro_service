import consul
from conf.config import disconf
import json
import requests

class Myconsul(object):
    '''consul增删改'''

    def __init__(self):
        self._consul = consul.Consul(
            disconf.consulHost, disconf.consulPort)

    def __repr__(self):
        print('-----------consul初始化连接会话--------')

    def put(self, value):
        self._consul.kv.put(disconf.serviceName, json.dumps(value))

    def get(self, key):
        return self._consul.kv.get(key)

    def delete(self, key):
        self._consul.kv.delete(key)

    def get_all_service(self):
        """获取所有的服务"""
        cli = self._consul.agent.services()
        return cli  # 服务类表

    def get_active_service(self):
        '''获取活跃存活的服务'''
        endpoint = '/v1/health/state/passing'
        response = requests.request('get',f'http://{disconf.consulHost}:{disconf.consulPort}{endpoint}').json()
        try:
            return [ _v.get("ServiceName") for _v in response if _v.get("ServiceName") ]
        except:
            return None
