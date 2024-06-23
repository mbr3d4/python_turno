import json
import os
from datetime import datetime

# Função para adicionar uma nova atividade
def adicionar_atividade():
    nome_devops = input("Nome do DevOps: ")
    numero_change = input("Numero da Change: ")
    
    # Captura automática da data e hora atual para Data de Início e Data de Fim
    data_inicio = datetime.now().strftime("%Y-%m-%d %H:%M")
    data_fim = ""  # Inicialmente vazio
    
    detalhes_atividade = input("Detalhes da Atividade: ")
    
    complexidade = input("Complexidade (Baixa/Media/Alta): ")
    
    # Estrutura inicial da atividade
    atividade = {
        "Nome do DevOps": nome_devops,
        "Numero da Change": numero_change,
        "Data de Inicio": data_inicio,
        "Data de Fim": data_fim,
        "Status": "Em Andamento",  # Por padrão, a atividade começa como "Em Andamento"
        "Detalhes da Atividade": detalhes_atividade,
        "Complexidade": complexidade,
        "Tasks": []
    }
    
    # Menu para adicionar mais tasks à atividade
    while True:
        opcao = input("\nDeseja adicionar uma nova task? (S/N): ").upper()
        if opcao == 'S':
            task = {}
            task["Numero da Task"] = input("Numero da Task: ")
            task["Etapas"] = []
            
            # Menu para adicionar etapas à task
            while True:
                descricao_etapa = input("Descrição da Etapa da Task (ou deixe em branco para encerrar a task): ")
                if not descricao_etapa:
                    break
                hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M")
                etapa = {
                    "Hora do Inicio": hora_atual,
                    "Descricao": descricao_etapa
                }
                task["Etapas"].append(etapa)
            
            atividade["Tasks"].append(task)
        elif opcao == 'N':
            status = input("Status da atividade (Concluído/Em Andamento/Pendente): ")
            solucao = input("Solução da atividade: ")
            atividade["Status"] = status
            atividade["Solucao"] = solucao
            # Adicionar data de fim apenas se a solução estiver definida como "Concluída"
            if status.lower() == 'concluido':
                data_fim = datetime.now().strftime("%Y-%m-%d %H:%M")
                atividade["Data de Fim"] = data_fim
            break
        else:
            print("Opção inválida. Por favor, escolha S para Sim ou N para Não.")
    
    # Salvar a atividade no arquivo JSON correspondente ao nome do DevOps
    arquivo_json = f"{nome_devops}.json"
    if os.path.exists(arquivo_json):
        with open(arquivo_json, 'r') as file:
            dados = json.load(file)
            dados.append(atividade)
        with open(arquivo_json, 'w') as file:
            json.dump(dados, file, indent=4)
    else:
        with open(arquivo_json, 'w') as file:
            json.dump([atividade], file, indent=4)
    
    print(f"Atividade adicionada com sucesso no arquivo '{arquivo_json}'.")

# Função principal para executar o programa
def main():
    while True:
        print("\n### Menu Principal ###")
        print("1. Adicionar nova atividade")
        print("2. Sair do programa")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_atividade()
        elif opcao == '2':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
