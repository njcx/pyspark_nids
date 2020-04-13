# -*- coding: utf-8 -*-
# @Author  : nJcx
# @Email   : njcx86@gmail.com

from utils.log_ import Logger
logger = Logger.get_logger(__name__)

try:
    import orjson as json
except ImportError:
    try:
        import ujson as json
    except ImportError:
        import json


def json_to_py(str_):

    try:
        return json.loads(str_)
    except Exception as e:
        logger.error(str(e))
        return {}


def py_to_json(data_):
    try:
        return json.dumps(data_)
    except Exception as e:
        logger.error(str(e))
        return '{}'


def json_write_to_file(path, json_str=None, py_data_struct=None):
    try:
        if json_str:
            with open(path, 'a') as f:
                f.write(str(json_str, 'utf-8') + "\n")
                return True
        if py_data_struct:
            with open(path, 'a') as f:
                f.write(str(py_to_json(py_data_struct), 'utf-8') + "\n")
                return True
    except Exception as e:
        logger.error(str(e))
        return False


def json_file_to_py(path):
    import json
    try:
        with open(path, 'r') as load_f:
            return json.load(load_f)
    except Exception as e:
        logger.error(str(e))
        return {}


if __name__ == '__main__':

    data = {
        'no': 1,
        'name': 'njcx',
        'url': 'http://www.chaiji.com'
    }

    json_str = py_to_json(data)
    print("Python 原始数据：", repr(data))
    print("JSON 对象：", json_str)

    json_write_to_file("/log/test.log", py_data_struct=data)
    json_write_to_file("/log/test.log", json_str=json_str)