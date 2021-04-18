from agileutil.rpc.client import TcpRpcClient
from conf.config import disconf
from utils.server_register import Myconsul

#rpc客户端连接实例
cli = TcpRpcClient()
#配置中心连接
session = Myconsul()
#rpc实例使用配置中心配置
cli.setDiscoveryConfig(disconf)

print('#######################场景使用示例#############################')
#获取活跃的服务信息
print('1:活跃的微服务名\n',session.get_active_service())
#获取全部的服务信息
print('2:全部的微服务信息\n',session.get_all_service())
#获取相应服务的配置信息
print('3:查询微服务配置信息\n',session.get('cmdb-report-service'))
#微服务远程调用
print('4:微服务函数调度方式\n',cli.call('sum',1,4))
print(cli.call('hello'))

print('5:远程调度类方法')
print(cli.call('CmdbService.get'))


# print('5:调用类方法\n',cli.call('CmdbService.get'))

