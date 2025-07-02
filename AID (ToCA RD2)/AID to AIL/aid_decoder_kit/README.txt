
=== ToCA Race Driver - AID Decoder Kit ===

1) Coloque o seu arquivo .AID na mesma pasta.
2) Renomeie para 'eur.aid' OU ajuste o script.
3) Execute 'run_decoder.bat'
4) O arquivo decodificado será salvo como 'eur_decoded.bin'.

Para converter para .AIL:
- Abra 'eur_decoded.bin' num editor HEX.
- Verifique offsets, headers, dados internos.
- Ajuste conforme necessário para criar um .AIL compatível.

Para criar um EXE:
- Instale PyInstaller: pip install pyinstaller
- Gere o executável: pyinstaller --onefile aid_decoder.py

Boa engenharia reversa!
