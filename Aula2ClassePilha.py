class Pilha:
    def __init__(self) :
        self .items = []

    def esta__vazia(self):
        return len(self.items) == 0
    
    def empilhar(self, item):
        self.items.append(item)
    def desempilhar (self):
        if not self.esta__vazia():
            return self.items.pop()
        
    def topo (self):
        if not self .esta__vazia():
            return self.items [-1]
              
# Criando uma Pilha
pilha = Pilha()

# Verificando se a pilha está vazia
print("A pilha está vazia?", pilha.esta__vazia())

# Empilhando elementos 
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)

# Verificando o topo da pllha
print ("Topo da Pilha:", pilha.topo())

# Desempilhando elementos
print("Desempilhando:", pilha.desempilhar())
print("Desempilhando:", pilha.desempilhar())

# Veriificando o topo da pilha após o desempilhamento
print("Topo da pilha:", pilha.topo())

# Verficando se a pilha está vazia novamente
print("A pilha está vazia?", pilha.esta__vazia())

