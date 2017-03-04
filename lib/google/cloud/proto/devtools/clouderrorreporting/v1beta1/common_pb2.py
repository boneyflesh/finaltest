# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/proto/devtools/clouderrorreporting/v1beta1/common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import monitored_resource_pb2 as google_dot_api_dot_monitored__resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/proto/devtools/clouderrorreporting/v1beta1/common.proto',
  package='google.devtools.clouderrorreporting.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\nDgoogle/cloud/proto/devtools/clouderrorreporting/v1beta1/common.proto\x12+google.devtools.clouderrorreporting.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a#google/api/monitored_resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x81\x01\n\nErrorGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08group_id\x18\x02 \x01(\t\x12S\n\x0ftracking_issues\x18\x03 \x03(\x0b\x32:.google.devtools.clouderrorreporting.v1beta1.TrackingIssue\"\x1c\n\rTrackingIssue\x12\x0b\n\x03url\x18\x01 \x01(\t\"\xef\x01\n\nErrorEvent\x12.\n\nevent_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12T\n\x0fservice_context\x18\x02 \x01(\x0b\x32;.google.devtools.clouderrorreporting.v1beta1.ServiceContext\x12\x0f\n\x07message\x18\x03 \x01(\t\x12J\n\x07\x63ontext\x18\x05 \x01(\x0b\x32\x39.google.devtools.clouderrorreporting.v1beta1.ErrorContext\"I\n\x0eServiceContext\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x15\n\rresource_type\x18\x04 \x01(\t\"\xc9\x01\n\x0c\x45rrorContext\x12U\n\x0chttp_request\x18\x01 \x01(\x0b\x32?.google.devtools.clouderrorreporting.v1beta1.HttpRequestContext\x12\x0c\n\x04user\x18\x02 \x01(\t\x12T\n\x0freport_location\x18\x03 \x01(\x0b\x32;.google.devtools.clouderrorreporting.v1beta1.SourceLocation\"\x88\x01\n\x12HttpRequestContext\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x12\n\nuser_agent\x18\x03 \x01(\t\x12\x10\n\x08referrer\x18\x04 \x01(\t\x12\x1c\n\x14response_status_code\x18\x05 \x01(\x05\x12\x11\n\tremote_ip\x18\x06 \x01(\t\"O\n\x0eSourceLocation\x12\x11\n\tfile_path\x18\x01 \x01(\t\x12\x13\n\x0bline_number\x18\x02 \x01(\x05\x12\x15\n\rfunction_name\x18\x04 \x01(\tB\xc6\x01\n/com.google.devtools.clouderrorreporting.v1beta1B\x0b\x43ommonProtoP\x01Z^google.golang.org/genproto/googleapis/devtools/clouderrorreporting/v1beta1;clouderrorreporting\xaa\x02#Google.Cloud.ErrorReporting.V1Beta1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_monitored__resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ERRORGROUP = _descriptor.Descriptor(
  name='ErrorGroup',
  full_name='google.devtools.clouderrorreporting.v1beta1.ErrorGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorGroup.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorGroup.group_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tracking_issues', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorGroup.tracking_issues', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=347,
)


_TRACKINGISSUE = _descriptor.Descriptor(
  name='TrackingIssue',
  full_name='google.devtools.clouderrorreporting.v1beta1.TrackingIssue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='google.devtools.clouderrorreporting.v1beta1.TrackingIssue.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=377,
)


_ERROREVENT = _descriptor.Descriptor(
  name='ErrorEvent',
  full_name='google.devtools.clouderrorreporting.v1beta1.ErrorEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_time', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorEvent.event_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='service_context', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorEvent.service_context', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorEvent.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='context', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorEvent.context', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=380,
  serialized_end=619,
)


_SERVICECONTEXT = _descriptor.Descriptor(
  name='ServiceContext',
  full_name='google.devtools.clouderrorreporting.v1beta1.ServiceContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='google.devtools.clouderrorreporting.v1beta1.ServiceContext.service', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='google.devtools.clouderrorreporting.v1beta1.ServiceContext.version', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='google.devtools.clouderrorreporting.v1beta1.ServiceContext.resource_type', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=621,
  serialized_end=694,
)


_ERRORCONTEXT = _descriptor.Descriptor(
  name='ErrorContext',
  full_name='google.devtools.clouderrorreporting.v1beta1.ErrorContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='http_request', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorContext.http_request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorContext.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='report_location', full_name='google.devtools.clouderrorreporting.v1beta1.ErrorContext.report_location', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=697,
  serialized_end=898,
)


_HTTPREQUESTCONTEXT = _descriptor.Descriptor(
  name='HttpRequestContext',
  full_name='google.devtools.clouderrorreporting.v1beta1.HttpRequestContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='google.devtools.clouderrorreporting.v1beta1.HttpRequestContext.method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='google.devtools.clouderrorreporting.v1beta1.HttpRequestContext.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_agent', full_name='google.devtools.clouderrorreporting.v1beta1.HttpRequestContext.user_agent', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='referrer', full_name='google.devtools.clouderrorreporting.v1beta1.HttpRequestContext.referrer', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response_status_code', full_name='google.devtools.clouderrorreporting.v1beta1.HttpRequestContext.response_status_code', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remote_ip', full_name='google.devtools.clouderrorreporting.v1beta1.HttpRequestContext.remote_ip', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=901,
  serialized_end=1037,
)


_SOURCELOCATION = _descriptor.Descriptor(
  name='SourceLocation',
  full_name='google.devtools.clouderrorreporting.v1beta1.SourceLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_path', full_name='google.devtools.clouderrorreporting.v1beta1.SourceLocation.file_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='line_number', full_name='google.devtools.clouderrorreporting.v1beta1.SourceLocation.line_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='function_name', full_name='google.devtools.clouderrorreporting.v1beta1.SourceLocation.function_name', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1039,
  serialized_end=1118,
)

_ERRORGROUP.fields_by_name['tracking_issues'].message_type = _TRACKINGISSUE
_ERROREVENT.fields_by_name['event_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ERROREVENT.fields_by_name['service_context'].message_type = _SERVICECONTEXT
_ERROREVENT.fields_by_name['context'].message_type = _ERRORCONTEXT
_ERRORCONTEXT.fields_by_name['http_request'].message_type = _HTTPREQUESTCONTEXT
_ERRORCONTEXT.fields_by_name['report_location'].message_type = _SOURCELOCATION
DESCRIPTOR.message_types_by_name['ErrorGroup'] = _ERRORGROUP
DESCRIPTOR.message_types_by_name['TrackingIssue'] = _TRACKINGISSUE
DESCRIPTOR.message_types_by_name['ErrorEvent'] = _ERROREVENT
DESCRIPTOR.message_types_by_name['ServiceContext'] = _SERVICECONTEXT
DESCRIPTOR.message_types_by_name['ErrorContext'] = _ERRORCONTEXT
DESCRIPTOR.message_types_by_name['HttpRequestContext'] = _HTTPREQUESTCONTEXT
DESCRIPTOR.message_types_by_name['SourceLocation'] = _SOURCELOCATION

ErrorGroup = _reflection.GeneratedProtocolMessageType('ErrorGroup', (_message.Message,), dict(
  DESCRIPTOR = _ERRORGROUP,
  __module__ = 'google.cloud.proto.devtools.clouderrorreporting.v1beta1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.ErrorGroup)
  ))
_sym_db.RegisterMessage(ErrorGroup)

TrackingIssue = _reflection.GeneratedProtocolMessageType('TrackingIssue', (_message.Message,), dict(
  DESCRIPTOR = _TRACKINGISSUE,
  __module__ = 'google.cloud.proto.devtools.clouderrorreporting.v1beta1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.TrackingIssue)
  ))
_sym_db.RegisterMessage(TrackingIssue)

ErrorEvent = _reflection.GeneratedProtocolMessageType('ErrorEvent', (_message.Message,), dict(
  DESCRIPTOR = _ERROREVENT,
  __module__ = 'google.cloud.proto.devtools.clouderrorreporting.v1beta1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.ErrorEvent)
  ))
_sym_db.RegisterMessage(ErrorEvent)

ServiceContext = _reflection.GeneratedProtocolMessageType('ServiceContext', (_message.Message,), dict(
  DESCRIPTOR = _SERVICECONTEXT,
  __module__ = 'google.cloud.proto.devtools.clouderrorreporting.v1beta1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.ServiceContext)
  ))
_sym_db.RegisterMessage(ServiceContext)

ErrorContext = _reflection.GeneratedProtocolMessageType('ErrorContext', (_message.Message,), dict(
  DESCRIPTOR = _ERRORCONTEXT,
  __module__ = 'google.cloud.proto.devtools.clouderrorreporting.v1beta1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.ErrorContext)
  ))
_sym_db.RegisterMessage(ErrorContext)

HttpRequestContext = _reflection.GeneratedProtocolMessageType('HttpRequestContext', (_message.Message,), dict(
  DESCRIPTOR = _HTTPREQUESTCONTEXT,
  __module__ = 'google.cloud.proto.devtools.clouderrorreporting.v1beta1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.HttpRequestContext)
  ))
_sym_db.RegisterMessage(HttpRequestContext)

SourceLocation = _reflection.GeneratedProtocolMessageType('SourceLocation', (_message.Message,), dict(
  DESCRIPTOR = _SOURCELOCATION,
  __module__ = 'google.cloud.proto.devtools.clouderrorreporting.v1beta1.common_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.clouderrorreporting.v1beta1.SourceLocation)
  ))
_sym_db.RegisterMessage(SourceLocation)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n/com.google.devtools.clouderrorreporting.v1beta1B\013CommonProtoP\001Z^google.golang.org/genproto/googleapis/devtools/clouderrorreporting/v1beta1;clouderrorreporting\252\002#Google.Cloud.ErrorReporting.V1Beta1'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
