#!/usr/bin/python 
# -*- coding: utf-8 -*-
__NAME__ = 'CoolVMTerminaler'
__ID__ = 'cool_vm_terminaler'
__GROUP__ = '.'
__RED__ = '\033[31;1m'
__GREEN__ = '\033[32;1m'
class CoolVMTerminaler(object):
    def __init__(self):
        pass

    def init(self):
        pass

    def run(self):
        pass

class CoolVMTerminalerAPI(CoolVMTerminaler):
    def __init__(self):
        super(CoolVMTerminalerAPI, self).__init__()

    def init(self):
        pass

    def run(self):
        pass


if __name__ == "__main__":
    app = CoolVMTerminaler()
    app_api = CoolVMTerminalerAPI()
    app.init()
    app_api.init()
    app.run()
    app_api.run()