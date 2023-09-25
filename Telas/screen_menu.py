
from Config.Models.models import *

from Config.Functions.functions_menu import Functions

class Screen_menu(Functions):

    def __init__(self) -> None:
        
        self.root_menu = Tk()

        self.config()
        self.menu()
        self.frames()
        self.labels()

        self.root_menu.mainloop()

    #---------------------------TELA INICIAL---------------------------
    def config(self):
        self.root_menu.title('Construção de gráficos')
        self.root_menu.columnconfigure(1,weight=1)
        self.root_menu.config(background='white')
        self.root_menu.iconbitmap('Icone\icon_grafico.ico')
    def menu(self):
        self.menu_bar = Menu(self.root_menu) # Criando barra de menu
        self.root_menu.config(menu=self.menu_bar) # Adcionando ela na tela

        self.arquivo_menu = Menu(self.menu_bar,tearoff=0) # Criando um icone de 'arquivo'
        self.menu_bar.add_cascade(label='Arquivo',menu=self.arquivo_menu) # Mostrando o icone na tela
        
        self.arquivo_menu.add_cascade(label='Abrir',command=self.abrir)
    def frames(self):
        self.frame_botoes = Frame(self.root_menu, background='white')
        self.frame_botoes.grid(row=1, column=0, padx=10, pady=10, sticky=N+S)

    def labels(self):
        #--------------------------FRAME RELATORIOS---------------------------------
        self.button_editar_dados = Button(self.frame_botoes, text='Editar Dados', command=self.init_editar_dados)
        self.button_editar_dados.grid(row=0, column=0,padx=10, pady=10, sticky='NESW')
        #------------------------------------------------------------------------------

        #--------------------------FRAME BOTÕES GRÁFICOS---------------------------------
        self.button_colunas = Button(self.frame_botoes, text='Gráfico de Colunas',command=self.init_graf_coluna)
        self.button_colunas.grid(row=1, column=0,padx=10,pady=10, sticky='NESW')
        
        self.button_pizza = Button(self.frame_botoes, text='Gráfico de Pizza', command=self.init_graf_pizza)
        self.button_pizza.grid(row=2, column=0,padx=10,pady=10, sticky='NESW')

        self.button_linha = Button(self.frame_botoes, text='Gráfico de Linha', command=self.init_graf_linha)
        self.button_linha.grid(row=3, column=0,padx=10,pady=10, sticky='NESW')
        
        self.button_area = Button(self.frame_botoes, text='Gráfico de Area', command=self.init_graf_area)
        self.button_area.grid(row=4, column=0,padx=10,pady=10, sticky='NESW')

        self.button_funil = Button(self.frame_botoes, text='Gráfico de Funil', command=self.init_graf_funil)
        self.button_funil.grid(row=5, column=0,padx=10,pady=10, sticky='NESW')
        #------------------------------------------------------------------------------

        self.fig = plt.figure(figsize=(6,6), dpi=100)

        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root_menu)

        self.canvas.get_tk_widget().grid(row=1,column=1,padx=10, pady=10, sticky=N+S+E+W)      
    #-------------------------------------------------------------------

    #----------------------------TELA GRAFICO COLUNA---------------------- 
    def init_graf_coluna(self):
        try:
            self.config_graf_coluna()
            self.labels_graf_coluna()
        except: 
            messagebox.showerror('Erro','Selecione um arquivo')
            self.root_graf_conluna.destroy()
    def config_graf_coluna(self):
        self.root_graf_conluna = Toplevel()
        self.root_graf_conluna.title('Gráfico Colunas')
        self.root_graf_conluna.geometry('300x300')
        
        self.root_graf_conluna.focus_force()
        self.root_graf_conluna.grab_set()  
    def labels_graf_coluna(self):
        #-------------------------------Eixo X------------------------------------
        self.txt_eixo_x = Label(self.root_graf_conluna, text='Eixo: X')
        self.txt_eixo_x.pack(pady=5)

        self.input_eixo_x = Combobox(self.root_graf_conluna, values=self.df.columns.to_list())
        self.input_eixo_x.pack(pady=5)
        #-------------------------------------------------------------------------

        #-------------------------------Eixo Y------------------------------------
        self.txt_eixo_y = Label(self.root_graf_conluna, text='Eixo Y')
        self.txt_eixo_y.pack(pady=5)

        self.input_eixo_y = Combobox(self.root_graf_conluna, values=self.df.columns.to_list())
        self.input_eixo_y.pack(pady=5)
        #-------------------------------------------------------------------------

        #-------------------------------imagem------------------------------------
        self.txt_titulo = Label(self.root_graf_conluna, text='Título')
        self.txt_titulo.pack(pady=5)
        
        self.input_titulo = Entry(self.root_graf_conluna)
        self.input_titulo.pack(pady=5)
        #-------------------------------------------------------------------

        #-------------------------------gerar Grefico 2------------------------------------
        self.txt_gerar_img_coluna_2 = Button(self.root_graf_conluna, text='Gerar Gráfico',command=self.gerar_graf_coluna_2)
        self.txt_gerar_img_coluna_2.pack()
        #-------------------------------------------------------------------

    #----------------------------TELA GRAFICO PIZZA---------------------- 
    def init_graf_pizza(self):
        try:
            self.config_graf_pizza()
            self.labels_graf_pizza()
        except: 
            messagebox.showerror('Erro','Selecione um arquivo')
            self.root_graf_pizza.destroy()
    def config_graf_pizza(self):
        self.root_graf_pizza = Toplevel()
        self.root_graf_pizza.title('Gráfico Pizza')
        self.root_graf_pizza.geometry('300x300')
        
        self.root_graf_pizza.focus_force()
        self.root_graf_pizza.grab_set()  
    def labels_graf_pizza(self):
        #-------------------------------Eixo X------------------------------------
        self.txt_eixo_x = Label(self.root_graf_pizza, text='Eixo: X')
        self.txt_eixo_x.pack(pady=5)

        self.input_eixo_x = Combobox(self.root_graf_pizza, values=self.df.columns.to_list())
        self.input_eixo_x.pack(pady=5)
        #-------------------------------------------------------------------------

        #-------------------------------Eixo Y------------------------------------
        self.txt_eixo_y = Label(self.root_graf_pizza, text='Eixo Y')
        self.txt_eixo_y.pack(pady=5)

        self.input_eixo_y = Combobox(self.root_graf_pizza, values=self.df.columns.to_list())
        self.input_eixo_y.pack(pady=5)
        #-------------------------------------------------------------------------

        #-------------------------------imagem------------------------------------
        self.txt_titulo = Label(self.root_graf_pizza, text='Título')
        self.txt_titulo.pack(pady=5)
        
        self.input_titulo = Entry(self.root_graf_pizza)
        self.input_titulo.pack(pady=5)
        #-------------------------------------------------------------------

        #-------------------------------gerar Grefico 2------------------------------------
        self.txt_gerar_img_pizza_2 = Button(self.root_graf_pizza, text='Gerar Gráfico',command=self.gerar_graf_pizza_2)
        self.txt_gerar_img_pizza_2.pack()
        #-------------------------------------------------------------------

    #----------------------------TELA GRAFICO LINHA---------------------- 
    def init_graf_linha(self):
        try:
            self.config_graf_linha()
            self.labels_graf_linha()
        except: 
            messagebox.showerror('Erro','Selecione um arquivo')
            self.root_graf_linha.destroy()
    def config_graf_linha(self):
        self.root_graf_linha = Toplevel()
        self.root_graf_linha.title('Gráfico Area')
        self.root_graf_linha.geometry('300x300')
        
        self.root_graf_linha.focus_force()
        self.root_graf_linha.grab_set()  
    def labels_graf_linha(self):
        #-------------------------------Eixo X------------------------------------
        self.txt_eixo_x = Label(self.root_graf_linha, text='Eixo: X')
        self.txt_eixo_x.pack(pady=5)

        self.input_eixo_x = Combobox(self.root_graf_linha, values=self.df.columns.to_list())
        self.input_eixo_x.pack(pady=5)
        #-------------------------------------------------------------------------

        #-------------------------------Eixo Y------------------------------------
        self.txt_eixo_y = Label(self.root_graf_linha, text='Eixo Y')
        self.txt_eixo_y.pack(pady=5)

        self.input_eixo_y = Combobox(self.root_graf_linha, values=self.df.columns.to_list())
        self.input_eixo_y.pack(pady=5)
        #-------------------------------------------------------------------------

        #-------------------------------imagem------------------------------------
        self.txt_titulo = Label(self.root_graf_linha, text='Título')
        self.txt_titulo.pack(pady=5)
        
        self.input_titulo = Entry(self.root_graf_linha)
        self.input_titulo.pack(pady=5)
        #-------------------------------------------------------------------

        #-------------------------------gerar Grefico 2------------------------------------
        self.txt_gerar_img_linha_2 = Button(self.root_graf_linha, text='Gerar Gráfico',command=self.gerar_graf_linha_2)
        self.txt_gerar_img_linha_2.pack()
        #-------------------------------------------------------------------

    #----------------------------TELA GRAFICO AREA---------------------- 
    def init_graf_area(self):
        try:
            self.config_graf_are()
            self.labels_graf_are()
        except: 
            messagebox.showerror('Erro','Selecione um arquivo')
            self.root_graf_area.destroy()
    def config_graf_are(self):
        self.root_graf_area = Toplevel()
        self.root_graf_area.title('Gráfico Pizza')
        self.root_graf_area.geometry('300x300')
        
        self.root_graf_area.focus_force()
        self.root_graf_area.grab_set()  
    def labels_graf_are(self):
        #-------------------------------Eixo X------------------------------------
        self.txt_eixo_x = Label(self.root_graf_area, text='Eixo: X')
        self.txt_eixo_x.pack(pady=5)

        self.input_eixo_x = Combobox(self.root_graf_area, values=self.df.columns.to_list())
        self.input_eixo_x.pack(pady=5)
        #-------------------------------------------------------------------------

        #-------------------------------Eixo Y------------------------------------
        self.txt_eixo_y = Label(self.root_graf_area, text='Eixo Y')
        self.txt_eixo_y.pack(pady=5)

        self.input_eixo_y = Combobox(self.root_graf_area, values=self.df.columns.to_list())
        self.input_eixo_y.pack(pady=5)
        #-------------------------------------------------------------------------

        #-------------------------------imagem------------------------------------
        self.txt_titulo = Label(self.root_graf_area, text='Título')
        self.txt_titulo.pack(pady=5)
        
        self.input_titulo = Entry(self.root_graf_area)
        self.input_titulo.pack(pady=5)
        #-------------------------------------------------------------------

        #-------------------------------gerar Grefico 2------------------------------------
        self.txt_gerar_img_pizza_2 = Button(self.root_graf_area, text='Gerar Gráfico',command=self.gerar_graf_area_2)
        self.txt_gerar_img_pizza_2.pack()
        #-------------------------------------------------------------------

    #----------------------------TELA GRAFICO FUNIL---------------------- 
    def init_graf_funil(self):
        try:
            self.config_graf_funil()
            self.labels_graf_funil()
        except: 
            messagebox.showerror('Erro','Selecione um arquivo')
            self.root_graf_funil.destroy()
    def config_graf_funil(self):
        self.root_graf_funil = Toplevel()
        self.root_graf_funil.title('Gráfico Pizza')
        self.root_graf_funil.geometry('300x300')
        
        self.root_graf_funil.focus_force()
        self.root_graf_funil.grab_set()  
    def labels_graf_funil(self):
        #-------------------------------Eixo X------------------------------------
        self.txt_eixo_x = Label(self.root_graf_funil, text='Eixo: X')
        self.txt_eixo_x.pack(pady=5)

        self.input_eixo_x = Combobox(self.root_graf_funil, values=self.df.columns.to_list())
        self.input_eixo_x.pack(pady=5)
        #-------------------------------------------------------------------------

        #-------------------------------Eixo Y------------------------------------
        self.txt_eixo_y = Label(self.root_graf_funil, text='Eixo Y')
        self.txt_eixo_y.pack(pady=5)

        self.input_eixo_y = Combobox(self.root_graf_funil, values=self.df.columns.to_list())
        self.input_eixo_y.pack(pady=5)
        #-------------------------------------------------------------------------

        #-------------------------------imagem------------------------------------
        self.txt_titulo = Label(self.root_graf_funil, text='Título')
        self.txt_titulo.pack(pady=5)
        
        self.input_titulo = Entry(self.root_graf_funil)
        self.input_titulo.pack(pady=5)
        #-------------------------------------------------------------------

        #-------------------------------gerar Grefico 1------------------------------------
        self.txt_gerar_img_pizza = Button(self.root_graf_funil, text='Gerar Gráfico', command=self.gerar_graf_funil)
        self.txt_gerar_img_pizza.pack()
        #-------------------------------------------------------------------

    #----------------------------TELA EDITAR DADOS---------------------- 
    def init_editar_dados(self):
        try:
            self.config_editar_dados()
            self.labels_editar_dados()
            self.menu_editar_dados()
        except: 
            messagebox.showerror('Erro','Selecione um arquivo')
            self.root_editar_dados.destroy()
    def config_editar_dados(self):
        self.root_editar_dados = Toplevel()
        self.root_editar_dados.title('Editar Dados')
        
        self.root_editar_dados.focus_force()
        self.root_editar_dados.grab_set()
    def menu_editar_dados(self):
        self.menu_bar_dados = Menu(self.root_editar_dados, tearoff=0)
        self.root_editar_dados.config(menu=self.menu_bar_dados)

        self.menu_salvar = Menu(self.root_editar_dados, tearoff=0)
        self.menu_bar_dados.add_cascade(label='Formatar',menu=self.menu_salvar)
        self.menu_salvar.add_command(label='Renomear Coluna', command=self.init_renomear_colunas)
        self.menu_salvar.add_command(label='Remover coluna', command=self.init_remover_colunas)
        self.menu_salvar.add_command(label='Remover linhas Alternadas', command=self.remover_linhas)
        self.menu_salvar.add_command(label='Remover duplicados', command=self.init_remover_duplicatas)
        self.menu_salvar.add_command(label='Remover linhas em branco', command=self.remover_blanks)
    def labels_editar_dados(self):
        titulo = Label(self.root_editar_dados,
                       text='Edite seus dados: {}'.format(','.join(self.df.columns)))
        titulo.grid(row=1, column=0, columnspan=2)

        self.treeview_editar_dados = ttk.Treeview(self.root_editar_dados,
                                columns=list(self.df.columns), show="headings")
              
        for col in self.df.columns:
            
            self.treeview_editar_dados.heading(col, text=col)
            
        for i, row in self.df.iterrows():
            
            self.treeview_editar_dados.insert("", "end", values=list(row))
            
        self.treeview_editar_dados.grid(row=2, column=0, columnspan=2)
        
    #----------------------------TELA Renomear Colunas---------------------- 
    def init_renomear_colunas(self):
        self.config_renomear_coluna()
        self.labels_renomear_coluna()
    def config_renomear_coluna(self):
        self.root_renomear_coluna = Toplevel()
        self.root_renomear_coluna.title('Renomear coluna')
        self.root_renomear_coluna.geometry('300x300')
        self.root_renomear_coluna.focus_force()
        self.root_renomear_coluna.grab_set()
    def labels_renomear_coluna(self):
        txt_coluna = Label(self.root_renomear_coluna, text='Selecione uma coluna')
        txt_coluna.pack(pady=10)

        self.input_coluna = Combobox(self.root_renomear_coluna,values=self.df.columns.to_list())
        self.input_coluna.pack(pady=10)

        txt_coluna_novo = Label(self.root_renomear_coluna, text='Digite o novo nome')
        txt_coluna_novo.pack(pady=10)

        self.input_coluna_novo = Entry(self.root_renomear_coluna,width=30)
        self.input_coluna_novo.pack(pady=10)

        self.button_renomear = Button(self.root_renomear_coluna,text='renomear', command=lambda: self.renomear_coluna(self.input_coluna.get(),
                                                                                                                        self.input_coluna_novo.get()))
        self.button_renomear.pack(pady=10)
    
    #----------------------------TELA REMOVER Colunas---------------------- 
    def init_remover_colunas(self):
        self.config_remover_coluna()
        self.labels_remover_coluna()
    def config_remover_coluna(self):        
        self.root_remover_coluna = Toplevel()
        self.root_remover_coluna.title('Remover Coluna')
        self.root_remover_coluna.geometry('300x300')
        self.root_remover_coluna.focus_force()
        self.root_remover_coluna.grab_set()
    def labels_remover_coluna(self):
        self.input_coluna = Combobox(self.root_remover_coluna,values=self.df.columns.to_list())
        self.input_coluna.pack(pady=10)

        self.button_remover = Button(self.root_remover_coluna,text='Remover', command=lambda: self.remover_coluna(self.input_coluna.get()))
        self.button_remover.pack(pady=10)

    #----------------------------TELA REMOVER DUPLICATAS---------------------- 
    def init_remover_duplicatas(self):
        self.config_remover_duplicatas()
        self.labels_remover_duplicatas()
    def config_remover_duplicatas(self):
        self.root_remover_duplicatas = Toplevel()
        self.root_remover_duplicatas.title('Remover Coluna')
        self.root_remover_duplicatas.geometry('300x300')
        self.root_remover_duplicatas.focus_force()
        self.root_remover_duplicatas.grab_set()
    def labels_remover_duplicatas(self):
        self.input_coluna = Combobox(self.root_remover_duplicatas,values=self.df.columns.to_list())
        self.input_coluna.pack(pady=10)

        self.button_remover = Button(self.root_remover_duplicatas,text='Remover', command=lambda: self.remover_duplicatas(self.input_coluna.get()))
        self.button_remover.pack(pady=10)

if __name__ == '__main__':
    Screen_menu()