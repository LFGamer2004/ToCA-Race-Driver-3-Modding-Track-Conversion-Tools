import struct
import zlib

# === CONFIG ===
INPUT_FILE = 'eur.aid'
DECODED_FILE = 'eur_decoded.bin'
OUTPUT_OBJ = 'waypoints.obj'
XOR_KEY = 0x55  # Tente mudar, ex: 0xAA, 0xFF

# === Ler arquivo ===
with open(INPUT_FILE, 'rb') as f:
    data = f.read()

# === XOR Decode ===
decoded = bytes([b ^ XOR_KEY for b in data])

with open(DECODED_FILE, 'wb') as f:
    f.write(decoded)

print(f'Decode XOR com chave {XOR_KEY} salvo em {DECODED_FILE}')

# === Tentar decompress ===
try:
    decompressed = zlib.decompress(decoded)
    print('Sucesso: dado era zlib!')
except:
    decompressed = decoded
    print('Não é zlib ou falhou decompress — usando cru.')

# === Extrair floats e gerar OBJ ===
floats = []
for i in range(0, len(decompressed) - 4, 4):
    val = struct.unpack('<f', decompressed[i:i+4])[0]
    if -100000 < val < 100000:
        floats.append(val)

print(f'{len(floats)} floats encontrados.')

with open(OUTPUT_OBJ, 'w') as f:
    for i in range(0, len(floats) - 2, 3):
        x, y, z = floats[i], floats[i+1], floats[i+2]
        f.write(f'v {x} {y} {z}\\n')
    for i in range(1, len(floats)//3):
        f.write(f'l {i} {i+1}\\n')

print(f'Arquivo OBJ salvo em {OUTPUT_OBJ}')
