import sys

# variável da soma
sum = 0

# variável que controla se o somador está ativo ou não
capturing = True

# buffer para guardar os números
num_buf = ""

for linha in sys.stdin:
    i = 0
    l = len(linha)

    while (i<l):
        if i+2 < l and linha[i:i+3].lower() == "off":
            capturing = False
            i += 2
        elif i+1 < l and linha[i:i+2].lower() == "on":
            capturing = True
            i += 1
        elif linha[i].isdigit():
            num_buf += linha[i]
        else:
            if num_buf:
                if capturing:
                    sum += int(num_buf)
                num_buf = ""
            
            if linha[i] == '=':
                if capturing and num_buf:
                    sum += int(num_buf)
                print(sum)

        i += 1
    
    if num_buf:
        if capturing:
            sum += int(num_buf)
        num_buf = ""

print(sum)
