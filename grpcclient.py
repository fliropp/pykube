import grpc

import pykube_pb2
import pykube_pb2_grpc

def grpcPing():
    print("running request...")
    channel = grpc.insecure_channel('localhost:50051')
    stub = pykube_pb2_grpc.PingStub(channel)
    req = pykube_pb2.PingReq(request="ping")
    print("getting some ping...")
    response = stub.GetPing(req)
    print("got some ping . . . ?")
    return response.response

print("run request . . .")
grpcPing()