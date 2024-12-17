import streamlit as st
import pandas as pd
from view.views import View
import time

class ReajustarProduto:
    def main():
        produtos = View.produto_listar()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            selecionado = st.selectbox("Reajuste de preço de produtos", produtos)

            porcentagem = st.number_input("Informe a porcentagem em decimal", value = 0.0, step = 0.01)

            if st.button("Reajustar"):
                View.produto_reajustar(porcentagem, selecionado.get_id())
                st.success("Produto com valor reajustado")
                time.sleep(2)
                st.rerun()
