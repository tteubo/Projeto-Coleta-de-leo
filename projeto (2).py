Horario_Norte = "Todos as segundas e quartas de manhã/tarde"
Horario_Sul = "Todos as segundas e quartas de manhã/tarde"
Horario_Oeste = "Todos as segundas e quartas de manhã/tarde"

while True:

    print("1.Norte 2.Centro-oeste 3.Sul")
    regiao = int(input("Qual bairro você mora? "))
    if regiao == 1:
        print("No norte nós temos as seguintes datas e turnos:")
        print(Horario_Norte)
        break

    elif regiao == 2:
        print("No centro oeste nós temos as seguintes datas e turnos:")
        print(Horario_Oeste)
        break


    else:
        print("Região não identificada por favor tente novamente.")




quantidade = float(input("Quantos litros de óleo serão coletados? "))

if quantidade >= 2:
    print("Parabéns sua coleta está agendada, por favor aguarde!")
elif quantidade <= 2:
    print("Poxa não podemos coletar essa quantidade no momento :(, continue acumulando óleo até atingir a quantidade mínima! (2 litros é o minimo necessário)")
    exit()


resultado = str(input("Seu óleo foi coletado? S/N "))
if resultado.lower() == "s":
    print("Obrigado por utilizar dos nossos serviços!")
elif resultado.lower() == "n":
    print("Poxa que pena :(")

