# ui_loader.py
# Convert .ui to .py 
# To make autocomplet in IDE
# Ref : https://stackoverflow.com/questions/58770646/autocomplete-from-ui
 
from distutils.dep_util import newer
import os
from PyQt5 import uic
 
 
def ui_auto_complete(ui_dir, ui_to_py_dir):
    encoding = 'utf-8'
 
    if not os.path.isfile(ui_dir):
        print("The required file does not exist.")
        return
     
    if not newer(ui_dir, ui_to_py_dir):
        print("UI has not changed!")
    else:
        print("UI changed detected, compiling...")        
        fp = open(ui_to_py_dir, "w", encoding=encoding)        
        uic.compileUi(ui_dir, fp,
                      execute=True, indent=4, from_imports=True)
        fp.close()


if __name__ == "__main__" :
    ui_auto_complete("main.ui", "main_ui.py")