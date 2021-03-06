import sys
import os
import glob

from caption import caption
from collectcv import collectcv

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("incluir desc, por exemplo, 0.06")
        exit()
    DIRNAME = "c:/Users/Heitor/Desktop/code/imagecaption/original/"
    TARGET_DIRNAME = "c:/Users/Heitor/Desktop/code/imagecaption/anotado/"
    os.chdir(DIRNAME)
    cods = collectcv(desc=str(sys.argv[1]))
    errors = ""
    for fname in glob.glob('**/*.jpg'):
        fname = fname.replace('\\', '/')
        cod = fname.split("/")[-1].split(".")[0].upper()
        # try creating anotado folder

        folder = fname.split('/')[0]
        
        try:
            os.mkdir(TARGET_DIRNAME + folder)
        except FileExistsError:
            pass

        try:
            caption(DIRNAME + fname, cods[cod][1])
            print(fname, cods[cod][0])

        except KeyError:
            errors += "CV de " + cod + " nao existe\n"
        

    print()
    print(errors)
    
