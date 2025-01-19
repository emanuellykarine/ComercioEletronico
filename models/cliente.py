import json
from models.modelo import Modelo

class Cliente:
    def __init__(self, id, nome, email, fone, senha): #atributo de instancia
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)
    
    def set_id(self, id):
        self.__id = id

    def set_nome(self, n):
        self.__nome = n
    
    def set_email(self, e):
        self.__email = e
    
    def set_fone(self, f):
        self.__fone = f

    def set_senha(self, s):
        self.__senha = s

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email
    
    def get_fone(self):
        return self.__fone
    
    def get_id(self):
        return self.__id

    def get_senha(self):
        return self.__senha
    
    def __str__(self):
        return f"ID = {self.get_id()}  |  NOME = {self.get_nome()}  |  EMAIL = {self.get_email()}  |  FONE = {self.get_fone()}"
    
    def to_dict(self):
        return {
            "id": self.get_id(), 
            "nome": self.get_nome(), 
            "email": self.get_email(), 
            "fone": self.get_fone(),
            "senha": self.get_senha()
        }
    
class Clientes(Modelo):
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump([cliente.to_dict() for cliente in cls.objetos], arquivo, indent=4) #vars - converte um objeto em dicionario
            #dump - pega a lista de obejtos e salva no arquivo
            
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
                    cls.objetos.append(c)    
        except FileNotFoundError:
            pass
