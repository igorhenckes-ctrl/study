'''Lista de compras

Lista costumizavel que pode ser criada e editada pelo usuario
'''

lista_compras = ['Feijão', 'Arroz', 'Abacate'] #lista vazia para inicio da aplicação

#Texto de comandos, pode sempre ser acessado com o comando "ajuda"
texto_comandos = '''
Selecione uma opção
[i]nserir   [a]pagar   [l]istar
'''

#Lista para conferencia de input, caso não esteja nessa lista exibira um error
comandos_aceitos = ['i', 'a', 'l', 's', 'ajuda'] 
novo_item = ''

def lista_sem_paranteses(item):
    print(str(item).replace('(','').replace(')','').replace("'",""))
    

while True:
    print(texto_comandos)
    comando_inserido = input().strip().casefold()

    if comando_inserido == 'i':
        while True:
            print(f'\nDigite um item para sua lista\nDigite [S]air para retornar')
            novo_item = input()

            if novo_item == 's':
                break
            
            lista_compras.append(novo_item)

    elif comando_inserido == 'l':
        for item in enumerate(lista_compras):
            lista_sem_paranteses(item)

    elif comando_inserido == 'a':
        while True:

            list_range = range(len(lista_compras))

            for item in enumerate(lista_compras):
                lista_sem_paranteses(item)

            print(f'\nEscolha um dos valores a ser excluido o digite [r]etronar:')
            idicie_excluido = input('').casefold().strip()

            try:
                idicie_excluido_int = int(idicie_excluido)

            except:
                idicie_excluido_int = -1
            

            if idicie_excluido_int in list_range:

                print(f'Tem certeza que deseja excluir o item {lista_compras[idicie_excluido_int]}\n[s]im ou [n]ão')

                confirmacao_apagar = input().strip().casefold()

                if confirmacao_apagar == 's':

                    lista_compras.pop(idicie_excluido_int)

                elif confirmacao_apagar == 'n':  
                    break  

                else:
                    print(f'\nInsira uma opção valida\n')
                    continue
            
            elif idicie_excluido_int not in list_range and idicie_excluido != 'r':
                print('\ninsira um valor existente na lista\n')
                continue    

            elif idicie_excluido == 'r':
                ...
            break

