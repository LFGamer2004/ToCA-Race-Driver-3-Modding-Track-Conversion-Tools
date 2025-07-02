
=== ToCA Race Driver - AID to AIL Converter Kit ===

O que faz:
- Decodifica arquivos .AID (TRD2) usando XOR.
- Substitui cabeçalho (AID0 → AIL0) para gerar .AIL (TRD3).
- Salva o arquivo convertido.

Como usar:
1) Coloque o seu .AID na mesma pasta.
2) Renomeie para 'eur.aid' OU edite o script.
3) Clique duas vezes em 'run_converter.bat'.
4) O arquivo 'eur.ail' será criado na mesma pasta.

Para criar um .EXE:
1) Instale Python 3 e PyInstaller:
   pip install pyinstaller

2) Gere o executável:
   pyinstaller --onefile aid_to_ail.py

3) O .EXE fica em 'dist/'.

Atenção:
- É um conversor básico. Compare offsets no hex se precisar.
- Campos extras podem ser necessários para 100% de compatibilidade.
