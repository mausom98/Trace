# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simple_supply_protobuf/payload.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='simple_supply_protobuf/payload.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$simple_supply_protobuf/payload.proto\"\xde\x02\n\x13SimpleSupplyPayload\x12+\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x1b.SimpleSupplyPayload.Action\x12(\n\x0c\x63reate_agent\x18\x02 \x01(\x0b\x32\x12.CreateAgentAction\x12*\n\rcreate_record\x18\x03 \x01(\x0b\x32\x13.CreateRecordAction\x12*\n\rupdate_record\x18\x04 \x01(\x0b\x32\x13.UpdateRecordAction\x12.\n\x0ftransfer_record\x18\x05 \x01(\x0b\x32\x15.TransferRecordAction\x12\x11\n\ttimestamp\x18\x06 \x01(\x04\"U\n\x06\x41\x63tion\x12\x10\n\x0c\x43REATE_AGENT\x10\x00\x12\x11\n\rCREATE_RECORD\x10\x01\x12\x11\n\rUPDATE_RECORD\x10\x02\x12\x13\n\x0fTRANSFER_RECORD\x10\x03\"!\n\x11\x43reateAgentAction\x12\x0c\n\x04name\x18\x01 \x01(\t\"L\n\x12\x43reateRecordAction\x12\x11\n\trecord_id\x18\x01 \x01(\t\x12\x10\n\x08latitude\x18\x02 \x01(\x12\x12\x11\n\tlongitude\x18\x03 \x01(\x12\"L\n\x12UpdateRecordAction\x12\x11\n\trecord_id\x18\x01 \x01(\t\x12\x10\n\x08latitude\x18\x02 \x01(\x12\x12\x11\n\tlongitude\x18\x03 \x01(\x12\"B\n\x14TransferRecordAction\x12\x11\n\trecord_id\x18\x01 \x01(\t\x12\x17\n\x0freceiving_agent\x18\x02 \x01(\tb\x06proto3'
)



_SIMPLESUPPLYPAYLOAD_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='SimpleSupplyPayload.Action',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CREATE_AGENT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATE_RECORD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_RECORD', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRANSFER_RECORD', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=306,
  serialized_end=391,
)
_sym_db.RegisterEnumDescriptor(_SIMPLESUPPLYPAYLOAD_ACTION)


_SIMPLESUPPLYPAYLOAD = _descriptor.Descriptor(
  name='SimpleSupplyPayload',
  full_name='SimpleSupplyPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='SimpleSupplyPayload.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_agent', full_name='SimpleSupplyPayload.create_agent', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_record', full_name='SimpleSupplyPayload.create_record', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_record', full_name='SimpleSupplyPayload.update_record', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transfer_record', full_name='SimpleSupplyPayload.transfer_record', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='SimpleSupplyPayload.timestamp', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SIMPLESUPPLYPAYLOAD_ACTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=391,
)


_CREATEAGENTACTION = _descriptor.Descriptor(
  name='CreateAgentAction',
  full_name='CreateAgentAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CreateAgentAction.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=393,
  serialized_end=426,
)


_CREATERECORDACTION = _descriptor.Descriptor(
  name='CreateRecordAction',
  full_name='CreateRecordAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='record_id', full_name='CreateRecordAction.record_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='CreateRecordAction.latitude', index=1,
      number=2, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='CreateRecordAction.longitude', index=2,
      number=3, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=428,
  serialized_end=504,
)


_UPDATERECORDACTION = _descriptor.Descriptor(
  name='UpdateRecordAction',
  full_name='UpdateRecordAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='record_id', full_name='UpdateRecordAction.record_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='UpdateRecordAction.latitude', index=1,
      number=2, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='UpdateRecordAction.longitude', index=2,
      number=3, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=506,
  serialized_end=582,
)


_TRANSFERRECORDACTION = _descriptor.Descriptor(
  name='TransferRecordAction',
  full_name='TransferRecordAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='record_id', full_name='TransferRecordAction.record_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receiving_agent', full_name='TransferRecordAction.receiving_agent', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=584,
  serialized_end=650,
)

_SIMPLESUPPLYPAYLOAD.fields_by_name['action'].enum_type = _SIMPLESUPPLYPAYLOAD_ACTION
_SIMPLESUPPLYPAYLOAD.fields_by_name['create_agent'].message_type = _CREATEAGENTACTION
_SIMPLESUPPLYPAYLOAD.fields_by_name['create_record'].message_type = _CREATERECORDACTION
_SIMPLESUPPLYPAYLOAD.fields_by_name['update_record'].message_type = _UPDATERECORDACTION
_SIMPLESUPPLYPAYLOAD.fields_by_name['transfer_record'].message_type = _TRANSFERRECORDACTION
_SIMPLESUPPLYPAYLOAD_ACTION.containing_type = _SIMPLESUPPLYPAYLOAD
DESCRIPTOR.message_types_by_name['SimpleSupplyPayload'] = _SIMPLESUPPLYPAYLOAD
DESCRIPTOR.message_types_by_name['CreateAgentAction'] = _CREATEAGENTACTION
DESCRIPTOR.message_types_by_name['CreateRecordAction'] = _CREATERECORDACTION
DESCRIPTOR.message_types_by_name['UpdateRecordAction'] = _UPDATERECORDACTION
DESCRIPTOR.message_types_by_name['TransferRecordAction'] = _TRANSFERRECORDACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimpleSupplyPayload = _reflection.GeneratedProtocolMessageType('SimpleSupplyPayload', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLESUPPLYPAYLOAD,
  '__module__' : 'simple_supply_protobuf.payload_pb2'
  # @@protoc_insertion_point(class_scope:SimpleSupplyPayload)
  })
_sym_db.RegisterMessage(SimpleSupplyPayload)

CreateAgentAction = _reflection.GeneratedProtocolMessageType('CreateAgentAction', (_message.Message,), {
  'DESCRIPTOR' : _CREATEAGENTACTION,
  '__module__' : 'simple_supply_protobuf.payload_pb2'
  # @@protoc_insertion_point(class_scope:CreateAgentAction)
  })
_sym_db.RegisterMessage(CreateAgentAction)

CreateRecordAction = _reflection.GeneratedProtocolMessageType('CreateRecordAction', (_message.Message,), {
  'DESCRIPTOR' : _CREATERECORDACTION,
  '__module__' : 'simple_supply_protobuf.payload_pb2'
  # @@protoc_insertion_point(class_scope:CreateRecordAction)
  })
_sym_db.RegisterMessage(CreateRecordAction)

UpdateRecordAction = _reflection.GeneratedProtocolMessageType('UpdateRecordAction', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERECORDACTION,
  '__module__' : 'simple_supply_protobuf.payload_pb2'
  # @@protoc_insertion_point(class_scope:UpdateRecordAction)
  })
_sym_db.RegisterMessage(UpdateRecordAction)

TransferRecordAction = _reflection.GeneratedProtocolMessageType('TransferRecordAction', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERRECORDACTION,
  '__module__' : 'simple_supply_protobuf.payload_pb2'
  # @@protoc_insertion_point(class_scope:TransferRecordAction)
  })
_sym_db.RegisterMessage(TransferRecordAction)


# @@protoc_insertion_point(module_scope)
