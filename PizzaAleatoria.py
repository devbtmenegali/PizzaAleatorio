import matplotlib.pyplot as plt
import random 

def vendas_pizza():

    calabreza = []
    portuguesa = []
    mussarela = []

    dias_da_semana = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]

    for i in range (0,7):

        calabreza.append(random.randint(10,30))
        portuguesa.append(random.randint(10,30))
        mussarela.append(random.randint(10,30))

    return dias_da_semana, calabreza, portuguesa, mussarela

def grafico_barra(dias_da_semana, calabreza, portuguesa, mussarela):

    plt.bar(dias_da_semana, calabreza,label = "Calabresa", color = "blue", width = 0.4, align = "center")
    plt.bar(dias_da_semana, portuguesa,label = "Portuguesa", color = "red", width = 0.4, align = "edge")
    plt.bar(dias_da_semana, mussarela,label = "Mussarela", color = "orange", width = 0.4, align = "edge")

    plt.title ("Vendas Pizzas")

    plt.legend()

    plt.xlabel ("Dias da Semana")
    plt.ylabel ("Quantida")

    plt.show()

def grafico_pizza(calabreza, portuguesa, mussarela):

    soma_calabresa = sum(calabreza)
    soma_portuguesa = sum(portuguesa)
    soma_mussarela = sum(mussarela)

    soma_total_pizza = [soma_calabresa, soma_portuguesa, soma_mussarela]
    lista_sabor = ["Calabresa","Portuguesa", "Mussarela"]

    plt.pie (soma_total_pizza, labels=lista_sabor, autopct="%1.1f%%")

    plt.title("Quantidade de Pizzas Vendidas/Sabor/Semana")

    plt.show()

def grafico_linha(dias_da_semana, calabreza, portuguesa, mussarela):

    plt.plot(dias_da_semana, calabreza, label = "Calabreza", color = "blue")
    plt.plot(dias_da_semana, portuguesa, label = "Portuguesa", color = "red")
    plt.plot(dias_da_semana, mussarela, label = "Mussarela", color = "orange")

    plt.xlabel("Dias da Semana")
    plt.ylabel("Pizzas Vendidas")
    plt.title("Relatório das Vendas")

    plt.legend()

    plt.show()

def main():

    print("ESCOLHA O TIPO DO GRÁFICO")
    print("1 - Barra \n")
    print("2 - Linha \n")
    print("3 - Pizza \n")

    dias_da_semana, calabreza, portuguesa, mussarela = vendas_pizza()

    tipo_de_grafico = int(input("Escolha o tipo de gráfico:"))


    if tipo_de_grafico == 2:
        grafico_linha(dias_da_semana, calabreza, portuguesa, mussarela)

    if tipo_de_grafico == 3:
        grafico_pizza(calabreza, portuguesa, mussarela)

    if tipo_de_grafico == 1:
        grafico_barra(dias_da_semana, calabreza, portuguesa, mussarela)

if __name__=="__main__":

    main()