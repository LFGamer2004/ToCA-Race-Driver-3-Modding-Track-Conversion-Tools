
import struct
import sys

def red_to_obj(red_file, obj_file):
    with open(red_file, 'rb') as f:
        data = f.read()

    num_floats = len(data) // 4
    floats = struct.unpack('<' + 'f'*num_floats, data)

    points = [floats[i:i+4] for i in range(0, len(floats), 4)]

    with open(obj_file, 'w') as f:
        for p in points:
            f.write(f"v {p[0]} {p[1]} {p[2]}\n")
        f.write("\n")
        for i in range(1, len(points)):
            f.write(f"l {i} {i+1}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python red_to_obj.py arquivo.red arquivo.obj")
    else:
        red_to_obj(sys.argv[1], sys.argv[2])
