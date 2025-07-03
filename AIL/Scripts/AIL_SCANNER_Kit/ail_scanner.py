
import struct
import json
import csv

INPUT_FILE = "input.ail"

with open(INPUT_FILE, "rb") as f:
    data = f.read()

# Vamos supor header de 4 bytes 'AIL0'
header = data[:4]
meta = {
    "header": header.decode(errors="ignore"),
    "file_size": len(data)
}

# Tentativa: depois do header, ler blocos de XYZ + conexões
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

# Busca possíveis blocos de conexões (pares de unsigned short?)
# Padrão: 2 bytes cada, então 4 bytes = 2 índices
conn_offset = offset
while conn_offset + 4 <= len(data):
    a, b = struct.unpack('<HH', data[conn_offset:conn_offset+4])
    if a < len(vertices) and b < len(vertices):
        connections.append([a, b])
        conn_offset += 4
    else:
        break

meta["connection_count"] = len(connections)

# Salva vertices.csv
with open("vertices.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "X", "Y", "Z"])
    for idx, (x, y, z) in enumerate(vertices):
        writer.writerow([idx, x, y, z])

# Salva connections.csv
with open("connections.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["From_ID", "To_ID"])
    for pair in connections:
        writer.writerow(pair)

# Salva meta.json
with open("meta.json", "w") as f:
    json.dump(meta, f, indent=4)

print("Scanner concluído! Arquivos gerados: vertices.csv, connections.csv, meta.json")
