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

#linha = r'^[^\;]*?;[^\;]*?;[^\;]*?;[^\;]*?;[^\;]*?;[^\;]*;[^\;]*?\n'
linha = r'[\w\&\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\&\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\&\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\&\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\&\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\&\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\&\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*\n'
#[^\;]+;[^\;]+|\n;[^\;]*;[^\;]*;[^\;]*;[^\;]*;[^\;]*\n
ficheiro = open("obras.csv", mode = 'r', encoding='utf8')

texto = ficheiro.read()

linhas = re.findall(linha,texto)

#print(linhas)

lista = []
i=1
for linha in linhas[1:]:
    print (f"Esta é a linha {i}: {linha}\n")
    i+=1
    parte = linha.strip().split(';')
    if len(parte) == 7:
        #print(f"{parte}\n")
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
        print(f"Nome: {obra.nome}\n")
        #print(f"Descrição: {obra.desc}\n")
        print(f"Ano de Criação: {obra.anoCriacao}\n")
        print(f"Período: {obra.periodo}\n")
        print(f"Compositor: {obra.compositor}\n")
        print(f"Duração: {obra.duracao}\n")
        print(f"Identificador: {obra.ident}\n")
        print("-" * 40 + "\n")

print (len(lista))

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
        print("Lista de compositores ordenada:", compositores)
    elif linha == '2':
        print("Distribuição das obras por período:", dict(periodo_contagem))
    elif linha == '3':
        print("Dicionário de períodos com listas alfabéticas das obras:", dict(periodo_obras))
    elif linha == '0':
        print("A sair...")
        break
    else:
        print("Entrada inválida, tente novamente.")