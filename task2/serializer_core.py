
import types


def serialize(item):
    def serialize_elements(item):
        elements = dict()
        for i in range(len(item)):
            elements[f"el{i}"] = serialize(item[i])
        return elements

    def serialize_pub_attribs(item):
        elements = dict()
        pub_attributes = list(
            filter(lambda item: not item.startswith('_'), dir(item)))
        for attr in pub_attributes:
            elements[attr] = serialize(item.__getattribute__(attr))
        return elements

    if isinstance(item, int | str):
        return item
    elif isinstance(item, tuple):
        return {"tuple": serialize_elements(item)}
    elif isinstance(item, list):
        return {"list": serialize_elements(item)}
    elif isinstance(item, dict):
        return {"dict": item}
    elif isinstance(item, bytes):
        return {"bytes": item.hex()}
    elif isinstance(item, types.MappingProxyType):
        item_dict = dict(item)
        for key in item_dict.keys():
            item_dict[key] = serialize(item_dict[key])
        print("hello")
        return item_dict

    elif isinstance(item, types.CodeType):
        return {"code": serialize_pub_attribs(item)}
    elif isinstance(item, types.FunctionType):
        return {"func": serialize(item.__code__)}
    elif isinstance(item, type):
        attribs_dict = dict(item.__dict__)
        for key in attribs_dict.keys():
            attribs_dict[key] = serialize(attribs_dict[key])
        attribs_dict['__annotations__'] = None
        return {"type": {"name": item.__name__, "attribs": attribs_dict}}


def deserialize(item: dict[str, any]):
    if not isinstance(item, dict):
        return item

    for (key, value) in item.items():
        if(key == 'tuple'):
            return tuple([deserialize(element) for element in value.values()])
        elif(key == 'list'):
            return [deserialize(element) for element in value.values()]
        elif(key == 'dict'):
            return value
        elif(key == 'bytes'):
            return bytes.fromhex(value)
        elif(isinstance(value, int | float | str)):
            return value

        elif(key == 'type'):
            attribs = value['attribs']
            for key in attribs.keys():
                attribs[key] = deserialize(attribs[key])

            print(value['name'])

            return type(
                value['name'],
                (),
                attribs
            )

        elif(key == 'func'):
            def func(): pass
            func.__code__ = deserialize(value)
            return func

        elif(key == 'code'):
            return types.CodeType(
                deserialize(value["co_argcount"]),
                deserialize(value["co_posonlyargcount"]),
                deserialize(value["co_kwonlyargcount"]),
                deserialize(value["co_nlocals"]),
                deserialize(value["co_stacksize"]),
                deserialize(value["co_flags"]),
                deserialize(value["co_code"]),
                deserialize(value["co_consts"]),
                deserialize(value["co_names"]),
                deserialize(value["co_varnames"]),
                "deserialized",  # deserialize(value["co_filename"]),
                deserialize(value["co_name"]),
                deserialize(value["co_firstlineno"]),
                deserialize(value["co_lnotab"]),
                deserialize(value["co_freevars"]),
                deserialize(value["co_cellvars"])
            )
