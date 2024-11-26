import tkinter as tk
from tkinter import ttk

def abrir_janela():
    janela2 = tk.Toplevel()
    janela2.title("Janela Nova")
    janela2.configure(bg='black')

    
    mensagem = tk.Label(janela2, text="Sistema de Busca de produtos", fg='white', bg='black', width=65, height=5, font='Georgia 25 bold')
    mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

    
    mensagem2 = tk.Label(janela2, text="Selecione o produto que deseja conferir", fg='white', bg='black', font='Georgia 10 bold')
    mensagem2.grid(row=1, column=0, sticky='w', padx=10, pady=(10, 0))

    #produtos
    produtos = {
        'Xbox 360': 650,
        'Playstation 3': 520,
        'Nintendo Wii': 450,
        'Nintendo WiiU': 234,
        'Playstation 4 Slim + jogo': 1454,
        'Concord': 1000,
        'God of War Ragnarok': 250,
        'Elden Ring + Shadow of Erdtree': 350,
        'Dragon Ball Sparking 0': 350,
        'Cabo USB 5.0': 80,
        'Guitarra para PS2': 560, 
        "Fone Gamer": 740,
        "Cartão Presente PSN R$ 30": 30,
        "Cartão Presente PSN R$ 300": 300,
        "Cartão Presente PSN R$ 350": 350,
        "Cartão Presente PSN R$ 10": 10,
        "Cartão Presente PSN R$ 110": 110,
        "Super Nintendo ":450,
        "Nintendo 64":567,
        "DualSense":559.99,
        "Apex Pro Tkl": 1299.99,



    }

    moedas = list(produtos.keys())
    moeda = ttk.Combobox(janela2, values=moedas)
    moeda.grid(row=2, column=0, sticky="w", padx=10)

    # Função mostrar o valor produto
    mensagem_cotacao = tk.Label(janela2, text='')
    def mostrar_valor():
        produto_selecionado = moeda.get().strip()
        valor = produtos.get(produto_selecionado)
        if valor is not None:
            mensagem_cotacao["text"] = f'O valor do {produto_selecionado} é R$ {valor}'
        else:
            mensagem_cotacao["text"] = "Produto não encontrado"
        mensagem_cotacao.configure(bg='black', fg='white')
        mensagem_cotacao.grid(row=5, column=0, sticky="w")
      

    # Botão para mostrar o valor do produto
    botao_valor = tk.Button(janela2, text="Mostrar Valor", command=mostrar_valor)
    botao_valor.grid(row=3, column=0, sticky="w", padx=10)
    botao_valor.configure(fg='white', bg='black')

    # Mensagem para encomenda
    mensagem3 = tk.Label(janela2, text="Caso deseje realizar uma encomenda,insira aqui:")
    mensagem3.grid(row=6, column=0, sticky='w', padx=10, pady=(10, 0)) 
    mensagem3.configure(fg='white', bg='black')

    # Caixa de encomenda
    caixa_texto = tk.Text(janela2, width=30, height=5)
    caixa_texto.grid(row=8, column=0, columnspan=2, sticky="NSWE", padx=10)

    #confirmar reserva
    def confirmar_reserva():
        reserva = caixa_texto.get("1.0", tk.END).strip() 
        if not reserva:  # Verifica se o campo está vazio
            mensagem_cotacao["text"] = "Por favor, preencha o campo de encomenda."
            mensagem_cotacao.configure(fg='red') 
        else:
            # Limpa a caixa de encomenda
            caixa_texto.delete("1.0", tk.END)
           
            mensagem_cotacao["text"] = "Encomenda realizada com sucesso"
            mensagem_cotacao.configure(fg='green') 

    # Botão encomenda
    botao_fechar = tk.Button(janela2, text="Realizar encomenda", command=confirmar_reserva)
    botao_fechar.grid(row=9, column=0, pady=10, sticky="w")
    botao_fechar.configure(fg='white', bg='black')

# Janela 1
janela = tk.Tk()
janela.title("Janela Principal")
janela.configure(bg='black')

mensagem = tk.Label(janela, text="JF GAMES", fg='white', bg='black', width=65, height=5, font='Georgia 25 bold')
mensagem.grid(row=1, column=1, columnspan=2, sticky="NSEW")

# Botão de  nova janela
botao = tk.Button(janela, text="Abrir página de busca de produtos", fg='white', bg='black', command=abrir_janela)
botao.grid(row=2, columnspan=3, pady=10)

janela.mainloop()
