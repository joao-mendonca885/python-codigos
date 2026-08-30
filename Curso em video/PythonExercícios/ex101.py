# mais de 65: opicional
# mais que 17: obrigatorio
# menos que 17: negado
def voto(ano):
    age = 2026 - ano
    if age <18:
        return f"Com {age} anos: Voto Negado"
    elif age <= 65:
        return f"Com {age} anos: Voto Obrigatório"
    else: return f"Com {age} anos: Voto Opicional"   
    

print(voto(ano = int(input("Digite seu ano de nascimento: "))))