from _bibliotecas import *
from _conn import banco_select, banco_default, teste

def incluir_funcionario(tela): 
    def cancel():
        incluir_funcionario.destroy()
        
    def salvar(nome, senha):
        nome = nome.get()
        senha = senha.get()
        
        if((nome != '') and (senha != '')):
            querry = f"INSERT INTO usuario (nome, senha, tipo) VALUES ('{nome}', '{senha}', '1')"
            banco_default(querry=querry, last_ID=False)
            messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso")
            incluir_funcionario.destroy()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos")
                 
    # Receber último id cadastrado no banco
    ultimo_id = banco_select('SELECT MAX(id) FROM usuario')
    ultimo_id = ultimo_id[0][0] + 1
        
    frame()

    incluir_funcionario = ttk.Frame(tela, style='EstiloFrame2.TFrame'
                    )
    incluir_funcionario.place(relx = 0.1 , rely = 0.1, relwidth=0.8, relheight=0.8)

    Label(incluir_funcionario, text='ID').place(relx = 0.17 , rely = 0.2, relwidth=0.1, relheight=0.1)
    id = Entry(incluir_funcionario)
    id.insert(0, ultimo_id)
    id.config(state='disabled')
    id.place(relx = 0.27 , rely = 0.2, relwidth=0.6, relheight=0.1)
    
    Label(incluir_funcionario, text='Nome:').place(relx = 0.17 , rely = 0.4, relwidth=0.1, relheight=0.1)
    nome = Entry(incluir_funcionario)
    nome.place(relx = 0.27 , rely = 0.4, relwidth=0.6, relheight=0.1)
    
    Label(incluir_funcionario, text='Senha:').place(relx = 0.17 , rely = 0.6, relwidth=0.1, relheight=0.1)
    senha = Entry(incluir_funcionario)
    senha.place(relx = 0.27 , rely = 0.6, relwidth=0.6, relheight=0.1)
    

    Salvar = ttk.Button(incluir_funcionario,
                       text='Salvar',
                       style="EstiloBotao.TButton",
                       command=lambda:salvar(nome, senha))
    Salvar.place(relx = 0.35 , rely = 0.8, relwidth=0.15, relheight=0.1)

    cancelar = ttk.Button(incluir_funcionario,
                       text='Cancelar',
                       style="EstiloBotao.TButton",
                       command=cancel)
    cancelar.place(relx = 0.55 , rely = 0.8, relwidth=0.15, relheight=0.1)

