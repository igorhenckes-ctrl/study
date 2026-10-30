# Calculadora

while True:

    print('''
    
    
    Bem viando a calculadora simplificada
    
    A qualquer momento digite [sair] para encerrar o programa

    Para ver a descrição dos operadors digite [help] (WIP)
    
    ''')

    number_1 = input ('Insira o primeiro valor: ').strip()
    if number_1.casefold().strip() == 'sair':
        break

    operador = input ('Insira o operador (+, -, *, / or ^): ').strip()
    if operador.casefold().strip() == 'sair':
        break
    number_2 = input ('Insira o segundo valor: ').strip()
    if number_2.casefold().strip() == 'sair':
        break


    try:
        verificador_number = isinstance (float(number_1), float) and isinstance (float(number_2), float)

        if  verificador_number:

            #Converte as variveira number para float, para tornar operações possiveis 
            number_1 = float(number_1)
            number_2 = float(number_2)



           
            if operador == '+':
                resultado = number_1 + number_2
                print(f'{resultado:.2f}')

            elif operador == '-':
                resultado = number_1 - number_2
                print(f'{resultado:.2f}')

            elif operador == '*':
                resultado = number_1 * number_2
                print(f'{resultado:.2f}')

            elif operador == '/':
                resultado = number_1 / number_2
                print(f'{resultado:.2f}')

            elif operador == '^':
                resultado = number_1 ** number_2
                print(f'{resultado:.2f}')

            else:
                print('Insira um operador valido')

    except:
        print('Isira Valores validos: ')
