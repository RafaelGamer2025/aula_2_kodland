<div align="center">

# 🔐 Sistema de Gerenciamento de Senhas

**Um projeto educacional focado em segurança, geração de senhas criptograficamente seguras e interfaces gráficas em Python.**

[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange.svg?style=for-the-badge)](https://docs.python.org/3/library/tkinter.html)
[![Status](https://img.shields.io/badge/Status-Concluído-success.svg?style=for-the-badge)]()

---

</div>

## 📖 Sobre o Projeto

Este repositório contém os materiais desenvolvidos durante a **Aula 2**. O objetivo principal é demonstrar a criação de um sistema robusto para geração e gerenciamento de senhas, abordando desde a lógica fundamental via terminal até a implementação de uma interface gráfica (GUI) completa e amigável.

O projeto está dividido em duas frentes de aprendizado:
1.  **Lógica e Segurança (`teste_da_aula2.py`):** Foco na utilização da biblioteca `secrets` para gerar senhas que resistem a ataques de força bruta, além de demonstrar operações básicas de I/O (leitura e escrita de arquivos).
2.  **Interface e Experiência do Usuário (`aula2.py`):** Construção de um sistema de login, cadastro e um painel de usuário utilizando `tkinter` e `ttk`, proporcionando uma experiência visual moderna.

---

## 🚀 Como Começar (Fluxo de Aprendizado)

Para extrair o máximo deste projeto, recomendamos seguir a ordem abaixo:

### 1️⃣ Entenda a Lógica (Modo Terminal)

Antes de mergulhar na interface gráfica, execute o script de teste. Ele opera diretamente no terminal e permite que você compreenda como as senhas são geradas de forma segura e como são salvas localmente.

```bash
# Execute o testador via terminal
python teste_da_aula2.py
```

**O que você aprenderá aqui:**
*   Geração de senhas usando a biblioteca `secrets` (criptograficamente segura).
*   Manipulação de strings e seleção de caracteres.
*   Escrita e leitura de dados em um arquivo de texto (`senhas.txt`).

### 2️⃣ Explore a Interface Gráfica (Modo GUI)

Após dominar a lógica base, inicie a aplicação principal. Esta versão oferece uma experiência completa com janelas, botões e abas.

```bash
# Inicie a aplicação com interface gráfica
python aula2.py
```

**Recursos da Interface:**
*   **Sistema de Autenticação:** Telas de Login e Cadastro de usuários.
*   **Painel do Usuário:** Área restrita após o login.
*   **Gerador Interativo:** Visualização das etapas de geração da senha e controle de comprimento.
*   **Histórico:** Tabela (`Treeview`) mostrando as senhas geradas anteriormente na sessão.

---

## 🛠️ Tecnologias e Bibliotecas

Este projeto foi construído utilizando exclusivamente bibliotecas nativas do Python, garantindo facilidade de execução sem a necessidade de instalações complexas.

| Tecnologia | Descrição |
| :--- | :--- |
| **Python 3.11+** | A linguagem de programação base de todo o projeto. |
| **Tkinter / TTK** | Bibliotecas padrão para criação da Interface Gráfica do Usuário (GUI). |
| **Secrets** | Módulo utilizado para gerar números pseudoaleatórios criptograficamente fortes. |
| **Random** | Utilizado em partes específicas para fins didáticos de seleção aleatória. |
| **Datetime** | Responsável por registrar a data e hora exatas no histórico de senhas. |

---

## ⚙️ Instalação e Configuração

Como o projeto utiliza apenas bibliotecas nativas, a configuração é extremamente simples:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2.  **Verifique sua versão do Python:**
    Certifique-se de ter o Python 3.11 ou superior instalado.
    ```bash
    python --version
    ```

3.  **Execute os scripts:**
    Siga as instruções da seção "Como Começar" acima.

*(Opcional) Um arquivo `requirements.txt` está incluído apenas para fins de documentação, confirmando que não há dependências externas.*

---

## ⚠️ Avisos Importantes de Segurança

Este é um projeto **educacional**. Por favor, atente-se aos seguintes pontos antes de considerar qualquer uso em produção:

*   **Armazenamento em Texto Plano:** O script `teste_da_aula2.py` salva as senhas em um arquivo `.txt` sem qualquer tipo de criptografia. **Nunca faça isso com senhas reais ou dados sensíveis.**
*   **Senhas de Login:** No `aula2.py`, as senhas dos usuários são mantidas em memória (dicionário) em texto plano. Em um sistema real, você **deve** utilizar algoritmos de *hashing* (como `bcrypt`, `argon2` ou `PBKDF2`) para armazenar senhas de forma segura.

---

<div align="center">
  <i>Desenvolvido com dedicação para a Aula 2.</i>
</div>
