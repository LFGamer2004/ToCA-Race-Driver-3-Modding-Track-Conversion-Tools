import struct

INPUT_AID = "eur.aid"
OUTPUT_AIL = "output.ail"

with open(INPUT_AID, "rb") as f:
    data = f.read()

# Decodificar se necessário
decoded = bytes([b ^ 0x55 for b in data])

# Substituir header 'AID0' -> 'AIL0'
if decoded[:4] == b"AID0":
    converted = b"AIL0" + decoded[4:]
else:
    converted = decoded

# Opcional: reescrever blocos se offsets mudarem
# Exemplo: se os nós começarem em offset 0x100 em AID e 0x120 em AIL

# Salvar
with open(OUTPUT_AIL, "wb") as f:
    f.write(converted)

print("Salvo como output.ail")
