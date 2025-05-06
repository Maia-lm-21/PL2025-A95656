# TPC2 - Analisador Léxico

**Data:** 06/05/2025

## Autor
**Nome:** Luís Gustavo Aires Guimarães Maia

**Número de Aluno:** 95656

![Foto do Autor](../foto.jpeg)

## Resumo do trabalho
- Este trabalho consistiu na criação de um analisador léxico para uma linguagem de query com a qual se podem escrever frases do género:
```
codeselect ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
```

## Lista de Resultados
- [Resultado1](resultado1.txt) - 