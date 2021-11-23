from sources import *

local_template = r"G:\HD 1 TB\Photoshopy\Banner 2021 Concurso Finalista.psd"

auto_save = str(input("\033[1;36mSave automático? [y/n]: ")).strip()[0]

if auto_save in 'Yy':
    timing = int(input('\033[1;33mTempo para salve automático: '))

while True:
    nomeArquivo = str(input('\033[1;36mNome: ')).strip()
    instagram = '@' + str(input('\033[1;33mInstagram: ')).strip()
    cidade = str(input('\033[1;32mCidade: ')).strip()
    local_replace = str(input('\033[1;37mNúmero da Foto: ')).strip()

    local_pasta = "G:\Dropbox\Finalistas 2021 Etapa 2"
    local_save = f"{local_pasta}\{nomeArquivo}"
    nome_cidade = f'de {cidade} 2021'

    p = inicio(local_template)

    p.mudar_layer_maquiadora(layer='maquiadora',nome=nomeArquivo)
    p.mudar_layer_maquiadora(layer='@instagram', nome=instagram)
    p.mudar_layer_maquiadora(layer='de cidade 2021', nome=nome_cidade)
    p.replace_image(local_replace=local_replace)
    if auto_save in 'Yy':
        inicio.contador(time=timing)
    else:
        contin = input('\033[1;33mQualquer tecla para save! ')
    p.save_files(local_save)
    p.closePSD()

