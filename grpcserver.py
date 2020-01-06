import grpc
from concurrent import futures
import time

import pykube_pb2
import pykube_pb2_grpc


class PingServicer(pykube_pb2_grpc.PingServicer):

    def GetPing(self, request, context):
        print("got request . . .")
        response = pykube_pb2.PingResp()
        response.response = "pong"
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

pykube_pb2_grpc.add_PingServicer_to_server(
        PingServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        print("server cycle . . .")
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)