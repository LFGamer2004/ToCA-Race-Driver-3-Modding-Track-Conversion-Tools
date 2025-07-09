
=====================================
COL <=> OBJ Converter Kit
=====================================

Inclui:
- col_to_obj.py : Converte .COL para .OBJ
- obj_to_col.py : Converte .OBJ para .COL

====================
COMO USAR
====================

1) Coloque o arquivo .COL como 'input.col'
2) Edite 'vertex_offset', 'num_vertices', 'face_offset', 'num_faces'
   no col_to_obj.py para bater com seu arquivo.
3) Rode: python col_to_obj.py
   => Gera 'output.obj' (abra no Blender!)

4) Edite o OBJ, salve como 'output.obj'
5) Rode: python obj_to_col.py
   => Gera 'rebuild.col' para testar no jogo.

====================
DICA
====================

- Vértice: 12 bytes (XYZ float32)
- Face: 6 bytes (3 uint16)
- Estrutura bruta, sem compressão.
- Teste offsets e contagens com um HEX editor.

Bom modding!
