import consul
from conf.config import disconf
import json

class Consul(object):
    def __init__(self):
        self._consul = consul.Consul(
            disconf.consulHost,disconf.consulPort)
        self._consul.kv.put('clsname',json.dumps({'clsname':'cmdbservice','func':'cmdbservice'}))

    def __getitem__(self, item):
        return item

    def registerService(self):
        '''
        注册器，注册函数和方法的相关信息
        （函数：函数名，参数，函数说明）
        （类：类名，方法名，参数）
        :return:
        '''

        self._consul.agent.service.register(
            name='wusi-test',
            address='192.168.31.10',
            port=9000,
            tags=['today is nice !!'],
        )

    def getService(self,name):
        cli = self._consul.agent.services()
        print(json.dumps(cli)) #服务类表
        service = cli.get(name)
        return service



ins = Consul()
ins.registerService()
print(ins.getService('wusi-test'))


c = consul.Consul()
# print(c.kv.)