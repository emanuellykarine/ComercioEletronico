import json
from models.modelo import Modelo

class Categoria:
    def __init__(self, id, d):
        self.set_id(id)
        self.set_descricao(d)
        
    def set_id(self, id):
        self.__id = id
    
    def set_descricao(self, d):
        self.__d = d

    def get_id(self):
        return self.__id

    def get_descricao(self):
        return self.__d

    def __str__(self):
        return f"ID = {self.get_id()}  |  DESCRIÇÃO = {self.get_descricao()}"
    
    def to_dict(self):
        return {
            "id": self.get_id(), "descricao": self.get_descricao()
        }
    
class Categorias(Modelo):     
    @classmethod
    def salvar(cls):
        with open("categorias.json", mode="w") as arquivo:
            json.dump([categoria.to_dict() for categoria in cls.objetos], arquivo, indent=2)
    
    @classmethod
    def abrir(cls):
        # esvazia a lista de objetos
        cls.objetos = []
        try:
            with open("categorias.json", mode="r") as arquivo:
                categorias_json = json.load(arquivo)
                for obj in categorias_json:
                    c = Categoria(obj["id"], obj["descricao"])
                    cls.objetos.append(c)    
        except FileNotFoundError:
            pass
