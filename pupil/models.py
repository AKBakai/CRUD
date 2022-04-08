from django.db import models

class Pupil(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
