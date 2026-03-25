🔐 Projeto de Gerenciamento de Senhas - Aula 2
Este repositório contém os materiais da Aula 2, focados no desenvolvimento de sistemas de segurança e interfaces gráficas em Python. O projeto está dividido em duas partes principais: um testador de lógica via terminal e uma interface gráfica completa.
🚀 Como começar (Fluxo sugerido)
Para entender melhor o funcionamento do sistema, sugerimos seguir esta ordem de execução:
1. Teste a Lógica Primeiro (teste_da_aula2.py)
Antes de abrir a interface gráfica, execute o script de teste. Ele funciona via terminal e permite que você entenda a lógica de geração de senhas criptograficamente seguras e o armazenamento básico em arquivos.
O que ele faz: Gera senhas usando a biblioteca secrets, permite escolher o tamanho e salvar o resultado em um arquivo senhas.txt.
Como executar:
Bash
python teste_da_aula2.py
2. Explore a Interface Gráfica (aula2.py)
Após entender a lógica, execute o sistema principal. Esta é uma aplicação completa com interface visual moderna (usando tkinter e ttk).
O que ele faz:
Sistema de Cadastro e Login de usuários.
Gerador de senhas com visualização de etapas do processo.
Histórico de senhas geradas por usuário.
Interface baseada em abas (Notebook) e temas modernos (clam).
Como executar:
Bash
python aula2.py
🛠️ Tecnologias Utilizadas
Tecnologia
Descrição
Python 3.11+
Linguagem base do projeto.
Tkinter / TTK
Criação da interface gráfica (GUI) com temas.
Secrets
Geração de senhas criptograficamente seguras.
Random
Seleção aleatória de caracteres para fins didáticos.
Datetime
Registro de data e hora para o histórico.
📋 Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina. Não são necessárias bibliotecas externas complexas, pois o projeto utiliza principalmente módulos nativos do Python.
Para garantir que tudo funcione corretamente, você pode instalar as dependências listadas no arquivo requirements.txt:
Bash
pip install -r requirements.txt
⚠️ Avisos de Segurança
O armazenamento de senhas no arquivo senhas.txt é feito em texto plano (sem criptografia). Isso é apenas para fins didáticos e não deve ser usado em produção.
Em um sistema real, as senhas de login dos usuários (em aula2.py) deveriam ser armazenadas usando técnicas de hashing (como bcrypt ou argon2).