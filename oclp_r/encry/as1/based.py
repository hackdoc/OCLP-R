import pybase64
import base64
from oclp_r.encry.panic.panic import Panic

class Encry:
    def __init__(self):
        pass
    def encry(self,data):
        #判断data是否为bytes
        try:
            if not isinstance(data, bytes):
                raise Panic("Panic:This type is not bytes.",4,"TypeError").raise_panic()
            self.encry = pybase64.b64encode(data)
            
            return self.encry
        except Exception as e:
            raise Exception(str(e))

    def encry_32(self,data):
        #判断data是否为bytes
        try:
            if not isinstance(data, bytes):
                raise Panic("Panic:This type is not bytes.",4,"TypeError").raise_panic()
            self.encry = base64.b32encode(data)
            
            return self.encry
        except Exception as e:
            raise Exception(str(e))
    def encry_16(self,data):
        try:
            if not isinstance(data, bytes):
                raise TypeError("Panic:This type is not bytes.")
            self.encry_16 = base64.b16encode(data)
            
            return self.encry_16
        except Exception as e:
            raise Exception(str(e))
    
    def encry_85(self,data):
        #判断data是否为bytes
        try:
            if not isinstance(data, bytes):
                raise TypeError("Panic:This type is not bytes.")
            self.encry = base64.b85encode(data)
            
            return self.encry
        except Exception as e:
            raise Exception(str(e))
    
class Decry:
    def __init__(self):
        pass
        
    def _validate_input(self, data):
        if not isinstance(data, bytes):
            raise Panic("TypeError", "Input must be bytes", 4, "TypeError").raise_panic()
    def decry(self,data):
        #判断data是否为bytes
        try:
            if not isinstance(data, bytes):
                raise TypeError("Panic:This type is not bytes.")
            self.encry = pybase64.b64decode(data)
           
            return self.encry
        except Exception as e:
            raise Exception(str(e))
    def decry_16(self,data):
        try:
            if not isinstance(data, bytes):
                raise TypeError("Panic:This type is not bytes.")
            self.encry_16 = base64.b16decode(data)
            
            return self.encry_16
        except Exception as e:
            raise Exception(str(e))
    
    def decry_32(self,data):
        #判断data是否为bytes
        try:
            if not isinstance(data, bytes):
                raise TypeError("Panic:This type is not bytes.")
            self.encry = base64.b32decode(data)
            
            return self.encry
        except Exception as e:
            raise Exception(str(e))
    def decry_85(self,data):
        #判断data是否为bytes
        try:
            if not isinstance(data, bytes):
                raise TypeError("Panic:This type is not bytes.")
            self.encry = base64.b85decode(data)
            
            return self.encry
        except Exception as e:
            raise Exception(str(e))
    
    