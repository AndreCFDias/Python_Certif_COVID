# Importar bibliotecas que utilizarei:
import pandas as pd
# Importar funcao de outro arquivo *.py
from utente import utentes
from testagem import testes
from vacinas import vacina
from certificados import certificado
from functions import evitar_erro_4

# Importar os arquivos CSV e transformá-los em uma lista de listas:
dict_csv = pd.read_csv('utentes.csv', sep='\t', encoding='utf-8',
                       header=None).to_dict()
valores = dict_csv[0].values()
lista_valores = list(valores)
lista_separada_utentes = []
for i in lista_valores:
    lista_separada_utentes.append(i.split(";"))

dict_csv = pd.read_csv('testes.csv', sep='\t', encoding='utf-8',
                       header=None).to_dict()
valores = dict_csv[0].values()
lista_valores = list(valores)
lista_separada_teste = []
for i in lista_valores:
    lista_separada_teste.append(i.split(";"))

dict_csv = pd.read_csv('vacinacao.csv', sep='\t', encoding='utf-8',
                       header=None).to_dict()
valores = dict_csv[0].values()
lista_valores = list(valores)
lista_separada_vacina = []
for i in lista_valores:
    lista_separada_vacina.append(i.split(";"))

dict_csv = pd.read_csv('certificado.csv', sep='\t', encoding='utf-8',
                       header=None).to_dict()
valores = dict_csv[0].values()
lista_valores = list(valores)
lista_separada_certificado = []
for i in lista_valores:
    lista_separada_certificado.append(i.split(";"))

# Deixei a impressão das listas para visualizar os dados e poder testá-los:
print(lista_separada_utentes)
print(lista_separada_teste)
print(lista_separada_vacina)
print(lista_separada_certificado)

# Saudação inicial geral do programa:
resp_1 = input("\n\nOlá, bem vindo ao novo programa de gerenciamento de "
               "dados dos utentes em relação ao COVID.\n\n"
               "Para área de UTENTES.......carregue => 1\n"
               "Para área de TESTES........carregue => 2\n"
               "Para área de VACINAS.......carregue => 3\n"
               "Para área de CERTIFICADOS..carregue => 9\n"
               "=====>")
# Funcao para evitar erro:
decid = evitar_erro_4(resp_1, "Gestão de Utentes", "Gestão de Testes", "Gestão de Vacinas", "Certificados")
# Entra na área desejada e chama a função pertinente:
if decid == "1":
    utentes(lista_separada_utentes, lista_separada_teste, lista_separada_vacina)
elif decid == "2":
    testes(lista_separada_utentes, lista_separada_teste, lista_separada_certificado)
elif decid == "3":
    vacina(lista_separada_utentes, lista_separada_vacina, lista_separada_certificado)
else:
    certificado(lista_separada_certificado)
