from utils import service_info
from agileutil.rpc.server import TcpRpcServer
from conf.config import disconf
from utils import my_consul
from app.hello import sum,hello
from app.post_cmdb import CmdbService


server = TcpRpcServer(disconf.serviceHost,disconf.servicePort)
server.setDiscoverConfig(disconf)

def register(fn,content):
    service_info.register_conf(fn,content)
    server.regist(fn)

def run_all():
    register(sum,content="测试加法运算")
    register(hello,content="测试函数")
    register(CmdbService,content='测试cmdb上报业务')
    service_info.push()
    server.serve()

def shutdown():
    my_consul.delete(disconf.serviceName)

if __name__ =='__main__':
    run_all()