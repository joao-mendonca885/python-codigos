n = int(input())
numberStarAttacked = 0
i = 0
stars =[]
jaFoiVisitado = []
stars = int(input())
while True:
    # se a casa que ele vai olhar nao existir quebra
    if i < 0:
        break
    # se a casa que ele vai olhar passar do numero de estrelas quebra
    if i > n-1:
        break
    if stars[i] % 2 == 1:
        i = i + 1
        stars[i] = stars[i] - 1
        if i not in jaFoiVisitado:
            numberStarAttacked += 1
        else:
            jaFoiVisitado[i] = i
    if stars[i] % 2 == 0:
        i = i - 1
        if stars[i] > 0:
            stars[i] = stars[i] - 1
        if i not in jaFoiVisitado:
            numberStarAttacked += 1
            jaFoiVisitado[i] = i
    
print(sum(stars), numberStarAttacked)