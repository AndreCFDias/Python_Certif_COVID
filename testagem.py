def testes(uten, tes, cert):
    # Importar bibliotecas:
    import numpy as np
    # Importar funcao de outro arquivo *.py:
    from functions import evitar_erro_4, reg_alt
    # Saudação inicial:
    print("\nOlá, bem vindo à gestão de TESTES dos utentes.\n"
          "Aqui podes registar testes e justificar as faltas.\n"
          "Além de visualizar as Justificativas\n")

    # Registar teste de um utente:
    decisao_0 = input("Se desejas REGISTAR testes de um utente, carregue -> 1.\n"
                      "Para justificar uma falta -> 2.\n"
                      "Para Visualizar uma Justificativa de falta, carregue -> 3.\n"
                      "Para finalizar, carregue -> 9: ")
    # Funcao para evitar que o utilizador carregue em algo não solicitado:
    decisao = evitar_erro_4(decisao_0, "REGISTAR", "Justificar falta",
                            "Visualizar a Justificativa de falta", "finalizar")

    if decisao == "1":
        # Funcao para registar teste:
        reg_alt(uten, tes, cert, "Data_Teste", 0, 4, 1, 5, 2, 6, "o teste", 1)
        # Salvar no próprio ficheiro, assim ele será atualizado:
        np.savetxt("certificado.csv", cert, delimiter=";", fmt='% s')

    # Justificar Faltas:
    elif decisao == "2":
        achar = []
        while not achar:
            achar = input("Qual utente queres Justificar?\n"
                          "Procure pelo NUS: ")
        editar = []
        for i in tes:
            if i[0] == achar:
                editar = i
        # Se não houver utente correspondente:
        if not editar:
            print("Utente não localizado. Reinicie e")
        else:
            if editar[2] == "F":
                # Posicao do utente a ser justificado na lista_separada_teste:
                posicao = tes.index(editar)
                visualizar = dict(zip(tes[0], editar))
                print("\nDados do Utente a ser Justificada a falta:\n")
                for y in visualizar:
                    print(y, ": ", visualizar[y])
                justificativa = str(input("Qual a justificativa da falta?: "))
                editar[4] = justificativa
                tes[posicao] = editar
            else:
                print("Utente não faltou a testagem. Confira o NUS, "
                      "reinicie o programa e tente novamente.")
    elif decisao == "3":
        ut = []
        while not ut:
            ut = input("Qual utente queres ver a Justificativa?\n"
                       "Procure pelo NUS: ")
        edit = []
        for i in tes:
            if i[0] == ut:
                edit = i
        if not edit:
            print("Utente não localizado. Reinicie e")
        else:
            lista_nome = []
            for g in uten:
                if ut == g[0]:
                    lista_nome = g
            if edit[2] == "F" and edit[4] == "":
                print("Utente não justificou a falta")
            elif edit[2] != "F":
                print("Utente realizou teste.")
            else:
                print("NUS =", edit[0], "\nNome =", lista_nome[1],
                      "\nData agendada =", edit[1], "\nJustificativa =", edit[4])
    print("Obrigado por utilizar nosso programa. Até a próxima.")
    # Salvar no próprio ficheiro, assim ele será atualizado:
    np.savetxt("testes.csv", tes, delimiter=";", fmt='% s')
