import tkinter as tk
from comparar import Comparar
from calculo import calculo_custos
from alertas import alertas_e_sugestoes
from educacao import informacoes_educacao
from impacto import ImpactoCicloVida

class GerenciadorEnergia:
    def __init__(self, master):
        self.master = master
        self.master.title("Adipia")
        self.master.geometry("1920x1080")
        self.master.configure(bg="#e9f7ef")

        titulo = tk.Label(master, text="Adipia", font=("Arial", 30, "bold"), bg="#e9f7ef", fg="#2e7d32")
        titulo.pack(pady=20)

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
        nova_janela = tk.Toplevel(self.master)
        nova_janela.title("Comparar Consumo")
        nova_janela.geometry("600x400")
        Comparar(nova_janela)
        
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
