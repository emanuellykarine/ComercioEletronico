import json
from models.modelo import Modelo

class Venda_item:
    def __init__(self, id, q, p, id_venda, id_produto):
        self.set_id(id)
        self.set_qtd(q)
        self.set_preco(p)
        self.set_id_venda(id_venda)
        self.set_id_produto(id_produto)

    def set_id(self, id):
        self.__id = id

    def set_qtd(self, q):
        self.__qtd = q
    
    def set_preco(self, p):
        self.__preco = p

    def set_id_venda(self, id_venda):
        self.__id_venda = id_venda

    def set_id_produto(self, id_produto):
        self.__id_produto = id_produto

    def get_id(self):
        return self.__id
    
    def get_qtd(self):
        return self.__qtd

    def get_preco(self):
        return self.__preco
    
    def get_id_venda(self):
        return self.__id_venda

    def get_id_produto(self):
        return self.__id_produto
    
    def __str__(self):
        return f"ID = {self.get_id()}  |  QTD = {self.get_qtd()}  |  PREÇO = R${self.get_preco()}  |  ID VENDA = {self.get_id_venda()}  |  ID PRODUTO = {self.get_id_produto()}"

    def to_dict(self):
        return {
            "id": self.get_id(), 
            "qtd": self.get_qtd(), 
            "preco": self.get_preco(), 
            "id_venda": self.get_id_venda(), 
            "id_produto": self.get_id_produto()
    }

class Venda_itens(Modelo):
    @classmethod
    def salvar(cls):
        with open("venda_itens.json", mode="w") as arquivo:
            json.dump([venda_item.to_dict() for venda_item in cls.objetos], arquivo, indent=5) 
            #vars - converte um objeto em dicionario
            #dump - pega a lista de obejtos e salva no arquivo
            
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("venda_itens.json", mode="r") as arquivo:
                venda_item_json = json.load(arquivo)
                for obj in venda_item_json:
                    c = Venda_item(obj["id"], obj["qtd"], obj["preco"], obj["id_venda"], obj["id_produto"])
                    cls.objetos.append(c)    
        except FileNotFoundError:
            pass
