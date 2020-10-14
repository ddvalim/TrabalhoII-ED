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
            raise Exception(f'O parâmetro {elemento} não é da classe Elemento!')
    

    def consulta_por_posicao(self, posicao:int):
        i = self.__primeiro_elemento
        
        for x in range(posicao):
            i = i.get_proximo()
        
        return i.get_numero()

    # OPERACOES SOBRE O CURSOR

    def ir_para_inicio(self):
        self.__cursor = self.__primeiro_elemento
        return self.__cursor
    

    def ir_para_final(self):
        self.__cursor = self.__ultimo_elemento
        return self.__cursor
    

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
        if self.lista_vazia() == True:
            raise Exception('A lista está vazia e deve ser inicializada!')
        else:
            if isinstance(elemento, Elemento):
                if self.lista_cheia() == False:
                    if self.__cursor == self.__ultimo_elemento:
                        self.__cursor.set_proximo(elemento)
                        elemento.set_anterior(self.__cursor)

                        self.__ultimo_elemento = elemento
                        self.__numero_elementos += 1
                        return (f'Elemento {elemento} inserido com sucesso')
                    else:
                        prox = self.__cursor.get_proximo()
                        self.__cursor.set_proximo(elemento)
                        prox.set_anterior(elemento)

                        elemento.set_anterior(self.__cursor)
                        elemento.set_proximo(prox)

                        self.__numero_elementos += 1
                        return (f'Elemento {elemento} inserido com sucesso!')
                else:
                    raise Exception('Lista cheia!')
            else:
                raise Exception(f'O parâmetro {elemento} não é do tipo Elemento!')
    

    def inserir_antes_atual(self, elemento:object):
        if self.lista_vazia() == True:
            raise Exception('A lista está vazia e deve ser inicializada!')
        else:
            if isinstance(elemento, Elemento):
                if self.lista_cheia() == False:
                    if self.__cursor == self.__primeiro_elemento:
                        elemento.set_proximo(self.__cursor)
                        self.__cursor.set_anterior(elemento)

                        self.__primeiro_elemento = elemento
                        self.__numero_elementos += 1
                        return (f'Elemento {elemento} inserido com sucesso!')
                    else:
                        anterior = self.__cursor.get_anterior()
                        self.__cursor.set_anterior(elemento)
                        anterior.set_proximo(elemento)

                        elemento.set_anterior(anterior)
                        elemento.set_proximo(self.__cursor)

                        self.__numero_elementos += 1
                        return (f'Elemento {elemento} inserido com sucesso!')
                else:
                    raise Exception('Lista cheia!')
            else:
                raise Exception(f'O parâmetro {elemento} não é do tipo Elemento!')


    def excluir_atual(self):
        anterior = self.__cursor.get_anterior()
        proximo = self.__cursor.get_proximo()

        anterior.set_proximo(proximo)
        proximo.set_anterior(anterior)

        self.__cursor = self.__primeiro_elemento

        return ('Operação concluída com sucesso!')


    def inserir_no_fim(self, elemento: object):
        if isinstance(elemento, Elemento):
            if self.lista_vazia == True:
                raise Exception('A lista está vazia e deve ser inicializada!')
            else:
                if self.lista_cheia() != True:
                    c = self.ir_para_final()
                    elemento.set_anterior(c)
                    c.set_proximo(elemento)
                    self.__ultimo_elemento = elemento
                    self.__numero_elementos += 1
                    return (f'Elemento {elemento} inserido com sucesso!')
                else:
                    raise Exception('Lista cheia, impossível adicionar novo elemento')
        else:
            raise Exception(f'O parâmetro {elemento} não é do tipo Elemento!')


    def inserir_na_frente(self, elemento: object): #METODO INICIALIZADOR
        if isinstance(elemento, Elemento):
            if self.lista_vazia == True:
                self.__primeiro_elemento = elemento
                self.__ultimo_elemento = elemento
                self.__cursor = elemento
            else:
                if self.lista_cheia() != False:
                    c = self.ir_para_inicio()
                    elemento.set_proximo(c)
                    c.set_anterior(elemento)
                    self.__primeiro_elemento = elemento
                    self.__numero_elementos += 1
                    return (f'Elemento {elemento} inserido com sucesso!')
        else:
            raise Exception(f'O parâmetro {elemento} não é do tipo Elemento!')


    def inserir_na_posicao(self, posicao: int, elemento: object):
        if isinstance(elemento, Elemento):
            if self.lista_vazia() == True:
                raise Exception('A lista está vazia e deve ser inicializada!')
            else:
                self.ir_para_inicio()
                contador = int(posicao) - 1
                self.avancar_cursor(contador)

                anterior = self.__cursor.get_anterior()
                anterior.set_proximo(elemento)
                self.__cursor.set_anterior(elemento)

                elemento.set_anterior(anterior)
                elemento.set_proximo(self.__cursor)
            
                self.__cursor = elemento
                self.__numero_elementos += 1

                return (f'O elemento {elemento} foi inserido na posição {posicao} com sucesso!')
        else:
            raise Exception(f'O parâmetro {elemento} não é do tipo Elemento!')

