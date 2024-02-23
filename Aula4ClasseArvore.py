class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:        
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor) 
        else:
            self._inserir_recursivo(self.raiz, valor)       
    
    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivo(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)  
            else:
                self._inserir_recursivo(no.direita, valor)     

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor) 

    def _buscar_recursivo(self, no, valor):  
        if no is None or no.valor == valor:
            return no
        if valor < no.valor:
            return self._buscar_recursivo(no.esquerda, valor)  
        else:
            return self._buscar_recursivo(no.direita, valor)     

# Exemplo de uso da árvore binária
arvore = ArvoreBinaria()   
arvore.inserir(50)
arvore.inserir(30)                 
arvore.inserir(70)
arvore.inserir(20) 
arvore.inserir(40)  

no_encontrado = arvore.buscar(40)
if no_encontrado:
    print("Nó encontrado com valor:", no_encontrado.valor)
else:
    print("Nó não encontrado.")
