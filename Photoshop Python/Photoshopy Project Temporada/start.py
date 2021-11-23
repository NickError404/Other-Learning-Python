
from sources import *

local_template = r"G:\HD 1 TB\ARQUIVOS\Nel\NEL TEMPLATE\Photoshopy\photoshopy Temporada.psd"

# city = []
# date = []

# conti = True
# while conti:

#     city.append(inicio.adicionar_cidades()),
#     date.append(inicio.adicionar_datas())

#     quest = str(input('[y/n] para continuar:'))[0]   
#     if quest in 'Nn':
#         conti = False


# cidades_datas = {
#     'cidades': city,
#     'datas': date
# }

# try:
#     dados = inicio.load_date()
# except FileNotFoundError:
#     inicio.write_date(cidades_datas)

while True:
    cidade = str(input('\033[1;32mCidade: ')).strip()
    data = str(input('\033[1;33mData: ')).strip() + ' De Dezembro'

    local_pasta = "G:\Dropbox\Temporada Cidades"
    local_save = f"{local_pasta}\{cidade}"


    p = inicio(local_template)

    p.mudar_layer(layer='cidade',nome=cidade)
    p.mudar_layer(layer='data', nome=data)

    contin = input('\033[1;33mQualquer tecla para save! ')
    
    p.save_files(local_save)
    p.closePSD()

