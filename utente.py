def utentes(uten, tes, vac):
    # Importar biblioteca:
    import numpy as np
    # Importar funcao de outro arquivo *.py:
    from functions import evitar_erro_3, inserir_data, localizar, reg_alt

    # Saudação inicial:
    print("\nOlá, bem vindo à gestão dos UTENTES.\n"
          "Aqui podes conferir, editar e apagar os dados de um Utente.\n"
          "Também podes adicionar novos Utentes.\n")
    decisao_0 = input("Se desejas LOCALIZAR um utente, carregue -> 1.\n"
                      "Para ir à próxima opção, carregue -> 2.\n"
                      "Para finalizar, carregue -> 9: ")
    # Funcao para evitar que o utilizador carregue em algo não solicitado:
    decisao = evitar_erro_3(decisao_0, "Localizar", "ir à próxima opção")
    # Localizar e conferir dados de um utente:
    if decisao == "1":
        localizar(uten)
    elif decisao == "2":
        decisao_1 = input("\nSe desejas EDITAR um utente, carregue -> 1.\n"
                          "Para ir a próxima opção, carregue -> 2.\n"
                          "Para finalizar, carregue -> 9: ")
        # Funcao para evitar que o utilizador carregue em algo não solicitado:
        decisao = evitar_erro_3(decisao_1, "Editar", "ir à próxima opção")
        # Editar utente:
        if decisao == "1":
            # Funcao para registar teste:
            reg_alt(uten, uten, 0, "data nascimento", 0, 0, 0, 0, 0, 0, "", 0)

        elif decisao == "2":
            decisao_2 = input("\nSe desejas APAGAR um utente, carregue -> 1.\n"
                              "Para ir a próxima opção, carregue -> 2.\n"
                              "Para finalizar, carregue -> 9: ")
            # Funcao para evitar que o utilizador carregue em algo não solicitado:
            decisao = evitar_erro_3(decisao_2, "APAGAR", "ir à próxima opção")
            # Apagar utente
            if decisao == "1":
                # Evitar que carreguem espaço vazio
                apagar = []
                while not apagar:
                    apagar = input("Qual Utente deseja APAGAR?\n"
                                   "Procure pelo NUS ou pelo numero do "
                                   "Cartão Cidadão para "
                                   "evitar ambiguidades: ")
                apagado = []
                for i in uten:
                    for j in i:
                        if j == apagar:
                            apagado = i
                            apagado = dict(zip(uten[0], apagado))
                            print("\nDados do Utente que serão apagados:\n")
                            for x in apagado:
                                print(x, ": ", apagado[x])
                            certeza = input("\nO processo irá APAGAR todos os "
                                            "dados do utente.\n"
                                            "Tens certeza que queres apagar?\n"
                                            "'S' para APAGAR\n"
                                            "'N' para finalizar o "
                                            "programa e NÃO apagar: ")
                            certeza = certeza.upper()
                            # Evitar que o utilizador carregue em algo não solicitado:
                            while certeza != "S" and certeza != "N":
                                print("\nCarregaste ", certeza)
                                certeza = input("Por favor, "
                                                "responda somente com 'S' "
                                                "para APAGAR,\n"
                                                "ou 'N' para para finalizar e "
                                                "NÃO apagar: ")
                                certeza = certeza.upper()
                            if certeza == "S":
                                del (uten[uten.index(i)])
                                print("\nUtente apagado.")
                            else:
                                print("\nUtente não apagado.")
                # se não houver utente correspondente
                if not apagado:
                    print("\nUtente não localizado. Reinicie e")

            elif decisao == "2":
                decisao_3 = input("\nSe desejas ADICIONAR um NOVO Utente,"
                                  " carregue -> 1.\n"
                                  "Para finalizar, carregue -> 9: ")
                # Evitar que o utilizador carregue em algo não solicitado:
                while decisao_3 != "1" and decisao_3 != "9":
                    print("\nCarregaste: ", decisao_3)
                    decisao_3 = input("\nPor favor, "
                                      "responda somente com:\n"
                                      "'1' para ADICIONAR\n"
                                      "'9' para finalizar : ")
                # adicionar novo utente:
                if decisao_3 == "1":
                    print("\nPara adicionar um novo utente, "
                          "é necessário pelo menos o Nome e "
                          "indicação se teve ou não COVID")

                    nus = input("digite teu NUS: ")
                    while nus == "":
                        print("É através do NUS que iremos te identificar.\n"
                              "Não podes deixar vazio.")
                        nus = input("Digite teu NUS: ")
                    igual = []
                    for i in uten:
                        for j in i:
                            if j == nus:
                                igual = nus
                    a = 0
                    while nus == igual and a < 3:
                        print("\nDigitaste: ", nus,
                              "Este NUS já existe.\n")
                        nus = input("Digite um novo NUS: ")
                        a = a + 1
                        for i in uten:
                            for j in i:
                                if j == nus:
                                    igual = nus
                    if nus == igual:
                        print("Demasiadas tentativas. Se desejas editar um utente, "
                              "reinicie o programa e tente a opção EDITAR. ")
                    else:

                        nome = input("Digite teu Nome: ")
                        morada = input("Tua Morada: ")
                        cartao_cidadao = input("N. Cartao Cidadao: ")
                        d_n = input("Data de nascimento "
                                    "(formato dd/mm/aaaa): ")
                        data_nascimento = inserir_data(d_n)
                        doenca = input("Se já teve COVID, responda 'S'\n "
                                       "Se não teve ou não sabe, 'N': ")
                        doenca = doenca.upper()
                        # Evitar que o utilizador carregue em algo não solicitado:
                        while doenca != "S" and doenca != "N":
                            print("\nCarregaste: ", doenca)
                            doenca = input("Resposta obrigatória.\n"
                                           "Se já teve COVID, responda 'S'\n "
                                           "Se não teve ou não sabe, 'N': ")
                            doenca = doenca.upper()

                        novo_utente = [nus, nome, morada,
                                       cartao_cidadao,
                                       data_nascimento, doenca]
                        # Outro modo de evitar que o
                        # utilizador não preencha o Nome:
                        if novo_utente[1] == "":
                            print("Para adicionar um novo utente, "
                                  "é necessário pelo menos o Nome e "
                                  "indicação se teve ou não COVID\n"
                                  "Reinicie e")
                        else:
                            uten.append(novo_utente)
                            p_teste = [novo_utente[0], "", "", "", ""]
                            tes.append(p_teste)
                            p_vacina = [novo_utente[0], "", "", "", ""]
                            vac.append(p_vacina)

    print("Obrigado por utilizar nosso programa. Até a próxima.")
    np.savetxt("utentes.csv", uten, delimiter=";", fmt='% s')
    np.savetxt("testes.csv", tes, delimiter=";", fmt='% s')
    np.savetxt("vacinacao.csv", vac, delimiter=";", fmt='% s')
