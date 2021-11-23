# import  json
from photoshop import  Session

# def load_json_w(dados):
#     with open ('cidades.json', 'w', encoding='utf8') as f:
#         json.dump(dados, f, ensure_ascii=False, indent=4, separators=(',', ':'))


# def load_json_r():
#     with open ('cidades.json', 'r', encoding='utf8') as f:
#         return json.load(f)


# escrever = 'Olá'
# data = load_json_w(escrever)



# cidades_lista = {
#     'cidades': ['Grajaú', 'Vila Tucum', 'Imperatriz'],
#     'datas': ['7, 5, 6']
# }

# print(cidades_lista['cidades'])

# cidades_lista['cidades'].append(str(input('Cidade: ')))

# print(cidades_lista['cidades'])


with Session() as ps:
            replace_contents = ps.app.stringIDToTypeID("placedLayerReplaceContents")
            desc = ps.ActionDescriptor
            idnull = ps.app.charIDToTypeID("null")
            desc.putPath(idnull, f"Photoshopy Project Concurso\images\10.jpeg")
            ps.app.executeAction(replace_contents, desc)