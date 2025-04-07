import re

def markdown_to_html(markdown):
    html = markdown

    # Cabeçalhos (h1 a h6)
    for i in range(6, 0, -1):
        pattern = rf'^{"#"*i} (.+)$'
        replacement = rf'<h{i}>\1</h{i}>'
        html = re.sub(pattern, replacement, html, flags=re.MULTILINE)
    
    # Imagens ![alt](url)
    html = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', html)

    # Links [texto](url)
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html)

    # Negrito **texto**
    html = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', html)

    # Itálico *texto*
    html = re.sub(r'\*(.*?)\*', r'<i>\1</i>', html)

    # Lista numerada
    # Converte linhas que começam com "n. " para <li>
    html = re.sub(r'^\d+\.\s+(.*)$', r'<li>\1</li>', html, flags=re.MULTILINE)

    # Envolve blocos de <li> consecutivos em <ol>
    html = re.sub(r'((<li>.*?</li>\n?)+)', r'<ol>\1</ol>', html, flags=re.DOTALL)

    return html


with open("./teste.txt", "r", encoding="utf-8") as ficheiro:
    texto_markdown = ficheiro.read()

texto_html = markdown_to_html(texto_markdown)

with open("resultado.txt", "w", encoding="utf-8") as file:
    file.write(texto_html)