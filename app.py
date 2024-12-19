import time
import sys
from InquirerPy import inquirer

def calcular_beneficios(salario_bruto, meses_trabalhados=12):
    # Constantes para cálculos
    aliquota_fgts = 0.08  # FGTS (8%)

    # Função para calcular INSS baseado no salário de contribuição
    def calcular_inss(salario):
        if salario <= 1412.00:
            return salario * 0.075
        elif salario <= 2666.68:
            return (1412.00 * 0.075) + ((salario - 1412.00) * 0.09)
        elif salario <= 4000.03:
            return (1412.00 * 0.075) + ((2666.68 - 1412.00) * 0.09) + ((salario - 2666.68) * 0.12)
        elif salario <= 7786.02:
            return (1412.00 * 0.075) + ((2666.68 - 1412.00) * 0.09) + ((4000.03 - 2666.68) * 0.12) + ((salario - 4000.03) * 0.14)
        else:
            return (1412.00 * 0.075) + ((2666.68 - 1412.00) * 0.09) + ((4000.03 - 2666.68) * 0.12) + ((7786.02 - 4000.03) * 0.14)

    # Cálculo do 1/3 de férias
    um_terco_ferias = salario_bruto / 3

    # Cálculo do 13º salário (parcela total e cada parcela)
    decimo_terceiro_total = (salario_bruto * meses_trabalhados) / 12
    decimo_terceiro_parcela = decimo_terceiro_total / 2

    # Cálculo de FGTS mensal e do INSS mensal
    fgts_mensal = salario_bruto * aliquota_fgts
    inss_mensal = calcular_inss(salario_bruto)

    return {
        "1/3 de Férias": um_terco_ferias,
        "13º Total": decimo_terceiro_total,
        "13º Parcela": decimo_terceiro_parcela,
        "FGTS": fgts_mensal,
        "INSS": inss_mensal
    }

def mostrar_progresso(iteracao, total):
    porcentagem = (iteracao / total) * 100
    barra = '█' * int(porcentagem // 2) + '-' * (50 - int(porcentagem // 2))
    sys.stdout.write(f'\r[{barra}] {porcentagem:.2f}%')
    sys.stdout.flush()

def exibir_resultados(resultados, tipo_calculo):
    print("\n" + "="*40)
    print(f"         RESULTADO: {tipo_calculo}         ")
    print("="*40)
    if tipo_calculo == "FGTS Mensal":
        print(f"Depósito Mensal de FGTS: R$ {resultados['FGTS']:.2f}")
    elif tipo_calculo == "13º Salário Total":
        print(f"13º Salário Total: R$ {resultados['13º Total']:.2f}")
    elif tipo_calculo == "13º Salário por Parcela":
        print(f"13º Salário por Parcela: R$ {resultados['13º Parcela']:.2f}")
    elif tipo_calculo == "1/3 de Férias":
        print(f"1/3 de Férias: R$ {resultados['1/3 de Férias']:.2f}")
    print("="*40 + "\n")

def menu_principal():
    while True:
        opcao = inquirer.select(
            "Escolha uma opção:",
            choices=[
                "Calcular FGTS Mensal",
                "Calcular 13º Salário Total",
                "Calcular 13º Salário por Parcela",
                "Calcular 1/3 de Férias",
                "Sair"
            ],
            default="Calcular FGTS Mensal"
        ).execute()

        if opcao == 'Calcular FGTS Mensal':
            salario_bruto = float(input("\nInforme o seu salário bruto: R$ "))
            resultados = calcular_beneficios(salario_bruto)
            exibir_resultados(resultados, "FGTS Mensal")

        elif opcao == 'Calcular 13º Salário Total':
            salario_bruto = float(input("\nInforme o seu salário bruto: R$ "))
            meses_trabalhados = int(input("Quantos meses você trabalhou no ano? "))
            resultados = calcular_beneficios(salario_bruto, meses_trabalhados)
            exibir_resultados(resultados, "13º Salário Total")

        elif opcao == 'Calcular 13º Salário por Parcela':
            salario_bruto = float(input("\nInforme o seu salário bruto: R$ "))
            meses_trabalhados = int(input("Quantos meses você trabalhou no ano? "))
            resultados = calcular_beneficios(salario_bruto, meses_trabalhados)
            exibir_resultados(resultados, "13º Salário por Parcela")

        elif opcao == 'Calcular 1/3 de Férias':
            salario_bruto = float(input("\nInforme o seu salário bruto: R$ "))
            resultados = calcular_beneficios(salario_bruto)
            exibir_resultados(resultados, "1/3 de Férias")

        elif opcao == 'Sair':
            print("\nSaindo do programa. Até logo!")
            break

# Chamada da função principal
if __name__ == "__main__":
    menu_principal()
