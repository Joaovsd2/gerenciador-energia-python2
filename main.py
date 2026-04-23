import tkinter as tk
from comparar import Comparar  # Importando a classe Comparar
from calculo import calculo_custos  # Função ou classe de cálculo de custos
from alertas import alertas_e_sugestoes  # Função ou classe de alertas
from educacao import informacoes_educacao  # Função ou classe de educação
from impacto import ImpactoCicloVida  # Função ou classe de análise de impacto

class GerenciadorEnergia:
    def __init__(self, master):
        self.master = master
        self.master.title("Adipia")  # Título da janela agora é "Adipia"
        self.master.geometry("1920x1080")
        self.master.configure(bg="#e9f7ef")

        # Subtítulo modificado para "🌱 Gerenciador de Energia 🌱"
        titulo = tk.Label(master, text="Adipia", font=("Arial", 30, "bold"), bg="#e9f7ef", fg="#2e7d32")
        titulo.pack(pady=20)

        # Agora, "🌱 Gerenciador de Energia 🌱" será o subtítulo e estará logo abaixo do título
        subtitulo = tk.Label(master, text="🌱 Gerenciador de Energia 🌱", font=("Arial", 20, "bold"), bg="#e9f7ef", fg="#388e3c")
        subtitulo.pack(pady=10)

        botoes = [
            ("1 - Comparar Consumo", self.abrir_comparar),
            ("2 - Informações e Educação", self.abrir_educacao),
            ("3 - Cálculo de Custos", self.abrir_calculo),
            ("4 - Alertas e Sugestões", self.abrir_alertas),
            ("5 - Análise do Ciclo de Vida", self.abrir_impacto),
            ("Sair", master.quit)
        ]

        for texto, comando in botoes:
            botao = tk.Button(master, text=texto, font=("Arial", 14), bg="#a5d6a7", fg="#1b5e20", activebackground="#81c784", activeforeground="white", command=comando)
            botao.pack(fill="x", padx=50, pady=5)

        rodape = tk.Label(master, text="Contribuindo para um futuro sustentável 🌎", font=("Arial", 10, "italic"), bg="#e9f7ef", fg="#388e3c")
        rodape.pack(side="bottom", pady=10)

    def abrir_comparar(self):
        nova_janela = tk.Toplevel(self.master)  # Cria a nova janela
        nova_janela.title("Comparar Consumo")  # Define o título da nova janela
        nova_janela.geometry("600x400")  # Define o tamanho da nova janela
        Comparar(nova_janela)  # Passa a nova janela para a classe Comparar
        
    def abrir_calculo(self):
        calculo_custos(self.master)

    def abrir_alertas(self):
        alertas_e_sugestoes(self.master)

    def abrir_educacao(self):
        informacoes_educacao(self.master)

    def abrir_impacto(self):
        ImpactoCicloVida(self.master)

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorEnergia(root)
    root.mainloop()
