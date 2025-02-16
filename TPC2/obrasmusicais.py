import re
from dataclasses import dataclass

@dataclass
class Obra:
    nome: str
    desc: str
    anoCriacao: str
    periodo: str
    compositor: str
    duracao: str
    ident: str


linha = r'[\w\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*;[\w\,\s\"\.\:\(\)\[\]\'À-ÖØ-öø-ÿ–—\-\/«!?»↑♭♯’\u0400-\u04FF]*\n'

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

print(lista, len(lista))