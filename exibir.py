import json

def exibir_json_legivel(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            dados = json.load(file)
            # Iterar sobre cada atividade no arquivo JSON
            for atividade in dados:
                print("\n=== Atividade ===")
                print(f"Nome do DevOps: {atividade['Nome do DevOps']}")
                print(f"Número da Change: {atividade['Numero da Change']}")
                print(f"Data de Início: {atividade['Data de Inicio']}")
                print(f"Data de Fim: {atividade['Data de Fim']}")
                print(f"Status: {atividade['Status']}")
                print(f"Detalhes da Atividade: {atividade['Detalhes da Atividade']}")
                print(f"Complexidade: {atividade['Complexidade']}")
                
                if 'Tasks' in atividade:
                    print("\nTasks:")
                    for task in atividade['Tasks']:
                        if 'Nome da Task' in task:
                            print(f"  - Nome da Task: {task['Nome da Task']}")
                        if 'Status da Task' in task:
                            print(f"    Status da Task: {task['Status da Task']}")
                        if 'Etapas' in task:
                            print("    Etapas:")
                            for etapa in task['Etapas']:
                                print(f"      - Hora do Início: {etapa['Hora do Inicio']}")
                                print(f"        Descrição: {etapa['Descricao']}")
                
                if 'Solucao' in atividade:
                    print(f"\nSolução: {atividade['Solucao']}")
                    
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo JSON '{nome_arquivo}'. Verifique o formato.")

def main():
    nome_arquivo = input("Digite o nome do arquivo JSON que deseja exibir: ")
    exibir_json_legivel(nome_arquivo)

if __name__ == "__main__":
    main()
