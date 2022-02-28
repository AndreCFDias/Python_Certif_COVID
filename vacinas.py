def vacina(uten, vac, cert):
    # Importar bibliotecas:
    import numpy as np
    from datetime import date, datetime
    # Importar funcao de outro arquivo *.py:
    from functions import evitar_erro_3, reg_alt
    # Saudação inicial:
    print("\nOlá, bem vindo à gestão de VACINAS dos utentes.\n"
          "Aqui podes registar as vacinas dos "
          "utentes e observar alguns dados estatisticos")
    decisao_0 = input("\nSe desejas Alterar as informações de "
                      "vacina de um utente, carregue -> 1.\n"
                      "Para as estatísticas, carregue -> 2.\n"
                      "Para finalizar, carregue -> 9: ")
    # Funcao para evitar que o utilizador carregue em algo não solicitado:
    decisao = evitar_erro_3(decisao_0, "Alterar/adicionar informações", "Observar estatísticas")
    # Registar teste de um utente:
    if decisao == "1":
        # Funcao para alterar vacinas:
        reg_alt(uten, vac, cert, "Data", 1, 8, 2, 9, 4, 7, "a vacicação", 1)
        np.savetxt("certificado.csv", cert, delimiter=";", fmt='% s')
    # Ver as Estatisticas:
    elif decisao == "2":
        vacinados = 0
        faltas = 0
        for i in vac:
            if i[4] == "":
                faltas = faltas + 1
            else:
                vacinados = vacinados + 1
        # Como não retiramos o header, ele ocupa a primeira posicao[0]
        # para não contá-lo, subtraimos 1:
        vacinados = vacinados - 1
        # Total utentes da tabela utentes.csv:
        total_utentes = len(uten) - 1
        nao_vacinados = total_utentes - vacinados

        print("\nEm nossos registos, existem:", total_utentes, "Utentes.",
              "\nDestes,", vacinados,
              "Utentes estão vacinados.(pelo menos 1 dose)\nContra",
              nao_vacinados, "Utentes sem vacina.\n",
              round(vacinados / total_utentes * 100, 2),
              "% dos utentes ESTÃO vacinados com pelo menos 1 dose.\n",
              round(nao_vacinados / total_utentes * 100, 2),
              "% dos utentes NÃO estão vacinados.")
        # Como a data da primeira vacinação ja ocorreu, vamos fixá-la:
        dia_1_vacina = date(2020, 12, 27)
        # Usar biblioteca "datetime" para saber o dia de hoje:
        dia_de_hoje = date.today()
        # Contar dias de uma data até dia presente:
        quantidade_dias = abs((dia_1_vacina - dia_de_hoje).days)
        dias_vacina_1_registo = 0
        for i in vac:
            sembarra = i[3].split('/')
            sembarra = "".join(sembarra)
            # Só queremos datas com numeros:
            if sembarra.isdigit() is True:
                date = datetime.strptime(i[3], '%d/%m/%Y').date()
                tempo = abs((date - dia_de_hoje).days)
                if tempo > dias_vacina_1_registo:
                    dias_vacina_1_registo = tempo
        print("\nA partir do primeiro dia de vacinação, já se passaram",
              quantidade_dias, "dias até hoje:"
              "\n(o primeiro dia de vacinação ocorreu no dia 27/12/2020)")
        print("A Média de vacinados desde o primeiro dia é de:",
              round((vacinados - 1) / quantidade_dias, 2),
              "Utentes vacinados por dia.")
        print("\nEm nosso banco de dados, já se passaram", dias_vacina_1_registo,
              "dias desde o nosso primeiro registo.")
        print("Ao considerar o primeiro dia do nosso banco de dados, "
              "a média de vacinados é de:",
              round((vacinados - 1) / dias_vacina_1_registo, 2),
              "Utentes vacinados por dia.")
    print("Obrigado por utilizar nosso programa. Até a próxima.")
    # Salvar no próprio ficheiro, assim ele será atualizado:
    np.savetxt("vacinacao.csv", vac, delimiter=";", fmt='% s')
