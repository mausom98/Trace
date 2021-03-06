from simple_supply_addressing.addresser import AddressSpace
from simple_supply_addressing.addresser import get_address_type
from simple_supply_protobuf.agent_pb2 import AgentContainer
from simple_supply_protobuf.record_pb2 import RecordContainer


CONTAINERS = {
    AddressSpace.AGENT: AgentContainer,
    AddressSpace.RECORD: RecordContainer
}


def deserialize_data(address, data):
    data_type = get_address_type(address)

    if data_type == AddressSpace.OTHER_FAMILY:
        return []

    try:
        container = CONTAINERS[data_type]
    except KeyError:
        raise TypeError('Unknown data type: {}'.format(data_type))

    entries = _parse_proto(container, data).entries
    return data_type, [_convert_proto_to_dict(pb) for pb in entries]


def _parse_proto(proto_class, data):
    deserialized = proto_class()
    deserialized.ParseFromString(data)
    return deserialized


def _convert_proto_to_dict(proto):
    result = {}

    for field in proto.DESCRIPTOR.fields:
        key = field.name
        value = getattr(proto, key)

        if field.type == field.TYPE_MESSAGE:
            if field.label == field.LABEL_REPEATED:
                result[key] = [_convert_proto_to_dict(p) for p in value]
            else:
                result[key] = _convert_proto_to_dict(value)

        elif field.type == field.TYPE_ENUM:
            number = int(value)
            name = field.enum_type.values_by_number.get(number).name
            result[key] = name

        else:
            result[key] = value

    return result
