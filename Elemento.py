class Elemento:
    def __init__(self, valor):
        self.__valor = valor
        self.__anterior = None
        self.__proximo = None


    def set_proximo(self, element:object):
        self.__proximo = element

        
    def get_valor(self):
        return self.__valor

    
    def set_anterior(self, element:Elemento):
        self.__anterior = element
    

    def get_proximo(self):
        return self.__proximo
    

    def get_anterior(self):
        return self.__anterior
