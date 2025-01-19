import json
from datetime import date
from models.modelo import Modelo

class Venda:
    def __init__(self, id, data, carrinho, total, id_cliente):
        self.set_id(id)
        self.set_data(data)
        self.set_carrinho(carrinho)
        self.set_total(total)
        self.set_id_cliente(id_cliente)

    def set_id(self, id):
        self.__id = id
    
    def set_data(self, data):
        if data != None:
            self.__data = data
        else:
            dia_atual = date.today()
            self.__data = dia_atual.isoformat()

    def set_carrinho(self, carrinho):
        self.__carrinho = carrinho
    
    def set_total(self, total):
        self.__total = total
    
    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_carrinho(self):
        return self.__carrinho

    def get_total(self):
        return self.__total
    
    def get_id_cliente(self):
        return self.__id_cliente

    def __str__(self):
        return f"ID = {self.get_id()}  |  DATA = {self.get_data()}  |  CONFIRMADA = {self.get_carrinho()}  |  TOTAL = {self.get_total()}  |  ID CLIENTE = {self.get_id_cliente()}"
    
    def to_dict(self):
        return {
            "id": self.get_id(), 
            "data": self.get_data(), 
            "carrinho": self.get_carrinho(), 
            "total": self.get_total(), 
            "id_cliente": self.get_id_cliente()
        }
    
class Vendas(Modelo):
    @classmethod
    def salvar(cls):
        with open("vendas.json", mode="w") as arquivo:
            json.dump([venda.to_dict() for venda in cls.objetos], arquivo, indent=5) 
            #vars - converte um objeto em dicionario
            #dump - pega a lista de obejtos e salva no arquivo
            
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("vendas.json", mode="r") as arquivo:
                vendas_json = json.load(arquivo)
                for obj in vendas_json:
                    c = Venda(obj["id"], obj["data"], obj["carrinho"], obj["total"], obj["id_cliente"])
                    cls.objetos.append(c)    
        except FileNotFoundError:
            pass
