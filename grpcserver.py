#!/usr/bin/pythona
# -*- coding: utf-8 -*-

import grpc
from concurrent import futures
import time
import threading

import protokube_pb2
import protokube_pb2_grpc


class StreamerServicer(protokube_pb2_grpc.StreamerServicer):

    def StreamBullshit(self, request, context):
        items = ["pykube1","pykube2", "pykube3" ,"pykube4", "pykube5"]
        print("get that stream going . . .")
        for item in items:
            response = protokube_pb2.BullshitOut()
            response.bo = item
            yield response

def foobar():
    while True:
        print("cycle . . .")
        time.sleep(1)

def startGrpcServer():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    protokube_pb2_grpc.add_StreamerServicer_to_server(
            StreamerServicer(), server)

    # listen on port 50051
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()

    while True:
        time.sleep(86400)
    #except KeyboardInterrupt:
    #    print("shutting down")
    #    server.stop()




