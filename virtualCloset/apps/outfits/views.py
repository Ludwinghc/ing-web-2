from django.shortcuts import render, redirect
from django.contrib import messages 
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from apps.outfits.models import Outfit, OutfitClothes, Clothes, Season
# Create your views here.

def newOutfit(request):
  if request.method == 'POST':
    name_outfit = request.POST.get('name_outfit')
    season_id_temp = request.POST.get('season')
    date_scheduled = request.POST.get('date_scheduled')
    # selected_clothes_ids = request.POST.getlist('clothes')
    selected_clothes = {}
    for kind in request.POST.keys():
      if kind.startswith('clothes_'):
        selected_clothes[kind] = request.POST.get(kind)
    print('el usuario selecciono:')
    print(name_outfit)
    print(season_id_temp)
    print(date_scheduled)
    print(selected_clothes)

    try:
      season_id =  get_object_or_404(Season, ID_SEASON=season_id_temp) 
      outfit_instance =Outfit.objects.create(
        NAME_OUTFIT = name_outfit,
        ID_SEASON_FK = season_id,
        DATE_SCHEDULED = date_scheduled
      )
# Asociar las prendas seleccionadas al outfit
      for kind, cloth_id in selected_clothes.items():
          if cloth_id:  # Verifica que se haya hecho una selección
            try:
              clothes_instance = Clothes.objects.get(ID_CLOTHES=cloth_id)
              print(f"Creando relación para prenda {clothes_instance.BRAND} del tipo {kind}.")
              OutfitClothes.objects.create(ID_OUTFIT=outfit_instance, ID_CLOTHES_FK=clothes_instance)
            except Clothes.DoesNotExist:
              print(f"Error: Prenda con ID {cloth_id} no existe.")

      
  # Validar el outfit
      if outfit_instance.validar_outfit():
          messages.success(request, "¡Outfit registrado exitosamente!")
          return redirect('verOutfit')
      else:
          messages.warning(request, "El outfit no cumple con los requisitos necesarios.")
    except Exception as e:
          messages.error(request, f"Error al guardar el outfit: {e}")
          return redirect('newOutfit')

  verClothes = Clothes.objects.select_related('KIND_CLOTHES_FK', 'SEASON_FK')
  clothes_list =  Clothes.objects.all()
  # Verificar si se ha solicitado limpiar los filtros
  if 'clear_filters' in request.GET:
      color_filter = ''
      season_filter = ''
  else:
      color_filter = request.GET.get('color_filter', '')
      season_filter = request.GET.get('season_filter', '')
  # Obtener el valor del filtro de color desde el request (si existe)
  color_filter = request.GET.get('color_filter', '').strip()
  # Filtrar por color si se ha proporcionado un filtro
  if color_filter:
    verClothes = verClothes.filter(COLOR__icontains=color_filter)  # Asumiendo que COLOR es el campo de color en el modelo
  
  season_filter = request.GET.get('season_filter', '').strip()
  # Filtrar por temporada si se ha proporcionado un filtro
  if season_filter:
    verClothes = verClothes.filter(SEASON_FK__NAME_SEASON__icontains=season_filter)
  
  # Obtener todas las temporadas disponibles para el filtro
  seasons = Season.objects.all()


  # Obtener categorías únicas de prendas
  kind_clothes = verClothes.values_list('KIND_CLOTHES_FK__NAME_KIND_CLOTHES', flat=True).distinct()

  contexto = {

    'color_filter': color_filter,
    'season_filter': season_filter,  # Para mantener el valor del filtro de temporada
    'season': seasons,  # Para mostrar las temporadas en el select
    'clothes': clothes_list,
    'kind_name': kind_clothes,
  }

  return render(request, 'pages/newoutfit.html', contexto)

def verOutfit(request):

  # Obtener todas las temporadas disponibles para el filtro
  seasons = Season.objects.all()
  # Obtener los outfits
  outfits = Outfit.objects.all()
  #obtener las relaciones
  outfitAndClothes = OutfitClothes.objects.select_related('ID_CLOTHES_FK', 'ID_OUTFIT')

  context = {
    'seasons': seasons,  # Para mostrar las temporadas en el select
    'outfits': outfits,
    'fulloutfit': outfitAndClothes,
  }
  return render(request, 'pages/verOutfit.html', context)

def calendar_view(request):
    # Filtrar los outfits con fechas programadas
    outfits = Outfit.objects.filter(DATE_SCHEDULED__isnull=False)

    # Pasar los datos a la plantilla
    return render(request, 'pages/calendar.html', {'outfits': outfits})