class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(self.__saldo)
    
    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    def get_limite(self):
        return self.__limite
    
    def set_limite(self, limite):
        self.__limite = limite