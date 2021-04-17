from utils.server_register import Register_serivce,Myconsul
service_info = Register_serivce()
my_consul = Myconsul
print('微服务名：',service_info.service_name)
