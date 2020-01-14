#!/usr/bin/pythona
# -*- coding: utf-8 -*-

import grpc
from concurrent import futures
import time
import threading

import protokube_pb2
import protokube_pb2_grpc


class BiStreamerServicer(protokube_pb2_grpc.BiStreamerServicer):

    def BidirectionalStream(self, request_iterator, context):
        print("get that stream going . . .")
        for item in request_iterator:
            print(item)
            response = protokube_pb2.Vessel()
            print(response)
            response.Val = item.Val + 1
            time.sleep(1)
            yield response

def startGrpcServer():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    protokube_pb2_grpc.add_BiStreamerServicer_to_server(
            BiStreamerServicer(), server)

    # listen on port 50051
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()

    while True:
        time.sleep(86400)
    #except KeyboardInterrupt:
    #    print("shutting down")
    #    server.stop()




