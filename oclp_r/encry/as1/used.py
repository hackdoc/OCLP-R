from oclp_r.encry.as1.based import *
from oclp_r.encry.log.log import *
def encry_64(data)->bytes:
    try:
        if not isinstance(data, bytes):
            raise Panic("encry_64","Panic:This type is not bytes.",4,"TypeError").raise_panic()
        a = Encry()
        b=a.encry(data)
        return b
    except Exception as e:
        raise Panic("encry_64",str(e),4,"Exception").raise_panic()
def encry_85(data)->bytes:
    try:
        if not isinstance(data, bytes):
            raise Panic("encry_85","Panic:This type is not bytes.",4,"TypeError").raise_panic()
        a = Encry()
        b=a.encry_85(data)
        return b
    except Exception as e:
        raise Panic("encry_85",str(e),4,"Exception").raise_panic()
def encry_32(data)->bytes:
    try:
        if not isinstance(data, bytes):
            raise Panic("encry_32","Panic:This type is not bytes.",4,"TypeError").raise_panic()
        a = Encry()
        b=a.encry_32(data)
        return b
    except Exception as e:
        raise Panic("encry_32",str(e),4,"Exception").raise_panic()
def encry_16(data)->bytes:
    try:
        if not isinstance(data, bytes):
            raise Panic("encry_16","Panic:This type is not bytes.",4,"TypeError").raise_panic()
        a = Encry()
        b=a.encry_16(data)
        return b
    except Exception as e:
        raise Panic("encry_16",str(e),4,"Exception").raise_panic()

def decry_64(data)->bytes:
    try:
        if not isinstance(data, bytes):
            raise Panic("decry_64","Panic:This type is not bytes.",4,"TypeError").raise_panic()
        a = Decry()
        b=a.decry(data)
        return b
    except Exception as e:
        raise Panic("decry_64",str(e),4,"Exception").raise_panic()
def decry_16(data)->bytes:
    try:
        if not isinstance(data, bytes):
            raise Panic("decry_16","Panic:This type is not bytes.",4,"TypeError").raise_panic()
        a = Decry()
        b=a.decry_16(data)
        return b
    except Exception as e:
        raise Panic("decry_16",str(e),4,"Exception").raise_panic()
def decry_32(data)->bytes:
    try:
        if not isinstance(data, bytes):
            raise Panic("decry_32","Panic:This type is not bytes.",4,"TypeError").raise_panic()
        a = Decry()
        b=a.decry_32(data)
        return b
    except Exception as e:
        raise Panic("decry_32",str(e),4,"Exception").raise_panic()
def decry_85(data)->bytes:
    try:
        if not isinstance(data, bytes):
            raise Panic("decry_85","Panic:This type is not bytes.",4,"TypeError").raise_panic()
        a = Decry()
        b=a.decry_85(data)
        return b
    except Exception as e:
        raise Panic("decry_85",str(e),4,"Exception").raise_panic()
contact_encry="%(contact)s base%(based)s Done. (%(time)s / %(total)s)"
def encry_primary(data)->bytes:
    try:
        log=LogManager("encry_primary","INFO")
        if not isinstance(data, bytes):
            log.auto("data is not bytes, encoding...")
            data=data.encode()
            log.auto("data encoded")
        data_encryed=encry_64(data)
        log.auto(contact_encry % {"contact":"Encry","based":"64","time":"1","total":"2"})
        data_encryed=encry_16(data_encryed)
        log.auto(contact_encry % {"contact":"Encry","based":"16","time":"2","total":"2"})
        log.auto("Done.")
        return data_encryed
    except Exception as e:
        raise Panic("encry_primary",str(e),4,"Exception").raise_panic()
def decry_primary(data)->bytes:
    try:
        log=LogManager("decry_primary","INFO")
        if not isinstance(data, bytes):
            log.auto("data is not bytes, encoding...")
            data=data.encode()
            log.auto("data encoded")
        data_decryed = decry_16(data)
        log.auto(contact_encry % {"contact":"Decry","based":"16","time":"1","total":"2"})
        data_decryed=decry_64(data_decryed)
        log.auto(contact_encry % {"contact":"Decry","based":"64","time":"2","total":"2"})
        log.auto("Done.")
        return data_decryed
    except Exception as e:
        raise Panic("decry_primary",str(e),4,"Exception").raise_panic()
def encry_standard(data)->bytes:
    try:
        log=LogManager("encry_standard","INFO")
        if not isinstance(data, bytes):
            log.auto("data is not bytes, encoding...")
            data=data.encode()
            log.auto("data encoded")
        
        data_encryed=encry_85(data)
        log.auto(contact_encry % {"contact":"Encry","based":"5","time":"1","total":"3"})
        data_encryed=encry_32(data_encryed)
        log.auto(contact_encry % {"contact":"Encry","based":"32","time":"2","total":"3"})
        data_encryed = encry_16(data_encryed)
        log.auto(contact_encry % {"contact":"Encry","based":"16","time":"3","total":"3"})
        log.auto("Done.")
        return data_encryed
    except Exception as e:
        raise Panic("encry_standard",str(e),4,"Exception").raise_panic()
def decry_standard(data)->bytes:
    try:
        log=LogManager("decry_standard","INFO")
        if not isinstance(data, bytes):
            log.auto("data is not bytes, encoding...")
            data=data.encode()
            log.auto("data encoded")
        data_decryed = decry_16(data)
        log.auto(contact_encry % {"contact":"Decry","based":"16","time":"1","total":"3"})
        data_decryed=decry_32(data_decryed)
        log.auto(contact_encry % {"contact":"Decry","based":"32","time":"2","total":"3"})
        data_decryed=decry_85(data_decryed)
        log.auto(contact_encry % {"contact":"Decry","based":"85","time":"3","total":"3"})
        log.auto("Done.")
        return data_decryed
    except Exception as e:
        raise Panic("decry_standard",str(e),4,"Exception").raise_panic()
def encry_high(data)->bytes:
    try:
        log=LogManager("encry_high","INFO")
        if not isinstance(data, bytes):
            log.auto("data is not bytes, encoding...")
            data=data.encode()
            log.auto("data encoded")
        data_encryed=encry_85(data)
        log.auto(contact_encry % {"contact":"Encry","based":"85","time":"1","total":"5"})
        data_encryed = encry_64(data_encryed)
        log.auto(contact_encry % {"contact":"Encry","based":"64","time":"2","total":"5"})
        data_encryed=encry_32(data_encryed)
        log.auto(contact_encry % {"contact":"Encry","based":"32","time":"3","total":"5"})
        data_encryed = encry_64(data_encryed)
        log.auto(contact_encry % {"contact":"Encry","based":"64","time":"4","total":"5"})
        data_encryed = encry_16(data_encryed)
        log.auto(contact_encry % {"contact":"Encry","based":"16","time":"5","total":"5"})
        log.auto("Done.")
        return data_encryed
    except Exception as e:
        raise Panic("encry_high",str(e),4,"Exception").raise_panic()
def decry_high(data=str|bytes)->bytes:
    try:
        log=LogManager("decry_high","INFO")
        if not isinstance(data, bytes):
            log.auto("data is not bytes, encoding...")
            data=data.encode()
            log.auto("data encoded")
        data_decryed = decry_16(data)
        log.auto(contact_encry % {"contact":"Decry","based":"16","time":"1","total":"5"})
        data_decryed = decry_64(data_decryed)
        log.auto(contact_encry % {"contact":"Decry","based":"64","time":"2","total":"5"})
        data_decryed=decry_32(data_decryed)
        log.auto(contact_encry % {"contact":"Decry","based":"32","time":"3","total":"5"})
        data_decryed = decry_64(data_decryed)
        log.auto(contact_encry % {"contact":"Decry","based":"64","time":"4","total":"5"})
        data_decryed=decry_85(data_decryed)
        log.auto(contact_encry % {"contact":"Decry","based":"85","time":"5","total":"5"})
        log.auto("Done.")
        return data_decryed
    except Exception as e:
        raise Panic("decry_high",str(e),4,"Exception").raise_panic()
def encry_prof(data)->bytes:
    try:
        log=LogManager("encry_prof","INFO")

        if not isinstance(data, bytes):
            log.auto("data is not bytes, encoding...")
            data=data.encode()
            log.auto("data encoded")
        for i in range(10):
            if(i==0):
                data_encryed=encry_32(data)
                log.auto(contact_encry % {"contact":"Encry","based":"32","time":1,"total":"23"})
            else:
                data_encryed=encry_32(data_encryed)
                log.auto(contact_encry % {"contact":"Encry","based":"32","time":i*2+1,"total":"23"})
            data_encryed = encry_64(data_encryed)
            log.auto(contact_encry % {"contact":"Encry","based":"64","time":i*2+2,"total":"23"})
        data_encryed=encry_32(data_encryed)
        log.auto(contact_encry % {"contact":"Encry","based":"32","time":21,"total":"23"})
        data_encryed = encry_64(data_encryed)
        log.auto(contact_encry % {"contact":"Encry","based":"64","time":22,"total":"23"})
        data_encryed = encry_16(data_encryed)
        log.auto(contact_encry % {"contact":"Encry","based":"16","time":23,"total":"23"})
        log.auto("Done.")
        return data_encryed
    except Exception as e:
        raise Panic("encry_prof",str(e),4,"Exception").raise_panic()
def decry_prof(data)->bytes:
    try:
        log=LogManager("decry_prof","INFO")
        if not isinstance(data, bytes):
            log.auto("data is not bytes, encoding...")
            data=data.encode()
            log.auto("data encoded")
        data_decryed = decry_16(data)
        log.auto(contact_encry % {"contact":"Decry","based":"16","time":1,"total":"23"})
        data_decryed = decry_64(data_decryed)
        log.auto(contact_encry % {"contact":"Decry","based":"64","time":2,"total":"23"})
        data_decryed=decry_32(data_decryed)
        log.auto(contact_encry % {"contact":"Decry","based":"32","time":3,"total":"23"})
        for i in range(10):
            data_decryed = decry_64(data_decryed)
            log.auto(contact_encry % {"contact":"Decry","based":"64","time":i*2+4,"total":"23"})
            data_decryed=decry_32(data_decryed)
            log.auto(contact_encry % {"contact":"Decry","based":"32","time":i*2+5,"total":"23"})
        log.auto("Done.")
        return data_decryed
    except Exception as e:
        raise Panic("decry_prof",str(e),4,"Exception").raise_panic()

def encry_max(data)->bytes:
    try:
        log=LogManager("encry_max","INFO")
        if not isinstance(data, bytes):
            log.auto("data is not bytes, encoding...")
            data=data.encode()
            log.auto("data encoded")
        for i in range(35):
            if(i==0):
                data_encryed=encry_85(data)
                log.auto(contact_encry % {"contact":"Encry","based":"85","time":i*2+1,"total":"103"})
            else:
                data_encryed=encry_85(data_encryed)
                log.auto(contact_encry % {"contact":"Encry","based":"85","time":i*2+1,"total":"103"})
            data_encryed = encry_64(data_encryed)
            log.auto(contact_encry % {"contact":"Encry","based":"64","time":i*2+2,"total":"103"})
        for i in range(15):
            data_encryed=encry_32(data_encryed)
            log.auto(contact_encry % {"contact":"Encry","based":"32","time":i*2+201,"total":"103"})
            data_encryed = encry_64(data_encryed)
            log.auto(contact_encry % {"contact":"Encry","based":"64","time":i*2+202,"total":"103"})
        data_encryed=encry_64(data_encryed)
        log.auto(contact_encry % {"contact":"Encry","based":"64","time":101,"total":"103"})
        data_encryed = encry_32(data_encryed)
        log.auto(contact_encry % {"contact":"Encry","based":"32","time":102,"total":"103"})
        data_encryed = encry_16(data_encryed)
        log.auto(contact_encry % {"contact":"Encry","based":"16","time":103,"total":"103"})
        log.auto("Done.")
        return data_encryed
    except Exception as e:
        raise Panic("encry_max",str(e),4,"Exception").raise_panic()
def decry_max(data)->bytes:
    try:
        log=LogManager("decry_max","INFO")
        if not isinstance(data, bytes):
            log.auto("data is not bytes, encoding...")
            data=data.encode()
            log.auto("data encoded")
        data_decryed = decry_16(data_decryed)
        log.auto(contact_encry % {"contact":"Decry","based":"16","time":1,"total":"103"})
        data_decryed = decry_32(data_decryed)
        log.auto(contact_encry % {"contact":"Decry","based":32,"time":2,"total":"103"})
        data_decryed=decry_64(data_decryed)
        log.auto(contact_encry % {"contact":"Decry","based":"64","time":3,"total":"103"})
        for i in range(15):
            data_decryed = decry_64(data_decryed)
            log.auto(contact_encry % {"contact":"Decry","based":"64","time":i*2+4,"total":"103"})
            data_decryed=decry_32(data_decryed)
            log.auto(contact_encry % {"contact":"Decry","based":"32","time":i*2+5,"total":"103"})
        for i in range(35):
            data_decryed = decry_64(data_decryed)
            log.auto(contact_encry % {"contact":"Decry","based":"64","time":i*2+34,"total":"103"})
            data_decryed=decry_85(data_decryed)
            log.auto(contact_encry % {"contact":"Decry","based":"85","time":i*2+35,"total":"103"})
        log.auto("Done.")
        return data_decryed
    except Exception as e:
        raise Panic("decry_max",str(e),4,"Exception").raise_panic()
def encry_max_auto(data,tem=int)->bytes:
    try:
        import time
        log=LogManager("encry_max_auto","INFO")
        if(tem>=4 and tem<2147483647):
            lin_log=LogManager("encry_max_auto_lin","WARNING")
            lin_log.auto("Temperature is too high")
            Panic("encry_max_auto","Temperature is too high",1,"WARNING").raise_panic()
            time.sleep(2)
        elif (tem>=2147483647):
            lin_log=LogManager("encry_max_auto_lin","ERROR")
            lin_log.auto("Temperature is toooooo high")
            Panic("encry_max_auto","Temperature is toooooo high",2,"ERROR").raise_panic()
            time.sleep(10)
        if not isinstance(data, bytes):
            log.auto("data is not bytes, encoding...")
            data=data.encode()
            log.auto("data encoded")
        cal=(pow(tem,4)+pow(tem,2))*3+1
        for i in range(pow(tem,4)):
            if(i==0):
                data_encryed=encry_85(data)
                log.auto(contact_encry % {"contact":"Encry","based":"85","time":i*3+1,"total":cal})
            else:
                data_encryed = encry_85(data_encryed)
                log.auto(contact_encry % {"contact":"Encry","based":"85","time":i*3+1,"total":cal})
            data_encryed = encry_64(data_encryed)
            log.auto(contact_encry % {"contact":"Encry","based":"64","time":i*3+2,"total":cal})
            data_encryed = encry_32(data_encryed)
            log.auto(contact_encry % {"contact":"Encry","based":"64","time":i*3+3,"total":cal})
        for i in range(pow(tem,2)):
            data_encryed=encry_85(data_encryed)
            log.auto(contact_encry % {"contact":"Encry","based":"85","time":i*3+1+pow(tem,4)*3,"total":cal})
            data_encryed=encry_32(data_encryed)
            log.auto(contact_encry % {"contact":"Encry","based":"32","time":i*3+2+pow(tem,3)*3,"total":cal})
            data_encryed = encry_64(data_encryed)
            log.auto(contact_encry % {"contact":"Encry","based":"64","time":i*3+3+pow(tem,3)*3,"total":cal})
        data_encryed = encry_16(data_encryed)
        log.auto(contact_encry % {"contact":"Encry","based":"16","time":cal,"total":cal})
        log.auto("Done.")
        return data_encryed
    except Exception as e:
        raise Panic("encry_max_auto",str(e),4,"Exception").raise_panic()
def decry_max_auto(data,tem=int)->bytes:
    try:
        log=LogManager("decry_max_auto","INFO")
        if(tem>=4 and tem<12):
            lin_log=LogManager("encry_max_auto_lin","WARNING")
            lin_log.auto("Temperature is too high")
            Panic("decry_max_auto","Temperature is too high",1,"WARNING").raise_panic()
        elif (tem>=12):
            
            lin_log=LogManager("encry_max_auto_lin","ERROR")
            lin_log.auto("Temperature is too high")
            raise Panic("decry_max_auto","Temperature is toooooo high",3,"WARNING").raise_panic()
        if not isinstance(data, bytes):
            log.auto("data is not bytes, encoding...")
            data=data.encode()
            log.auto("data encoded")
        cal=(pow(tem,4)+pow(tem,2))*3+1
        data_decryed = decry_16(data)
        log.auto(contact_encry % {"contact":"Decry","based":"16","time":1,"total":cal})
        for i in range(pow(tem,2)):
            #85 32 64
            data_decryed = decry_64(data_decryed)
            log.auto(contact_encry % {"contact":"Decry","based":"64","time":i*3+2,"total":cal})
            data_decryed=decry_32(data_decryed)
            log.auto(contact_encry % {"contact":"Decry","based":"32","time":i*3+3,"total":cal})
            data_decryed = decry_85(data_decryed)
            log.auto(contact_encry % {"contact":"Decry","based":"85","time":i*3+4,"total":cal})
        for i in range(pow(tem,4)):
            data_decryed = decry_32(data_decryed)
            log.auto(contact_encry % {"contact":"Decry","based":"32","time":pow(tem,2)*3+2+i*3,"total":cal})
            data_decryed = decry_64(data_decryed)
            log.auto(contact_encry % {"contact":"Decry","based":"64","time":pow(tem,2)*3+3+i*3,"total":cal})
            data_decryed = decry_85(data_decryed)
            log.auto(contact_encry % {"contact":"Decry","based":"85","time":pow(tem,2)*3+4+i*3,"total":cal})
        log.auto("Done.")
        return data_decryed
    except Exception as e:
        raise Panic("decry_max_auto",str(e),4,"Exception").raise_panic()