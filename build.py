#!/usr/bin/python 
# -*- coding: utf-8 -*-
import subprocess, os, platform, json, base64

def comResult(type):
    if type == 'config':
        global config, NAME, ICO_B64, MAIN_FILE, LIB_FILE
        with open(file='build.json', mode='r', encoding='utf-8') as configData:
            config = json.loads(configData.read())
            configData.close()
        NAME = str(config['NAME'])
        ICO_B64 = str(config['ICON_BASE64']['no_head'])
        MAIN_FILE = str(config['MAIN_PY_FILE'])
    elif type == 'os':
        global systemType
        systemType = platform.system()

def comGenerate():
    if systemType == 'Windows':
        command = 'J:/Python/Python38/Scripts/pyinstaller ' + MAIN_FILE + ' -D -n ' + NAME + ' -i assets\\ico\\logo.ico'
        if os.path.isdir('dist'):
            os.system('copy *.py dist\\')
            os.system(command)
        else:
            os.mkdir('dist')
            os.system('copy *.py dist\\' + NAME + '\\')
            os.system(command)
    else:
        print('请安装全部依赖库直接执行.py文件!!!!\nPlease install all dependent libraries to execute. Py file directly!!!!')

def comRun():
    comResult(type='config')
    comResult(type='os')
    comGenerate()

if __name__ == "__main__":
    comRun()