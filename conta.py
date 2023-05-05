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
    
    def __pode_sacar(self, valor_requerido):
        valor_disponivel_para_saque = self.__saldo + self.__limite
        return valor_requerido <= valor_disponivel_para_saque

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("Você não possui limite o suficiente para essa operação")

    def transfere(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa':'104', 'Bradesco':'237'}