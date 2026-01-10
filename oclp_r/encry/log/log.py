import logging,getpass,os,multiprocessing
from oclp_r.encry.panic.panic import *
import os
if os.name == 'nt':  
    import colorama
    colorama.init()  
class ProcessNameFormatter(logging.Formatter):
    def format(self, record):
        record.process_name = multiprocessing.current_process().name
        return super().format(record)
class ColoredFormatter(ProcessNameFormatter):
    """为不同日志级别添加颜色的格式化器"""
    COLOR_CODES = {
        'DEBUG': '\033[0;36m',  # 青色
        'INFO': '\033[0;32m',   # 绿色
        'WARNING': '\033[1;33m', # 黄色
        'ERROR': '\033[1;31m',   # 红色
        'CRITICAL': '\033[1;41m' # 红色背景
    }
    RESET_CODE = '\033[0m'

    def format(self, record):
        # 先调用父类方法格式化
        formatted_message = super().format(record)
        # 根据日志级别添加颜色
        color = self.COLOR_CODES.get(record.levelname, '')
        if color:
            return f"{color}{formatted_message}{self.RESET_CODE}"
        return formatted_message
class LogManager:
    def __init__(self,log_name,log_level="INFO",write_info=False,no_files=True,no_console=True,no_debug=False,no_log=False):
        
        self.log_level = log_level.upper()#日志级别
        self.write_info=write_info#是否写入INFO级别日志
        self.no_files=no_files#是否创建日志文件
        self.no_console=no_console#是否输出到控制台
        self.log_name = log_name#日志名称(通常为函数)
        self.no_debug=no_debug#是否输出DEBUG级别日志(文件+控制台)
        self.no_log=no_log#是否输出日志
        if self.no_log:
            return
        if(log_level is None or (log_level!="DEBUG" and log_level!="INFO" and log_level!="WARNING" and log_level!="ERROR" and log_level!="CRITICAL")):
            raise Panic("LogManager__init__",f"Log_level must str,not None.",3,"LogManager").raise_panic()
        # 日志级别映射
        self.LEVELS = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }
        self.logger = logging.getLogger(self.log_name)
        self.logger.setLevel(self.LEVELS[self.log_level])
        if os.name == 'nt':  
            self.path = os.path.join(os.environ["APPDATA"],".encry","log")
        elif os.name == 'posix':
            self.path=f"/Users/{getpass.getuser()}/.encry/log/encry_{log_level}.log"
        else:
            self.path = f"/var/log/encry/log/encry_{log_level}.log"
        try:
            os.makedirs(os.path.dirname(self.path))
        except Exception:
            pass
        self.formatter = ProcessNameFormatter(
            '%(asctime)s - %(process_name)s - %(name)s  - %(levelname)s - %(message)s'   
        )
        if (self.log_level!="INFO".upper() or self.write_info) and not self.no_files and not self.no_log:
            self.file_handler = logging.FileHandler(self.path)
            self.file_handler.setLevel(self.LEVELS[self.log_level])
            self.file_formatter = self.formatter
            self.file_handler.setFormatter(self.file_formatter)
        elif self.log_level=="DEBUG".upper() and not self.no_files and not self.no_log and not self.no_debug:
            self.file_handler = logging.FileHandler(self.path)
            self.file_handler.setLevel(self.LEVELS[self.log_level])
            self.file_formatter = self.formatter
            self.file_handler.setFormatter(self.file_formatter)
        # 创建控制台处理器
        self.console_formatter = ColoredFormatter(
            '%(asctime)s - %(process_name)s - %(name)s - %(message)s - %(levelname)s'
        )
        if(not self.no_console and not self.no_log):    
            self.console_handler = logging.StreamHandler()
            self.console_handler.setLevel(self.LEVELS[self.log_level])
            self.console_handler.setFormatter(self.console_formatter)
        # 添加处理器
        if (self.log_level!="INFO".upper() or write_info) and not self.no_files:
            self.logger.addHandler(self.file_handler)
        #self.logger.addHandler(self.file_handler)
        if(not self.no_console and not self.no_log):
            self.logger.addHandler(self.console_handler)
    def info(self, msg):
        if self.no_log:
            return
        if(self.log_level!="info".upper() and self.log_level is not None):
            raise Panic("info",f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
        self.logger.info(msg)
    def warning(self, msg):
        if self.no_log:
            return
        if(self.log_level!="warning".upper() and self.log_level is not None):
            raise Panic("warning",f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
        self.logger.warning(msg)
    def error(self, msg):
        if self.no_log:
            return
        if(self.log_level!="error".upper() and self.log_level is not None):
            raise Panic("error",f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
        self.logger.error(msg)
    def debug(self, msg):
        if self.no_log:
            return
        if(self.log_level!="debug".upper() and self.log_level is not None):
            raise Panic("debug",f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
        self.logger.debug(msg)
    def critical(self, msg):
        if self.no_log:
            return
        if(self.log_level!="critical".upper()):
            raise Panic("critical",f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
        self.logger.critical(msg)
    def auto(self, msg):
        if self.no_log:
            return
        if self.log_level is  None:
            raise Panic("auto",f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
        elif(self.log_level=="DEBUG".upper()):
            self.logger.debug(msg)
        elif(self.log_level=="info".upper()):
            self.logger.info(msg)
        elif(self.log_level=="warning".upper()):
            self.logger.warning(msg)
        elif(self.log_level=="error".upper()):
            self.logger.error(msg)
        elif(self.log_level=="critical".upper()):
            self.logger.critical(msg)
        else:
            raise Panic("auto",f"Use incorrect log level.You:{self.log_level}",3,"LogManager").raise_panic()
    

    

