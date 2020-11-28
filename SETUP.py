import glob
import pip
import subprocess
import shutil


def INSTALLWHLS():
    for path in glob.glob("E:/WHLFILES/*.whl"):
        #pip.main(['install', path])
        subprocess.run(f'python -m pip install {path}')


def MOVWHLS():
    for path in glob.glob("E:/WHLFILES/*.whl"):
        shutil.move(path, "E:/PYWHL/")

    print("FILES MOVED TO E:/PYWHL/")


# INSTALLWHLS()
MOVWHLS()
