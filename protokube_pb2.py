# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protokube.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protokube.proto',
  package='protokube',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0fprotokube.proto\x12\tprotokube\"\x18\n\nBullshitIn\x12\n\n\x02\x62i\x18\x01 \x01(\t\"\x19\n\x0b\x42ullshitOut\x12\n\n\x02\x62o\x18\x01 \x01(\t2O\n\x08Streamer\x12\x43\n\x0eStreamBullshit\x12\x15.protokube.BullshitIn\x1a\x16.protokube.BullshitOut\"\x00\x30\x01\x62\x06proto3')
)




_BULLSHITIN = _descriptor.Descriptor(
  name='BullshitIn',
  full_name='protokube.BullshitIn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bi', full_name='protokube.BullshitIn.bi', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=54,
)


_BULLSHITOUT = _descriptor.Descriptor(
  name='BullshitOut',
  full_name='protokube.BullshitOut',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bo', full_name='protokube.BullshitOut.bo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=81,
)

DESCRIPTOR.message_types_by_name['BullshitIn'] = _BULLSHITIN
DESCRIPTOR.message_types_by_name['BullshitOut'] = _BULLSHITOUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BullshitIn = _reflection.GeneratedProtocolMessageType('BullshitIn', (_message.Message,), {
  'DESCRIPTOR' : _BULLSHITIN,
  '__module__' : 'protokube_pb2'
  # @@protoc_insertion_point(class_scope:protokube.BullshitIn)
  })
_sym_db.RegisterMessage(BullshitIn)

BullshitOut = _reflection.GeneratedProtocolMessageType('BullshitOut', (_message.Message,), {
  'DESCRIPTOR' : _BULLSHITOUT,
  '__module__' : 'protokube_pb2'
  # @@protoc_insertion_point(class_scope:protokube.BullshitOut)
  })
_sym_db.RegisterMessage(BullshitOut)



_STREAMER = _descriptor.ServiceDescriptor(
  name='Streamer',
  full_name='protokube.Streamer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=83,
  serialized_end=162,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamBullshit',
    full_name='protokube.Streamer.StreamBullshit',
    index=0,
    containing_service=None,
    input_type=_BULLSHITIN,
    output_type=_BULLSHITOUT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STREAMER)

DESCRIPTOR.services_by_name['Streamer'] = _STREAMER

# @@protoc_insertion_point(module_scope)