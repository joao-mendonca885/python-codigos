class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = [] # lista de transações
    
    def deposit(self, amount, description = ""):
        dicionario ={
            "amount": amount,
            "description": description
        }
        self.ledger.append(dicionario)
    
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
    
    def get_balance(self):
        return sum(transacao["amount"] for transacao in self.ledger)
    
    def transfer(self, amount, category):
        # se der para transferir, retorna True
        if self.withdraw(amount, f"Transfer to {category.name}"): #chama o check_funds pelo withdraw
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        # se não retorna false
        return False 

    def check_funds(self, amount):
        if self.get_balance() - amount < 0:
            return False
        return True  
    def __str__(self):
        titulo =  self.name.center(30, "*")
        cabecario = []
        for transacao in self.ledger:
            descricao = transacao["description"][:23]
            valor = f"{transacao['amount']:.2f}"
            cabecario.append(f"{descricao:<23}{valor:>7}")
        final = f"Total: {self.get_balance():.2f}"
        meio = "\n".join(cabecario)
        return titulo + "\n" + meio + "\n" + final

def create_spend_chart(categories):
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
        temp = int(value*100 / total) #pega o valor sem casas decimais em %
        temp = (temp // 10) * 10 # arredonda para baixo
        porcentagem.append(temp)
    

balanca = Category("Joao")
balanca.deposit(50.23, "Golden knight")
print(balanca)