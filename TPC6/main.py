from anasin import rec_Parser
import sys

for linha in sys.stdin:
    resultado = rec_Parser(linha)
    print("Linha: ", linha.strip())
    print(f"Resultado:{resultado} \n")
