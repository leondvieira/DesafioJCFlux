from django.db import models


class Chave(models.Model):
    codigo = models.CharField(max_length=44)
    arquivado = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.codigo
