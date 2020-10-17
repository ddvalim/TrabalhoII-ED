
from Elemento import Elemento

class Lista:
    def __init__(self, limite):
        self.__primeiro_elemento = None
        self.__ultimo_elemento = None
        self.__numero_elementos = 0
        self.__cursor = None
        self.__limite = limite


    def valida_lista_inclusao(self):
        if self.lista_vazia():
            raise Exception('A lista está vazia e deve ser inicializada!')
        elif self.lista_cheia():
            raise Exception('Lista cheia!')
    
    # OPERACOES DE CONSULTA
    
    def lista_vazia(self):
        return self.__numero_elementos == 0

    
    def lista_cheia(self):
        return self.__limite == self.__numero_elementos


    def consulta_por_posicao(self, posicao:int):
        i = self.__primeiro_elemento
        
        for x in range(posicao-1):
            i = i.get_proximo()
        
        return i.get_numero()

    # OPERACOES SOBRE O CURSOR

    def ir_para_inicio(self):
        if self.__cursor == None:
            raise Exception('A lista está vazia e deve ser inicializada!')
        else:
            self.__cursor = self.__primeiro_elemento
            return self.__cursor
    

    def ir_para_final(self):
        if self.__cursor == None:
            raise Exception('A lista está vazia e deve ser inicializada!')
        else:
            self.__cursor = self.__ultimo_elemento
            return self.__cursor
    

    def avancar_cursor(self, k:int):
        if self.__cursor == None:
            raise Exception('A lista está vazia e deve ser inicializada!')
        else:
            for i in range(k):
                temp = self.__cursor.get_proximo()
                self.__cursor = temp
        
            return self.__cursor
    

    def retroceder_cursor(self, k:int):
        if self.__cursor == None:
            raise Exception('A lista está vazia e deve ser inicializada!')
        else:
            for i in range(k):
                temp = self.__cursor.get_anterior()
                self.__cursor = temp
        
            return self.__cursor

    # OPERACOES SOBRE ESTRUTURA

    def acessar_atual(self):
        return self.__cursor
    

    def inserir_apos_atual(self, value:int):
        if self.__cursor == self.__ultimo_elemento:
            self.inserir_no_fim()
            return
        else:
            self.valida_lista_inclusao()
            elemento = Elemento(int(value))
            prox = self.__cursor.get_proximo()
            self.__cursor.set_proximo(elemento)
            prox.set_anterior(elemento)

            elemento.set_anterior(self.__cursor)
            elemento.set_proximo(prox)
            self.__numero_elementos += 1
            print(f'Elemento {value} inserido com sucesso!')
        

    def inserir_antes_atual(self, value:int):
        if self.__cursor == self.__primeiro_elemento:
            self.inserir_na_frente(value)
            return
        else:
            
            self.valida_lista_inclusao()
            elemento = Elemento(int(value))
            anterior = self.__cursor.get_anterior()
            self.__cursor.set_anterior(elemento)
            anterior.set_proximo(elemento)

            elemento.set_anterior(anterior)
            elemento.set_proximo(self.__cursor)
            self.__numero_elementos += 1
            print(f'Elemento {value} inserido com sucesso!')
         



    def excluir_atual(self):
        anterior = self.__cursor.get_anterior()
        proximo = self.__cursor.get_proximo()

        anterior.set_proximo(proximo)
        proximo.set_anterior(anterior)

        self.__cursor = self.__primeiro_elemento

        return ('Operação concluída com sucesso!')


    def inserir_no_fim(self, value: int):
        self.valida_lista_inclusao()
        elemento = Elemento(int(value))    
        self.ir_para_final()
        elemento.set_anterior(self.__cursor)
        self.__cursor.set_proximo(elemento)
        self.__ultimo_elemento = elemento
        self.__numero_elementos += 1
        print(f'Elemento {elemento} inserido com sucesso!')
                


    def inserir_na_frente(self, value: int): #METODO INICIALIZADOR
        elemento = Elemento(int(value))
        if self.lista_vazia():
            self.__primeiro_elemento = elemento
            self.__ultimo_elemento = elemento
            self.__cursor = elemento
        else:
            self.valida_lista_inclusao()
            self.ir_para_inicio()
            elemento.set_proximo(self.__cursor)
            self.__cursor.set_anterior(elemento)
            self.__primeiro_elemento = elemento
            self.__numero_elementos += 1
        print(f'Elemento {value} inserido com sucesso!')
            

    def inserir_na_posicao(self, posicao: int, value:int):
        self.valida_lista_inclusao()
        elemento = Elemento(int(value))
        
        self.ir_para_inicio()
        contador = (int(posicao) - 1)
        self.avancar_cursor(contador)

        anterior = self.__cursor.get_anterior()
        anterior.set_proximo(elemento)
        self.__cursor.set_anterior(elemento)

        elemento.set_anterior(anterior)
        elemento.set_proximo(self.__cursor)
    
        self.__cursor = elemento
        self.__numero_elementos += 1
        print(f'O elemento {elemento} foi inserido na posição {posicao} com sucesso!')
   
    def excluir_item(self, elemento: Elemento):
        ant = elemento.get_anterior()
        prox = elemento.get_proximo()
        if prox is not None:
            prox.set_anterior(ant)
        if ant is not None:
            ant.set_proximo(prox)
        del elemento
 
    def excluir_primeiro(self):
        self.ir_para_inicio()
        self.__primeiro_elemento = self.__cursor.get_proximo()
        self.excluir_item(self.__cursor)
        self.ir_para_inicio()
 
 
    def excluir_ultimo(self):
        self.ir_para_final()
        self.__ultimo_elemento = self.__cursor.get_anterior()
        self.excluir_item(self.__cursor)
        self.ir_para_final()
 
    def excluir_valor

    def excluir_da_posicao(self, k: int):
        self.ir_para_inicio()
        if k > self.__numero_elementos:
            raise Exception(f'A posição {k} é maior do que o tamanho da lista')
        elif k == 0:
            self.excluir_primeiro()
        elif k == self.__numero_elementos:
            self.excluir_ultimo()
        else: 
            for k in range(k):
                self.avancar_cursor(1)
            self.excluir_item(self.__cursor)
            self._ir_para_inicio()



    def buscar(self, valor):
        if(self.__primeiro_elemento.__numero == valor or self.__ultimo_elemento.__numero == valor):
            return True
        
        self.ir_para_inicio()
        while True: 
            self.avancar_cursor(1)
            atual = self.acessar_atual().__numero
            if atual == self.__ultimo_elemento:
                return atual == valor
            elif atual == valor:
                return True
