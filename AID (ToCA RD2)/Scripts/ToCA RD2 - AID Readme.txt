=== ToCA Race Driver 2 - AID Reverse Engineering Kit ===

O que faz:
- Decodifica .AID via XOR simples
- Tenta decompress zlib
- Extrai floats presumindo coordenadas 3D
- Exporta para Wavefront OBJ

Como usar:
1) Coloque eur.aid na mesma pasta do script.
2) Tenha Python 3.x.
3) Execute:
   python aid_decode.py
4) Importe waypoints.obj no Blender (File > Import > Wavefront OBJ).

Dica:
Se der tudo zero ou ruído, altere XOR_KEY para outra chave.
Codemasters usava chaves como 0xAA ou 0xFF.
