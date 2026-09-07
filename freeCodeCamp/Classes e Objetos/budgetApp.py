class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = [] # lista de transações
    # método para depositar dinheiro 
    def deposit(self, amount, description = ""):
        dicionario ={
            "amount": amount,
            "description": description
        }
        self.ledger.append(dicionario)
    # método para sacar dinheiro
    def withdraw(self, amount, description=""):
        dicionario = {
            "amount": -1 * amount,
            "description": description
        }
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append(dicionario)
            return True
    # método para retornar o saldo atual da pessoa
    def get_balance(self):
        return sum(transacao["amount"] for transacao in self.ledger)

    # método para transferir dinheiro de uma pessoa para outra
    # que basicamente saca a quantia da pessoa que está chamando o método e deposita na outra pessoa
    # usando as funções withdraw e deposit
    def transfer(self, amount, category):
        # se der para transferir, retorna True
        if self.withdraw(amount, f"Transfer to {category.name}"): #chama o check_funds pelo withdraw
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        # se não retorna false
        return False 

    #método para checar se a pessoa tem dinheiro suficiente para sacar ou transferir
    def check_funds(self, amount):
        if self.get_balance() - amount < 0:
            return False
        return True
    # méotodo para  
    def __str__(self):
        titulo =  self.name.center(30, "*") # Coloca o nome no meio
        cabecario = []
        for transacao in self.ledger:
            descricao = transacao["description"][:23] #23 é o tamanho máximo da descrição
            valor = f"{transacao['amount']:.2f}"
            cabecario.append(f"{descricao:<23}{valor:>7}")
        final = f"Total: {self.get_balance():.2f}"
        meio = "\n".join(cabecario)
        return titulo + "\n" + meio + "\n" + final

# mostra o gráfico de gastos de cada pessoa, com base nos saques de cada uma 
def create_spend_chart(categories):
    titulo = "Percentage spent by category"
    saques = []
    for categoria in categories:
        valor = 0
        for transacao in categoria.ledger:
            if transacao["amount"] < 0:
                valor += transacao["amount"]
        saques.append(abs(valor))
    total = sum(saques)
    porcentagem = []
    for value in saques:
        temp = int(value*100 / total) 
        temp = (temp // 10) * 10 
        porcentagem.append(temp) # temos a lista de porcentagens

    # primeira parte
    lista_dezenas = [dezena for dezena in range(100, -1, -10)]
    linhas = []
    for idx in range(len(lista_dezenas)):
        dezena = f"{lista_dezenas[idx]:>3}| "
        celula = []
        for p in porcentagem:
            if p >= lista_dezenas[idx]:
                celula.append("o  ")
            else:
                celula.append("   ")
        linhas.append(dezena + "".join(celula))
    primeira_parte = "\n".join(linhas)

    #segunda parte
    quatro_espacos = "    "
    resto = "---" * len(categories) + '-'
    segunda_parte = quatro_espacos + resto
    # terceira parte
    maior = max(len(categoria.name) for categoria in categories)
    terceira_parte = []
    for i in range(maior):
        linha = "   "
        for categoria in categories:
            if i < len(categoria.name):
                linha += "  " + categoria.name[i]
            else:
                linha += "   "
        linha += "  "
        terceira_parte.append(linha)
    terceira_parte = "\n".join(terceira_parte)
    return titulo + "\n" + primeira_parte + "\n" + segunda_parte + "\n" + terceira_parte


joao = Category("João")
joao.deposit(1000, "Depósito inicial")
joao.withdraw(200, "Compra de roupas")
maria = Category("Maria")
maria.deposit(500, "Depósito inicial")
maria.withdraw(100, "Compra de sapatos")
print(create_spend_chart([joao, maria]))
pedro = Category("Pedro")
pedro.deposit(800, "Depósito inicial")
pedro.withdraw(300, "Compra de eletrônicos")
print(create_spend_chart([joao, maria, pedro]))