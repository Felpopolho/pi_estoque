from _bibliotecas import *


    
def tree_view(produtos,in_out):

    def atualizar_treeview():
        querry = f"SELECT * FROM produtos"
        resultado = banco_select(querry)
            
        tree.delete(*tree.get_children())  # Limpa a Treeview

        # Obtém os cabeçalhos das colunas dinamicamente a partir do dicionário
        cabecalhos = ["ID Produto", "Produto", "Quem cadastrou", "Quantidade"]

        # Define os cabeçalhos da Treeview dinamicamente
        tree['columns'] = cabecalhos
        for cabecalho in cabecalhos:
            tree.heading(cabecalho, text=cabecalho)
            tree.column(cabecalho, width=50,  anchor="center",)

         # Obtém o número de linhas da lista de valores no dicionário
        for row in resultado:
            tree.insert("", "end", values=row)

        # Insere os dados na Treeview

    # Frame para a Treeview
    tree = ttk.Treeview(produtos, style='estilo_treeview.Treeview', columns=(), show='headings')
    tree.place(relx = 0 , rely =0, relwidth=1, relheight=1)

    # Botão para atualizar a Treeview com os dados
    atualizar_button = ttk.Button(in_out, text='Atualizar Treeview',style="EstiloBotao.TButton", command=atualizar_treeview)
    atualizar_button.place(relx = 0.25 , rely =0.7, relwidth=0.5, relheight=0.2)

    # Atualiza a Treeview com os dados ao iniciar a janela
    atualizar_treeview()