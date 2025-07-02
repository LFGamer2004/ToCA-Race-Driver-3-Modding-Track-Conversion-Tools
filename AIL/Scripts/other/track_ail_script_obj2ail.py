import struct

# Caminhos de entrada/sa�da
input_file = "track.ail"   # Substitua pelo nome do seu arquivo .AIL
output_file = "track_points.obj"

# Abrir arquivo bin�rio
with open(input_file, "rb") as f:
    data = f.read()

# Pular assinatura m�gica "AILD" (4 bytes)
offset = 4

# Ler blocos de 4 floats
floats = []
while offset + 4 <= len(data):
    chunk = data[offset:offset+4]
    if len(chunk) < 4:
        break
    value = struct.unpack('<f', chunk)[0]
    floats.append(value)
    offset += 4

# Agrupar em blocos de 4
n_blocks = len(floats) // 4
points = [floats[i*4:(i+1)*4] for i in range(n_blocks)]

# Gerar arquivo OBJ
with open(output_file, "w") as f:
    f.write("# OBJ export of ToCA Race Driver 3 track points\n")
    # V�rtices
    for p in points:
        x, y, z, param = p
        f.write(f"v {x} {y} {z}\n")
    # Linhas conectando v�rtices em sequ�ncia
    for i in range(1, len(points)):
        f.write(f"l {i} {i+1}\n")

print(f"Arquivo OBJ salvo como: {output_file}")