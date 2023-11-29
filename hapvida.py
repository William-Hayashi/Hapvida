# Define a lista de profissionais de saúde
profissionais_saude = []

# Define a lista de consultas agendadas
consultas_agendadas = []

# Inicializa o sistema
def inicializar_sistema():
    print("Sistema de Agendamento de Consultas Médicas")
    print("-" * 40)
    print("1. Cadastrar Profissional de Saúde")
    print("2. Agendar Consulta")
    print("3. Listar Consultas Agendadas")
    print("4. Sair")
    print("-" * 40)

    # Exibe o menu e lê a opção escolhida pelo usuário
    opcao = int(input("Digite a opção desejada: "))

    return opcao

def cadastrar_profissional_saude():
    profissional = {}

    profissional["cpf"] = input("Digite o CPF do profissional de saúde: ")
    profissional["nome"] = input("Digite o nome do profissional de saúde: ")
    profissional["idade"] = int(input("Digite a idade do profissional de saúde: "))
    profissional["tipo_atendimento"] = input("Digite o tipo de atendimento: ")
    profissional["Registro"] = input("Digite o registro do profissional de saúde: ")

    return profissional


def agendar_consulta():
    consulta = {}

    consulta["nome_paciente"] = input("Digite o nome do paciente: ")
    consulta["rg_paciente"] = input("Digite o RG do paciente: ")
    consulta["cpf_paciente"] = input("Digite o CPF do paciente: ")
    consulta["endereco_paciente"] = input("Digite o endereço do paciente: ")
    consulta["data_consulta"] = input("Digite a data da consulta (dd/mm/aaaa): ")
    consulta["hora_consulta"] = input("Digite a hora da consulta (hh:mm): ")

    return consulta

def listar_consultas_agendadas():
    if len(consultas_agendadas) == 0:
        print("Não há consultas agendadas.")
    else:
        print("Consultas Agendadas:")
        for consulta in consultas_agendadas:
            print("-" * 40)
            print("Nome do Paciente: ", consulta["nome_paciente"])
            print("RG do Paciente: ", consulta["rg_paciente"])
            print("CPF do Paciente: ", consulta["cpf_paciente"])
            print("Endereço do Paciente: ", consulta["endereco_paciente"])
            print("Registro do Profissional de Saúde: ", consulta["profissional_saude"])
            print("Data da Consulta: ", consulta["data_consulta"])
            print("Hora da Consulta: ", consulta["hora_consulta"])

# Executa o sistema de agendamento de consultas médicas
def main():
    while True:
        opcao = inicializar_sistema()

        if opcao == 1:
            profissional = cadastrar_profissional_saude()
            if profissional:
                print("Profissional de saúde cadastrado com sucesso.")
                profissionais_saude.append(profissional)
        elif opcao == 2:
            consulta = agendar_consulta()
            if consulta:
                print("Consulta agendada com sucesso.")
                consultas_agendadas.append(consulta)
        elif opcao == 3:
            listar_consultas_agendadas()
        elif opcao == 4:
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()