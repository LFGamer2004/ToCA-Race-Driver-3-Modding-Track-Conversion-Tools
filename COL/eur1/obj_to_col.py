
import struct

INPUT_FILE = "col.obj"
OUTPUT_FILE = "rebuild.col"

verts = []
faces = []

with open(INPUT_FILE, "r") as f:
    for line in f:
        if line.startswith("v "):
            _, x, y, z = line.strip().split()
            verts.append((float(x), float(y), float(z)))
        elif line.startswith("f "):
            _, i1, i2, i3 = line.strip().split()
            i1, i2, i3 = int(i1) - 1, int(i2) - 1, int(i3) - 1
            faces.append((i1, i2, i3))

with open(OUTPUT_FILE, "wb") as f:
    for v in verts:
        f.write(struct.pack('<3f', v[0], v[1], v[2]))
    for f_ in faces:
        f.write(struct.pack('<3H', *f_))

print(f"Reconstruído: {OUTPUT_FILE} ({len(verts)} vértices, {len(faces)} faces)")
