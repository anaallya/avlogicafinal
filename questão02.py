# Solicita ao usuário que digite seu salário
salario = float(input("Solicite seu salário: "))
# Verificar a faixa de salário e calcular o reajuste e o novo salário correspondentes
if salario <= 400.00:
    S1 = salario + salario * 0.15
    S2 = salario * 0.15
    print (f"Reajuste ganho:{S2:.2f}")
    print ("Em percentual: 15%")
    print (f"Novo salario :{S1:.2f}")
elif salario <= 800.00:
    # Para salários entre 400.01 e 800.00, aplicar um reajuste de 12%
    S1 = salario + salario * 0.12
    S2 = salario * 0.12
    print ("Em percentual: 12%")
    print (f"Reajuste ganho:{S2:.2f}")
    print (f"Novo salario :{S1:.2f}")
elif salario <= 1200.00:
    # Para salários entre 800.01 e 1200.00, aplicar um reajuste de 10%
    S1 = salario + salario * 0.10
    S2 = salario * 0.10
    print (f"Reajuste ganho:{S2:.2f}")
    print ("Em percentual: 10%")
    print (f"Novo salário :{S1:.2f}")
elif salario >= 1200.01 and salario <= 2000.00:
    # Para salários entre 1200.01 e 2000.00, aplicar um reajuste de 7%
    S1 = salario + salario * 0.07
    S2 = salario * 0.07
    print (f"Reajuste ganho:{S2:.2f}")
    print ("Em percentual: 7%")
    print (f"Novo salario :{S1:.2f}")
elif salario >= 2000.01:
    # Para salários acima de 2000.00, aplicar um reajuste de 4%
    S1 = salario + salario * 0.04
    S2 = salario * 0.04
    print (f"Reajuste ganho:{S2:.2f}")
    print ("Em percentual: 4%")
    print (f"Novo salario :{S1:.2f}")


