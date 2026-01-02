from pathlib import Path
from oclp_r.encry import as2
import threading
import os
from .. import constants
from .translate_language import TranslateLanguage
class PRIVATE:
    def __init__(self):
        self.constants: constants.Constants = constants.Constants()
        self.trans: dict = TranslateLanguage(self.constants).private()
        self.base_path= Path("~/Library/Logs/Hackdoc/PRIVATE").expanduser()
        if not self.base_path.exists():
            self.base_path.mkdir()
        self.filepath=Path(self.base_path,".PRIVATE")
        if not self.filepath.exists():
            self.filepath.touch()
        if self.check():
            threading.Thread(target=self.write,daemon=True).start()    
    def check(self):
        path=Path("~/.hackdoc_developer").expanduser()
        if path.exists():
            return True
        os.remove(self.filepath)
    def write(self):
        import json
        print(self.trans["writing"])
        soc = Path("~/Library/Logs/Hackdoc/JSON/control.json").expanduser()
        
        # 读取并解析JSON文件
        try:
            with open(soc, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(self.trans["File {0} not found"].format(soc))
            return
        except json.JSONDecodeError:
            print(self.trans["Invalid JSON in file {0}"].format(soc))
            return
        
        # 处理数据
        for key in data:
            if data[key] != "1":
                data[key] = "1"
        
        data=str(data)
        # 写入加密后的数据到文件
        self.filepath.write_text(data)

            