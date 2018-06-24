#!D:\pythonwork\test\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'landslide==1.1.3','console_scripts','landslide'
__requires__ = 'landslide==1.1.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('landslide==1.1.3', 'console_scripts', 'landslide')()
    )
