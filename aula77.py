import unicodedata

#função que remove os assentos da palavra secreta, para que o input sejam comparados e validados com characteres
#com assentos correpontentes ex.: a = ã = á = à ou u = ü
def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

palavra_secreta = 'aviãozinho'.casefold()
palavra_secr_formatada = remover_acentos(palavra_secreta) #cria uma string sem acentos apenas para comparação
palavra_descobrir = list('_'*len(palavra_secreta)) #Variavel despeaço vazios que vai sendo preenchidas a cada acerto

print(f'Descubra a palavra\n{''.join(palavra_descobrir)}\n')

contador = 0
numeros = ['0','1','2','3','4','5','6','7','8','9']
letras_tentadas = []
alfabeto = "abcdefghijklmnopqrstuvwxyz"

#Enquanto tiverem str '_' o loop continuará.
while '_' in palavra_descobrir:

    tentativa_letra = remover_acentos(input('Digite uma Letra: ').strip().casefold())
    print('')

    if len(tentativa_letra.strip()) == 1 and tentativa_letra not in numeros and tentativa_letra in alfabeto:

        if tentativa_letra in letras_tentadas:
            print('Você já tentou essa letra')
            continue
        
        contador += 1

        letras_tentadas.append(tentativa_letra)

        #esse bloco irá comparar letra a letra se sua entrada correponde com alguma letra da palavra secreta
        for i, letra in enumerate(palavra_secr_formatada):
            #caso a entrada corresponda com alguma letra a variavel com '_' será preenchica com a letra correpondente
            if letra == tentativa_letra:
                palavra_descobrir[i]= palavra_secreta[i]


    elif tentativa_letra in numeros:
            print(f'{tentativa_letra} é um número. Isira apenas uma letra')
            continue

    elif len(tentativa_letra.strip())>1:
       
        if any(caractere.isdigit() for caractere in tentativa_letra.strip()):
            print(f'{tentativa_letra} contem {len(tentativa_letra)} caracteres e possui números. Isira apenas uma letra')
            continue

        elif any(caractere not in alfabeto for caractere in tentativa_letra.strip()):
            print(f'{tentativa_letra} contem {len(tentativa_letra)} caracteres e possi caracteres especiais, Isira apenas uma letra')

        else:
            print(f'"{tentativa_letra}" possui {len(tentativa_letra)} letras. Insira apenas uma unica letra')
            continue

    elif len(tentativa_letra.strip()) == 0:
        print('Digite alguma letra')
        continue    

    elif tentativa_letra not in alfabeto:
        print(f'{tentativa_letra} é um caractere especial, digite apena uma letra')
    

    print(f'{''.join(palavra_descobrir)}\n')

    print('Letras tentadas', letras_tentadas)

else:
    print(f'Parabéns você descobriu a palavra secreta \n{palavra_secreta}\n\nVocê descobriu em {contador} vezes')