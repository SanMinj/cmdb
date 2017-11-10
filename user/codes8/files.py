#encoding: utf-8
import os
import sys

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
    if len(sys.argv) < 2:
        print 'usage: python files.py dirpath'
        sys.exit(-1)
    
    print get_files(sys.argv[1])
        