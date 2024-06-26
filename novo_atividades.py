import json
import os
from datetime import datetime

# Função para criar um novo evento
def criar_evento():
    eventos = []

    while True:
        nome_evento = input("\nNome do Evento: ")
        descricao_evento = input("Descrição do Evento: ")

        # Captura automática da data e hora atual
        data_evento = datetime.now().strftime("%Y-%m-%d %H:%M")
        horario_inicio = data_evento
        horario_fim = ""

        evento = {
            "Nome do Evento": nome_evento,
            "Descrição do Evento": descricao_evento,
            "Data do Evento": data_evento,
            "Horário de Início": horario_inicio,
            "Horário de Fim": horario_fim
        }

        eventos.append(evento)

        mais_eventos = input("\nDeseja adicionar outro evento? (S/N): ").strip().upper()
        if mais_eventos != 'S':
            break

    salvar_eventos(eventos, "eventos.json")
    print("\nEventos salvos com sucesso!")

# Função para criar uma nova task
def criar_task():
    tasks = []

    while True:
        nome_task = input("\nNome da Task: ")
        descricao_task = input("Descrição da Task: ")
        complexidade_task = input("Complexidade da Task (Baixa/Média/Alta): ").capitalize()
        status_task = input("Status da Task (Concluído/Em Andamento/Pendente): ").capitalize()

        # Captura automática da data e hora atual
        data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M")
        horario_inicio = data_criacao
        horario_fim = ""

        task = {
            "Nome da Task": nome_task,
            "Descrição da Task": descricao_task,
            "Complexidade": complexidade_task,
            "Status da Atividade": status_task,
            "Data de Criação": data_criacao,
            "Horário de Início": horario_inicio,
            "Horário de Fim": horario_fim
        }

        tasks.append(task)

        mais_tasks = input("\nDeseja adicionar outra task? (S/N): ").strip().upper()
        if mais_tasks != 'S':
            break

    salvar_tasks(tasks, "tasks.json")
    print("\nTasks salvas com sucesso!")

# Função para criar um novo incidente
def criar_incidente():
    incidentes = []

    while True:
        tipo_incidente = input("\nTipo de Incidente: ")
        descricao_incidente = input("Descrição do Incidente: ")
        complexidade_incidente = input("Complexidade do Incidente (Baixa/Média/Alta): ").capitalize()
        status_incidente = input("Status do Incidente (Concluído/Em Andamento/Pendente): ").capitalize()

        # Captura automática da data e hora atual
        data_registro = datetime.now().strftime("%Y-%m-%d %H:%M")
        horario_inicio = data_registro
        horario_fim = ""

        incidente = {
            "Tipo de Incidente": tipo_incidente,
            "Descrição do Incidente": descricao_incidente,
            "Complexidade": complexidade_incidente,
            "Status da Atividade": status_incidente,
            "Data de Registro": data_registro,
            "Horário de Início": horario_inicio,
            "Horário de Fim": horario_fim
        }

        incidentes.append(incidente)

        mais_incidentes = input("\nDeseja adicionar outro incidente? (S/N): ").strip().upper()
        if mais_incidentes != 'S':
            break

    salvar_incidentes(incidentes, "incidentes.json")
    print("\nIncidentes salvos com sucesso!")

# Função para salvar eventos em um arquivo JSON
def salvar_eventos(eventos, nome_arquivo):
    with open(nome_arquivo, 'w') as file:
        json.dump(eventos, file, indent=4)

# Função para salvar tasks em um arquivo JSON
def salvar_tasks(tasks, nome_arquivo):
    with open(nome_arquivo, 'w') as file:
        json.dump(tasks, file, indent=4)

# Função para salvar incidentes em um arquivo JSON
def salvar_incidentes(incidentes, nome_arquivo):
    with open(nome_arquivo, 'w') as file:
        json.dump(incidentes, file, indent=4)

# Função principal para exibir o menu
def menu_principal():
    while True:
        print("\n### Menu Principal ###")
        print("1. Criar Eventos")
        print("2. Criar Tasks")
        print("3. Criar Incidentes")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            criar_evento()
        elif opcao == '2':
            criar_task()
        elif opcao == '3':
            criar_incidente()
        elif opcao == '4':
            print("\nEncerrando o programa.")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu_principal()
