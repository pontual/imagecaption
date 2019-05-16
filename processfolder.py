import os
import glob

from caption import caption
from collectcv import collectcv

if __name__ == "__main__":
    DIRNAME = "c:/Users/Heitor/Desktop/code/imagecaption/original/"
    TARGET_DIRNAME = "c:/Users/Heitor/Desktop/code/imagecaption/anotado/"
    os.chdir(DIRNAME)
    cods = collectcv(desc="0.06")
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
            caption(DIRNAME + fname, cods[cod])
        except KeyError:
            print("Codigo para", cod, "nao existe")
        
