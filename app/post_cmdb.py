from utils.server_register import Register_serivce

inst1 = Register_serivce()

# @inst1.register_conf
class CmdbService():

    def get(self):
        return getattr(self,'name')

    def addComponent(self,compName,**kargs):
        self.comp_name = compName
        self.state = kargs
        return self.__dict__

    def delComponent(self,compName):
        del self.comp_name


# print([ key for key,value in CmdbService.__dict__.items() if callable(value)])
