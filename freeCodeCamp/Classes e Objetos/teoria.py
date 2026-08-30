# You build a class to define shared behaviors
class Dog: # define a class called Dog
    #método de instância
    def __init__(self, name, age): # método construtor que é chamado quando um objeto é criado
        self.name = name # atributo de nome
        self.age = age # atributo de idade

    def bark(self): #método de latir
        return f"{self.name} says Woof!"

# classe: modelo ou o projeto
# objeto: é o que é criado usando esse modelo


#Você escreve uma classe uma vez e pode criar muitos objetos 
#a partir dela, cada um com dados diferentes.
# Sintaxe:
# objeto = NomeDaClasse(atributo1, atributo2, ...)

objeto_cachorro1 = Dog("Buddy", 3) # cria um objeto cachorro1 com os atributos name e age
objeto_cachorro2 = Dog("Max", 5) # cria um objeto cachorro2 com os atributos name e age

objeto_cachorro1.bark() # chama o método bark do objeto cachorro1 (Buddy says Woof!)
objeto_cachorro1.name # acessa o atributo name do objeto cachorro1 (Buddy)