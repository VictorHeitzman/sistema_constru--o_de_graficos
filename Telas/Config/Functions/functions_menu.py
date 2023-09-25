from Config.Models.models import *

class Functions():
    
    def abrir(self):
        path = filedialog.askopenfilename(defaultextension='.xlsx',filetypes=[('Excel Files','*.xlsx')])
        # path = r'D:\Documentos\cursos_projetos\projetos\Projeto_Python\sistema_construção_de_graficos\Arquivos\Estado.xlsx'
        if path:
            try:
                
                self.df = pd.read_excel(path)

                messagebox.showinfo('Aviso','Arquivo aberto com sucesso!')

            except Exception as e:
                messagebox.showerror('Error', f'Não foi possível abrir o arquio: {e}')
        
    
    def gerar_graf_coluna_2(self):
        self.ax.clear()

        col_x = self.input_eixo_x.get()
        col_y = self.input_eixo_y.get()
        
        df_agrupado = self.df.groupby(col_x).sum()[col_y]

        titulo = self.input_titulo.get()

        self.ax.bar(df_agrupado.index,df_agrupado.values)
        self.ax.set_xlabel(col_x)
        self.ax.set_ylabel(col_y)

        self.ax.set_xticklabels(df_agrupado.index, rotation=45, ha='right')
        self.ax.grid(True, axis='y')
        self.ax.figure.set_size_inches(10,6)

        if titulo == '':
            self.ax.set_title(f'Gráfico de Colunas: {col_x} x {col_y}')
        else:
            self.ax.set_title(f'{titulo}')
        for i, v in enumerate(df_agrupado.values):

            self.ax.annotate('{:,.0f}'.format(v), xy=(i, v), ha='center', va='bottom')
        
        self.canvas.draw()

        if self.input_titulo.get() == '':
            self.ax.figure.savefig('Graficos\grafico_coluna.png', dpi=80)
        else: self.ax.figure.savefig(f'Graficos\{self.input_titulo.get()}.png', dpi=80)

        self.root_graf_conluna.destroy()
    
    def gerar_graf_pizza_2(self):
        self.ax.clear()

        col_x = self.input_eixo_x.get()
        col_y = self.input_eixo_y.get()
        
        df_agrupado = self.df.groupby(col_x).sum()[col_y]

        titulo = self.input_titulo.get()

        total = df_agrupado.sum()
        pedacos = [(v / total) * 100 for v in df_agrupado.values]

        self.ax.pie(df_agrupado.values,labels=[f'{label} ({value:.0f})'
                                               for label, value in zip(df_agrupado.index, df_agrupado.values)],
                                               autopct='%1.0f%%')
                        
        
        if titulo == '':
            self.ax.set_title(f'Gráfico de Pizza: {col_x} x {col_y}')
        else:
            self.ax.set_title(f'{titulo}')
        for i, v in enumerate(df_agrupado.values):

            self.ax.annotate('{:,.0f}'.format(v), xy=(i, v), ha='center', va='bottom')
        
        self.canvas.draw()
        
        if self.input_titulo.get() == '':
            self.ax.figure.savefig('Graficos\grafico_Pizza.png', dpi=80)
        else: self.ax.figure.savefig(f'Graficos\{self.input_titulo.get()}.png', dpi=80)

        self.root_graf_pizza.destroy()

    def gerar_graf_linha_2(self):
        self.ax.clear()

        col_x = self.input_eixo_x.get()
        col_y = self.input_eixo_y.get()
        
        df_agrupado = self.df.groupby(col_x).sum()[col_y]

        titulo = self.input_titulo.get()

        self.ax.plot(df_agrupado.index,df_agrupado.values,
                     '-o',color='mediumseagreen',
                     linewidth=2,
                     markersize=8)
        
        self.ax.set_xlabel(col_x)
        self.ax.set_ylabel(col_y)

        if titulo == '':
            self.ax.set_title(f'Gráfico de Linha: {col_x} x {col_y}')
        else:
            self.ax.set_title(f'{titulo}')
        for i, v in enumerate(df_agrupado.values):

            valor_formatado = '{:,.0f}'.format(v)
            self.ax.annotate(valor_formatado,
                             xy=(df_agrupado.index[i],
                                 df_agrupado.values[i]),
                                 ha='center',
                                 va='bottom')
        
        self.ax.set_facecolor('white')
        self.ax.grid(color='lightgray', linestyle='-', linewidth=0.5)

        self.ax.set_xticklabels(df_agrupado.index, rotation=40)

        self.canvas.draw()

        if self.input_titulo.get() == '':
            self.ax.figure.savefig('Graficos\grafico_linha.png', dpi=80)
        else: self.ax.figure.savefig(f'Graficos\{self.input_titulo.get()}.png', dpi=80)

        self.root_graf_linha.destroy()

    def gerar_graf_area_2(self):
        self.ax.clear()

        col_x = self.input_eixo_x.get()
        col_y = self.input_eixo_y.get()
        
        df_agrupado = self.df.groupby(col_x).sum()[col_y]

        titulo = self.input_titulo.get()

        self.ax.fill_between(df_agrupado.index, 
                             df_agrupado.values,
                            color='blue',
                            alpha=0.2,
                            label=col_y)
        
        self.ax.plot(df_agrupado.index,
                     df_agrupado.values,
                     color='blue',
                     label=f'{col_y} (linha)')
        self.ax.set_xlabel(col_x)
        self.ax.set_ylabel(f'Soma de {col_y}')
        self.ax.legend()

        self.ax.grid()
        if titulo == '':
            self.ax.set_title(f'Gráfico de Colunas: {col_x} x {col_y}')
        else:
            self.ax.set_title(f'{titulo}')
        for i, v in enumerate(df_agrupado.values):

            self.ax.annotate('{:,.0f}'.format(v), xy=(df_agrupado.index[i], df_agrupado.values[i]), ha='center', va='bottom')
        
        self.ax.set_xticklabels(df_agrupado.index, rotation=45, ha='right')

        self.canvas.draw()

        if self.input_titulo.get() == '':
            self.ax.figure.savefig('Graficos\grafico_area.png', dpi=80)
        else: self.ax.figure.savefig(f'Graficos\{self.input_titulo.get()}.png', dpi=80)

        self.root_graf_area.destroy()

    def gerar_graf_funil(self):
        self.ax.clear()

        col_x = self.input_eixo_x.get()
        col_y = self.input_eixo_y.get()
        
        df_agrupado = self.df.groupby(col_x).sum()[col_y]

        titulo = self.input_titulo.get()

        df_agrupado =  df_agrupado.sort_values(ascending=True)

        if titulo == '':
            self.ax.set_title(f'Gráfico de Colunas: {col_x} x {col_y}')
        else:
            self.ax.set_title(f'{titulo}')

        perc_acumulada = (df_agrupado.cumsum() / df_agrupado.sum()) *100

        altura = [perc_acumulada[0]] + [perc_acumulada.iloc[i] - perc_acumulada[i-1] for i in range(1, len(perc_acumulada))]

        cores = ['#00FFFF','#00CED1','#40E0D0','#48D1CC','#20B2AA','#008B8B','#008080','#7FFFD4','#66CDAA']

        cores = plt.get_cmap('tab10', len(df_agrupado))(np.arange(len(df_agrupado)))

        nome = []

        for i, (indice, valor) in enumerate(df_agrupado.items()):
            

            esquerda = (100 - altura[i]) / 2
            

            self.ax.barh(i, altura[i], left=esquerda, 
                         color=cores[i],
                         alpha=0.7,
                         edgecolor="white")
            label = f"{indice}: {int(valor):,d}"
            largura_barra = altura[i]
            centraliza_barra = esquerda + largura_barra / 2
           

            self.ax.text(centraliza_barra,
                        i,
                        label,
                        color="black",
                        fontsize=10,
                        ha='center',
                        va='center')
            
        #Ordena o eixo x
        df_agrupado = df_agrupado.sort_index()
            
        #Remove os eixos do gráfico x e y
        fig, ax = plt.subplots()
        ax.set_axis_off()
        self.ax.axis("off")

        self.canvas.draw()

        if self.input_titulo.get() == '':
            self.ax.figure.savefig('Graficos\grafico_funil.png', dpi=80)
        else: self.ax.figure.savefig(f'Graficos\{self.input_titulo.get()}.png', dpi=80)

        self.root_graf_funil.destroy()

    def renomear_coluna(self, coluna, coluna_nova):
        self.df = self.df.rename(columns={coluna: coluna_nova})
        self.atualiza_treeview()
        self.root_renomear_coluna.destroy()

    def atualiza_treeview(self):
        self.treeview_editar_dados.delete(*self.treeview_editar_dados.get_children())
        
        self.treeview_editar_dados.config(columns= list(self.df.columns))
        
        for col in self.df.columns:
            self.treeview_editar_dados.heading(col, text=col)
            print(col)

        for i, row in self.df.iterrows():

            values = list(row)

            for j, value in enumerate(values):        
                self.treeview_editar_dados.grid(row=2, column=0, columnspan=2)

                if isinstance(value, np.generic):
                    values[j] = np.asscalar(value)
            
            self.treeview_editar_dados.insert('',END,values=values)
            
    def remover_coluna(self, coluna):
        self.df = self.df.drop(columns=coluna)
        self.atualiza_treeview()
        self.root_remover_coluna.destroy()       

    def remover_linhas(self, linha_inicio=None, linha_fim=None):

        linha_inicio = int(simpledialog.askstring('Remover Linhas', 'Digite a linha inicial'))
        
        linha_fim = int(simpledialog.askstring('Remover Linhas', 'Digite a linha fim'))

        self.df = self.df.drop(self.df.index[linha_inicio-1:linha_fim])

        self.atualiza_treeview()
    
    def remover_duplicatas(self, coluna):

        self.df = self.df.drop_duplicates(subset=coluna, keep=FIRST)
        
        self.atualiza_treeview()

        self.root_remover_duplicatas.destroy()
    
    def remover_blanks(self):

        resp = messagebox.askyesno('Remover brancas','Tem certeza que deseja remover linhas em branco')

        if resp == 1:
            self.df = self.df.dropna(axis=0)
        
        self.atualiza_treeview()
