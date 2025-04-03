from django.db import models

# Create your models here.


class Questao(models.Model):
    texto_questao = models.CharField("Texto da Questão", max_length=200)
    data_publicacao = models.DateTimeField("Data Publicação:")

    def __str__(self):
        return self.texto_questao


class Alternativa(models.Model):
    questao = models.ForeignKey(
        Questao, on_delete=models.CASCADE, verbose_name="Questão")
    texto_alternativa = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto_alternativa
