import tkinter as tk
from tkinter import ttk, messagebox
import random
from datetime import datetime

class SistemaLoginGUI:
    """Sistema de login e gerador de senhas com interface gráfica usando tkinter e ttk"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Sistema de Login e Gerador de Senhas")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # Configurar estilo ttk
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Dados em memória
        self.usuarios = {}
        self.usuario_logado = None
        self.caracteres_senha = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        self.etapas_completas = {
            "caracteres": False,
            "comprimento": False,
            "variavel_senha": False,
            "loop_random": False,
            "exibir_resultado": False
        }
        self.historico_senhas = []
        
        # Criar frames principais
        self.criar_interface_login()
    
    def limpar_janela(self):
        """Remove todos os widgets da janela"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def criar_interface_login(self):
        """Cria a interface de login/cadastro"""
        self.limpar_janela()
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = ttk.Label(main_frame, text="🔐 SISTEMA DE LOGIN", font=("Arial", 16, "bold"))
        titulo.pack(pady=20)
        
        # Notebook para abas
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Aba de Login
        frame_login = ttk.Frame(notebook, padding="15")
        notebook.add(frame_login, text="Login")
        
        ttk.Label(frame_login, text="Nome de Usuário:", font=("Arial", 10)).pack(anchor=tk.W, pady=5)
        self.entry_login_user = ttk.Entry(frame_login, width=40)
        self.entry_login_user.pack(anchor=tk.W, pady=5)
        
        ttk.Label(frame_login, text="Senha:", font=("Arial", 10)).pack(anchor=tk.W, pady=5)
        self.entry_login_senha = ttk.Entry(frame_login, width=40, show="*")
        self.entry_login_senha.pack(anchor=tk.W, pady=5)
        
        btn_login = ttk.Button(frame_login, text="Entrar", command=self.fazer_login)
        btn_login.pack(pady=20, fill=tk.X)
        
        # Aba de Cadastro
        frame_cadastro = ttk.Frame(notebook, padding="15")
        notebook.add(frame_cadastro, text="Cadastro")
        
        ttk.Label(frame_cadastro, text="Nome de Usuário:", font=("Arial", 10)).pack(anchor=tk.W, pady=5)
        self.entry_cadastro_user = ttk.Entry(frame_cadastro, width=40)
        self.entry_cadastro_user.pack(anchor=tk.W, pady=5)
        
        ttk.Label(frame_cadastro, text="Senha:", font=("Arial", 10)).pack(anchor=tk.W, pady=5)
        self.entry_cadastro_senha = ttk.Entry(frame_cadastro, width=40, show="*")
        self.entry_cadastro_senha.pack(anchor=tk.W, pady=5)
        
        ttk.Label(frame_cadastro, text="Confirmar Senha:", font=("Arial", 10)).pack(anchor=tk.W, pady=5)
        self.entry_cadastro_confirm = ttk.Entry(frame_cadastro, width=40, show="*")
        self.entry_cadastro_confirm.pack(anchor=tk.W, pady=5)
        
        btn_cadastro = ttk.Button(frame_cadastro, text="Cadastrar", command=self.cadastrar_usuario)
        btn_cadastro.pack(pady=20, fill=tk.X)
    
    def fazer_login(self):
        """Realiza o login do usuário"""
        username = self.entry_login_user.get().strip()
        senha = self.entry_login_senha.get()
        
        if not username or not senha:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        
        if username not in self.usuarios:
            messagebox.showerror("Erro", "Usuário não encontrado!")
            return
        
        if self.usuarios[username]["senha"] != senha:
            messagebox.showerror("Erro", "Senha incorreta!")
            return
        
        self.usuario_logado = username
        self.historico_senhas = self.usuarios[username]["historico"]
        self.etapas_completas = {
            "caracteres": False,
            "comprimento": False,
            "variavel_senha": False,
            "loop_random": False,
            "exibir_resultado": False
        }
        messagebox.showinfo("Sucesso", f"Bem-vindo, {username}!")
        self.criar_interface_usuario()
    
    def cadastrar_usuario(self):
        """Cadastra um novo usuário"""
        username = self.entry_cadastro_user.get().strip()
        senha = self.entry_cadastro_senha.get()
        confirm = self.entry_cadastro_confirm.get()
        
        if not username or not senha or not confirm:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        
        if senha != confirm:
            messagebox.showerror("Erro", "As senhas não conferem!")
            return
        
        if username in self.usuarios:
            messagebox.showerror("Erro", "Usuário já existe!")
            return
        
        self.usuarios[username] = {
            "senha": senha,
            "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "historico": []
        }
        
        messagebox.showinfo("Sucesso", f"Usuário '{username}' cadastrado com sucesso!")
        self.entry_cadastro_user.delete(0, tk.END)
        self.entry_cadastro_senha.delete(0, tk.END)
        self.entry_cadastro_confirm.delete(0, tk.END)
    
    def criar_interface_usuario(self):
        """Cria a interface do usuário logado"""
        self.limpar_janela()
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Cabeçalho
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=10)
        
        titulo = ttk.Label(header_frame, text=f"👤 Bem-vindo, {self.usuario_logado}!", 
                          font=("Arial", 14, "bold"))
        titulo.pack(side=tk.LEFT)
        
        btn_logout = ttk.Button(header_frame, text="Logout", command=self.fazer_logout)
        btn_logout.pack(side=tk.RIGHT)
        
        # Notebook para abas
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Aba de Gerador
        frame_gerador = ttk.Frame(notebook, padding="15")
        notebook.add(frame_gerador, text="Gerar Senha")
        self.criar_interface_gerador(frame_gerador)
        
        # Aba de Histórico
        frame_historico = ttk.Frame(notebook, padding="15")
        notebook.add(frame_historico, text="Histórico")
        self.criar_interface_historico(frame_historico)
    
    def criar_interface_gerador(self, parent):
        """Cria a interface do gerador de senhas"""
        
        # Seção de Etapas
        etapas_frame = ttk.LabelFrame(parent, text="📋 Etapas do Gerador de Senhas", padding="10")
        etapas_frame.pack(fill=tk.X, pady=10)
        
        self.etapas_vars = {}
        etapas = [
            ("Variável com caracteres", "caracteres"),
            ("Solicitar comprimento da senha", "comprimento"),
            ("Variável para armazenar senha", "variavel_senha"),
            ("Loop com random para selecionar caracteres", "loop_random"),
            ("Exibir senha resultante", "exibir_resultado")
        ]
        
        for descricao, chave in etapas:
            var = tk.BooleanVar(value=False)
            self.etapas_vars[chave] = var
            check = ttk.Checkbutton(etapas_frame, text=descricao, variable=var, state="disabled")
            check.pack(anchor=tk.W, pady=5)
        
        # Seção de Entrada
        entrada_frame = ttk.LabelFrame(parent, text="🔑 Configurações de Geração", padding="10")
        entrada_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(entrada_frame, text="Comprimento da Senha (mínimo 4):", font=("Arial", 10)).pack(anchor=tk.W, pady=5)
        self.spinbox_comprimento = ttk.Spinbox(entrada_frame, from_=4, to=100, width=10)
        self.spinbox_comprimento.set(12)
        self.spinbox_comprimento.pack(anchor=tk.W, pady=5)
        
        btn_gerar = ttk.Button(entrada_frame, text="Gerar Senha", command=self.gerar_senha)
        btn_gerar.pack(pady=10, fill=tk.X)
        
        # Seção de Resultado
        resultado_frame = ttk.LabelFrame(parent, text="🎉 Senha Gerada", padding="10")
        resultado_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.text_resultado = tk.Text(resultado_frame, height=15, width=50, wrap=tk.WORD)
        self.text_resultado.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(resultado_frame, orient=tk.VERTICAL, command=self.text_resultado.yview)
        self.text_resultado.config(yscrollcommand=scrollbar.set)
        
        # Botão para copiar
        btn_copiar = ttk.Button(parent, text="Copiar Senha para Área de Transferência", 
                               command=self.copiar_senha)
        btn_copiar.pack(pady=10, fill=tk.X)
    
    def criar_interface_historico(self, parent):
        """Cria a interface do histórico de senhas"""
        
        # Frame para a tabela
        tree_frame = ttk.Frame(parent)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        # Criar Treeview
        columns = ("Data", "Comprimento", "Senha")
        self.tree_historico = ttk.Treeview(tree_frame, columns=columns, height=15)
        self.tree_historico.column("#0", width=0, stretch=tk.NO)
        self.tree_historico.column("Data", anchor=tk.W, width=150)
        self.tree_historico.column("Comprimento", anchor=tk.CENTER, width=100)
        self.tree_historico.column("Senha", anchor=tk.W, width=200)
        
        self.tree_historico.heading("#0", text="", anchor=tk.W)
        self.tree_historico.heading("Data", text="Data", anchor=tk.W)
        self.tree_historico.heading("Comprimento", text="Comprimento", anchor=tk.CENTER)
        self.tree_historico.heading("Senha", text="Senha", anchor=tk.W)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree_historico.yview)
        self.tree_historico.configure(yscroll=scrollbar.set)
        
        self.tree_historico.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Atualizar histórico
        self.atualizar_historico()
        
        # Botão para limpar histórico
        btn_limpar = ttk.Button(parent, text="Limpar Histórico", command=self.limpar_historico)
        btn_limpar.pack(pady=10, fill=tk.X)
    
    def gerar_senha(self):
        """Gera uma nova senha seguindo as etapas"""
        try:
            comprimento = int(self.spinbox_comprimento.get())
            if comprimento < 4:
                messagebox.showerror("Erro", "O comprimento deve ser no mínimo 4!")
                return
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido!")
            return
        
        # Resetar etapas
        for chave in self.etapas_completas:
            self.etapas_completas[chave] = False
        
        # Limpar texto anterior
        self.text_resultado.delete(1.0, tk.END)
        
        # Etapa 1: Variável com caracteres
        self.text_resultado.insert(tk.END, "✓ Etapa 1: Variável com caracteres disponíveis\n")
        self.text_resultado.insert(tk.END, f"Caracteres: {self.caracteres_senha}\n\n")
        self.etapas_completas["caracteres"] = True
        self.etapas_vars["caracteres"].set(True)
        self.root.update()
        
        # Etapa 2: Solicitar comprimento
        self.text_resultado.insert(tk.END, "✓ Etapa 2: Solicitar comprimento da senha\n")
        self.text_resultado.insert(tk.END, f"Comprimento solicitado: {comprimento} caracteres\n\n")
        self.etapas_completas["comprimento"] = True
        self.etapas_vars["comprimento"].set(True)
        self.root.update()
        
        # Etapa 3: Variável para armazenar senha
        self.text_resultado.insert(tk.END, "✓ Etapa 3: Variável para armazenar a senha gerada\n")
        self.text_resultado.insert(tk.END, "Variável 'senha_gerada' criada e inicializada como vazia\n\n")
        self.etapas_completas["variavel_senha"] = True
        self.etapas_vars["variavel_senha"].set(True)
        self.root.update()
        
        # Etapa 4: Loop com random
        self.text_resultado.insert(tk.END, f"✓ Etapa 4: Loop com random para selecionar {comprimento} caracteres\n")
        self.text_resultado.insert(tk.END, "Gerando senha...\n")
        
        senha_gerada = ""
        for i in range(comprimento):
            caractere_aleatorio = random.choice(self.caracteres_senha)
            senha_gerada += caractere_aleatorio
            self.text_resultado.insert(tk.END, f"  [{i+1}/{comprimento}] Caractere adicionado: {caractere_aleatorio}\n")
            self.root.update()
        
        self.etapas_completas["loop_random"] = True
        self.etapas_vars["loop_random"].set(True)
        
        # Etapa 5: Exibir resultado
        self.text_resultado.insert(tk.END, "\n✓ Etapa 5: Exibir a senha resultante\n")
        self.text_resultado.insert(tk.END, "="*50 + "\n")
        self.text_resultado.insert(tk.END, "🎉 SENHA GERADA COM SUCESSO!\n")
        self.text_resultado.insert(tk.END, f"Comprimento: {comprimento} caracteres\n")
        self.text_resultado.insert(tk.END, f"Senha: {senha_gerada}\n")
        self.text_resultado.insert(tk.END, "="*50 + "\n\n")
        
        self.etapas_completas["exibir_resultado"] = True
        self.etapas_vars["exibir_resultado"].set(True)
        
        # Exibir checklist completo
        self.text_resultado.insert(tk.END, "📋 CHECKLIST DE ETAPAS COMPLETO:\n")
        self.text_resultado.insert(tk.END, "="*50 + "\n")
        for descricao, chave in [
            ("Variável com caracteres", "caracteres"),
            ("Solicitar comprimento da senha", "comprimento"),
            ("Variável para armazenar senha", "variavel_senha"),
            ("Loop com random para selecionar caracteres", "loop_random"),
            ("Exibir senha resultante", "exibir_resultado")
        ]:
            status = "☑️ " if self.etapas_completas[chave] else "☐ "
            self.text_resultado.insert(tk.END, f"{status}{descricao}\n")
        
        self.text_resultado.insert(tk.END, "="*50 + "\n")
        
        # Salvar no histórico
        self.historico_senhas.append({
            "senha": senha_gerada,
            "comprimento": comprimento,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })
        
        # Atualizar histórico na aba
        self.atualizar_historico()
        
        # Armazenar no dicionário de usuários
        self.usuarios[self.usuario_logado]["historico"] = self.historico_senhas
        
        self.text_resultado.see(tk.END)
    
    def atualizar_historico(self):
        """Atualiza a tabela de histórico"""
        # Limpar items antigos
        for item in self.tree_historico.get_children():
            self.tree_historico.delete(item)
        
        # Adicionar novos items
        for item in reversed(self.historico_senhas):
            self.tree_historico.insert("", 0, values=(
                item["data"],
                item["comprimento"],
                item["senha"]
            ))
    
    def limpar_historico(self):
        """Limpa o histórico de senhas"""
        if messagebox.askyesno("Confirmação", "Tem certeza que deseja limpar o histórico?"):
            self.historico_senhas.clear()
            self.usuarios[self.usuario_logado]["historico"] = []
            self.atualizar_historico()
            messagebox.showinfo("Sucesso", "Histórico limpo!")
    
    def copiar_senha(self):
        """Copia a última senha gerada para a área de transferência"""
        if not self.historico_senhas:
            messagebox.showwarning("Aviso", "Nenhuma senha gerada ainda!")
            return
        
        ultima_senha = self.historico_senhas[-1]["senha"]
        self.root.clipboard_clear()
        self.root.clipboard_append(ultima_senha)
        messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência!")
    
    def fazer_logout(self):
        """Faz logout do usuário"""
        if messagebox.askyesno("Confirmação", "Deseja fazer logout?"):
            self.usuario_logado = None
            self.historico_senhas = []
            self.criar_interface_login()


def main():
    root = tk.Tk()
    app = SistemaLoginGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()