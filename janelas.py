from tkinter import *


def show_frame(frame):
    frame.tkraise()


def titulo_padrao(frame, parent, texto):
    frame = Frame(parent, bg='red')
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.grid(row=0, column=0, columnspan=2, sticky='nsew')
    texto = Label(frame, text=f'{texto}', bg='white')
    texto.grid(row=0, column=0)


def menu_padrao(frame, parent):
    frame = Frame(parent, bg='grey')
    frame.columnconfigure(0, weight=1, uniform='a')
    frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1, uniform='a')
    frame.grid(row=1, column=0, sticky='nsew')
    return frame


def painel_padrao(frame, parent):
    frame = Frame(parent, bg='yellow')
    frame.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1, uniform='a')
    frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1, uniform='a')
    frame.grid(row=1, column=1, sticky='nsew')
    return frame


def botoes_menu(parent):
    botao_inicio = Button(
        parent, text='Início', command=lambda: show_frame(janela_home))
    botao_inicio.grid(row=2, column=0, sticky='nsew')

    botao_gerador = Button(
        parent, text='Gerador', command=lambda: show_frame(janela_gerador))
    botao_gerador.grid(row=3, column=0, sticky='nsew')

    botao_acompanhamentoprocessual = Button(
        parent, text='Acompanhamento Processual', command=lambda: show_frame(janela_acompanhamentoprocessual))
    botao_acompanhamentoprocessual.grid(row=4, column=0, sticky='nsew')

    botao_diariooficial = Button(
        parent, text='Diário Oficial', command=lambda: show_frame(janela_diariooficial))
    botao_diariooficial.grid(row=5, column=0, sticky='nsew')

    botao_jurimetria = Button(
        parent, text='Jurimetria', command=lambda: show_frame(janela_jurimetria))
    botao_jurimetria.grid(row=6, column=0, sticky='nsew')

    botao_jurisprudencia = Button(
        parent, text='Jurisprudência', command=lambda: show_frame(janela_jurisprudencia))
    botao_jurisprudencia.grid(row=7, column=0, sticky='nsew')


def botao_proximo(nome, parent, destino):
    nome = Button(parent, text='Próximo', command=lambda: show_frame(destino))
    nome.grid(row=9, column=8, columnspan=1, sticky='new')
    return nome


def botao_voltar(nome, parent, destino):
    nome = Button(parent, text='Voltar', command=lambda: show_frame(destino))
    nome.grid(row=9, column=1, sticky='new')


janela = Tk()

janela.state('zoomed')
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

# ====================== Criação das janelas padrão
janela_home = Frame(janela)
janela_gerador = Frame(janela)
janela_gerador_documentos = Frame(janela)
janela_gerador_documentos_opcoes = Frame(janela)
janela_gerador_documentos_form = Frame(janela)
janela_acompanhamentoprocessual = Frame(janela)
janela_diariooficial = Frame(janela)
janela_jurimetria = Frame(janela)
janela_jurisprudencia = Frame(janela)


# ======================= Configuração das janelas padrão
for frame in janela.winfo_children():
    frame.columnconfigure(0, weight=1, uniform='a')
    frame.columnconfigure(1, weight=4, uniform='a')
    frame.rowconfigure(0, weight=1, uniform='a')
    frame.rowconfigure(1, weight=9, uniform='a')
    frame.grid(row=0, column=0, sticky='nsew')


# ======================= Configuração dos frames (titulo, menu e painel)
frame_titulo = Frame()
titulo_home = Frame()
titulo_gerador = Frame()
titulo_gerador_documentos = Frame()
titulo_gerador_documentos_opcoes = Frame()
titulo_gerador_documentos_form = Frame()
titulo_acompanhamentoprocessual = Frame()
titulo_diariooficial = Frame()
titulo_jurimetria = Frame()
titulo_jurisprudencia = Frame()

frame_menu = Frame()
menu_home = None
menu_home = menu_padrao(menu_home, janela_home)
menu_gerador = None
menu_gerador = menu_padrao(menu_gerador, janela_gerador)
menu_gerador_documentos = None
menu_gerador_documentos = menu_padrao(
    menu_gerador_documentos, janela_gerador_documentos)
menu_gerador_documentos_opcoes = None
menu_gerador_documentos_opcoes = menu_padrao(
    menu_gerador_documentos_opcoes, janela_gerador_documentos_opcoes)
menu_gerador_documentos_form = None
menu_gerador_documentos_form = menu_padrao(
    menu_gerador_documentos_form, janela_gerador_documentos_form)
menu_acompanhamentoprocessual = None
menu_acompanhamentoprocessual = menu_padrao(
    menu_acompanhamentoprocessual, janela_acompanhamentoprocessual)
menu_diariooficial = None
menu_diariooficial = menu_padrao(menu_diariooficial, janela_diariooficial)
menu_jurimetria = None
menu_jurimetria = menu_padrao(menu_jurimetria, janela_jurimetria)
menu_jurisprudencia = None
menu_jurisprudencia = menu_padrao(menu_jurisprudencia, janela_jurisprudencia)

frame_painel = Frame()
painel_home = None
painel_home = painel_padrao(painel_home, janela_home)
painel_gerador = None
painel_gerador = painel_padrao(painel_gerador, janela_gerador)
painel_gerador_documentos = None
painel_gerador_documentos = painel_padrao(painel_gerador_documentos, janela_gerador_documentos)
painel_gerador_documentos_opcoes = None
painel_gerador_documentos_opcoes = painel_padrao(painel_gerador_documentos_opcoes, janela_gerador_documentos_opcoes)
painel_gerador_documentos_form = None
painel_gerador_documentos_form = painel_padrao(painel_gerador_documentos_form, janela_gerador_documentos_form)
painel_acompanhamentoprocessual = None
painel_acompanhamentoprocessual = painel_padrao(painel_acompanhamentoprocessual, janela_acompanhamentoprocessual)
painel_diariooficial = None
painel_diariooficial = painel_padrao(painel_diariooficial, janela_diariooficial)
painel_jurimetria = None
painel_jurimetria = painel_padrao(painel_jurimetria, janela_jurimetria)
painel_jurisprudencia = None
painel_jurisprudencia = painel_padrao(painel_jurisprudencia, janela_jurisprudencia)


# =========================== Configuração painéis
# for frame in (painel_home, painel_gerador, painel_gerador_documentos, painel_gerador_documentos_opcoes, painel_gerador_documentos_form):


# ========================== Criando botões das funções
botao_proximo_gerador = None
botao_proximo_gerador = botao_proximo(botao_proximo_gerador, painel_gerador, janela_gerador_documentos)
botao_proximo_gerador_documentos = None
botao_proximo_gerador_documentos = botao_proximo(botao_proximo_gerador_documentos, painel_gerador_documentos, janela_gerador_documentos_opcoes)
botao_proximo_gerador_documentos_opcoes = None
botao_proximo_gerador_documentos_opcoes = botao_proximo(botao_proximo_gerador_documentos_opcoes, painel_gerador_documentos_opcoes, janela_gerador_documentos_form)
botao_voltar_gerador_documentos = None
botao_voltar_gerador_documentos = botao_voltar(botao_voltar_gerador_documentos, painel_gerador_documentos, janela_gerador)
botao_voltar_gerador_documentos_opcoes = None
botao_voltar_gerador_documentos_opcoes = botao_voltar(botao_voltar_gerador_documentos_opcoes, painel_gerador_documentos_opcoes, janela_gerador_documentos)
botao_voltar_gerador_documentos_form = None
botao_voltar_gerador_documentos_form = botao_voltar(botao_voltar_gerador_documentos_form, painel_gerador_documentos_form, janela_gerador_documentos_opcoes)

# ========================== Home
titulo_padrao(titulo_home, janela_home, 'início')
menu_home
botoes_menu(menu_home)
painel_home

# ========================== Gerador
titulo_padrao(titulo_gerador, janela_gerador, 'gerador')
menu_gerador
botoes_menu(menu_gerador)
painel_gerador
botao_proximo_gerador

# ========================== Gerador-documentos
titulo_padrao(titulo_gerador_documentos,
              janela_gerador_documentos, 'Escolha o(s) documento(s)')
menu_gerador_documentos
botoes_menu(menu_gerador_documentos)
painel_gerador_documentos
botao_proximo_gerador_documentos
botao_voltar_gerador_documentos

# ========================== Gerador-documentos-opções
titulo_padrao(titulo_gerador_documentos_opcoes,
              janela_gerador_documentos_opcoes, 'Opções')
menu_gerador_documentos_opcoes
botoes_menu(menu_gerador_documentos_opcoes)
painel_gerador_documentos_opcoes
botao_proximo_gerador_documentos_opcoes
botao_voltar_gerador_documentos_opcoes

# ========================== Gerador-documentos-formulário
titulo_padrao(titulo_gerador_documentos_form,
              janela_gerador_documentos_form, 'Preencha o formulário abaixo')
menu_gerador_documentos_form
botoes_menu(menu_gerador_documentos_form)
painel_gerador_documentos_form
botao_voltar_gerador_documentos_form

# ========================== Acompanhamento Processual
titulo_padrao(titulo_acompanhamentoprocessual,
              janela_acompanhamentoprocessual, 'Movimentações Processuais')
menu_acompanhamentoprocessual
botoes_menu(menu_acompanhamentoprocessual)
painel_padrao(painel_acompanhamentoprocessual, janela_acompanhamentoprocessual)

# ========================== Diário Oficial
titulo_padrao(titulo_diariooficial,
              janela_diariooficial, 'Publicações')
menu_diariooficial
botoes_menu(menu_diariooficial)
painel_padrao(painel_diariooficial, janela_diariooficial)

# ========================== Jurimetria
titulo_padrao(titulo_jurimetria,
              janela_jurimetria, 'Jurimetria')
menu_jurimetria
botoes_menu(menu_jurimetria)
painel_padrao(painel_jurimetria, janela_jurimetria)

# ========================== Jurisprudência
titulo_padrao(titulo_jurisprudencia,
              janela_jurisprudencia, 'Pesquisa de Jurisprudência')
menu_jurisprudencia
botoes_menu(menu_jurisprudencia)
painel_padrao(painel_jurisprudencia, janela_jurisprudencia)

show_frame(janela_home)

janela.mainloop()
