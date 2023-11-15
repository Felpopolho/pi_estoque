from _bibliotecas import *

def incluir(tela, usuario):
    
    # Cria o frame
    frame()
    incluir1 = ttk.Frame(tela, style='EstiloFrame2.TFrame'
                      )
    incluir1.place(relx = 0.015 , rely = 0.025, relwidth=0.97, relheight=0.95
                  )
    
    # Scroll bar
    incluir = CTkScrollableFrame(incluir1,
                    bg_color='silver',
                    fg_color='silver', 
                    corner_radius=25,
                    border_color='black')

    incluir.place(relx = 0.015 , rely = 0.025, relwidth=0.97, relheight=0.70
                  )
    
    # Função que cria uma nova caixa de texto
    def adicionar_campo():
        
        qtd_campos = len(nomes)
        Label(incluir, text=f"Produto {qtd_campos+1}", background='silver').pack()
        
        # Recebendo do banco todos os nomes de produtos pra colocar no select box
        querry = f"SELECT `nome_produto` FROM `produtos` WHERE 1"
        options = banco_select(querry)
        
        # Variável pra colocar no widget select box senão ele dá piti
        produto_selecionado = StringVar()
        
        # Por algum motivo o select daqui chama combobox
        nome = ttk.Combobox(incluir, textvariable=produto_selecionado, values=options)
        nome.pack()
        nome.set("Selecione um produto")
        
        # Aqui é pra escolher a quantidade 
        Label(incluir, text="Quantidade" ,background='silver').pack()
        quantidade = ttk.Entry(incluir, style="EstiloEntry.TEntry")
        quantidade.pack()
        
        # Não estamos mexendo com preço ainda (e nem sei se vamos)
        # Label(incluir, text="Preço unitário").pack()
        # preco = tk.Entry(incluir)
        # preco.pack()
        
        # Não, isso aqui não inclui o produto na lista pq ele ainda não existe, isso inclui o endereço de memória do widget textbox na lista pra eu acessar depois ;)
        nomes.append(nome)
        quantidades.append(quantidade)
        
    # Função que salva os produtos no banco de dados
    def salvar():
        # Dicionário que vai armazenar os produtos e suas quantidades
        produtos = {}
        
        # Registro de data e hora para salvar na compra 
        data_hora_atual = datetime.now()
        data_hora_formatada = data_hora_atual.strftime('%Y-%m-%d %H:%M:%S')
        
        # Resgata o id do usuário logado por meio de uma gambiarra com parâmetros de função (que falta faz uma variável de sessão)
        usuario_logado = usuario
        
        # Função incrível que eu criei que recebe uma querry como string, executa toda a lacuaca de conn e cursor longe daqui e me retorna só o resultado <3
        # Essa aqui cria o registro da compra no banco
        querry = f"INSERT INTO `compra`(`id_usuario_compra`, `registro_compra`, `valor_compra`) VALUES ('{usuario_logado}','{data_hora_formatada}','0')"
        last_id = banco_default(querry=querry, last_ID=True)        
        
        # Aqui é onde o filho chora e a mãe não vê...
        # ... um laço que faz o insert de cada produto da compra no banco
        for nome in nomes:
            
            # Recupera o nome do produto daquela lista lá de cima, um por um
            nome_produto = nome.get()
            
            # Adiciona o produto (chave) e sua quantidade (valor) no dicionário
            produtos[nome_produto] = quantidades[nomes.index(nome)].get()
            
            # Recupera o id do produto no banco (que função linda)            
            querry = f"SELECT `nome_produto`,`id_produto` FROM `produtos` WHERE nome_produto='{nome_produto}'"
            resultado = banco_select(querry)
                            
            # O ID do produto vem pra cá (o comentário tá redundante? Por isso que eu não comento código, meu deus...)
            id_item = resultado[0][1]
            
            # Recuperando a quantidade daquele dicionário que eu criei lá em cima
            qtd = produtos[nome_produto]

            # Com quantidade e id em mãos, cria o registro do produto, relacionado à compra
            querry = f"INSERT INTO `produtos_compra`(`id_compra`, `id_produto`, `quantidade_unitaria`, `preco_unitario`) VALUES ('{last_id}','{id_item}','{qtd}','0')"
            banco_default(querry=querry, last_ID=False)
            
            # E aqui atualiza a quantidade total do produto no banco ("Ah mas a de cima já não tem quantidade?" SIM, mas ela é mais pra registro e afins, isso aqui atualiza a quantidade total mesmo, eu pensei assim, fzr oq?)
            querry = f"UPDATE `produtos` SET `quantidade_total`=quantidade_total+{qtd} WHERE id_produto = {id_item}"
            banco_default(querry=querry, last_ID=False)
            
        # Sucesso papai 👌
        messagebox.showinfo("Sucesso", "Produtos adicionados com sucesso")
        
        # Fecha o frame de incluir produtos
        incluir1.destroy()
                
    # Cria as listas globais pra acessar nas funções (eu sei que é gambiarra, mas é o que tem pra hoje)
    global nomes
    global quantidades

    nomes = []
    quantidades = []
     
    # Botão que adiciona os campos de texto 
    botao_adicionar = ttk.Button(incluir1, text="Adicionar produto", command=adicionar_campo)

    # Botão que salva os produtos no banco
    botao_mostrar = ttk.Button(incluir1, text="Salvar", command=salvar)
    
    # Botão que fecha o frame de incluir produtos
    botao_voltar = ttk.Button(incluir1, text="Voltar", command=lambda:incluir1.destroy())
    
    botao_adicionar.place(relx = 0.1 , rely = 0.7, relwidth=0.2, relheight=0.2)
    botao_mostrar.place(relx = 0.4 , rely = 0.7, relwidth=0.2, relheight=0.2)
    botao_voltar.place(relx = 0.7 , rely = 0.7, relwidth=0.2, relheight=0.2)