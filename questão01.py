renda = float(input("digite ao lado o valor da sua renda atual: ")) #aqui sera adicionado o lavor da renda 

if renda <= 2000.00: #calcula o imposto de 2000.01 ate 3000.00
    print ("insento")

elif renda == 2000.01 or renda <= 3000.00: #calcula o imposto de 2000.01 ate 3000.00
    print ("o imposto da sua renda é de 8%.")
    imposto = (renda * 8)/100
    print (f"{imposto:.2f}")

elif renda == 3000.01 or renda <= 4500.00: #calcula o imposto de 3000.01 ate 4500.00
    print ("o imposto da sua renda é de 18%.")
    imposto2 = (renda * 18)/100
    print (f"{imposto2:.2f}")
else: #calcule o imposto ate 4500.00
    print("o imposto da sua renda é de 28%. ")
    imposto3 = (renda * 28)/100
    print (f"{imposto3:.2f}")
