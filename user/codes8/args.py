#encoding: utf-8
import os
import sys
import argparse

def get_files(dirpath):
    _rt_list = []
    if os.path.isdir(dirpath):
        _names = os.listdir(dirpath)
        for _name in _names:
            _path = dirpath + '/' + _name
            if os.path.isdir(_path):
                _rt_list.extend(get_files(_path))
            elif _path.endswith('.py'):
                _rt_list.append(_path)

    return _rt_list


if __name__ == '__main__':
    _parser = argparse.ArgumentParser()
    _parser.add_argument('-H', '--host', help="connect host ip addr", default="localhost")
    _parser.add_argument('-P', '--port', help="connect host port addr", type=int, default=80)
    _parser.add_argument('-C', '--cmds', help="excute cmd", nargs='+', default=[])
    _args = _parser.parse_args()
    #1. cmds不能为空list
    if len(_args.cmds) == 0:
        _parser.print_help()
        sys.exit(-1)

    print _args
    print 'success'

