# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import protokube_pb2 as protokube__pb2


class StreamerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.StreamBullshit = channel.unary_stream(
        '/protokube.Streamer/StreamBullshit',
        request_serializer=protokube__pb2.BullshitIn.SerializeToString,
        response_deserializer=protokube__pb2.BullshitOut.FromString,
        )


class StreamerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def StreamBullshit(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StreamerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'StreamBullshit': grpc.unary_stream_rpc_method_handler(
          servicer.StreamBullshit,
          request_deserializer=protokube__pb2.BullshitIn.FromString,
          response_serializer=protokube__pb2.BullshitOut.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'protokube.Streamer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
