import os
import shutil

# Função para copiar arquivos
def copiar_arquivo(arquivo_origem, pasta_destino):
    if os.path.exists(arquivo_origem):
        shutil.copy(arquivo_origem, pasta_destino)
        print(f"Arquivo {arquivo_origem} copiado para {pasta_destino}.")
    else:
        print(f"Arquivo {arquivo_origem} não encontrado. Verifique o caminho.")

# Função para criar um arquivo de exemplo (caso não exista)
def criar_arquivo_exemplo(arquivo_origem):
    if not os.path.exists(arquivo_origem):
        with open(arquivo_origem, 'w') as f:
            f.write("Este é um arquivo de exemplo.\n")
        print(f"Arquivo de exemplo {arquivo_origem} criado.")
    else:
        print(f"O arquivo {arquivo_origem} já existe.")

# Exemplo de uso da função
if __name__ == "__main__":
    arquivo_origem = r'C:\git\Automação de tarefas\arquivo\Imagens\frente.png'
    pasta_destino = r'C:\git\Automação de tarefas\arquivo\Imagens'
    
    # Criar um arquivo de exemplo caso ele não exista
    criar_arquivo_exemplo(arquivo_origem)
    
    # Copiar o arquivo criado
    copiar_arquivo(arquivo_origem, pasta_destino)
