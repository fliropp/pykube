#!/usr/bin/pythona
# -*- coding: utf-8 -*-

import time
import grpcserver
import threading

if __name__ == "__main__":
    print("WTF???")
    grpcs = threading.Thread(target=grpcserver.startGrpcServer, args=())
    #bogus = threading.Thread(target=grpcserver.foobar, args=())

    print("WTF?????")
    grpcs.deamon=True
    grpcs.start()
    #bogus.start()
    #bogus.join()

