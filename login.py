from _bibliotecas import *

from inicial import inicial

def login(tela): 
    frame()
    login = ttk.Frame(tela, style='EstiloFrame2.TFrame'
                      )
    login.place(relx = 0.1 , rely = 0.2, relwidth=0.8, relheight=0.6)

    Label(login, text = 'Usuário:', background='silver').place(relx = 0.25, rely = 0.3)
    usuario = ttk.Entry(login,
                       style="EstiloEntry.TEntry",
                       )
    
    usuario.place(relx = 0.25, rely = 0.37, relwidth=0.5, relheight=0.08)

    Label(login, text = 'Senha:' ,background='silver').place(relx = 0.25, rely = 0.45)
    senha = ttk.Entry(login,
                    show='*',
                    style="EstiloEntry.TEntry",
                    )
    
    senha.place(relx = 0.25 , rely = 0.52, relwidth=0.5, relheight=0.08)

    entrar = ttk.Button(login,
                       text='Entrar',
                       style="EstiloBotao.TButton",
                       command=lambda : confirmar(tela,usuario,senha)
                       )
    
    entrar.place(relx = 0.25 , rely = 0.61, relwidth=0.5, relheight=0.1)

def confirmar(tela,usuario,senha):
    usuario = usuario.get()
    senha = senha.get()
 
    querry = f"SELECT * FROM administrador WHERE id_administrador = '{usuario}' LIMIT 1"
    resultado = banco_select(querry)
       
    if len(resultado) != 0:
        for row in resultado:
            if row[2] == senha:
                inicial(tela, usuario)
            else:
                print("Usuário ou senha incorretos")
    else:
        print("Usuário ou senha incorretos")