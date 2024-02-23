class Fila:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return len(self.items) == 0

    def enfileirar (self, item):
        self.items.append(item)

    def desenfileirar (self):
        if not self.esta_vazia():
            return self.items.pop(0)

    def frente (self):
        if not self.esta_vazia():
            return self.items[0]            

fila = Fila()        
# Verificando se a fila está vazia
print ("A fila está vazia?", fila.esta_vazia())                

# Enfileirando elementos
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)

# Verificando o primeiro elemento da fila
print("Primeiro elemento da fila:", fila.frente())

# Desenfileirando elementos
print ("Desenfileirando", fila.desenfileirar())
print ("Desenfileirando", fila.desenfileirar())

# Verificando o primeiro elemento da fila após  o desenfileiramento
print ("Primeiro elemento da fila", fila.frente())

# Verificando se a fila está vazia novamente
print("A fila está vazia?", fila.esta_vazia())
