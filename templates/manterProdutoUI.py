import streamlit as st
import pandas as pd
from view.views import View
import time

class ManterProdutoUI:
    @staticmethod
    def main():
        st.header("Cadastro de produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1:
            ManterProdutoUI.produto_listar()
        with tab2:
            ManterProdutoUI.produto_inserir()
        with tab3:
            ManterProdutoUI.produto_atualizar()
        with tab4:
            ManterProdutoUI.produto_excluir()
        

    @classmethod 
    def produto_inserir(cls):
        descricao = st.text_input("Informe a descricao")
        preco = st.number_input("Informe o preço", value = 0, step = 1)
        estoque = st.number_input("Informe a quantidade no estoque", value = 0, step = 1)
        categorias = View.categoria_listar()
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            categoria = st.selectbox("Selecione a categoria", categorias)

        if st.button("Inserir"):
            View.produto_inserir(descricao, preco, estoque, categoria.get_id())
            st.success("Produto adicionado")
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

    @classmethod 
    def produto_atualizar(cls):
        produtos = View.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            selecionado = st.selectbox("Atualização de produtos", produtos)

            descricao = st.text_input("Informe a nova descricao", selecionado.get_descricao())
            preco = st.number_input("Informe o preço", value = selecionado.get_preco(), step = 1)
            estoque = st.number_input("Informe a nova quantidade no estoque", value = selecionado.get_estoque(), step = 1)
            categoria = st.text_input("Informe a nova categoria", selecionado.get_descricao())

            if st.button("Atualizar"):
                View.produto_atualizar(selecionado.get_id(), descricao, preco, estoque, categoria.get_id())
                st.success("Produto atualizado")
                time.sleep(2)
                st.rerun()

    @classmethod 
    def produto_excluir(cls):
        produtos = View.produto_listar()
        if (len(produtos) == 0):
            st.write("Nenhum produto cadastrado")
        else:
            selecionado = st.selectbox("Exclusão de produto", produtos)
       
            if st.button("Excluir"):
                View.produto_excluir(selecionado.get_id())
                st.success("produto excluído")
                time.sleep(2)
                st.rerun()
    
