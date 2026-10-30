# Calculadora
print('''
    
    
    Bem viando a calculadora simplificada
    
    A qualquer momento digite [sair] para encerrar o programa

    Para ver a descrição dos operadors digite [help] (WIP)
    
    ''')



help = (
'''
Lista de comandos:

  +  ...  Realiza soma entre valores. ex.: 2 + 3 = 5

  -  ...  Realiza subtração entre valores. ex.: 4 - 3 = 1

  *  ...  Realiza a multiplicação entre valores. ex.: 3 * 5 = 15

  /  ...  Realiza a divisão entre valores. ex.: 8 / 4 = 2

  ^  ...  Realiza função exponencial entre valores, sendo o segundo valor o valor do expoente.  ex.: 4 ^ 2 = 16

'''
)

while True:

    #Lista com texto 
    perguntas = [
        ('number_1','Insira o primeiro valor: '),
        ('operador','Insira o operador (+, -, *, / or ^): '),
        ('number_2','Insira o segundo valor: ')
    ]

    entradas = {}
    encerrar = False
   
    for chave, mensagem in perguntas:
        resposta = input(mensagem).strip()

        if resposta.casefold().strip() == 'sair':
            encerrar = True
            break # Sai do loop do 'for'

        elif resposta.casefold().strip() == 'help':
            print (help)
            break

        entradas[chave] = resposta

    if encerrar:
        break #Encerra o loop 'while'

    if resposta.casefold().strip() == 'help':
        continue

    print(" ")
    
    try:
         
        #Converte as variveira number para float, para tornar operações possiveis 
        number_1 = float(entradas['number_1'])
        number_2 = float(entradas['number_2'])
        operador = entradas['operador']
        
        operadores_validos = ['+','-','*','/','^']


        print(" ")
        
        if operador in operadores_validos:
        
            if operador == '+':
                resultado = number_1 + number_2

            elif operador == '-':
                resultado = number_1 - number_2
                
            elif operador == '*':
                resultado = number_1 * number_2
            
            elif operador == '/':
                resultado = number_1 / number_2
                
            elif operador == '^':
                resultado = number_1 ** number_2

            resultado_txt = f'{number_1} {operador} {number_2} = {resultado:.2f}'
            print(resultado_txt)
            print(" ")
                
    

        else:
            print('Insira um operador valido')
            print(" ")

    except:
        print('Isira Valores validos: ')
        print(" ")
