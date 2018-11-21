from django.forms import ModelForm, forms, Textarea, HiddenInput, ImageField, NumberInput
from .models import Trade


class TradeForm(ModelForm):


    class Meta:
        model = Trade


        fields = ['title', 'subtitle', 'description', 'mainimg', 'secondimg',
                  'thirdimg','interest','subinterest','interestdetails', 'interestimg','fk_profile']

        widgets = {'description' : Textarea(), 'interestdetails': Textarea(),
                    'fk_profile': HiddenInput(),
                   }

        labels = {
            "title": "Titulo do Anuncio",
            "subtitle": "Informação Adicional",
            "description": "Descrição do Anuncio",
            "mainimg": "Imagem Principal",
             "interestdetails": "Scamb",
            "subinterest" : "Complemente as informaões ou adicione outro Scamb",
            "interestimg": "Imagem Principal",
        }


