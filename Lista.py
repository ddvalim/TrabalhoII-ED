from Elemento import Elemento

class Lista:
    def __init__(self, limite):
        self.__primeiro_elemento = None
        self.__ultimo_elemento = None
        self.__numero_elementos = 0
        self.__cursor = None
        self.__limite = limite

    # OPERACOES DE CONSULTA
    
    def lista_vazia(self):
        return self.__numero_elementos == 0

    
    def lista_cheia(self):
        return self.__limite == self.__numero_elementos


    def contem_elemento(self, elemento:object):
        if isinstance(elemento, Elemento):
            if elemento == self.__primeiro_elemento or elemento == self.__ultimo_elemento:
                return True
            else:
                i = self.__primeiro_elemento
                while i != elemento:
                    if i == None:
                        return False
                    else:
                        i = i.get_proximo()
                        
                return True
        else:
            raise Exception('O parâmetro passado não é da classe Elemento!')
    

    def consulta_por_posicao(self, posicao:int):
        i = self.__primeiro_elemento
        
        for x in range(posicao):
            i = i.get_proximo()
        
        return i.get_numero()

    # OPERACOES SOBRE O CURSOR

    def ir_para_inicio(self):
        self.__cursor = self.__primeiro_elemento
    

    def ir_para_final(self):
        self.__cursor = self.__ultimo_elemento
    

    def avancar_cursor(self, k:int):
        for i in range(k):
            temp = self.__cursor.get_proximo()
            self.__cursor = temp
        
        return self.__cursor
    

    def retroceder_cursor(self, k:int):
        for i in range(k):
            temp = self.__cursor.get_anterior()
            self.__cursor = temp
        
        return self.__cursor

    # OPERACOES SOBRE A ESTRUTURA

    def acessar_atual(self):
        return self.__cursor
    

    def inserir_apos_atual(self, elemento:object):
        if isinstance(elemento, Elemento):
            if self.lista_cheia() == False:
                prox = self.__cursor.get_proximo()
                self.__cursor.set_proximo(elemento)
                prox.set_anterior(elemento)

                elemento.set_anterior(self.__cursor)
                elemento.set_proximo(prox)

                self.__numero_elementos += 1
                return ('Operação concluída com sucesso!')
            else:
                raise Exception('Lista cheia!')
        else:
            raise Exception('O parâmetro passado não é do tipo Elemento!')
    

    def inserir_antes_atual(self, elemento:object):
        if isinstance(elemento, Elemento):
            if self.lista_cheia() == False:
                anterior = self.__cursor.get_anterior()
                self.__cursor.set_anterior(elemento)
                anterior.set_proximo(elemento)

                elemento.set_anterior(anterior)
                elemento.set_proximo(self.__cursor)

                self.__numero_elementos += 1
                return ('Operação concluída com sucesso!')
            else:
                raise Exception('Lista cheia!')
        else:
            raise Exception('O parâmetro passado não é do tipo Elemento!')


    def excluir_atual(self):
        anterior = self.__cursor.get_anterior()
        proximo = self.__cursor.get_proximo()

        anterior.set_proximo(proximo)
        proximo.set_anterior(anterior)

        self.__cursor = self.__primeiro_elemento

        return ('Operação concluída com sucesso!')
