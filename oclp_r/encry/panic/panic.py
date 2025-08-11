from contextlib import redirect_stderr
from termcolor import cprint
from colorama import init
init()
class Panic(Exception):
    def __init__(self,name,log,level: int,type_panic: str):
        self.log =log
        self.name=name
        self.level =level
        self.type_panic =type_panic
        super().__init__(f"{type_panic}({level}): {log}")

    def panic(self,log):
        logl=log.split('\n')
        return logl
    def raise_panic(self):
        level_lookup={
            1:'Warning',
            2:'Error',
            3:'Serious',
            4:'Panic',
        }
        color='red'
        if self.level==1:
            color='yellow'
        cprint("PANIC: (FROM ENCRY.PANIC.PANIC)",color)
        cprint(f"LEVEL: {level_lookup[self.level]}",color)
        cprint(f'SOURCE: {self.name}',color)
        contact=self.panic(self.log)
        cprint(f'{self.type_panic}:', color,None,["reverse","underline","blink"])
        for i in contact:
            cprint(i.strip(),color,None,["reverse","underline","blink"])
        if self.level>=3:
            cprint("Please report https://github.com/pyquick/pyquick/issues/ to report this panic.".strip(),color,None)
            exit(self.level)
        else:
            return None
