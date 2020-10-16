class Elemento:
    def __init__(self, numero):
        self.__numero = numero
        self.__anterior = None
        self.__proximo = None


    def set_proximo(self, element:Elemento):
        self.__proximo = element

    
    def set_anterior(self, element:Elemento):
        self.__anterior = element
    

    def get_proximo(self):
        return self.__proximo
    

    def get_anterior(self):
        return self.__anterior