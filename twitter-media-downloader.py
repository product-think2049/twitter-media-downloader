'''
Author: mengzonefire
Date: 2021-09-21 15:48:35
LastEditTime: 2021-09-26 01:20:34
LastEditors: mengzonefire
Description: 程序主函数入口
'''
import sys
import os
from common.const import *
from common.text import *
from common.tools import *
from common.console import cmdMode
from common.exceptHandler import except_handler


def main():
    exe_path, exe_name = os.path.split(sys.argv[0])
    if exe_path:
        os.chdir(exe_path)  # 切换工作目录到程序根目录
    initalArgs()
    getEnv()
    if len(sys.argv) == 1:  # 命令行参数为空 -> 双击运行程序
        print('version: {}\nissue page: {}\n'.format(version, issue_page))
        checkUpdate()
        getProxy()
        getHeader()
        cmdMode()
    else:
        argsHandler()
    saveEnv()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        except_handler(e)
        if input(reset_ask):
            if sys.platform in ['win32', 'win64']:  # 判断是否为win平台
                os.system('cls')
            else:
                os.system('clear')
            main()
