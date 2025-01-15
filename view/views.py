from models.cliente import Cliente, Clientes
from models.categoria import Categoria, Categorias
from models.produto import Produto, Produtos
from models.venda import Venda, Vendas
from models.vendaItem import Venda_item, Venda_itens

class View:
    @staticmethod
    def cliente_admin():
        clientes = Clientes.listar()
        for cliente in clientes:
            if cliente.get_email() == "admin@gmail.com": return None
        View.cliente_inserir("admin", "admin@gmail.com", "0000", "1234")
    
    @staticmethod
    def cliente_autenticar(email, senha):
        clientes = Clientes.listar()
        for cliente in clientes:
            if cliente.get_email() == email and cliente.get_senha() == senha:
                return {"id": cliente.get_id(), "nome": cliente.get_nome()}
        return None
    @staticmethod
    def cliente_listar():
        return Clientes.listar()
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        clientes = Clientes.listar()
        if not email:
            raise ValueError("Email vazio")
        if not nome:
                raise ValueError("Nome vazio")
        for cliente in clientes:
            if email == cliente.get_email():
                raise ValueError("Email já cadastrado")
        c = Cliente(0, nome, email, fone, senha)
        Clientes.inserir(c)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        if not email:
            raise ValueError("Email vazio")
        if not nome:
            raise ValueError("Nome vazio")
        clientes = Clientes.listar()
        for cliente in clientes:
            if email == cliente.get_email():
                raise ValueError("Email já cadastrado")
        
        c = Cliente(id, nome, email, fone, senha)
        Clientes.atualizar(c)
    @staticmethod
    def cliente_excluir(id):
        c = Cliente(id, "", "", "", "")
        Clientes.excluir(c)


    @staticmethod
    def categoria_listar():
        return Categorias.listar()
    @staticmethod
    def categoria_listar_id(id):
        return Categorias.listar_id(id)
    @staticmethod
    def categoria_inserir(descricao):
        categorias = Categorias.listar()
        for categoria in categorias:
            if descricao == categoria.get_descricao():
                raise ValueError("Descrição ja cadastrada")
        if not descricao:
            raise ValueError("Descrição vazia")
        c = Categoria(0, descricao)
        Categorias.inserir(c)
    @staticmethod
    def categoria_atualizar(id, descricao):
        categorias = Categorias.listar()
        for categoria in categorias:
            if descricao == categoria.get_descricao():
                raise ValueError("Descrição ja cadastrada")
        if not descricao:
            raise ValueError("Descrição vazia")
        c = Categoria(id, descricao)
        Categorias.atualizar(c)
    @staticmethod
    def categoria_excluir(id):
        c = Categoria(id, "")
        Categorias.excluir(c)

    @staticmethod
    def produto_listar():
        return Produtos.listar()
    @staticmethod
    def produto_inserir(descricao, preco, estoque, id_categoria):
        if not descricao:
            raise ValueError("Descrição vazia")
        if not id_categoria:
            raise ValueError("Categoria vazia")
        if preco <= 0:
            raise ValueError("Preço inválido")
        if estoque <= 0:
            raise ValueError("Estoque inválido")
        p = Produto(0, descricao, preco, estoque, id_categoria)
        Produtos.inserir(p)
    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, id_categoria):
        if not descricao:
            raise ValueError("Descrição vazia")
        if not id_categoria:
            raise ValueError("Categoria vazia")
        if preco <= 0:
            raise ValueError("Preço inválido")
        if estoque <= 0:
            raise ValueError("Estoque inválido")
        p = Produto(id, descricao, preco, estoque, id_categoria)
        Produtos.atualizar(p)
    @staticmethod
    def produto_excluir(id):
        p = Produto(id, "", 0, 0, None)
        Produtos.excluir(p)
    @staticmethod
    def produto_reajustar(percentual, id):
        if not percentual:
            raise ValueError("Percentual vazio")

        for obj in View.produto_listar():
            if obj.get_id() == id:
                p = Produto(obj.get_id(), obj.get_descricao(), (obj.get_preco() * percentual) + obj.get_preco(), obj.get_estoque(), obj.get_id_categoria())
                Produtos.atualizar(p)
        
    @staticmethod
    def venda_inserir(carrinho, total, id_cliente):
        compra = False
        for venda in Vendas.listar():
            if venda.get_id_cliente() == id_cliente and venda.get_carrinho() == False:  
                compra = True
                break
        if compra == False:
            v = Venda(0, None, carrinho, total, id_cliente)
            Vendas.inserir(v)
    @staticmethod
    def venda_confirmar(id_cliente):
        for venda in Vendas.listar():
            if venda.get_id_cliente() == id_cliente and venda.get_carrinho() == False:
                id = venda.get_id()
                data = venda.get_data()
                carrinho = True
                total = venda.get_total()
                id_cliente = venda.get_id_cliente()
                v = Venda(id, data, carrinho, total, id_cliente,)
                Vendas.atualizar(v)
                v = Venda(0, None, False, 0, id_cliente)
                Vendas.inserir(v)
    @staticmethod
    def venda_listar():
        return Vendas.listar()
    @staticmethod
    def venda_listar_id(id):
        return Vendas.listar_id(id)
    @staticmethod
    def venda_atualizar(id, data, carrinho, total, id_cliente):
        v = Venda(id, data, carrinho, total, id_cliente)
        Vendas.atualizar(v)
    @staticmethod
    def venda_excluir(id):
        v = Venda(id, "", "", "", "")
        Vendas.excluir(v)
    
 
    @staticmethod
    def venda_item_listar():
        return Venda_itens.listar()
    @staticmethod
    def venda_item_listar_id( id):
        return Venda_itens.listar_id(id)
    @staticmethod
    def venda_item_inserir(q, p, id_venda, id_produto):
        v = Venda_item(0, q, p, id_venda, id_produto)
        Venda_itens.inserir(v)
    @staticmethod
    def venda_item_atualizar(id, q, p, id_venda, id_produto):
        v = Venda_item(id, q, p, id_venda, id_produto)
        Venda_itens.atualizar(v)
    @staticmethod
    def venda_item_excluir(id):
        v = Venda_item(id, "", "", "", "")
        Venda_itens.excluir(v)

    
