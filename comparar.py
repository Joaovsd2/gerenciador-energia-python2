import tkinter as tk
from tkinter import messagebox, Toplevel
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Função para análise da eficiência do consumo do aparelho
def analise_eficiencia(aparelho_escolhido, consumo_usuario, consumo_medio):
    if consumo_usuario > consumo_medio * 1.2:
        return f"⚠️ **ALERTA**: Seu consumo está significativamente acima da média para o aparelho '{aparelho_escolhido}'. Considere reduzir o uso para economizar energia e evitar custos excessivos."
    elif consumo_usuario < consumo_medio * 0.8:
        return f"✅ **INFORMAÇÃO**: Seu consumo está abaixo da média para o aparelho '{aparelho_escolhido}', o que é excelente para a eficiência energética."
    else:
        return f"🔄 **DICA**: Seu consumo está dentro da média esperada para o aparelho '{aparelho_escolhido}'. Tente manter esse equilíbrio para otimizar seus gastos e a eficiência."

class Comparar:
    def __init__(self, master):
        self.master = master
        self.master.title("Comparação de Consumo de Aparelhos")
        self.master.geometry("500x500")  # Aumentando o tamanho da janela principal
        self.master.configure(bg="#e9f7ef")

        # Carregar arquivo Excel
        file_path = r'C:\Users\Administrator\Documents\Estudos\Adipia\planilha\consumo_aparelhos.xlsx'
        self.df = pd.read_excel(file_path)
        self.aparelhos_disponiveis = self.df['Aparelho'].unique()

        self.criar_widgets()

    def criar_widgets(self):
        tk.Label(self.master, text="Selecione um aparelho:", font=("Arial", 12), bg="#e9f7ef").pack(pady=10)

        self.listbox_aparelhos = tk.Listbox(self.master, height=10, width=40)
        for aparelho in self.aparelhos_disponiveis:
            self.listbox_aparelhos.insert(tk.END, aparelho)
        self.listbox_aparelhos.pack(pady=10)

        tk.Button(self.master, text="Comparar", command=self.abrir_janela_comparar, bg="#4caf50", fg="white").pack(pady=20)

    def abrir_janela_comparar(self):
        selecionado = self.listbox_aparelhos.curselection()
        if not selecionado:
            messagebox.showerror("Erro", "Selecione um aparelho.")
            return

        self.aparelho_selecionado = self.listbox_aparelhos.get(selecionado[0])

        # Nova janela para comparar
        self.janela_comparar = Toplevel(self.master)
        self.janela_comparar.title("Inserir Dados de Consumo")
        self.janela_comparar.geometry("600x400")  # Aumentando o tamanho da janela de comparação
        self.janela_comparar.configure(bg="#e9f7ef")

        tk.Label(self.janela_comparar, text=f"Aparelho: {self.aparelho_selecionado}", font=("Arial", 12, "bold"), bg="#e9f7ef").pack(pady=10)

        tk.Label(self.janela_comparar, text="Potência do Aparelho (Watts):", font=("Arial", 12), bg="#e9f7ef").pack(pady=5)
        self.entry_potencia = tk.Entry(self.janela_comparar, width=35)  # Aumentando a largura da entrada
        self.entry_potencia.pack(pady=10)

        tk.Label(self.janela_comparar, text="Tempo de Uso Diário (horas):", font=("Arial", 12), bg="#e9f7ef").pack(pady=5)
        self.entry_tempo = tk.Entry(self.janela_comparar, width=35)  # Aumentando a largura da entrada
        self.entry_tempo.pack(pady=10)

        tk.Button(self.janela_comparar, text="Calcular", command=self.calcular_consumo, bg="#4caf50", fg="white").pack(pady=20)

    def calcular_consumo(self):
        try:
            potencia = float(self.entry_potencia.get())
            tempo = float(self.entry_tempo.get())

            # Calcular consumo mensal do usuário
            self.consumo_usuario = (potencia * tempo * 30) / 1000  # kWh/mês

            # Obter o consumo médio do aparelho selecionado
            self.consumo_medio = self.df[self.df['Aparelho'] == self.aparelho_selecionado]['Consumo Mensal (kWh)'].mean()

            tk.Label(self.janela_comparar, text=f"Consumo Calculado: {self.consumo_usuario:.2f} kWh/mês", font=("Arial", 12, "bold"), bg="#e9f7ef").pack(pady=10)
            tk.Button(self.janela_comparar, text="Ver Gráfico de Comparação", command=self.plotar_grafico_comparacao, bg="#4caf50", fg="white").pack(pady=10)
            tk.Button(self.janela_comparar, text="Análise de Eficiência", command=self.abrir_janela_analise, bg="#4caf50", fg="white").pack(pady=10)

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def abrir_janela_analise(self):
        # Nova janela para exibir a análise de eficiência
        self.janela_analise = Toplevel(self.master)
        self.janela_analise.title("Análise de Eficiência")
        self.janela_analise.geometry("600x400")  # Aumentando o tamanho da janela de análise de eficiência
        self.janela_analise.configure(bg="#e9f7ef")

        resultado = analise_eficiencia(self.aparelho_selecionado, self.consumo_usuario, self.consumo_medio)
        
        # Melhorando a aparência do texto
        tk.Label(self.janela_analise, text="Análise de Eficiência do Aparelho", font=("Arial", 14, "bold"), bg="#e9f7ef").pack(pady=10)

        tk.Label(self.janela_analise, text=resultado, font=("Arial", 12), bg="#e9f7ef", justify="left").pack(pady=15)

    def plotar_grafico_comparacao(self):
        # Nova janela para mostrar o gráfico de comparação
        self.janela_comparacao = Toplevel(self.master)
        self.janela_comparacao.title("Gráfico de Comparação")
        self.janela_comparacao.geometry("600x400")  # Aumentando o tamanho da janela do gráfico
        self.janela_comparacao.configure(bg="#e9f7ef")

        fig, ax = plt.subplots(figsize=(6, 4))

        categorias = ['Consumo Médio', 'Seu Consumo']
        valores = [self.consumo_medio, self.consumo_usuario]

        ax.bar(categorias, valores, color=['blue', 'green'])
        ax.set_title('Comparação de Consumo (kWh/mês)', fontsize=14)
        ax.set_ylabel('Consumo (kWh)', fontsize=12)
        ax.set_xlabel('Categoria', fontsize=12)

        # Adicionando valores sobre as barras
        for i, v in enumerate(valores):
            ax.text(i, v + 0.1, f'{v:.2f}', ha='center', fontweight='bold')

        # Inserir gráfico na interface gráfica
        canvas = FigureCanvasTkAgg(fig, master=self.janela_comparacao)
        canvas.get_tk_widget().pack(pady=20)
        canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = Comparar(root)
    root.mainloop()
