import json

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
    
class Clientes:
    objetos = [] #atributos de classe cls - forma de acessar o atributo da classe 

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        
        #calcular o id do objeto
        id = 0
        for cliente in cls.objetos:
            if cliente.get_id() > id: id = cliente.get_id()
        obj.set_id(id + 1)

        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        # percorre a lista procurando o id    
        for cliente in cls.objetos:
            if cliente.get_id() == id: return cliente
        return None

    @classmethod
    def atualizar(cls, obj):
        cliente = cls.listar_id(obj.get_id())
        if cliente != None:
            cls.objetos.remove(cliente)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cliente = cls.listar_id(obj.get_id())
        if cliente != None:
            cls.objetos.remove(cliente)
            cls.salvar()

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
