import streamlit as st
import pandas as pd
from view.views import View
import time

class ClienteProdutoUI:
    @staticmethod
    def produto_inserir():
        st.header("Inserir produto no carrinho")
        produtos = View.produto_listar()
        if len(produtos) == 0:
            st.write("Não tem produtos.")
        else:
            produto = st.selectbox("Selecione o produto", produtos)
            quantidade = st.number_input("Informe a quantidade", value = 0, step = 1)

            if st.button("Adicionar produto no carrinho"):
                if quantidade > produto.get_estoque() or quantidade < 1:
                    st.error("Quantidade não disponível")
                else:
                    for venda in View.venda_listar():
                        if venda.get_id_cliente() == st.session_state["cliente_id"] and venda.get_carrinho() == False:
                            View.venda_item_inserir(quantidade, produto.get_preco(), venda.get_id(), produto.get_id())
                            View.produto_atualizar(produto.get_id(), produto.get_descricao(), produto.get_preco(), produto.get_estoque() - quantidade, produto.get_id_categoria())
                            View.venda_atualizar(venda.get_id(), venda.get_data(), venda.get_carrinho(), venda.get_total() + (produto.get_preco() * quantidade), venda.get_id_cliente())
                            st.success("Produto adicionado no carrinho")
                            time.sleep(2)
                            st.rerun()
                        
    @staticmethod 
    def produto_excluir():
        st.header("Excluir produto do carrinho")
        ClienteProdutoUI.pedido_visualizar()
        for venda in View.venda_listar():
            if venda.get_id_cliente() == st.session_state["cliente_id"]:
                id_venda = venda.get_id()

        venda_itens = View.venda_item_listar()
        for venda_item in venda_itens:
            if venda_item.get_id_venda() != id_venda:
                venda_itens.remove(venda_item)
        
        if(len(venda_itens) == 0):
            st.write("Carrinho vazio")
        else:
            item = st.selectbox("Selecione o produto", venda_itens)
            for p in View.produto_listar():
                if item.get_id_produto() == p.get_id():
                    produto_descricao = p.get_descricao()
                    produto_estoque = p.get_estoque()
                    produto_categoria = p.get_id_categoria()

            if st.button("Remover"):
                View.venda_item_excluir(item.get_id())
                View.produto_atualizar(item.get_id_produto(), produto_descricao, item.get_preco(), produto_estoque + item.get_qtd(), produto_categoria)
                View.venda_atualizar(id_venda, venda.get_data(), venda.get_carrinho(), venda.get_total() - (item.get_preco() * item.get_qtd()), venda.get_id_cliente())
                st.success("Produto excluído do carrinho")
                time.sleep(2)
                st.rerun()
            
    @staticmethod
    def produto_atualizar():
        st.header("Atualizar pedido")
        ClienteProdutoUI.produto_listar()
        ClienteProdutoUI.pedido_visualizar()
        for venda in View.venda_listar():
            if venda.get_id_cliente() == st.session_state["cliente_id"]:
                id_venda = venda.get_id()

        venda_itens = View.venda_item_listar()
        for venda_item in venda_itens:
            if venda_item.get_id_venda() != id_venda or venda.get_carrinho() == True:
                venda_itens.remove(venda_item)
        
        if(len(venda_itens) == 0):
            st.write("Carrinho vazio")
        else:
            item = st.selectbox("Selecione o produto", venda_itens)
            quantidade = st.number_input("Informe a nova quantidade", value = 0, step = 1)
            for p in View.produto_listar():
                if item.get_id_produto() == p.get_id():
                    produto_descricao = p.get_descricao()
                    produto_estoque = p.get_estoque()
                    produto_categoria = p.get_id_categoria()
            if st.button("Atualizar"):
                if quantidade < 1 or quantidade > produto_estoque:
                    st.error("Quantidade indisponível")
                elif quantidade > item.get_qtd():
                    quantidade = quantidade - item.get_qtd()
                    View.venda_item_atualizar(item.get_id(), quantidade + item.get_qtd(), item.get_preco(), item.get_id_venda(), item.get_id_produto())
                    View.produto_atualizar(item.get_id_produto(), produto_descricao, item.get_preco(), produto_estoque - quantidade, produto_categoria)
                    View.venda_atualizar(venda.get_id(), venda.get_data(), venda.get_carrinho(), venda.get_total() + (item.get_preco() * quantidade), venda.get_id_cliente())
                    st.success("Produto atualizado no carrinho")
                    time.sleep(2)
                    st.rerun()
                else:
                    quantidade = item.get_qtd() - quantidade
                    View.venda_item_atualizar(item.get_id(), item.get_qtd() - quantidade, item.get_preco(), item.get_id_venda(), item.get_id_produto())
                    View.produto_atualizar(item.get_id_produto(),produto_descricao, item.get_preco(), produto_estoque + quantidade, produto_categoria)
                    View.venda_atualizar(venda.get_id(), venda.get_data(), venda.get_carrinho(), venda.get_total() - (item.get_preco() * quantidade), venda.get_id_cliente())
                    st.success("Produto atualizado no carrinho")
                    time.sleep(2)
                    st.rerun()

    @staticmethod
    def produto_listar():
        st.header("Produtos disponíveis")
        produtos = View.produto_listar()
        categorias = View.categoria_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            dic = []
            for obj in produtos: 
                nome_categoria = ""
                for cat in categorias:
                    if cat.get_id() == obj.get_id_categoria():
                        nome_categoria = cat.get_descricao()
                        break

                produto_dict = obj.__dict__.copy()
                produto_dict['_Produto__id_categoria'] = nome_categoria
                dic.append(produto_dict)
            df = pd.DataFrame(dic)

            df.rename(columns={
                '_Produto__id': "ID",
                '_Produto__descricao':'Descrição',
                '_Produto__preco': 'Preço (R$)',
                '_Produto__estoque': 'Estoque',
                '_Produto__id_categoria': 'Categoria'
            }, inplace=True)
            st.dataframe(df, hide_index=True)

    @staticmethod
    def comprar():
        st.header("Finalizar pedido")
        ClienteProdutoUI.pedido_visualizar()
        if st.button("Finalizar compra"):
            View.venda_confirmar(st.session_state["cliente_id"])
            st.success("Compra finalizada")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def pedido_visualizar():
        st.header("Carrinho")
        pedido = View.venda_item_listar()
        produtos = View.produto_listar()
        if len(pedido) == 0:
            st.write("Nenhum pedido cadastrado")
        else:
            dic = []
            id_venda = None
            for venda in View.venda_listar():
                if venda.get_id_cliente() == st.session_state["cliente_id"] and venda.get_carrinho() == False:
                    id_venda = venda.get_id()

            for obj in pedido: 
                if obj.get_id_venda() == id_venda:
                    produto_descricao = ""
                    for p in produtos:
                        if p.get_id() == obj.get_id_produto():
                            produto_descricao = p.get_descricao()
                            break
                    
                    item_dict = obj.__dict__.copy()
                    item_dict['_Venda_item__id_produto'] = produto_descricao
                    dic.append(item_dict)
                
            df = pd.DataFrame(dic)

            df.rename(columns={
                '_Venda_item__id': "ID",
                '_Venda_item__qtd':'Quantidade',
                 '_Venda_item__preco': 'Item preco (R$)',
                '_Venda_item__id_venda': 'ID venda',
                '_Venda_item__id_produto': 'Produto'
            }, inplace=True)
            st.dataframe(df, hide_index=True)

                
    
