def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("Erro!")
        if ok:
            break
    return valor




n = leiaint("Digite um número inteiro: ")

print(f"O número digitado foi {n}")

