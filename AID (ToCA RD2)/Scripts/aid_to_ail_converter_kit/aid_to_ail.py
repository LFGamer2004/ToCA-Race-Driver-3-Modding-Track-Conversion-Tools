
import struct

# === CONFIG ===
INPUT_FILE = "eur.aid"
OUTPUT_FILE = "eur.ail"
XOR_KEY = 0x55  # Chave XOR para decodificar (ajuste se precisar)

print(f"Convertendo {INPUT_FILE} para {OUTPUT_FILE}")

# === Ler AID ===
with open(INPUT_FILE, "rb") as f:
    aid_data = f.read()

# === Decodificar XOR ===
decoded = bytes([b ^ XOR_KEY for b in aid_data])

# === Converter para AIL (exemplo: trocar mágica se existir) ===
if decoded[:4] == b"AID0":
    ail_data = b"AIL0" + decoded[4:]
else:
    ail_data = decoded

# === Escrever novo arquivo ===
with open(OUTPUT_FILE, "wb") as f:
    f.write(ail_data)

print(f"Arquivo {OUTPUT_FILE} criado com sucesso!")
