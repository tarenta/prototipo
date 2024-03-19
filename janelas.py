from tkinter import *


def show_frame(frame):
    frame.tkraise()


def janela_padrao(janela_parent, frame_painel, id_janela):
    janela_padrao_titulo = Frame(janela_parent, bg='red')
    id = Label(janela_parent, text=f'{id_janela}', bg='red')
    janela_padrao_titulo.grid(row=0, column=0, columnspan=4, sticky='nsew')
    id.grid(row=0, column=0, columnspan=4, sticky='nsew')
    janela_padrao_menu = Frame(janela_parent, bg='grey')
    janela_padrao_menu.grid(row=1, rowspan=10, column=0, sticky='nsew')
    frame_painel = frame_painel



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

def botao_proximo(nome, parent, destino):
    nome = Button(parent, text='Próximo', command=lambda: show_frame(destino))
    nome.grid(row=10, column=1, sticky='e')
    nome = nome

def botao_voltar(nome, parent, destino):
    nome = Button(parent, text='Voltar', command=lambda: show_frame(destino))
    nome.grid(row=10, column=0, sticky='w')

janela = Tk()

janela.state('zoomed')
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

#====================== Criação dos frames
janela_home = Frame(janela)
painel_home = Frame(janela_home)
janela_gerador = Frame(janela)
painel_gerador = Frame(janela_gerador)
janela_gerador_documentos = Frame(janela)
painel_gerador_documentos = Frame(janela_gerador_documentos)
janela_gerador_documentos_opcoes = Frame(janela)
painel_gerador_documentos_opcoes = Frame(janela_gerador_documentos_opcoes)
janela_gerador_documentos_form = Frame(janela)
painel_gerador_documentos_form = Frame(janela_gerador_documentos_form)
janela_acompanhamentoprocessual = Frame(janela)
painel_acompanhamentoprocessual = Frame(janela_acompanhamentoprocessual)
janela_diariooficial = Frame(janela)
painel_diariooficial = Frame(janela_diariooficial)
janela_jurimetria = Frame(janela)
painel_jurimetria = Frame(janela_jurimetria)
janela_jurisprudencia = Frame(janela)
painel_jurisprudencia = Frame(janela_jurisprudencia)

#======================= Configuração das janelas padrão
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

#=========================== Configuração painéis
for frame in (painel_home, painel_gerador, painel_gerador_documentos, painel_gerador_documentos_opcoes, painel_gerador_documentos_form):
    frame.columnconfigure((0, 1), weight=1, uniform='a')
    frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                       weight=1, uniform='a')
    frame.grid(row=1, column=1, rowspan=10, columnspan=3, sticky='nsew')

#========================== Criando botões das funções
botao_proximo_gerador = ''
botao_proximo_gerador_documentos = ''
botao_proximo_gerador_documentos_opcoes = ''
botao_voltar_gerador_documentos = ''
botao_voltar_gerador_documentos_opcoes = ''
botao_voltar_gerador_documentos_form = ''

# ========================== Home
janela_padrao(janela_home, painel_home, 'início')
botoes_menu(janela_home)

# ========================== Gerador
janela_padrao(janela_gerador, painel_gerador, 'Gerador')
botoes_menu(janela_gerador)
botao_proximo(botao_proximo_gerador, painel_gerador, janela_gerador_documentos)

# ========================== Gerador-documentos
janela_padrao(janela_gerador_documentos, painel_gerador_documentos, 'Escolha o(s) documento(s)')
botoes_menu(janela_gerador_documentos)
botao_proximo(botao_proximo_gerador_documentos, painel_gerador_documentos, janela_gerador_documentos_opcoes)
botao_voltar(botao_voltar_gerador_documentos, painel_gerador_documentos, janela_gerador)

# ========================== Gerador-documentos-opções
janela_padrao(janela_gerador_documentos_opcoes, painel_gerador_documentos_opcoes, 'Opções')
botoes_menu(janela_gerador_documentos_opcoes)
botao_proximo(botao_proximo_gerador_documentos_opcoes, painel_gerador_documentos_opcoes, janela_gerador_documentos_form)
botao_voltar(botao_proximo_gerador_documentos_opcoes, painel_gerador_documentos_opcoes, janela_gerador_documentos)

# ========================== Gerador-documentos-formulário
janela_padrao(janela_gerador_documentos_form, painel_gerador_documentos_form, 'Preencha o formulário abaixo')
botoes_menu(janela_gerador_documentos_form)
botao_voltar(botao_voltar_gerador_documentos_form, painel_gerador_documentos_form, janela_gerador_documentos_opcoes)

# ========================== Acompanhamento Processual
janela_padrao(janela_acompanhamentoprocessual, painel_acompanhamentoprocessual, 'Movimentações Processuais')
botoes_menu(janela_acompanhamentoprocessual)

# ========================== Diário Oficial
janela_padrao(janela_diariooficial, painel_diariooficial, 'Publicações')
botoes_menu(janela_diariooficial)

# ========================== Jurimetria
janela_padrao(janela_jurimetria, painel_jurimetria,'Jurimetria')
botoes_menu(janela_jurimetria)

# ========================== Jurisprudência
janela_padrao(janela_jurisprudencia, painel_jurisprudencia, 'Pesquisa de jurisprudência')
botoes_menu(janela_jurisprudencia)

show_frame(janela_home)

janela.mainloop()
