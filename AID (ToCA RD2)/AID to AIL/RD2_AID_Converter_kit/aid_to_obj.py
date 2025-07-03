
import struct

input_file = "eur.aid"
output_file = "track_points.obj"

with open(input_file, "rb") as f:
    data = f.read()

offset = 4

floats = []
while offset + 4 <= len(data):
    chunk = data[offset:offset+4]
    if len(chunk) < 4:
        break
    value = struct.unpack('<f', chunk)[0]
    floats.append(value)
    offset += 4

n_blocks = len(floats) // 4
points = [floats[i*4:(i+1)*4] for i in range(n_blocks)]

with open(output_file, "w") as f:
    f.write("# OBJ export\n")
    for p in points:
        x, y, z, param = p
        f.write(f"v {x} {y} {z}\n")
    for i in range(1, len(points)):
        f.write(f"l {i} {i+1}\n")

print(f"Exported OBJ: {output_file}")
