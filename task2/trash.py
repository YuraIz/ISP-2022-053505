from xmlrpc.client import Boolean

import types


def get_function_members(function: types.FunctionType):
    members = dict()
    members['doc'] = function.__doc__
    members['name'] = function.__name__
    members['qualname'] = function.__qualname__
    members['code'] = function.__code__
    print(function.__code__.co_code)
    print(function.__code__.__str__())
    members['defaults'] = function.__defaults__
    members['kwdefaults'] = function.__kwdefaults__
    # members['globals'] = function.__globals__
    # members['builtins'] = function.__builtins__
    # members['annotations'] = function.__annotations__
    return members


def code_to_dict(code: types.CodeType):
    items = dict()
    pub_attributes = list(
        filter(lambda item: item.startswith('co'), dir(code)))
    for attr in pub_attributes:
        items[attr] = code.__getattribute__(attr)

    return items


def dict_to_code(dict: dict[str, any]):
    return types.CodeType(
        dict["co_argcount"],
        dict["co_posonlyargcount"],
        dict["co_kwonlyargcount"],
        dict["co_nlocals"],
        dict["co_stacksize"],
        dict["co_flags"],
        dict["co_code"],
        dict["co_consts"],
        dict["co_names"],
        dict["co_varnames"],
        dict["co_filename"],
        dict["co_name"],
        dict["co_firstlineno"],
        dict["co_lnotab"],
        dict["co_freevars"],
        dict["co_cellvars"]
    )


test = code_to_dict(mul.__code__)


def tuple_to_dict(tup: tuple):
    dictionary = dict()
    for i in range(len(tup)):
        dictionary[f"elem{i}"] = tup[i]

    return dictionary


def fix_dict(dictionary: dict[str, any]) -> dict[str, any]:
    for key in dictionary.keys():
        print(type(dictionary[key]))
        if(not isinstance(dictionary[key], str)):
            if(isinstance(dictionary[key], dict)):
                dictionary[key] = fix_dict(dictionary[key])
            elif(isinstance(dictionary[key], tuple)):
                dictionary[key] = tuple_to_dict(dictionary[key])
            elif(isinstance(dictionary[key], (int, float))):
                dictionary[key] = str(dictionary[key])

    return dictionary


def check_dict(dictionary: dict[str, any]) -> Boolean:
    if(isinstance(dictionary, dict)):
        for item in dictionary.items():
            print(type(item))
            if(not isinstance(item, str)):
                if(isinstance(item, dict)):
                    return check_dict(item)
                else:
                    return False
    return True
