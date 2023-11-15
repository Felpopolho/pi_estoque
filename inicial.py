from _bibliotecas import *

from tabela import tree_view
from incluir import incluir
from retirar import retirar

def inicial(tela, usuario): 
    frame()

    inicial = ttk.Frame(tela, style='EstiloFrame2.TFrame'
                    )
    inicial.place(relx = 0.015 , rely = 0.025, relwidth=0.97, relheight=0.95)

    titulo = ttk.Frame(inicial,style='EstiloFrame.TFrame'
                    )
    titulo.place(relx = 0.05 , rely = 0.05, relwidth=0.9, relheight=0.08)

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

    produtos = ttk.Frame(inicial,style='EstiloFrame.TFrame'
                    )
    produtos.place(relx = 0.05 , rely = 0.53, relwidth=0.9, relheight=0.3)

    tree_view(produtos,in_out)