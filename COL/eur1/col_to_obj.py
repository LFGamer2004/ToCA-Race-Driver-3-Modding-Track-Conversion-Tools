
import struct

INPUT_FILE = "col.col"
OUTPUT_FILE = "output.obj"

# === CONFIG ===
vertex_offset = 0
num_vertices = 10000
face_offset = num_vertices * 12
num_faces = 6000

with open(INPUT_FILE, "rb") as f:
    data = f.read()

verts = []
for i in range(num_vertices):
    pos = vertex_offset + i * 12
    x, y, z = struct.unpack('<3f', data[pos:pos+12])
    verts.append((x, y, z))

faces = []
for i in range(num_faces):
    pos = face_offset + i * 6
    i1, i2, i3 = struct.unpack('<3H', data[pos:pos+6])
    faces.append((i1 + 1, i2 + 1, i3 + 1))

with open(OUTPUT_FILE, "w") as f:
    for v in verts:
        f.write(f"v {v[0]} {v[1]} {v[2]}\n")
    for face in faces:
        f.write(f"f {face[0]} {face[1]} {face[2]}\n")

print(f"Exportado para {OUTPUT_FILE} ({len(verts)} vértices, {len(faces)} faces)")
