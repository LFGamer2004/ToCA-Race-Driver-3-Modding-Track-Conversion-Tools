import struct
import csv

OUTPUT_FILE = "eur1.ail"

vertices = []
connections = []

with open("vertices.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        x, y, z = float(row["X"]), float(row["Y"]), float(row["Z"])
        vertices.append((x, y, z))

with open("connections.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        a, b = int(row["From_ID"]), int(row["To_ID"])
        connections.append((a, b))

with open(OUTPUT_FILE, "wb") as f:
    # Escreve cabeçalho simples
    f.write(b"AILF")

    # Escreve vértices
    for x, y, z in vertices:
        f.write(struct.pack('<3f', x, y, z))

    # Escreve conexões
    for a, b in connections:
        f.write(struct.pack('<HH', a, b))

print(f"Reconstruído: {OUTPUT_FILE} (Vértices: {len(vertices)}, Ligações: {len(connections)})")
