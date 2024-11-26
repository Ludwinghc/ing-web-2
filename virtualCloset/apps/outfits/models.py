from django.db import models
from apps.clothes.models import Clothes,Kind_clothes,Season

class Outfit(models.Model):
  ID_OUTFIT = models.AutoField(primary_key=True)
  NAME_OUTFIT = models.CharField(max_length=255)
  CLOTHES_PARAM = models.ManyToManyField(Clothes, through='OutfitClothes')
  ID_SEASON_FK = models.ForeignKey(Season, on_delete=models.CASCADE, db_column='ID_SEASON_FK')
  DATE_SCHEDULED = models.DateField(null=True, blank=True)

  class Meta:
    db_table = 'OUTFIT'
  
  def validar_outfit(self):
      # Categorías requeridas para un outfit válido
      kind_required = {'superior', 'inferior', 'pies'}
      kind_present = set()  # Para rastrear las categorías presentes en el outfit

      dress = False  # Bandera para verificar si hay un traje o vestido

      # Mapeo de tipos de ropa a categorías
      kind_to_category = {
          'CAMISETAS': 'superior',
          'CAMISAS': 'superior',
          'CHAQUETAS': 'cubrirse',
          'ABRIGOS': 'cubrirse',
          'PANTALONES': 'inferior',
          'ZAPATOS': 'pies',
          'TENIS': 'pies',
          'BLUSAS': 'superior',
          'FALDAS': 'inferior',
          'VESTIDOS': 'vestido',
          'TACONES': 'pies',
          'TOPS': 'superior',
          'LEGGINS': 'inferior',
          'PANTALONETA': 'inferior',
          'TRAJE': 'traje',
          'BLAZZER': 'cubrirse',
          'ACCESORIO': None
      }

      # Iteramos sobre las prendas asociadas al outfit
      for outfit_clothes in self.outfitclothes_set.all():
          clothes_temp = outfit_clothes.ID_CLOTHES_FK  # Obtenemos la prenda
          kind_clothe = clothes_temp.KIND_CLOTHES_FK.NAME_KIND_CLOTHES  # Obtenemos el tipo de ropa

          # Asignamos la categoría correspondiente al tipo de ropa
          category = kind_to_category.get(kind_clothe)

          if category:  # Solo agregamos si tiene una categoría válida
              kind_present.add(category)

          # Si la prenda es un traje o vestido, marcamos la bandera
          if kind_clothe.lower() in ['traje', 'vestido']:
              dress = True

      # Validamos si se cumple al menos uno de los dos criterios
      if kind_required.issubset(kind_present) or dress:
          return True  # El outfit es válido

      # Si no se cumple ningún criterio, el outfit no es válido
      return False


class OutfitClothes(models.Model):
  ID_OUTFITCLOTHES = models.AutoField(primary_key=True)
  ID_OUTFIT = models.ForeignKey(Outfit, on_delete=models.CASCADE, db_column='ID_OUFIT_FK')
  ID_CLOTHES_FK = models.ForeignKey(Clothes, on_delete=models.CASCADE, db_column='ID_CLOTHES_FK')
  DATE = models.DateField(auto_now_add=True)

  class Meta:
    db_table = 'OUTFITXCLOTHES'
    unique_together = ('ID_OUTFIT', 'ID_CLOTHES_FK')
