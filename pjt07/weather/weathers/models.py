from django.db import models

# Create your models here.

class Weather(models.Model):
    dt_txt = models.DateTimeField()
    temp = models.FloatField() # 온도 (기본값:켈빈)
    feels_like = models.FloatField() # 체감온도 (기본값: 켈빈)