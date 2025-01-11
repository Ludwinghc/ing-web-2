from django.db import models

# Create your models here.

class Kind_clothes(models.Model):
  ID_KIND = models.AutoField(primary_key=True)
  NAME_KIND_CLOTHES = models.CharField(max_length=255)

  class Meta:
    db_table = 'KIND_CLOTHES'

class Season(models.Model):
  ID_SEASON = models.AutoField(primary_key=True)
  NAME_SEASON = models.CharField(max_length=255)

  class Meta:
    db_table = 'SEASON'

class Clothes(models.Model):
  ID_CLOTHES = models.AutoField(primary_key=True)
  COLOR = models.CharField(max_length=255)
  BRAND = models.CharField(max_length=255)
  MATERIAL = models.CharField(max_length=255)
  IMAGE_CLOTHES = models.ImageField(upload_to='clothes')
  KIND_CLOTHES_FK = models.ForeignKey(Kind_clothes, on_delete=models.CASCADE, db_column = 'KIND_CLOTHES_FK')
  SEASON_FK = models.ForeignKey(Season, on_delete=models.CASCADE, db_column = 'SEASON_FK')

  def es_extension_valida(self):
        extensiones_validas = ['.jpg', '.jpeg', '.png', '.gif']
        return any(self.IMAGE_CLOTHES.name.lower().endswith(ext) for ext in extensiones_validas)
  
  class Meta:
    db_table = 'CLOTHES'