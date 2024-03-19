from tkinter import *


def show_frame(frame):
    frame.tkraise()


def janela_padrao(janela, id_janela):
    global janela_padrao_titulo
    janela_padrao_titulo = Frame(janela, bg='red')
    janela_padrao_titulo.grid(row=0, column=0, columnspan=4, sticky='nsew')
    id = Label(janela, text=f'{id_janela}', bg='red')
    id.grid(row=0, column=0, columnspan=4, sticky='nsew')

    global janela_padrao_menu
    janela_padrao_menu = Frame(janela, bg='grey')
    janela_padrao_menu.grid(row=1, rowspan=10, column=0, sticky='nsew')

    global janela_padrao_painel
    janela_padrao_painel = Frame(janela, bg='white')



def botoes_menu(janela):
    botao_inicio = Button(
        janela, text='Início', command=lambda: show_frame(janela_home))
    botao_inicio.grid(row=2, column=0, sticky='nsew')

    botao_gerador = Button(
        janela, text='Gerador', command=lambda: show_frame(janela_gerador))
    botao_gerador.grid(row=3, column=0, sticky='nsew')

    botao_acompanhamentoprocessual = Button(
        janela, text='Acompanhamento Processual', command=lambda: show_frame(janela_acompanhamentoprocessual))
    botao_acompanhamentoprocessual.grid(row=4, column=0, sticky='nsew')

    botao_diariooficial = Button(
        janela, text='Diário Oficial', command=lambda: show_frame(janela_diariooficial))
    botao_diariooficial.grid(row=5, column=0, sticky='nsew')

    botao_jurimetria = Button(
        janela, text='Jurimetria', command=lambda: show_frame(janela_jurimetria))
    botao_jurimetria.grid(row=6, column=0, sticky='nsew')

    botao_jurisprudencia = Button(
        janela, text='Jurisprudência', command=lambda: show_frame(janela_jurisprudencia))
    botao_jurisprudencia.grid(row=7, column=0, sticky='nsew')


janela = Tk()

janela.state('zoomed')
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

janela_home = Frame(janela)
janela_gerador = Frame(janela)
janela_gerador_documentos = Frame(janela)
janela_gerador_documentos_opcoes = Frame(janela)
janela_gerador_documentos_form = Frame(janela)
janela_acompanhamentoprocessual = Frame(janela)
janela_diariooficial = Frame(janela)
janela_jurimetria = Frame(janela)
janela_jurisprudencia = Frame(janela)

for frame in (janela_home, janela_gerador, 
              janela_gerador_documentos, 
              janela_gerador_documentos_opcoes, 
              janela_gerador_documentos_form, 
              janela_acompanhamentoprocessual, 
              janela_diariooficial, 
              janela_jurimetria, 
              janela_jurisprudencia):
    frame.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
    frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                       weight=1, uniform='a')
    frame.grid(row=0, column=0, sticky='nsew')

# ========================== Home
janela_padrao(janela_home, 'início')
botoes_menu(janela_home)

# ========================== Gerador
janela_padrao(janela_gerador, 'gerador')
botoes_menu(janela_gerador)

# ========================== Gerador-documentos
janela_padrao(janela_gerador_documentos, 'Escolha o(s) documento(s)')
botoes_menu(janela_gerador_documentos)

# ========================== Gerador-documentos-opções
janela_padrao(janela_gerador_documentos_opcoes, 'Opções')
botoes_menu(janela_gerador_documentos_opcoes)

# ========================== Gerador-documentos-formulário
janela_padrao(janela_gerador_documentos_form, 'Preencha o formulário abaixo')
botoes_menu(janela_gerador_documentos_form)

# ========================== Acompanhamento Processual
janela_padrao(janela_acompanhamentoprocessual, 'Movimentações Processuais')
botoes_menu(janela_acompanhamentoprocessual)

# ========================== Diário Oficial
janela_padrao(janela_diariooficial, 'Publicações')
botoes_menu(janela_diariooficial)

# ========================== Jurimetria
janela_padrao(janela_jurimetria, 'Jurimetria')
botoes_menu(janela_jurimetria)

# ========================== Jurisprudência
janela_padrao(janela_jurisprudencia, 'Pesquisa de jurisprudência')
botoes_menu(janela_jurisprudencia)

show_frame(janela_home)

janela.mainloop()
