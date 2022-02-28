def evitar_erro_3(dec, acao, acao2):
    while dec != "1" and dec != "2" and dec != "9":
        print("\nCarregaste: ", dec, "\nPor favor, "
              "responda somente com:\n'1' para", acao, "\n"
              "'2' para", acao2, "\n"
              "'9' para finalizar: ")
        dec = input()
    return dec


def evitar_erro_4(dec, acao, acao2, acao3, acao4):
    while dec != "1" and dec != "2" and dec != "3" and dec != "9":
        print("\nCarregaste: ", dec, "\nPor favor, "
              "responda somente com:\n'1' para", acao, "\n"
              "'2' para", acao2, "\n"
              "'3' para", acao3, "\n'9' para", acao4, ": ")
        dec = input()
    return dec


def editar_data(variavel, letra, editas):
    posicao = variavel[0].index(letra)
    print("\nDigite nova", letra, "\n"
          "(no formato dd/mm/aaaa)")
    novo = input("= ")
    # Dividir em str onde houver " / ":
    novo = novo.split('/')
    # Temos que garantir que a entrada foi dividida em 3 str,
    # as duas primeiras tenham 2 algarismos,
    # a terceira, 4 algarismos e
    # todos os caracteres tem que ser numeros, não letras:
    while len(novo) != 3 or len(novo[0]) != 2 or \
            len(novo[1]) != 2 or len(novo[2]) != 4 or \
            novo[0].isdigit() is not True or \
            novo[1].isdigit() is not True or \
            novo[2].isdigit() is not True:
        print("\nDigite nova", letra, "\n"
              "(no formato dd/mm/aaaa)\n"
              "somente numeros")
        novo = input("= ")
        novo = novo.split('/')
    novo = '/'.join(novo)
    editas[posicao] = novo
    variavel[variavel.index(editas)] = editas


def inserir_data(var):
    # Dividir em str onde houver " / ":
    var = var.split('/')
    # Temos que garantir que a entrada foi dividida em 3 str,
    # as duas primeiras tenham 2 algarismos,
    # a terceira, 4 algarismos e
    # todos os caracteres tem que ser numeros, não letras:
    while len(var) != 3 or len(var[0]) != 2 or \
            len(var[1]) != 2 or len(var[2]) != 4 or \
            var[0].isdigit() is not True or \
            var[1].isdigit() is not True or \
            var[2].isdigit() is not True:
        print("\nDigite novamente no formato dd/mm/aaaa)\n"
              "somente com numeros")
        var = input("= ")
        var = var.split('/')
    var = '/'.join(var)
    return var


def localizar(var):
    # Evitar que carreguem espaço vazio
    indice = input("\nPodes localizar Utentes pelo NUS, Nome ou "
                   "N. Cartão Cidadão.\n= ")
    while not indice or indice == "NUS" or indice == "Nome" or \
            indice == "Cartao Cidadao":
        indice = input("\nDigite um NUS, Nome ou "
                       "N. Cartão Cidadão válido\n=")
    local = []
    for i in var:
        if indice == i[0] or indice == i[1] or \
                indice == i[3]:
            local = i
    # se não houver utente correspondente
    if not local:
        print("Utente não localizado. Reinicie e")
    else:
        local = dict(zip(var[0], local))
        print("Dados do Utente:\n")
        for i in local:
            print(i, ": ", local[i])


def localizar_pelo_nus_ncert(var, indice):
    # Evitar que carreguem espaço vazio
    while not indice or indice == "NUS" or indice == "N_Certif":
        indice = input("\nDigite um NUS ou N. do Certificado válido: ")
    lista_ut = []
    local = []
    for i in var:
        if indice == i[0] or indice == i[1]:
            local = i
    # se não houver utente correspondente
    if not local:
        print("Utente não localizado. Reinicie e")
    else:
        lista_ut = local
        local = dict(zip(var[0], local))
        print("\nDados do Utente")
        for i in local:
            print(i, ": ", local[i])
    return lista_ut


def cria_cert(cert, n_certf, nus, nome, n_cartaoc, data_teste,
              result, tipo_teste, data_vacina, dosagem, doses_vacina):
    novo_certf = [n_certf, nus, nome, n_cartaoc, data_teste, result, tipo_teste,
                  data_vacina, dosagem, doses_vacina]
    cert.append(novo_certf)


def cria_cert_inteiro(cert, uten, igual_todo, z, b, c, d, e, tv):
    import random
    tem = []
    for i in cert:
        if i[1] == igual_todo[0]:
            i[z] = igual_todo[b]
            i[c] = igual_todo[d]
            i[e] = igual_todo[3]
            cert[cert.index(i)] = i
            tem = "1"
    if tem != "1":
        n_certf = str(random.randint(1, 129099999))
        for f in cert:
            while f[0] == n_certf:
                n_certf = str(random.randint(1, 129099999))
        buscar_nome = []
        for g in uten:
            if igual_todo[0] == g[0]:
                buscar_nome = g
        buscar_cc = []
        for h in uten:
            if igual_todo[0] == h[0]:
                buscar_cc = h
        if tv == 1:
            dosagem = igual_todo[2]
            dosestomadas = igual_todo[4]
            data_vacina = igual_todo[3]
            data_teste = ""
            tipo_teste = ""
            result = ""
        else:
            dosagem = ""
            dosestomadas = ""
            data_vacina = ""
            tipo_teste = igual_todo[3]
            data_teste = igual_todo[1]
            result = igual_todo[2]
        cria_cert(cert, n_certf, igual_todo[0], buscar_nome[1],
                  buscar_cc[3], data_teste, result, tipo_teste, data_vacina,
                  dosagem, dosestomadas)


def reg_alt(uten, lis, cert, data, tv, z, b, c, d, e, vc_test, mudar_cert):
    # Evitar que carreguem espaço vazio:
    nus = []
    while not nus:
        print("Qual utente queres gerir ", vc_test, "?")
        nus = input("Procure pelo NUS: ")
    igual_todo = []
    igual_nus = []
    for i in lis:
        if i[0] == nus:
            igual_todo = i
            igual_nus = i[0]
    # Se não houver utente correspondente -> 3 chances para acertar:
    a = 0
    while not igual_nus and a < 3:
        print("\nDigitaste: ", nus, "\n"
                                    "Este NUS não está em nossos registos.\n")
        nus = input("Digite um NUS já registado: ")
        a = a + 1
        for i in lis:
            if i[0] == nus:
                igual_todo = i
                igual_nus = i[0]
    if not igual_nus:
        print("Demasiadas tentativas. Se desejas criar um utente, "
              "reinicie o programa e tente a opção\n"
              "Adicionar utente em GESTÃO de UTENTES.")
    else:
        visualizar = dict(zip(lis[0], igual_todo))
        print("\nDados do Utente a ser editado:\n")
        for y in visualizar:
            print(y, ": ", visualizar[y])
        for k in lis[0]:
            if igual_todo[lis[0].index(k)] == "":
                print("\nAtual", k, "não está preenchido.\n"
                      "Desejas preencher?")
            else:
                print("\nAtual", k, "=", igual_todo[lis[0].index(k)],
                      " - Desejas modificar?")
            sim = input("Digite 'S', caso contrário "
                        "carregue tecla 'enter': ")
            # Usuário pode digitar maiusculas ou minusculas:
            if sim == "S" or sim == "s":
                # Negar alteração do NUS:
                if k == "NUS":
                    print("NUS nao pode ser modificado")
                # Forçar data em formato dd/mm/aaaa:
                elif k == data:
                    editar_data(lis, k, igual_todo)
                elif k == "Resultado":
                    posicao = lis[0].index(k)
                    print("\nDigite novo", k, "carregue:\n"
                                              "P -> POSITIVO\n", "N -> NEGATIVO")
                    novo = input("= ")
                    novo = novo.upper()
                    while novo != "P" and novo != "N":
                        print("Carregaste: ", novo)
                        novo = input("Carregue\n"
                                     "P -> POSITIVO\n"
                                     "N -> NEGATIVO:")
                        novo = novo.upper()
                    igual_todo[posicao] = novo
                    lis[lis.index(igual_todo)] = igual_todo
                elif k == "Tipo_Teste":
                    posicao = lis[0].index(k)
                    print("\nDigite novo", k, "carregue:\n"
                                              "R -> teste rápido\n", "D -> teste demorado")
                    novo = input("= ")
                    novo = novo.upper()
                    while novo != "R" and novo != "D":
                        print("Carregaste: ", novo)
                        novo = input("Carregue\n"
                                     "R -> teste rápido\n"
                                     "D -> teste Demorado")
                        novo = novo.upper()
                    if novo == "R":
                        novo = "Rapido"
                    else:
                        novo = "Demorado"
                    igual_todo[posicao] = novo
                    lis[lis.index(igual_todo)] = igual_todo
                else:
                    posicao = lis[0].index(k)
                    print("\nDigite novo", k)
                    novo = input("= ")
                    igual_todo[posicao] = novo
                    lis[lis.index(igual_todo)] = igual_todo
            else:
                if k == "Resultado":
                    posicao = lis[0].index(k)
                    print("\nPrecisa inserir novo", k, "carregue:\n"
                          "P -> POSITIVO\n", "N -> NEGATIVO")
                    novo = input("= ")
                    novo = novo.upper()
                    while novo != "P" and novo != "N":
                        print("Carregaste: ", novo)
                        novo = input("Carregue\n"
                                     "P -> POSITIVO\n"
                                     "N -> NEGATIVO:")
                        novo = novo.upper()
                    igual_todo[posicao] = novo
                    lis[lis.index(igual_todo)] = igual_todo
                elif k == "Tipo_Teste":
                    posicao = lis[0].index(k)
                    print("\nPrecisa inserir novo", k, "carregue:\n"
                          "R -> teste rápido\n", "D -> teste demorado")
                    novo = input("= ")
                    novo = novo.upper()
                    while novo != "R" and novo != "D":
                        print("Carregaste: ", novo)
                        novo = input("Carregue\n"
                                     "R -> teste rápido\n"
                                     "D -> teste Demorado")
                        novo = novo.upper()
                    if novo == "R":
                        novo = "Rapido"
                    else:
                        novo = "Demorado"
                    igual_todo[posicao] = novo
                    lis[lis.index(igual_todo)] = igual_todo

        editar = dict(zip(lis[0], igual_todo))
        print("\nNovos dados do Utente:\n")
        for i in editar:
            print(i, ": ", editar[i])
        if mudar_cert == 1:
            # Funcao para certificado
            cria_cert_inteiro(cert, uten, igual_todo, z, b, c, d, e, tv)
