
from oclp_r.encry.as1.used import *
from oclp_r.encry.as2.based import *
from oclp_r.encry.log import *
from oclp_r.encry.panic import *
ascii=ASCII()
def encry_ascii(data=str):
    try:
        func=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _INFO" % {"func":func},"INFO")
        inf.auto("init succeed.")
        data_list=list(data)
        inf.auto(f"Convert data to list successfully . data_list: {data_list}")
        inf.auto("Preparing to convert to ascii.....")
        for i in range(len(data_list)):
            data_list[i]=ascii.to_ascii(data_list[i])
            inf.auto("Converting base16 char to ascii....")
            inf.auto(f"data_list[{i}]:{data_list[i]}")
            inf.auto(f"data_list: {data_list}")
        sb=""
        for i in data_list:
            sb+=str(i)+"|"
            inf.auto(f"sb:{sb}")
        sb=sb.rstrip(" | ")
        return sb
    except Exception as e:
        func=sys._getframe().f_code.co_name
        err=LogManager(" %(func)s _ERROR" % {"func":func},"ERROR")
        err.auto(f"Some serious problems: {str(e)}")
        raise Panic("%(func)s"%{"func":func},f"Some serious peoblems:\n{str(e)}",4,"UNE").raise_panic()
def decry_ascii(data=str):
    try:
        func=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _INFO" % {"func":func},"INFO")
        inf.auto("init succeed.")
        data_list=data.split("|")
        inf.auto(f"Convert data to list successfully . data_list: {data_list}")
        inf.auto("Preparing to convert to letter.....")
        for i in range(len(data_list)):
            data_list[i]=ascii.from_ascii(int(data_list[i]))
            inf.auto("Converting ascii char to letter....")
            inf.auto(f"data_list[{i}]:{data_list[i]}")
            inf.auto(f"data_list: {data_list}")
        sb=""
        for i in data_list:
            sb+=i
            inf.auto(f"sb:{sb}")
        sb=sb.rstrip(" ")
        return sb
    except Exception as e:
        func=sys._getframe().f_code.co_name
        err=LogManager(" %(func)s _ERROR" % {"func":func},"ERROR")
        err.auto(f"Some serious problems: {str(e)}")
        raise Panic("%(func)s"%{"func":func},f"Some serious peoblems:\n{str(e)}",4,"UNE").raise_panic()
def con_dec(data=str,convert_base=int,convert_to=int):
    try:
        func=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _INFO" % {"func":func},"INFO")
        inf.auto("init succeed.")
        data_list=data.split("|")
        inf.auto(f"Convert data to list successfully . data_list: {data_list}")
        inf.auto("Preparing to convert to decimal....")
        for i in range(len(data_list)):
            a=Convert_Dec(data_list[i],convert_base,convert_to)
            data_list[i]=a.convert()
            inf.auto("Converting ascii char to decimal....")
            inf.auto(f"data_list[{i}]:{data_list[i]}")
            inf.auto(f"data_list: {data_list}")
        sb=""
        for i in data_list:
            sb+=str(i)+"|"
            inf.auto(f"sb:{sb}")
        sb=sb.rstrip(" | ")
        return sb
    except Exception as e:
        func=sys._getframe().f_code.co_name
        err=LogManager(" %(func)s _ERROR" % {"func":func},"ERROR")
        err.auto(f"Some serious problems: {str(e)}")
        raise Panic("%(func)s"%{"func":func},f"Some serious peoblems:\n{str(e)}",4,"UNE").raise_panic()

def encry_standard2(data=str):
    try:
        func=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _INFO" % {"func":func},"INFO")
        data=encry_standard(data.encode()).decode()
        inf.auto("convert data successfully(1/3)")
        data=encry_ascii(data)
        inf.auto("convert data to ascii(2/3)")
        data=con_dec(data,10,2)
        inf.auto("convert ascii to decimal(3/3)")
        return data
    except Exception as e:
        func=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _ERROR" % {"func":func},"ERROR")
        inf.error(f"Some serious problems,{str(e)}")
        raise Panic("%(func)s"%{"func":func},f"Some serious peoblems:\n{str(e)}",4,"UNE").raise_panic()
def decry_standard2(data=str):
    try:
        func=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _INFO" % {"func":func},"INFO")
        inf.auto("init succeed.")
        data=con_dec(data,2,10)
        inf.auto("convert decimal to ascii succeed.(1/3)")
        data=decry_ascii(data)
        inf.auto("convert ascii to basexx succeed.(3/3)")
        data=decry_standard(data.encode()).decode()
        inf.auto("convert encryed to data succeed.(3/3)")
        return data
    except Exception as e:
        func=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _ERROR" % {"func":func},"ERROR")
        inf.error(f"Some serious problems,{str(e)}")
        raise Panic("%(func)s"%{"func":func},f"Some serious peoblems:\n{str(e)}",4,"UNE").raise_panic()
def encry_high2(data=str):
    try:
        func=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _INFO" % {"func":func},"INFO")
        inf.auto("init succeed.")
        data=encry_high(data.encode()).decode()
        inf.auto("encry data successfully.(1/5)")
        data=encry_ascii(data)
        inf.auto("convert data (to ascii) successfully.(2/5)")
        data=encry_ascii(data)
        inf.auto("convert data (to ascii) successfully.(3/5)")
        #10-8-2
        data=con_dec(data,10,8)
        inf.auto("convert dec10 (to 8) successfully.(4/5)")
        data=con_dec(data,8,2)
        inf.auto("convert dec8 (to 2) successfully.(5/5)")
        return data
    except Exception as e:
        func=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _ERROR" % {"func":func},"ERROR")
        inf.error(f"Some serious problems,{str(e)}")
        raise Panic("%(func)s"%{"func":func},f"Some serious peoblems:\n{str(e)}",4,"UNE").raise_panic()
def decry_high2(data=str):
    try:
        func=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _INFO" % {"func":func},"INFO")
        inf.auto("init succeed.")
        data=con_dec(data,2,8)
        inf.auto("convert dec2 (to 8) successfully.(1/6)")
        data=con_dec(data,8,10)
        inf.auto("convert dec8 (to 10) successfully.(3/6)")
        data=decry_ascii(data)
        inf.auto("convert data (to ascii) successfully.(4/6)")
        data=decry_ascii(data)
        inf.auto("convert data (to ascii) successfully.(5/6)")
        data=decry_high(data.encode()).decode()
        inf.auto("decry data successfully.(6/6)")
        return data
    except Exception as e:
        func=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _ERROR" % {"func":func},"ERROR")
        inf.error(f"Some serious problems,{str(e)}")
        raise Panic("%(func)s"%{"func":func},f"Some serious peoblems:\n{str(e)}",4,"UNE").raise_panic()
def encry_prof2(data=str):
    try:
        func=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _INFO" % {"func":func},"INFO")
        inf.auto("init succeed.")
        data=encry_high(data.encode()).decode()
        inf.auto("encry data successfully.(1/8)")
        data=encry_ascii(data)
        inf.auto("convert data (to ascii) successfully.(2/8)")
        data=encry_ascii(data)
        inf.auto("convert data (to ascii) successfully.(3/8)")
        data=encry_ascii(data)
        inf.auto("convert data (to ascii) successfully.(4/8)")
        #10-8-2
        data=con_dec(data,16,14)
        inf.auto("convert dec16 (to 8) successfully.(5/8)")
        data=con_dec(data,14,8)
        inf.auto("convert dec14 (to 8) successfully.(6/8)")
        data=con_dec(data,8,4)
        inf.auto("convert dec8 (to 4) successfully.(7/8)")
        data=con_dec(data,4,2)
        inf.auto("convert dec4 (to 2) successfully.(8/8)")
        return data
    except Exception as e:
        func=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _ERROR" % {"func":func},"ERROR")
        inf.error(f"Some serious problems,{str(e)}")
        raise Panic("%(func)s"%{"func":func},f"Some serious peoblems:\n{str(e)}",4,"UNE").raise_panic()
def decry_prof2(data=str):
    try:
        func=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _INFO" % {"func":func},"INFO")
        inf.auto("init succeed.")
        data=con_dec(data,2,4)
        inf.auto("convert dec2 (to 4) successfully.(1/8)")
        data=con_dec(data,4,8)
        inf.auto("convert dec4 (to 8) successfully.(2/8)")
        data=con_dec(data,8,14)
        inf.auto("convert dec8 (to 14) successfully.(3/8)")
        data=con_dec(data,14,16)
        inf.auto("convert dec14 (to 16) successfully.(4/8)")
        data=decry_ascii(data)
        inf.auto("convert data (to ascii) successfully.(5/8)")
        data=decry_ascii(data)
        inf.auto("convert data (to ascii) successfully.(6/8)")
        data=decry_ascii(data)
        inf.auto("convert data (to ascii) successfully.(7/8)")
        data=decry_high(data.encode()).decode()
        inf.auto("decry data successfully.(8/8)")
        return data
    except Exception as e:
        func=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _ERROR" % {"func":func},"ERROR")
        inf.error(f"Some serious problems,{str(e)}")
        raise Panic("%(func)s"%{"func":func},f"Some serious peoblems:\n{str(e)}",4,"UNE").raise_panic()
def encry_max2(data=str):
    try:
        fun=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _INFO" % {"func":fun},"INFO")
        inf.auto("init succeed.")
        all=75+14+1
        data=encry_max_auto(data.encode(),2).decode()
        inf.auto(f"encry data successfully.(1/{all})")
        for i in range(75):
            data=encry_ascii(data)
            inf.auto(f"encry data (to ascii) successfully.({i+2}/{all})")
        for i in range(14):
            if i==0:
                begin = 16
                func=begin-1
            else:
                begin = func
                func=begin-1
            data=con_dec(data,begin,func)
            inf.auto(f"convert dec{begin} (to dec{func}) successfully.({i+1+75+1}/{all})")
        return data
    except Exception as e:
        fun=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _ERROR" % {"func":fun},"ERROR")
        inf.error(f"Some serious problems,{str(e)}")
        raise Panic("%(func)s"%{"func":fun},f"Some serious peoblems:\n{str(e)}",4,"UNE").raise_panic()


def decry_max2(data=str):
    try:
        fun=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _INFO" % {"func":fun},"INFO")
        inf.auto("init succeed.")
        all=75+14+1
        for i in range(14):
            if i==0:
                begin = 2
                func=begin+1
            else:
                begin = func
                func=begin+1
            data=con_dec(data,begin,func)
            inf.auto(f"convert dec{begin} (to dec{func}) successfully.({i+1}/{all})")
        for i in range(75):
            data=encry_ascii(data)
            inf.auto(f"encry data (to ascii) successfully.({i+1+14}/{all})")
        data=decry_max_auto(data.encode(),2).decode()
        inf.auto(f"decry data successfully.({all}/{all})")
        return data
    except Exception as e:
        fun=sys._getframe().f_code.co_name
        inf=LogManager(" %(func)s _ERROR" % {"func":fun},"ERROR")
        inf.error(f"Some serious problems,{str(e)}")
        raise Panic("%(func)s"%{"func":fun},f"Some serious peoblems:\n{str(e)}",4,"UNE").raise_panic()