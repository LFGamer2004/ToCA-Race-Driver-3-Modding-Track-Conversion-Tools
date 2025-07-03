
import struct
import csv
import json

INPUT_FILE = "phi1.ail"

with open(INPUT_FILE, "rb") as f:
    data = f.read()

# Cabeçalho hipotético: 4 bytes
header = data[:4]
meta = {
    "header": header.decode(errors="ignore"),
    "file_size": len(data)
}

offset = 4
vertices = []
connections = []

while offset + 12 <= len(data):
    try:
        x, y, z = struct.unpack('<3f', data[offset:offset+12])
        if -100000 < x < 100000 and -100000 < y < 100000 and -100000 < z < 100000:
            vertices.append([x, y, z])
            offset += 12
        else:
            break
    except:
        break

meta["vertex_count"] = len(vertices)

conn_offset = offset
while conn_offset + 4 <= len(data):
    a, b = struct.unpack('<HH', data[conn_offset:conn_offset+4])
    if a < len(vertices) and b < len(vertices):
        connections.append([a, b])
        conn_offset += 4
    else:
        break

meta["connection_count"] = len(connections)

with open("vertices.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "X", "Y", "Z"])
    for idx, (x, y, z) in enumerate(vertices):
        writer.writerow([idx, x, y, z])

with open("connections.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["From_ID", "To_ID"])
    for pair in connections:
        writer.writerow(pair)

with open("meta.json", "w") as f:
    json.dump(meta, f, indent=4)

print("AIL ➜ CSV concluído! Gerados: vertices.csv, connections.csv, meta.json")
