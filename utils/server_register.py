#装饰器，用来注册类名接口以及方法名，以供rpc调用
from conf.config import disconf
import inspect
from utils.consul_service import Myconsul
from agileutil.rpc.server import rpc


class Register_serivce():
    "注册服务名，函数名，方法，参数。。。的注册器"
    def __init__(self):
        # super.__init__(self)
        self.service_name = disconf.serviceName
        self._service_list = []

    def register_conf(self,func,content=None,third_people=None,dev=None):
        '''
        注册器，注册对象信息，并且把信息同步至配置中心consul
        （类：类名，方法，方法参数）
        （函数：函数名，参数）
        :param func: 注册的对象
        :return: 返回注册信息列表
        '''
        def wrap():
            if inspect.isfunction(func):
                _service_map = {}
                _service_map.update(
                    {   'serviceName':self.service_name,
                        'class':None,
                        'func':func.__name__,
                        'args':inspect.getfullargspec(func).args,
                        'content':content,
                        'third_people':third_people,
                        'dev':dev
                    }
                )
                self._service_list.append(_service_map)
            elif inspect.isclass(func):
                func_list = [ key for key,value in func.__dict__.items() if callable(value) ]

                for _foo in func_list:
                    _service_map = {}
                    _service_map.update(
                        {   "serviceName":self.service_name,
                            "class":func.__name__,
                            "func":_foo,
                            "args":inspect.getfullargspec(func.__dict__[_foo]).args,
                            "content":content,
                            "third_people":third_people,
                            "dev":dev
                        }
                    )
                    self._service_list.append(_service_map)
            else:
                raise Exception('only register function or method!!')
            return func
        wrap()

    def register(self,content:str=None,third_people=None,dev=None):
        def dector(func):
            if inspect.isfunction(func):
                _service_map = {}
                _service_map.update(
                    {   'serviceName':self.service_name,
                        'class':None,
                        'func':func.__name__,
                        'args':inspect.getfullargspec(func).args,
                        'content':content,
                        'third_people':third_people,
                        'dev':dev
                    }
                )
                self._service_list.append(_service_map)
            elif inspect.isclass(func):
                func_list = [ key for key,value in func.__dict__.items() if callable(value) ]

                for _foo in func_list:
                    _service_map = {}
                    _service_map.update(
                        {   "serviceName":self.service_name,
                            "class":func.__name__,
                            "func":_foo,
                            "args":inspect.getfullargspec(func.__dict__[_foo]).args,
                            "content":content,
                            "third_people":third_people,
                            "dev":dev
                        }
                    )
                    self._service_list.append(_service_map)
            else:
                raise Exception('only register function or method!!')
            def wrap(*args,**kwargs):
                return func(*args,**kwargs)
            return wrap
        return dector

    def __repr__(self):
        print('-----------注册器函数参数初始化----------')

    def has(self,func)->bool:
        '''校验对象信息是否注册'''
        for _obj in self._service_list:
            if func in _obj.get('func'):return True
        return False

    def push(self):
        print("---------推送配置信息初始化----------\n")
        print(self._service_list)
        myconsul = Myconsul()
        myconsul.put(self._service_list)

    def get_all(self)->list:
        '''返回注册信息列表'''
        return self._service_list


if __name__ == '__main__':
    inst1 = Register_serivce()
    # @inst1.register_conf
    # def test_1(name,age,time=4):
    #     pass
    @rpc
    @inst1.register()
    class Test_1():
        def time(self,time):
            pass
    print(inst1._service_list)

    # consul_test= Myconsul()
    # consul_test.get("clsname")
