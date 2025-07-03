
import struct
import pandas as pd

input_obj = "track_points.obj"
input_csv = "track_params.csv"
output_ail = "new_track.ail"

points = []

with open(input_obj, "r") as f:
    for line in f:
        if line.startswith("v "):
            parts = line.strip().split()
            if len(parts) == 4:
                x, y, z = map(float, parts[1:4])
                points.append([x, y, z])

print(f"Found {len(points)} vertices")

df = pd.read_csv(input_csv)
params = df['Param'].tolist()

if len(params) != len(points):
    raise ValueError("Vertex count and Param count do not match!")

with open(output_ail, "wb") as f:
    f.write(b'AILD')
    for (x, y, z), param in zip(points, params):
        f.write(struct.pack('<ffff', x, y, z, param))

print(f"Exported AIL: {output_ail}")
