from django.shortcuts import render
from django.http import *
from wtforms import *
import elementpath
from xml.etree import ElementTree
import base64

class FormularioLerXml(Form):
    arquivoXml = StringField('Importar Arquivo')
    campo_pesquisa = StringField('')

class LerXml:

    def renderiza_tela(request):
        form = FormularioLerXml(request.POST or None)

        return render(request, 'LerXml/LerXml.html', {'form': form})
    # @crsf_token
    def ler_arquivo_xml(request):

        print()
        arquivoXml = base64.b64decode(request.POST.getlist('ArquivoXml[]')[0])
        with open("Arquivo.xml", 'wb') as f:
            f.write(arquivoXml)
            f.close()

        tree = ElementTree.parse('Arquivo.xml')
        root = tree.getroot()
        primeiro_nivel = []
        for x in root:
            primeiro_nivel.append({x.tag: x.attrib})

        segundo_nivel = []
        for x in root.iter('softwarepattern'):
            segundo_nivel.append({x.tag: x.attrib})

        terceiro_nivel = []
        for x in root.iter('feature'):
            terceiro_nivel.append({x.tag: x.attrib})

        quarto_nivel = []
        for x in root.iter('scenario'):
            quarto_nivel.append({x.tag: x.attrib})

        quinto_nivel = []
        for x in root.iter('example'):
            quinto_nivel.append({x.tag: x.attrib})

        print(quinto_nivel)


        return JsonResponse({'Retorno': quinto_nivel})

    def pesquisa_pessoas(request):
        tree = ElementTree.parse('Arquivo.xml')
        root = tree.getroot()

        dado = str(request.POST.get('ValorPesquisa'))
        print(dado)
        for a in root.iter('softwarepatternbag'):
            for b in root.iter('softwarepattern'):
                for c in root.iter('feature'):
                    for d in root.iter('scenario'):
                        for e in root.iter('example'):
                            _dados = e.attrib['Examples'].split('|')
                            for f in _dados:
                                print(f)
                                if dado == f.strip(' '):
                                    softwarepatternbag ={a.tag: a.attrib['Name']}
                                    softwarepattern = {b.tag: b.attrib['Name']}
                                    feature = {c.tag: c.attrib['Label']}
                                    softwarepatternbags = {a.tag: d.attrib['Label']}
                                    Examples = e.attrib
                                    print(softwarepatternbag)
                                    print(softwarepattern)
                                    print(Examples)

                                    return JsonResponse({'softwarepatternbag': softwarepatternbag, 'softwarepattern': softwarepattern,
                                                         'feature': feature, 'softwarepatternbags': softwarepatternbags,
                                                         'Examples': Examples})

        return JsonResponse({'softwarepatternbag': 0})