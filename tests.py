from pathlib import Path
kext_path = Path('/Library/Extensions/VoodooHDA.kext')
import os
if os.path.exists(kext_path):
    print(1)