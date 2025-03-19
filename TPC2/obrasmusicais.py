import re
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Obra:
    nome: str
    desc: str
    anoCriacao: str
    periodo: str
    compositor: str
    duracao: str
    ident: str

linha = r'[\w\&\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\&\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\&\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\&\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\&\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\&\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\&\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*\n'

ficheiro = open("obras.csv", mode = 'r', encoding='utf8')

texto = ficheiro.read()

linhas = re.findall(linha,texto)


lista = []
for linha in linhas[1:]:
    parte = linha.strip().split(';')
    if len(parte) == 7:
        obra = Obra(
            nome = parte[0],
            desc = parte[1],
            anoCriacao = parte[2],
            periodo = parte[3],
            compositor = parte[4],
            duracao = parte[5],
            ident = parte[6]
        )
        lista.append(obra)
        


# 1. Lista ordenada alfabeticamente dos compositores
compositores = sorted(set(obra.compositor for obra in lista))

# 2. Contagem de obras por período
periodo_contagem = defaultdict(int)
for obra in lista:
    periodo_contagem[obra.periodo] += 1

# 3. Dicionário com períodos e lista alfabética das obras desse período
periodo_obras = defaultdict(list)
for obra in lista:
    periodo_obras[obra.periodo].append(obra.nome)

# Ordenar listas de obras dentro de cada período
for periodo in periodo_obras:
    periodo_obras[periodo].sort()


print("escolha uma opção:\n1. Lista ordenada alfabeticamente dos compositores\n2. Contagem de obras por período\n3. Dicionário com períodos e lista alfabética das obras desse período\n")
while True:
    linha = input("Opção: ").strip()  # Ler entrada e remover espaços extras
    if linha == '1':
        with open("resultado1.txt", mode = 'w', encoding='utf8') as ficheiro:
            for c in compositores:
                ficheiro.write(f"{c}\n")
        print("Foi gerado o ficheiro \"resultado1.txt\" com o conteúdo desejado\n")

    elif linha == '2':
        with open("resultado2.txt", mode = 'w', encoding='utf8') as ficheiro:
            ficheiro.write(f"{dict(periodo_contagem)}")
        print("Foi gerado o ficheiro \"resultado2.txt\" com o conteúdo desejado\n")
    elif linha == '3':
        with open("resultado3.txt", mode = 'w', encoding='utf8') as ficheiro:
            for periodo, obras in periodo_obras.items():
                ficheiro.write(f"Período: {periodo}\n")
                ficheiro.write("Lista de obras:")
                for obra in obras:
                    ficheiro.write(f" - {obra}\n")
                ficheiro.write("\n")
        print("Foi gerado o ficheiro \"resultado3.txt\" com o conteúdo desejado\n")

    elif linha == '0':
        print("A sair...")
        break
    else:
        print("Entrada inválida, tente novamente.")