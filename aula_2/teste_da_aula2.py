import secrets
import string
import os

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True):
    """Gera uma senha aleatória criptograficamente segura."""
    caracteres = string.ascii_lowercase
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        # Adiciona caracteres de pontuação, mas exclui espaços e aspas para evitar problemas
        # com alguns sistemas ou parsers. Pode ser ajustado conforme a necessidade.
        caracteres += '!@#$%^&*()_+-=[]{}|;:,.<>?'

    if not caracteres:
        raise ValueError("Nenhum conjunto de caracteres selecionado para gerar a senha.")

    # secrets.choice é criptograficamente seguro para seleção de caracteres
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

def salvar_senha(servico, senha, arquivo="senhas.txt"):
    """
    Salva a senha em um arquivo de texto simples.
    AVISO: Armazenar senhas em texto plano não é seguro.
    Considere usar um gerenciador de senhas seguro ou criptografia para dados sensíveis.
    """
    try:
        with open(arquivo, "a", encoding="utf-8") as f:
            f.write(f"Serviço: {servico} | Senha: {senha}\n")
        print(f"Senha para '{servico}' salva com sucesso em {arquivo}!")
    except IOError as e:
        print(f"Erro ao salvar a senha: {e}")

def menu():
    print("\n--- SISTEMA DE GERENCIAMENTO DE SENHAS SEGURO ---")
    print("1. Gerar nova senha")
    print("2. Ver senhas salvas (AVISO: Não seguro)")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        try:
            tamanho_str = input("Tamanho da senha (padrão 12): ")
            tamanho = int(tamanho_str) if tamanho_str else 12
            
            if tamanho <= 0:
                print("Erro: O tamanho da senha deve ser um número positivo.")
                return True

            servico = input("Para qual serviço é esta senha? (ex: Gmail, Instagram): ")
            if not servico.strip():
                print("Erro: O nome do serviço não pode ser vazio.")
                return True
            
            senha = gerar_senha(tamanho)
            print(f"\nSenha gerada: {senha}")
            
            salvar = input("Deseja salvar esta senha? (s/n): ").lower()
            if salvar == 's':
                salvar_senha(servico, senha)
        except ValueError as ve:
            print(f"Erro: {ve}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            
    elif opcao == '2':
        if os.path.exists("senhas.txt"):
            print("\n--- SENHAS SALVAS (AVISO: Não seguro) ---")
            try:
                with open("senhas.txt", "r", encoding="utf-8") as f:
                    conteudo = f.read()
                    if conteudo:
                        print(conteudo)
                    else:
                        print("Nenhuma senha salva ainda.")
            except IOError as e:
                print(f"Erro ao ler o arquivo de senhas: {e}")
        else:
            print("\nNenhuma senha salva ainda.")
            
    elif opcao == '3':
        print("Saindo...")
        return False
    
    else:
        print("Opção inválida! Por favor, escolha 1, 2 ou 3.")
    
    return True


if __name__ == "__main__":
    while menu():
        pass