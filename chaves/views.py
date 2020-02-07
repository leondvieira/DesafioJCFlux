from django.http import HttpResponse
from django.shortcuts import render
import clipboard

# Create your views here.
from django.views import View
from chaves.models import Chave


class ListaChavesView(View):

    def get(self, request):
        arquivadas = Chave.objects.filter(arquivado=True).count()
        pendentes = Chave.objects.filter(arquivado=False)

        context = {
            'arquivadas': arquivadas,
            'pendentes': pendentes
        }
        return render(request, 'chaves/lista_chaves.html', context)

    def post(self, request):

        id_chave = request.POST.get('pendente')
        chave = Chave.objects.get(id=id_chave)

        if request.POST.get('copiar_chave'):
            arquivadas = Chave.objects.filter(arquivado=True).count()
            pendentes = Chave.objects.filter(arquivado=False)
            clipboard.copy(chave.codigo)
            context = {
                'chave': chave,
                'status': 'processamento',
                'arquivadas': arquivadas,
                'pendentes': pendentes
            }
        else:
            chave = Chave.objects.get(id=id_chave)
            chave.arquivado = True
            clipboard.copy(chave.codigo[8:12])
            chave.save()
            arquivadas = Chave.objects.filter(arquivado=True).count()
            pendentes = Chave.objects.filter(arquivado=False)

            context = {
                'chave': chave,
                'arquivadas': arquivadas,
                'pendentes': pendentes
            }
        return render(request, 'chaves/lista_chaves.html', context)