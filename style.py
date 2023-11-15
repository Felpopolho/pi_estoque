from customtkinter import *
from tkinter import *
from tkinter import ttk

def frame():
    estilo = ttk.Style()
    estilo.configure( 'EstiloFrame.TFrame',
                    background='white',
                    foreground='white', 
                    corner_radius=25,
                    border_color='black')
    
    estilo.configure( 'EstiloFrame2.TFrame',
                    background='silver',
                    foreground='silver', 
                    corner_radius=25,
                    border_color='black')
    
    estilo.configure("EstiloBotao.TButton",
                    background='black',  # Cor de fundo
                    foreground='black',  # Cor do texto
                    borderwidth=2,  # Largura da borda
                    relief="solid",  # Estilo da borda
                    padding=5,  # Preenchimento
                    font=('Helvetica', 8),  # Tamanho e fonte do texto
                    focuscolor='#52863D',  # Cor ao passar o mouse (hover)
                    bordercolor='black',  # Cor da borda
                    anchor="center",  # Alinhamento do texto
                    )

    estilo.configure("EstiloEntry.TEntry",
                    background='silver',  # Cor de fundo
                    foreground='black',  # Cor do texto
                    borderwidth=2,  # Largura da borda
                    relief="solid",  # Estilo da borda
                    padding=5,  # Preenchimento
                    font=('Helvetica', 8),  # Tamanho e fonte do texto
                    insertbackground='black',  # Cor do cursor
                    selectbackground='#52863D',  # Cor ao passar o mouse (hover)
                    selectforeground='black',  # Cor do texto ao passar o mouse (hover)
                    justify="left",  # Alinhamento do texto
                    )
    
    estilo.configure("estilo_treeview.Treeview.Heading",  # Estilo dos cabeçalhos
                    anchor="center",
                    font=('Helvetica', 10),  # Tamanho da fonte
                    foreground='black',  # Cor da fonte
                    background='lightgray')  # Cor de fundo
      
    estilo.configure("estilo_treeview.Treeview",  # Estilo das células
                    font=('Helvetica', 8),  # Tamanho da fonte
                    foreground='black',  # Cor da fonte
                    background='white')  # Cor de fundo
    estilo.map("estilo_treeview.Treeview",
               fieldbackground=[('selected', 'black')],
               background=[('selected', 'lightgray')],
               foreground=[('selected', 'black')],
               bordercolor=[('selected', 'lightgray')]
               )