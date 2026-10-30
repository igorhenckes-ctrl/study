while True:
    number = input(f'Insira um valor inteiro: ')

    if number.isdigit() == False:
            print(f'{number} não é um valor valido, insira um número inteiro')

    

    elif number.isdigit() == True:

        int_num = int(number)

        if int_num % 2 == 0 or int_num == 0:
            print (f'O número, {int_num}, é par')

        elif int_num % 2 != 0:
            print (f'O número, {int_num}, é impar')