
import struct

input_obj = "track_points.obj"
output_ail = "new_track.ail"
default_param = 5.0

points = []

with open(input_obj, "r") as f:
    for line in f:
        if line.startswith("v "):
            parts = line.strip().split()
            if len(parts) == 4:
                x, y, z = map(float, parts[1:4])
                points.append([x, y, z, default_param])

with open(output_ail, "wb") as f:
    f.write(b'AILD')
    for p in points:
        f.write(struct.pack('<ffff', *p))

print(f"Exported AIL: {output_ail}")
