import json
from datetime import datetime

# Funcao para carregar dados de um arquivo JSON
def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            dados = json.load(file)
    except FileNotFoundError:
        dados = []
    
    return dados

# Funcao para salvar dados em um arquivo JSON
def salvar_dados(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as file:
        json.dump(dados, file, indent=4)

# Funcao para escolher o status da atividade
def escolher_status():
    while True:
        print("\nEscolha o status da atividade:")
        print("1. Concluido")
        print("2. Em Andamento")
        print("3. Pendente")
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == '1':
            return "Concluido"
        elif opcao == '2':
            return "Em Andamento"
        elif opcao == '3':
            return "Pendente"
        else:
            print("Opcao invalida. Por favor, escolha uma opcao valida.")

# Funcao para criar um novo evento
def criar_evento():
    eventos = carregar_dados("eventos.json")

    while True:
        nome_evento = input("\nNome do Evento: ")
        descricao_evento = input("Descricao do Evento: ")
        complexidade_evento = input("Complexidade do Evento (Baixa/Média/Alta): ").capitalize()
        status_evento = escolher_status()

        # Captura automatica da data e hora atual
        data_evento = datetime.now().strftime("%Y-%m-%d %H:%M")
        horario_inicio = data_evento
        horario_fim = ""

        evento = {
            "Nome do Evento": nome_evento,
            "Descricao do Evento": descricao_evento,
            "Complexidade": complexidade_evento,
            "Status da Atividade": status_evento,
            "Data do Evento": data_evento,
            "Horario de Inicio": horario_inicio,
            "Horario de Fim": horario_fim
        }

        eventos.append(evento)

        mais_eventos = input("\nDeseja adicionar outro evento? (S/N): ").strip().upper()
        if mais_eventos != 'S':
            break

    salvar_dados(eventos, "eventos.json")
    print("\nEventos salvos com sucesso!")

# Funcao para criar uma nova task
def criar_task():
    tasks = carregar_dados("tasks.json")

    while True:
        nome_task = input("\nNome da Task: ")
        descricao_task = input("Descricao da Task: ")
        complexidade_task = input("Complexidade da Task (Baixa/Média/Alta): ").capitalize()
        status_task = escolher_status()

        # Captura automatica da data e hora atual
        data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M")
        horario_inicio = data_criacao
        horario_fim = ""

        task = {
            "Nome da Task": nome_task,
            "Descricao da Task": descricao_task,
            "Complexidade": complexidade_task,
            "Status da Atividade": status_task,
            "Data de Criacao": data_criacao,
            "Horario de Inicio": horario_inicio,
            "Horario de Fim": horario_fim
        }

        tasks.append(task)

        mais_tasks = input("\nDeseja adicionar outra task? (S/N): ").strip().upper()
        if mais_tasks != 'S':
            break

    salvar_dados(tasks, "tasks.json")
    print("\nTasks salvas com sucesso!")

# Funcao para criar um novo incidente
def criar_incidente():
    incidentes = carregar_dados("incidentes.json")

    while True:
        tipo_incidente = input("\nTipo de Incidente: ")
        descricao_incidente = input("Descricao do Incidente: ")
        complexidade_incidente = input("Complexidade do Incidente (Baixa/Média/Alta): ").capitalize()
        status_incidente = escolher_status()

        # Captura automatica da data e hora atual
        data_registro = datetime.now().strftime("%Y-%m-%d %H:%M")
        horario_inicio = data_registro
        horario_fim = ""

        incidente = {
            "Tipo de Incidente": tipo_incidente,
            "Descricao do Incidente": descricao_incidente,
            "Complexidade": complexidade_incidente,
            "Status da Atividade": status_incidente,
            "Data de Registro": data_registro,
            "Horario de Inicio": horario_inicio,
            "Horario de Fim": horario_fim
        }

        incidentes.append(incidente)

        mais_incidentes = input("\nDeseja adicionar outro incidente? (S/N): ").strip().upper()
        if mais_incidentes != 'S':
            break

    salvar_dados(incidentes, "incidentes.json")
    print("\nIncidentes salvos com sucesso!")

# Funcao para listar todas as tasks, eventos e incidentes não concluidos
def listar_nao_concluidos():
    tasks = carregar_dados("tasks.json")
    eventos = carregar_dados("eventos.json")
    incidentes = carregar_dados("incidentes.json")

    nao_concluidos = {
        "Tasks": [task for task in tasks if task["Status da Atividade"] != "Concluido"],
        "Eventos": [evento for evento in eventos if evento["Status da Atividade"] != "Concluido"],
        "Incidentes": [incidente for incidente in incidentes if incidente["Status da Atividade"] != "Concluido"]
    }

    if not nao_concluidos["Tasks"] and not nao_concluidos["Eventos"] and not nao_concluidos["Incidentes"]:
        return None

    return nao_concluidos

# Funcao para exibir e editar o status de um item selecionado
def visualizar_editar_item(tipo, index):
    arquivo = f"{tipo.lower()}s.json"
    dados = carregar_dados(arquivo)

    if index < 0 or index >= len(dados):
        print(f"\nindice invalido para {tipo.lower()}.")
        return

    item = dados[index]
    
    if item["Status da Atividade"] == "Concluido":
        print(f"\n{tipo} ja esta concluido e não pode ser editado.")
        return
    
    print(f"\nDetalhes do {tipo}:")
    for chave, valor in item.items():
        print(f"{chave}: {valor}")
    
    while True:
        print("\nEscolha o novo status da atividade:")
        print("1. Concluido")
        print("2. Em Andamento")
        print("3. Pendente")
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == '1':
            novo_status = "Concluido"
            item["Horario de Fim"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            break
        elif opcao == '2':
            novo_status = "Em Andamento"
            break
        elif opcao == '3':
            novo_status = "Pendente"
            break
        else:
            print("Opcao invalida. Por favor, escolha uma opcao valida.")

    item["Status da Atividade"] = novo_status
    dados[index] = item
    salvar_dados(dados, arquivo)
    print(f"\n{tipo} atualizado com sucesso.")

# Funcao para exibir o menu de itens não concluidos
def menu_nao_concluidos():
    nao_concluidos = listar_nao_concluidos()

    if nao_concluidos is None:
        print("\nNenhuma pendência encontrada.")
        return

    while True:
        print("\n### Itens Não Concluidos ###")
        print("1. Tasks")
        print("2. Eventos")
        print("3. Incidentes")
        print("4. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == '1':
            if not nao_concluidos["Tasks"]:
                print("\nNenhuma task pendente.")
            else:
                for i, task in enumerate(nao_concluidos["Tasks"]):
                    print(f"{i}. {task['Nome da Task']}")
                index = int(input("\nEscolha o indice da task para visualizar/editar: "))
                visualizar_editar_item("Task", index)
        elif opcao == '2':
            if not nao_concluidos["Eventos"]:
                print("\nNenhum evento pendente.")
            else:
                for i, evento in enumerate(nao_concluidos["Eventos"]):
                    print(f"{i}. {evento['Nome do Evento']}")
                index = int(input("\nEscolha o indice do evento para visualizar/editar: "))
                visualizar_editar_item("Evento", index)
        elif opcao == '3':
            if not nao_concluidos["Incidentes"]:
                print("\nNenhum incidente pendente.")
            else:
                for i, incidente in enumerate(nao_concluidos["Incidentes"]):
                    print(f"{i}. {incidente['Tipo de Incidente']}")
                index = int(input("\nEscolha o indice do incidente para visualizar/editar: "))
                visualizar_editar_item("Incidente", index)
        elif opcao == '4':
            break
        else:
            print("\nOpcao invalida. Por favor, escolha uma opcao valida.")

# Funcao principal para exibir o menu principal
def menu_principal():
    while True:
        print("\n### Menu Principal ###")
        print("1. Criar Novo Evento")
        print("2. Criar Nova Task")
        print("3. Criar Novo Incidente")
        print("4. Listar Itens Não Concluidos")
        print("5. Sair")
        
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == '1':
            criar_evento()
        elif opcao == '2':
            criar_task()
        elif opcao == '3':
            criar_incidente()
        elif opcao == '4':
            menu_nao_concluidos()
        elif opcao == '5':
            print("Encerrando o programa.")
            break
        else:
            print("\nOpcao invalida. Por favor, escolha uma opcao valida.")

if __name__ == "__main__":
    menu_principal()