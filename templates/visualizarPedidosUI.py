import streamlit as st
import pandas as pd
from view.views import View

class VisualizarPedidosUI:
    def main():
        st.header("Pedidos")
        pedidos = View.venda_listar()
        if len(pedidos) == 0:
            st.write("Nenhum pedido cadastrado")
        else:
            dic = []
        
            for obj in pedidos: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)

            df.rename(columns={
                '_Venda__id': "ID",
                '_Venda__data':'Data',
                '_Venda__carrinho': 'Compra confirmada',
                '_Venda__total': 'Total carrinho (R$)',
                '_Venda__id_cliente': 'ID cliente'
            }, inplace=True)
            st.dataframe(df, hide_index=True)
