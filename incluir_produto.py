from _bibliotecas import *
from _conn import banco_select, banco_default, teste

def incluir_produto(tela, usuario): 
    def cancel():
        incluir_produto.destroy()
        
    def salvar(nome, qtd_min):
        nome = nome.get().upper()
        qtd_min = qtd_min.get()
        
        is_repeat = banco_select(f"SELECT nome_produto FROM produtos WHERE nome_produto = '{nome}'")
        
        if(len(is_repeat) == 0):
            if((nome != '') and (qtd_min != '')):
                querry = f"INSERT INTO produtos (nome_produto, adm_cadastrou, quantidade_total, qtd_min) VALUES ('{nome}', {usuario}, {0}, '{qtd_min}')"
                banco_default(querry=querry, last_ID=False)
                messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso")
                incluir_produto.destroy()
            else: 
                messagebox.showerror("Erro", "Preencha todos os campos")
        else:
            messagebox.showerror("Erro", "Produto já cadastrado")
                        
    frame()

    incluir_produto = ttk.Frame(tela, style='EstiloFrame2.TFrame'
                    )
    incluir_produto.place(relx = 0.1 , rely = 0.1, relwidth=0.8, relheight=0.8)
    
    Label(incluir_produto, text='Nome:').place(relx = 0.15 , rely = 0.2, relwidth=0.28, relheight=0.1)
    nome = Entry(incluir_produto)
    nome.place(relx = 0.43 , rely = 0.2, relwidth=0.42, relheight=0.1)
    
    Label(incluir_produto, text='Quantidade mínima:').place(relx = 0.15 , rely = 0.4, relwidth=0.28, relheight=0.1)
    qtd_min = Entry(incluir_produto)
    qtd_min.place(relx = 0.43 , rely = 0.4, relwidth=0.42, relheight=0.1)
    

    Salvar = ttk.Button(incluir_produto,
                       text='Salvar',
                       style="EstiloBotao.TButton",
                       command=lambda:salvar(nome, qtd_min))
    Salvar.place(relx = 0.35 , rely = 0.8, relwidth=0.15, relheight=0.1)

    cancelar = ttk.Button(incluir_produto,
                       text='Cancelar',
                       style="EstiloBotao.TButton",
                       command=cancel)
    cancelar.place(relx = 0.55 , rely = 0.8, relwidth=0.15, relheight=0.1)

