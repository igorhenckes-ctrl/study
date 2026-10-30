while True:
     primeiro_nome = input(f'Insira seu primeiro nome: ')

     primeiro_nome_nospace = primeiro_nome.replace(" ","")
    
     if len(primeiro_nome_nospace) <=4:
         print(f'O nome {primeiro_nome} é um nome curto')

     elif 5<=len(primeiro_nome_nospace)<=6:
         print(f'O nome {primeiro_nome} é um nome médio')

     elif len(primeiro_nome_nospace)>6:
         print(f'O nome {primeiro_nome} é um nome longo')