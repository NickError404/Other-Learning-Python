import  photoshop.api as ps
import json

class inicio():
    def __init__(self, local_template):
        self.app = ps.Application()
        self.doc = self.app.load(local_template)


    def mudar_layer(self, layer, nome):

        replace_text_layer = self.doc.artLayers[layer]
        # replace_text_layer.textItem.position = position
        replace_text_layer.kind = ps.LayerKind.TextLayer
        replace_text_layer.textItem.contents = nome


    def save_files(self, local_save):

        option = ps.JPEGSaveOptions(quality=10)
        jpg = local_save
        self.doc.saveAs(jpg, option, asCopy=True)

    def closePSD(self):
        self.doc.close()

    def write_date(dados):
        with open ('cidades.json', 'w', encoding='utf8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4, separators=(',', ':'))
    
    def load_date():
        with open ('cidades.json', 'r', encoding='utf8') as f:
            return json.load(f)

    def adicionar_cidades():
        city = (str(input('Adicione a cidade: ')))
        return (city)

    def adicionar_datas():
        date = (str(input('Data: ')))
        return (date)
