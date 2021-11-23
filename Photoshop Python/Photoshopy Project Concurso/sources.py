import  photoshop.api as ps
from time import sleep
from photoshop import Session


class inicio():
    def __init__(self, local_template):
        self.app = ps.Application()
        self.doc = self.app.load(local_template)


    def mudar_layer_maquiadora(self, layer, nome):

        replace_text_layer = self.doc.artLayers[layer]
        # replace_text_layer.textItem.position = position
        replace_text_layer.kind = ps.LayerKind.TextLayer
        replace_text_layer.textItem.contents = nome


    def save_files(self, local_save):

        option = ps.JPEGSaveOptions(quality=10)
        jpg = local_save
        self.doc.saveAs(jpg, option, asCopy=True)


    def replace_image(self, local_replace):
        
        with Session() as ps:
            replace_contents = ps.app.stringIDToTypeID("placedLayerReplaceContents")
            desc = ps.ActionDescriptor
            idnull = ps.app.charIDToTypeID("null")
            desc.putPath(idnull, f"Photoshopy Project Concurso\images\{local_replace}.jpeg")
            ps.app.executeAction(replace_contents, desc)

    def contador(time):
        cont = time
        for c in range(0, time):
            sleep(1)
            print(f'\033[1;37m{cont}s \033[1;36mpara salvar a imagem')
            cont -= 1

    def closePSD(self):
        self.doc.close()

