
import photoshop.api as ps


app = ps.Application()
doc = app.load(r"G:\HD 1 TB\ARQUIVOS\Nel\NEL TEMPLATE\Concurso Maranhão\TEMPLATE BETA\Banner, Test.psd")


def inicio():
    # text_color = ps.SolidColor()
    # text_color.rgb.green = 255
    replace_text_layer = doc.artLayers['Karolzinha Bastos']
    replace_text_layer.kind = ps.LayerKind.TextLayer
    replace_text_layer.textItem.contents = "Hello, World!"
    # replace_text_layer.textItem.position = [160, 167]
    # replace_text_layer.textItem.size = 57.33
    # replace_text_layer.textItem.color = text_color


def save_files():
    # # save to jpg

    option = ps.JPEGSaveOptions(quality=10)
    jpg = r'G:\HD 1 TB\Photoshopy\Fotos_Test\teste1'
    doc.saveAs(jpg, option, asCopy=True)


inicio()
save_files()

