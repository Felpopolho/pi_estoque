from _bibliotecas import *

from tabela import tree_view
from incluir import incluir
from retirar import retirar

def inicial(tela, usuario):
    def sair():
        inicial.destroy()
         
    frame()

    inicial = ttk.Frame(tela, style='EstiloFrame2.TFrame'
                    )
    inicial.place(relx = 0.015 , rely = 0.025, relwidth=0.97, relheight=0.95)

    titulo = ttk.Frame(inicial,style='EstiloFrame.TFrame'
                    )
    titulo.place(relx = 0.05 , rely = 0.05, relwidth=0.9, relheight=0.08)
    Label(titulo, text = 'Bem vindo ao estoque', background='white', font=('arial', 12, 'bold')).place(relx = 0.33, rely = 0.2)

    in_out = ttk.Frame(inicial,style='EstiloFrame.TFrame'
                    )
    in_out.place(relx = 0.05 , rely = 0.18, relwidth=0.4, relheight=0.3)

    input = ttk.Button(in_out,
                       text='incluir produto',
                       style="EstiloBotao.TButton",
                       command=lambda:incluir(tela, usuario))
    input.place(relx = 0.25 , rely = 0.1, relwidth=0.5, relheight=0.2)

    out = ttk.Button(in_out,
                       text='retirar produto',
                       style="EstiloBotao.TButton",
                       command=lambda:retirar(tela, usuario))
    
    out.place(relx = 0.25 , rely = 0.4, relwidth=0.5, relheight=0.2)

    aviso = ttk.Frame(inicial,style='EstiloFrame.TFrame'
                    )
    aviso.place(relx = 0.55 , rely = 0.18, relwidth=0.4, relheight=0.3)
    
    logoff = ttk.Button(inicial,
                       text='Sair',
                       style="EstiloBotao.TButton",
                       command=sair)
    logoff.place(relx = 0.8 , rely = 0.85, relwidth=0.15, relheight=0.1)

    produtos = ttk.Frame(inicial,style='EstiloFrame.TFrame'
                    )
    produtos.place(relx = 0.05 , rely = 0.53, relwidth=0.9, relheight=0.3)

    tree_view(produtos,in_out)