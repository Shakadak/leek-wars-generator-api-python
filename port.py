import json
import os
import struct
import sys

def read():
    in_fd = sys.stdin.fileno()
    b = os.read(in_fd, 4)#buffer.read(4)
    size, = struct.unpack('>i', b)
    data = os.read(sys.stdin.fileno(), size)
    return json.loads(data.decode('utf-8'))

def write(data):
    out_fd = sys.stdout.fileno()
    data = json.dumps(data)
    size = struct.pack('>i', len(data))
    os.write(out_fd, size)
    os.write(out_fd, data.encode('utf-8'))
