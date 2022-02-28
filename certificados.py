def certificado(cert):
    # Importar biblioteca que utilizarei:
    from datetime import date, datetime
    # Importar funcao de outro arquivo *.py:
    from functions import localizar_pelo_nus_ncert, evitar_erro_3
    # Saudação inicial:
    print("\nOlá, bem vindo à sessão de Certificados dos utentes.\n"
          "Aqui podes verificar se um utente possui certificado valido "
          "ou visualizar informaçoes sobre os utentes.\n")
    decisao_0 = input("Se desejas Verificar se o Certificado de um utente está válido, carregue -> 1.\n"
                      "Para verificar dados de um Utente, carregue -> 2.\n"
                      "Para finalizar, carregue -> 9: ")
    # Funcao para evitar que o utilizador carregue em algo não solicitado:
    decisao = evitar_erro_3(decisao_0, "Verificar validade do Certificado",
                            "Verificar dados de um utente")

    if decisao == "1":
        numero = input("Digite o N. do Certificado ou o NUS: ")
        # Funcao para localizar utente pelo NUS ou N. certificado:
        certif = localizar_pelo_nus_ncert(cert, numero)
        if certif[7] != "":
            # Colocar em formato 'data' para contar os dias:
            dia_vacin = datetime.strptime(certif[7], '%d/%m/%Y').date()
            # Usar o dia atualizado em que o usuario irá utilizar
            # o programa e contar quantos dias se
            # passaram desde a vacinacao:
            qtos_dias_vacin = int(abs((date.today() - dia_vacin).days))
        else:
            qtos_dias_vacin = 0

        if certif[4] != "":
            # Colocar em formato 'data' para contar os dias:
            dia_teste = datetime.strptime(certif[4], '%d/%m/%Y').date()
            # Usar o dia atualizado em que o usuario irá utilizar
            # o programa e contar quantos dias se
            # passaram desde o teste:
            qtos_dias_teste = int(abs((date.today() - dia_teste).days))
        else:
            qtos_dias_teste = 0
        print("Considera-se certificado válido "
              "quando cumprir seguintes exigencias:\n"
              "- Pelo menos duas vacinações com mais de 15 dias\n"
              "- Teste rápido nos últimos 2 dias (resultado Negativo)\n"
              "- Teste demorado nos últimos 3 dias (resultado Negativo)\n"
              "- Ter informações completas das vacinas ou testes\n "
              "- O último teste realizado terá que ser Negativo.")
        if certif[9] == certif[8] and qtos_dias_vacin > 15:
            possui_cert = "S"
        elif certif[5] == "N" and qtos_dias_teste <= 2 and certif[6] == "Rapido":
            possui_cert = "S"
        elif certif[5] == "N" and qtos_dias_teste <= 3 and certif[6] == "Demorado":
            possui_cert = "S"
        else:
            possui_cert = "N"
        if certif[5] == "P":
            possui_cert = "N"
            print("\nComo o teu último teste registado é Positivo,\n"
                  "o certificado continuará não "
                  "válido até teres um teste Negativo resgistado")
        if possui_cert == "S":
            print("\nCERTIFICADO:\n.\n.\n.\n-----> VÁLIDO\n")
        else:
            print("\nCERTIFICADO:\n.\n.\n.\n-----> NÃO  VÁLIDO\n")
    # Visualização informações dos utentes:
    elif decisao == "2":
        numero = input("Digite o N. do Certificado ou o NUS: ")
        localizar_pelo_nus_ncert(cert, numero)

    print("Obrigado por utilizar nosso programa. Até a próxima.")
