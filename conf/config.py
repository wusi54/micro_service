from agileutil.rpc.discovery import DiscoveryConfig

disconf = DiscoveryConfig(
    consulHost='192.168.31.10',
    consulPort=8500,
    serviceName='cmdb-report-service',
    serviceHost= '127.0.0.1',
    servicePort=7652
)