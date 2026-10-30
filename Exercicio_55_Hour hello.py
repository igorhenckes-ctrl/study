while True:
    print(""""
    Insira o horário atual no formato de 24h,
    Digite apenas os dois digitos da horas, ignorando os minutos.

    Ex: Se são 22:45 digite apenas 22
        Se são 09:30 ditite apensa 9 ou 09
    """)
    
    str_hora = (input ())


    if str_hora.isdigit() and int(str_hora)<=24:
        

        hora = int(str_hora)

        manha = (5<=hora<=12)
        tarde = (12<hora<=17)
        noite = (17<hora<=24) or (0<=hora<5)
    
        if manha:
            print(f'Bom dia')
        
        elif tarde:
            print(f'Boa tarde')
        
        elif noite:
            print(f'Boa noite')

    else:
        print(f' não é um horario valido')