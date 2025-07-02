
# aid_decoder.py
# Decodifica um arquivo .AID (ToCA Race Driver 2)

INPUT_FILE = "eur.aid"
OUTPUT_FILE = "eur_decoded.bin"
XOR_KEY = 0xFF  # Chave XOR estimada

print(f"Decodificando {INPUT_FILE} -> {OUTPUT_FILE}")

with open(INPUT_FILE, "rb") as f:
    data = f.read()

decoded = bytes([b ^ XOR_KEY for b in data])

with open(OUTPUT_FILE, "wb") as f:
    f.write(decoded)

print(f"Arquivo decodificado salvo como {OUTPUT_FILE}")
