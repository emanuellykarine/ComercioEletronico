import streamlit as st
import pandas as pd
from view.views import View
import time

class ManterClienteUI:
    @staticmethod
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1:
            ManterClienteUI.cliente_listar()
        with tab2:
            ManterClienteUI.cliente_inserir()
        with tab3:
            ManterClienteUI.cliente_atualizar()
        with tab4:
            ManterClienteUI.cliente_excluir()
        

    @classmethod 
    def cliente_inserir(cls):
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Inserir"):
            try:
                View.cliente_inserir(nome, email, fone, senha)
                st.success("Cliente adicionado")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)
            

    @classmethod 
    def cliente_listar(cls):
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            dic = []
            for obj in clientes: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            df.rename(columns={
                '_Cliente__id': "ID",
                '_Cliente__nome':'Nome',
                '_Cliente__email': 'E-mail',
                '_Cliente__fone': 'Fone',
                '_Cliente__senha': 'Senha'
            }, inplace=True)
            st.dataframe(df, hide_index=True)

    @classmethod 
    def cliente_atualizar(cls):
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            selecionado = st.selectbox("Atualização de clientes", clientes)

            nome = st.text_input("Informe o novo nome", selecionado.get_nome())
            email = st.text_input("Informe o novo e-mail", selecionado.get_email())
            fone = st.text_input("Informe o novo fone", selecionado.get_fone())
            senha = st.text_input("Informe a nova senha", selecionado.get_senha(), type="password")
            
            if st.button("Atualizar"):
                try:
                    View.cliente_atualizar(selecionado.get_id(), nome, email, fone, senha)
                    st.success("Cliente atualizado")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)
                


    @classmethod 
    def cliente_excluir(cls):
        clientes = View.cliente_listar()
        if (len(clientes) == 0):
            st.write("Nenhum cliente cadastrado")
        else:
            selecionado = st.selectbox("Exclusão de cliente", clientes)
       
            if st.button("Excluir"):
                View.cliente_excluir(selecionado.get_id())
                st.success("Cliente excluído")
                time.sleep(2)
                st.rerun()
