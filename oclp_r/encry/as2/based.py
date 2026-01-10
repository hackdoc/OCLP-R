from ast import excepthandler
from doctest import FAIL_FAST
import re
from oclp_r.encry.as1.used  import *
from oclp_r.encry.as1.used import  *
from oclp_r.encry.panic.panic import *
from oclp_r.encry.log import *
import sys,time
lookup={
    "0000":"0",
    "0001":"1",
    "0010":"2",
    "0011":"3",
    "0100":"4",
    "0101":"5",
    "0110":"6",
    "0111":"7",
    '1000':"8",
    '1001':"9",
    '1010':"A",
    '1011':"B",
    '1100':"C",
    '1101':"D",
    '1110':"E",
    '1111': "F",
}
lookup16={v: k for k, v in lookup.items()}
lookup_check={
    "0":0,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "A":10,
    "B":11,
    "C":12,
    "D":13,
    "E":14,
    "F":15
}
lookup_check16={v: k for k, v in lookup_check.items()}
class Convert_Dec:
    
    def __init__(self, data,convert_base=int,to_convert=int):
        self.data = str(data) #数据
        self.to_convert = to_convert #要被转换的进制
        self.convert_base = convert_base #转换进制基础
        self.result=[]
    def check(self):
        try:
            func=sys._getframe().f_code.co_name
            log_info=LogManager("Convert %(func)s _INFO" % {"func":func},"INFO")
            log_error=LogManager("Convert %(func)s_ERROR" % {"func":func},"ERROR")
            log_critical=LogManager("Convert %(func)s_CRITICAl" % {"func":func},"CRITICAL")
            if not isinstance(self.convert_base,int)or not isinstance(self.to_convert,int):
                log_error.auto("Decimal data is wrong")
                return False
            self.data_list=list(str(self.data))
            log_info.auto("Covert data list successfully")
            if(self.convert_base>16 or self.to_convert>16): 
                log_error.auto(f"Decimal data is wrong: convert_base:{self.convert_base},to_convert:{self.to_convert}")
                return False
            log_info.auto("Check some numbers(convert_base and to_convert) successfully")
            for i in self.data_list:
                if(lookup_check[str(i)])>self.convert_base-1:
                    log_error.auto(f"Decimal data is wrong: lookup_check[str(i)]>self.convert_base-1(lookup_check[str(i)]:{lookup_check[str(i)]}  self.convert_base:{self.convert_base}) ")
                    return False
            log_info.auto("Check all datas successfully")
            return True
        except Exception as e:
            log_critical.critical(str(e))
            return False
    def panic(self):
        try:
            func=sys._getframe().f_code.co_name
            log=LogManager("Convert %(func)s _ERROR" % {"func":func},"ERROR")
            if not self.check():
                log.error("Decimal data is wrong,will be panic")
                raise Panic("Convert %(func)s"% {"func":func},"Decimal data is wrong",4,"DecimalError").raise_panic()
        except Exception as e:
            log=LogManager("Convert %(func)s" % {"func":func},"CRITICAL")
            log.critical(str(e))
            raise Panic("Convert %(func)s"% {"func":func},f"Critical Error:{str(e)}",4,"Exception")
    def dec10_convert_to_any(self):
        try:
            func=sys._getframe().f_code.co_name
            log_info=LogManager("Convert %(func)s _INFO" % {"func":func},"INFO")
            log=LogManager("Convert %(func)s _ERROR" % {"func":func},"ERROR")
            self.panic()
            if self.convert_base==10:
                self.data=int(self.data)
                log_info.auto("Convert_Dec.convert_base==10 and self.data is int")
            else:
                log.auto("Convert_Dec.convert_base>10, it is wrong")
                raise Panic("Convert %(func)s"  % {"func":func},"Convert_Dec.convert_base>10,Now it is unstopped",3,"DecimalError").raise_panic()
            self.data_in=self.data
            log_info.auto("Copy self.data to self.data_in(copy)")
            self.result=[]
            while(self.data_in>0):
                if(self.data_in%self.to_convert>=10):
                    self.result.append(lookup_check16[self.data_in%self.to_convert])
                    log_info.auto(f"self.result.append:[{lookup_check16[self.data_in%self.to_convert]}]")
                    log_info.auto(f"self.result:{self.result}")  
                else:
                    self.result.append(str(self.data_in%self.to_convert))
                    log_info.auto(f"self.result.append:[{str(self.data_in%self.to_convert)}]")
                    log_info.auto(f"self.result:{self.result}")
                self.data_in//=self.to_convert
                log_info.auto(f"Doing self.data_in//=self.to_convert task...")
                log_info.auto(f"self.data_in:{self.data_in}")
            self.result=self.result[::-1]
            log_info.auto(f"Convert self.result....")
            log_info.auto(f"self.result:{self.result}")
            self.result_send=""
            for i in self.result:
                self.result_send+=i
                log_info.auto(f"Adding self.result_send")
                log_info.auto(f"self.result_send:{self.result_send}")
            log_info.auto("Done.")
            return self.result_send
        except Exception as e:
            func=sys._getframe().f_code.co_name
            log=LogManager("Convert %(func)s _CRITICAL" % {"func":func},"CRITICAL")
            log.critical(str(e))
            raise Panic("Convert %(func)s"% {"func":func},f"Critical Error:{str(e)}",4,"Exception").raise_panic()
    def dec_16_to_2(self):
        try:
            func=sys._getframe().f_code.co_name
            log_info=LogManager("Convert %(func)s _INFO" % {"func":func},"INFO")
            if(self.convert_base!=16 or self.to_convert!=2):
                log=LogManager("Convert %(func)s _ERROR" % {"func":func},"ERROR")
                log.auto("Decimal data is wrong,will be panic")
                raise Panic("Convert %(func)s" % {"func":func},"Decimal data is wrong",3,"DecimalError").raise_panic()
            self.panic()
            log_info.auto("Check datas successfully")
            self.data_list=list(str(self.data))
            log_info.auto(f"Convert data to list successfully,data_list:{self.data_list}")
            self.result=[]
            self.result_send=""
            for i in range(len(self.data_list)):
                self.result.append(str(lookup16[str(self.data_list[i])]))
                log_info.auto(f"self.result.append:[{str(lookup16[str(self.data_list[i])])}]")
                log_info.auto(f"self.result:{self.result}")
            for i in self.result:
                self.result_send+=i
                log_info.auto(f"Adding self.result_send")
                log_info.auto(f"self.result_send:{self.result_send}")
            log_info.auto("Done.")
            return int(self.result_send)
        except Exception as e:
            func=sys._getframe().f_code.co_name
            log=LogManager("Convert %(func)s _CRITICAL" % {"func":func},"CRITICAL")
            log.critical(str(e))
            raise Panic("Convert %(func)s "% {"func":func},f"Critical Error:{str(e)}",4,"Exception").raise_panic()
    def dec_2_to_16(self):
        try:
            func=sys._getframe().f_code.co_name
            log_info=LogManager("Convert %(func)s _INFO" % {"func":func},"INFO")
            if(self.convert_base!=2 or self.to_convert!=16):
                log=LogManager("Convert %(func)s _ERROR" % {"func":func},"ERROR")
                log.auto("Decimal data is wrong,will be panic")
                raise Panic("Convert %(func)s" % {"func":func},"Decimal data is wrong",3,"DecimalError").raise_panic()
            self.panic()
            log_info.auto("Check datas successfully")
            self.data=str(self.data)
            log_info.auto(f"Convert data to str successfully")
            if(len(self.data)%4!=0):
                log_info.auto("Data length is not enough,will be add 0")
                while(True):
                    self.data="0"+self.data
                    log_info.auto(f"Doing self.data=\"0\"+self.data task...")
                    log_info.auto(f"self.data:{self.data}")
                    if(len(self.data)%4==0):
                        log_info.auto("Convert data successfully")
                        break
            self.result=[]
            self.result_send=""
            self.crashe=[""]
            self.x=0
            for i in range(len(self.data)):
                log_info.auto("Spliting data.....")
                self.crashe[self.x]+=self.data[i]
                log_info.auto(f"Change self.crashe[self.x] and self.data[i]")
                log_info.auto(f"self.crashe[self.x]:{self.crashe[self.x]}self.data[i]:{self.data[i]}")
                if(i+1)%4==0 and i!=len(self.data)-1:
                    self.x+=1
                    self.crashe.append("")
            for i in range(len(self.crashe)):
                self.result.append(lookup[self.crashe[i]])
                log_info.auto(f"self.result.append:[{lookup[self.crashe[i]]}]")
                log_info.auto(f"self.result:{self.result}")
            for i in self.result:
                self.result_send+=i
                log_info.auto(f"Adding self.result_send")
                log_info.auto(f"self.result_send:{self.result_send}")
            log_info.auto("Done.")
            return self.result_send
        except Exception as e:
            func=sys._getframe().f_code.co_name
            log=LogManager("Convert %(func)s _CRITICAL" % {"func":func},"CRITICAL")
            log.critical(str(e))
            raise Panic("Convert %(func)s "% {"func":func},f"Critical Error:{str(e)}",4,"Exception").raise_panic()
    def dec_8_to_2(self):
        try:
            func=sys._getframe().f_code.co_name
            log_info=LogManager("Convert %(func)s _INFO" % {"func":func},"INFO")
            if(self.convert_base!=8 or self.to_convert!=2):
                log=LogManager("Convert %(func)s _ERROR" % {"func":func},"ERROR")
                log.auto("Decimal data is wrong,will be panic")
                raise Panic("Convert %(func)s" % {"func":func},"Decimal data is wrong",3,"DecimalError").raise_panic()
            self.panic()
            log_info.auto("Check datas successfully")
            self.data=list(str(self.data))
            self.result=[]
            self.result_send=""
            for i in range(len(self.data)):
                log_info.auto(f"Changing data...")
                self.fun=str(int(lookup16[str(self.data[i])]))
                log_info.auto(f"self.fun:{self.fun}")
                if(len(self.fun)<3):
                    log_info.auto(f"Data length is not enough,will be add 0")
                    while(len(self.fun)<3):
                        self.fun="0"+self.fun
                        log_info.auto("Adding 0")
                        log_info.auto(f"self.fun:{self.fun}")
                self.result.append(self.fun)
                log_info.auto(f"self.result.append:[{self.fun}]")
                log_info.auto(f"self.result:{self.result}")
            for i in self.result:
                self.result_send+=i
                log_info.auto(f"Adding self.result_send")
                log_info.auto(f"self.result_send:{self.result_send}")
            log_info.auto("Done.")
            return int(self.result_send)
        except Exception as e:
            func=sys._getframe().f_code.co_name
            log=LogManager("Convert %(func)s _CRITICAL" % {"func":func},"CRITICAL")
            log.critical(str(e))
            raise Panic("Convert %(func)s"% {"func":func},f"Critical Error:{str(e)}",4,"Exception").raise_panic()
    def dec_2_to_8(self):
        try:
            func=sys._getframe().f_code.co_name
            log_info=LogManager("Convert %(func)s _INFO" % {"func":func},"INFO")
            if(self.convert_base!=2 or self.to_convert!=8):
                log=LogManager("Convert %(func)s _ERROR" % {"func":func},"ERROR")
                log.auto("Decimal data is wrong,will be panic")
                raise Panic("Convert %(func)s" % {"func":func},"Decimal data is wrong",3,"DecimalError").raise_panic()
            self.panic()
            log_info.auto("Check datas successfully")
            self.data=str(self.data)
            log_info.auto("Convert data to str successfully")
            if(len(self.data)%3!=0):
                log_info.auto("Data length is not enough,will be add 0 (self.data length)")
                while(True):
                    self.data="0"+self.data
                    log_info.auto(f"Doing self.data=\"0\"+self.data task...")
                    if(len(self.data)%3==0):
                        log_info.auto("Convert data successfully")
                        break
            self.result=[]
            self.result_send=""
            self.crashe=[""]
            self.x=0
            for i in range(len(self.data)):
                self.crashe[self.x]+=self.data[i]
                log_info.auto(f"Change self.crashe[self.x] and self.data[i]")
                log_info.auto(f"self.crashe[self.x]:{self.crashe[self.x]}  self.data[i]:{self.data[i]}")
                if(i+1)%3==0 and i!=len(self.data)-1:
                    self.x+=1
                    self.crashe.append("")
            try:
                self.crashe.remove("")
            except:
                pass
            log_info.auto(f"self.crashe:{self.crashe}")
            for i in range(len(self.crashe)):
                self.crashe[i]=str(int(self.crashe[i]))
                log_info.auto(f"convert self.crashe[i] to out 0..")
                log_info.auto(f"self.crashe[i]:{self.crashe[i]}")
            log_info.auto(f"self.crashe:{self.crashe}")
            for i in range(len(self.crashe)):
                self.fun=str(int(self.crashe[i]))
                while(len(self.fun)<4):
                    log_info.auto(f"Data length is not enough,will be add 0")
                    self.fun="0"+self.fun
                    log_info.auto("Adding 0")
                log_info.auto(f"self.fun:{self.fun}")
                self.fun=str(self.fun)
                self.crashe[i]=self.fun
            log_info.auto(f"self.crashe:{self.crashe}")
            for i in range(len(self.crashe)):
                
                self.result.append(lookup[str(self.crashe[i])])
                log_info.auto(f"self.result.append:[{lookup[self.crashe[i]]}]")
                log_info.auto(f"self.result:{self.result}")
            for i in self.result:
                self.result_send+=i
                log_info.auto(f"Adding self.result_send")
                log_info.auto(f"self.result_send:{self.result_send}")
            return self.result_send
        except Exception as e:
            func=sys._getframe().f_code.co_name
            log=LogManager("Convert %(func)s _CRITICAL" % {"func":func},"CRITICAL")
            log.critical(str(e))
            raise Panic("Convert %(func)s"% {"func":func},f"Critical Error:{str(e)}",4,"Exception").raise_panic()
    def dec_any_to_10(self):
        try:
            func=sys._getframe().f_code.co_name
            log_info=LogManager("Convert %(func)s _INFO" % {"func":func},"INFO")
            if(self.to_convert!=10):
                log=LogManager("Convert %(func)s _ERROR" % {"func":func},"ERROR")
                log.auto("Decimal data is wrong,will be panic")
                raise Panic("Convert %(func)s" % {"func":func},"Decimal data is wrong",3,"DecimalError").raise_panic()
            self.panic()
            log_info.auto("Check datas successfully")
            self.data_list=list(str(self.data))
            log_info.auto("Convert data to list successfully")
            for i in range(len(self.data_list)):
                log_info.auto(f"Change self.data_list[{i}]")
                self.data_list[i]=lookup_check[self.data_list[i]]
                log_info.auto(f"self.data_list[{i}]:{self.data_list[i]}")
            self.data_list=self.data_list[::-1]
            self.result=0
            for i in range(len(self.data_list)):
                self.result+=pow(self.convert_base,i)*self.data_list[i]
                log_info.auto(f"ADDING self.result")
                log_info.auto(f"self.result:{self.result}")
            log_info.auto("Done.")
            return self.result
        except Exception as e:
            func=sys._getframe().f_code.co_name
            log=LogManager("Convert %(func)s _CRITICAL" % {"func":func},"CRITICAL")
            log.critical(str(e))
            raise Panic("Convert %(func)s"% {"func":func},f"Critical Error:{str(e)}",4,"Exception").raise_panic()
    def convert(self):
        import time
        try:
            time_start=time.perf_counter()
            func=sys._getframe().f_code.co_name
            log_info=LogManager("Convert %(func)s _INFO" % {"func":func},"INFO")
            self.panic()
            if self.convert_base==self.to_convert:
                log_info.auto("convert_base is the same as to_convert")
                time_end=time.perf_counter()
                return self.data,time_end-time_start
            if self.convert_base==10:
                log_info.auto("convert_base=10,using dec10_convert_to_any...")
                self.fina=self.dec10_convert_to_any()
                
            elif self.to_convert==10:
                log_info.auto("to_convert=10,using dec_any_to_10...")
                self.fina=self.dec_any_to_10()
                
            elif(self.convert_base==2 and self.to_convert==8):
                log_info.auto("Using dec_2_to_8...")
                self.fina=self.dec_2_to_8()
                
            elif(self.convert_base==8 and self.to_convert==2):
                log_info.auto("Using dec_8_to_2...")
                self.fina=self.dec_8_to_2()
                
            elif(self.convert_base==2 and self.to_convert==16):
                log_info.auto("Using dec_2_to_16...")
                self.fina=self.dec_2_to_16()
                
            elif self.convert_base==16 and self.to_convert==2:
                log_info.auto("Using dec_16_to_2...")
                self.fina=self.dec_16_to_2()
                
            elif self.convert_base==16 and self.to_convert==8:
                log_info.auto("PREPARNING.....")
                self.to_convert_mi=self.to_convert
                log_info.auto("copy to_convert to to_convert_mi")
                self.to_convert=2
                log_info.auto("let to_convert=2")
                log_info.auto("Using dec_16_to_2....")
                self.data=self.dec_16_to_2()
                self.convert_base=2
                log_info.auto("let convert_base=2")
                self.to_convert=self.to_convert_mi
                log_info.auto("copy to_convert_mi to to_convert")
                log_info.auto("Using dec_2_to_8....")
                self.fina=self.dec_2_to_8()
                
            elif self.convert_base==8 and self.to_convert==16:
                log_info.auto("PREPARNING.....")
                self.to_convert_mi=self.to_convert
                log_info.auto("copy to_convert to to_convert_mi")
                self.to_convert=2
                log_info.auto("let to_convert=2")
                log_info.auto("Using dec_8_to_2....")
                self.data=self.dec_8_to_2()
                self.convert_base=2
                log_info.auto("let convert_base=2")
                self.to_convert=self.to_convert_mi
                log_info.auto("copy to_convert_mi to to_convert")
                log_info.auto("Using dec_2_to_16....")
                self.fina=self.dec_2_to_16()
            else:
                log_info.auto("PREPARNING.....")
                self.to_convert_mi=self.to_convert
                log_info.auto("copy to_convert to to_convert_mi")
                self.to_convert=10
                log_info.auto("let to_convert=10")
                log_info.auto("Using dec_8_to_2....")
                self.data=self.dec_any_to_10()
                self.convert_base=10
                log_info.auto("let convert_base=10")
                self.to_convert=self.to_convert_mi
                log_info.auto("copy to_convert_mi to to_convert")
                log_info.auto("Using dec10_convert_to_any....")
                self.fina=self.dec10_convert_to_any()
            time_end=time.perf_counter()
            log_info.auto(f"USING TIME:{time_end-time_start:.6f}s")
            return self.fina
        except Exception as e:
            func=sys._getframe().f_code.co_name
            log_cri=LogManager("Convert %(func)s _CRITICAL" % {"func":func},"CRITICAL")
            log_cri.auto(f"Some uncxcepted happened:{str(e)}")
            raise Panic("Convert %(func)s"% {"func":func},f"Some uncxcepted happened:{str(e)}",4,"UNKNOWNERROR").raise_panic()
class ASCII:
    def __init__(self):
        func = sys._getframe().f_code.co_name
        log_info = LogManager("ASCII %(func)s _INFO" % {"func": func}, "INFO")
        log_info.auto("ASCII class initialized.")
    def to_ascii(self,char=str):
        try:
            func = sys._getframe().f_code.co_name
            log_info = LogManager("ASCII %(func)s _INFO" % {"func": func}, "INFO")
            log_error = LogManager("ASCII %(func)s _ERROR" % {"func": func}, "ERROR")

            if not isinstance(char, str) or len(char) != 1:
                log_error.auto(f"Invalid input: '{char}'. Expected a single character string.")
                raise Panic("ASCII %(func)s" % {"func": func}, "Invalid input for ASCII conversion", 3, "ValueError").raise_panic()
            
            ascii_val = ord(char)
            log_info.auto(f"Converted character '{char}' to ASCII value {ascii_val}")
            return ascii_val
        except Exception as e:
            func = sys._getframe().f_code.co_name
            log_cri = LogManager("ASCII %(func)s _CRITICAL" % {"func": func}, "CRITICAL")
            log_cri.auto(f"An unexpected error occurred: {str(e)}")
            raise Panic("ASCII %(func)s" % {"func": func}, f"Critical Error: {str(e)}", 4, "Exception").raise_panic()

    def from_ascii(self, ascii_val):
        try:
            func = sys._getframe().f_code.co_name
            log_info = LogManager("ASCII %(func)s _INFO" % {"func": func}, "INFO")
            log_error = LogManager("ASCII %(func)s _ERROR" % {"func": func}, "ERROR")

            if not isinstance(ascii_val, int) or not (0 <= ascii_val <= 127): # ASCII values are 0-127
                log_error.auto(f"Invalid input: '{ascii_val}'. Expected an integer between 0 and 127.")
                raise Panic("ASCII %(func)s" % {"func": func}, "Invalid input for ASCII conversion", 3, "ValueError").raise_panic()
            
            char = chr(ascii_val)
            log_info.auto(f"Converted ASCII value {ascii_val} to character '{char}'")
            return char
        except Exception as e:
            func = sys._getframe().f_code.co_name
            log_cri = LogManager("ASCII %(func)s _CRITICAL" % {"func": func}, "CRITICAL")
            log_cri.auto(f"An unexpected error occurred: {str(e)}")
            raise Panic("ASCII %(func)s" % {"func": func}, f"Critical Error: {str(e)}", 4, "Exception").raise_panic()