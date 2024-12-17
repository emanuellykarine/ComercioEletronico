import json

class Produto:
    def __init__(self, id, d, p, e, id_categoria):
        self.set_id(id)
        self.set_descricao(d)
        self.set_preco(p)
        self.set_estoque(e)
        self.set_id_categoria(id_categoria)

    def set_id(self, id):
        self.__id = id
    
    def set_descricao(self, d):
        self.__descricao = d
    
    def set_preco(self, p):
        self.__preco = p

    def set_estoque(self, e):
        self.__estoque = e
    
    def set_id_categoria(self, id_categoria):
        self.__id_categoria = id_categoria

    def get_id(self):
        return self.__id
    
    def get_descricao(self):
        return self.__descricao
    
    def get_preco(self):
        return self.__preco

    def get_estoque(self):
        return self.__estoque
    
    def get_id_categoria(self):
        return self.__id_categoria
    
    def __str__(self):
        return f"ID = {self.get_id()}  |  DESCRIÇÃO = {self.get_descricao()}  |  PREÇO = R${self.get_preco()}   |  QTD DISPONÍVEL = {self.get_estoque()}  |  CATEGORIA = {self.get_id_categoria()}"
    
    def to_dict(self):
        return {
            "id": self.get_id(), 
            "descricao": self.get_descricao(), 
            "preco": self.get_preco(), 
            "estoque": self.get_estoque(), 
            "id_categoria": self.get_id_categoria()
        }
    
class Produtos:
    objetos = [] #atributos de classe cls - forma de acessar o atributo da classe 

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        
        #calcular o id do objeto
        id = 0
        for produto in cls.objetos:
            if produto.get_id() > id: id = produto.get_id()
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
        for produto in cls.objetos:
            if produto.get_id() == id: return produto
        return None

    @classmethod
    def atualizar(cls, obj):
        produto = cls.listar_id(obj.get_id())
        if produto != None:
            cls.objetos.remove(produto)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        produto = cls.listar_id(obj.get_id())
        if produto != None:
            cls.objetos.remove(produto)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump([produto.to_dict() for produto in cls.objetos], arquivo, indent=5) 
            #vars - converte um objeto em dicionario
            #dump - pega a lista de obejtos e salva no arquivo
            
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("produtos.json", mode="r") as arquivo:
                produtos_json = json.load(arquivo)
                for obj in produtos_json:
                    c = Produto(obj["id"], obj["descricao"], obj["preco"], obj["estoque"], obj["id_categoria"])
                    cls.objetos.append(c)    
        except FileNotFoundError:
            pass
