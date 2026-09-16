import glob
from arvores_utils import (
    processar_arquivo,
    construirNodo,
    somaArvore,
    altura,
    quantidadeNos,
)

for caminho in sorted(glob.glob("casom*.txt")):
  print(caminho)
  gerador = processar_arquivo(caminho)
  raiz = construirNodo(gerador)
  print(somaArvore(raiz))
  print(altura(raiz))
  print(quantidadeNos(raiz))