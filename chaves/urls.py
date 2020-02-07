from django.urls import path

from chaves.views import ListaChavesView

urlpatterns = [
    path('', ListaChavesView.as_view(), name='lista_chaves'),
]
