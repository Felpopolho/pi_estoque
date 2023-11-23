from _bibliotecas import *
from _conn import banco_select, banco_default, teste
from incluir_funcionario import incluir_funcionario
from incluir_produto import incluir_produto

def admin(tela, usuario): 
    def sair():
        admin.destroy()
        
    frame()

    admin = ttk.Frame(tela, style='EstiloFrame2.TFrame'
                    )
    admin.place(relx = 0.1 , rely = 0.1, relwidth=0.8, relheight=0.8)


    novo_funcionario = ttk.Button(admin,
                       text='incluir funcionario',
                       style="EstiloBotao.TButton",
                       command=lambda:incluir_funcionario(tela))
    novo_funcionario.place(relx = 0.25 , rely = 0.25, relwidth=0.5, relheight=0.2)

    novo_produto = ttk.Button(admin,
                       text='incluir produto',
                       style="EstiloBotao.TButton",
                       command=lambda:incluir_produto(tela, usuario))
    novo_produto.place(relx = 0.25 , rely = 0.55, relwidth=0.5, relheight=0.2)
    
    logoff = ttk.Button(admin,
                       text='Sair',
                       style="EstiloBotao.TButton",
                       command=sair)
    logoff.place(relx = 0.8 , rely = 0.85, relwidth=0.15, relheight=0.1)
