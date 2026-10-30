#Cria texto subilinhados a partir de variaveis 
def underline_txt(text):
    return ''.join(char + '\u0332' for char in text)



max_length = 90 #comprimento máximo de caracteres na tela

head_title = 'CONVERSOR DE CORES HEX E RGB'.center(max_length)

deco_txt_line = '_'*max_length #cria linha decorativa a partir do max_length

sub_txt_1 = 'Uma simples ferramenta para facilitar o seu dia nos processos de design'.center(max_length)


#exibe texto inicial
start_txt = f"""
{deco_txt_line}
   
{head_title}
{deco_txt_line}

    
{sub_txt_1}


{'\    /'.center(max_length)} 
{'\  /'.center(max_length)} 
{'\/'.center(max_length)} 

    """
    
print(start_txt)

exit_txt = 'R' #varivel para confirmação de saida


while exit_txt.strip().casefold() == 'r':  

    #Irá para um dos conversores RGB para HEX ou HEX pra RGB
    conversor = input ('Slecione o conversor - [R]GB para HEX ou [H]EX para RGB: ') 
       
    if conversor.strip().casefold() == 'h':

        hex_value = input('Isira o valor da cor em HEX: #').strip().upper()

        #Condicional que verifica se o valor inserido é hexadecimal usado para valores de cor
        if len(hex_value)==6 and all(c in '0123456789ACBDEF' for c in hex_value):

            red_value = int(hex_value[0:2],16)
            green_value = int(hex_value[2:4],16)
            blue_value = int(hex_value[4:6],16)

            print('o valor RGB é:')
            print(f'{red_value}, {green_value}, {blue_value}')
            

                    
        else:
            print('Insira um valor valido')


    elif conversor.strip().casefold() == 'r':

        wrong_rgb_value = '''        
Insira um valor entre 0 e 255
'''
        #Inserção do valor Vemelho do RGB
        while True:
            red_value = (input ('Insira o valor da cor Vermelha: ')).strip()
            if red_value.isdigit() and 0<=int(red_value)<=255:
                
                break

            print(wrong_rgb_value)

        #Inserção do valor Verder do RGB
        while True:
            green_value = (input ('Insira o valor da cor Verde: '))
            if green_value.isdigit() and 0<=int(green_value)<=255:
                break

            print(wrong_rgb_value)

        #Inserção do valor Azul do RGB
        while True:
            blue_value = (input ('Insira o valor da cor Azul: '))
            if blue_value.isdigit() and 0<=int(blue_value)<=255:
                print(f'O valor de equivalente em HEX é #{int(red_value):02X}{int(green_value):02X}{int(blue_value):02X}')
                break

            print(wrong_rgb_value)
                  
    else:
        print('Isira um valor valido, [R] ou [H] ')


    #Bloco para configurar repetição ou interrupção da aplicação
    while True:

        opcao = input ('Deseja [R]etornar ou [S]air da aplicação ').strip().casefold()

        if opcao == 'r':
            exit_txt = 'r'
            break

        elif opcao == 's':
            exit_txt = 's'
            break

        else:
            print('opção invalida. Digite R para retornar ou S pra sair')