
import struct
import sys

def obj_to_red(obj_file, red_file):
    vertices = []

    with open(obj_file, 'r') as f:
        for line in f:
            if line.startswith('v '):
                parts = line.strip().split()
                x, y, z = map(float, parts[1:4])
                param = 0.0
                vertices.append((x, y, z, param))

    with open(red_file, 'wb') as f:
        for v in vertices:
            f.write(struct.pack('<ffff', *v))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python obj_to_red.py arquivo.obj arquivo.red")
    else:
        obj_to_red(sys.argv[1], sys.argv[2])
