from django.shortcuts import render, redirect
from apps.clothes.utilities.generate import generate_unique_filename
from django.contrib import messages 
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from apps.clothes.models import Kind_clothes, Season, Clothes

# Create your views here.
def newClothes(request):
  if request.method == 'POST':
    image_temp = request.FILES.get('image')
    color_temp = request.POST.get('color')
    kind_clothes_temp = request.POST.get('kind')
    brand_temp = request.POST.get('brand')
    season_temp = request.POST.get('season')
    material_temp = request.POST.get('material')

    if image_temp:
      image_temp =  generate_unique_filename(image_temp)
    
    kind_clothes_instance = get_object_or_404(Kind_clothes, ID_KIND=kind_clothes_temp)
    season_instance = get_object_or_404(Season, ID_SEASON=season_temp)

    
    new_clothes = Clothes(
      COLOR = color_temp,
      BRAND = brand_temp,
      MATERIAL = material_temp,
      IMAGE_CLOTHES = image_temp,
      KIND_CLOTHES_FK = kind_clothes_instance,
      SEASON_FK = season_instance
    )

    new_clothes.save()
    messages.success(request, f"Felicitaciones, la prenda fue registrada correctamente 😉")
    return redirect('verClothes')

  kind_clothes_array = Kind_clothes.objects.all()
  season_array = Season.objects.all()

  context = {
    'kind': kind_clothes_array,
    'season': season_array

  }
  return render(request, 'pages/newClothes.html', context)

def verClothes(request):
  verClothes = Clothes.objects.select_related('KIND_CLOTHES_FK', 'SEASON_FK')

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


  kind_clothes = verClothes.values_list('KIND_CLOTHES_FK__NAME_KIND_CLOTHES', flat=True).distinct()
  context = {
    'clothes': verClothes,
    'kind_name': kind_clothes,
    'color_filter': color_filter,
    'season_filter': season_filter,  # Para mantener el valor del filtro de temporada
    'seasons': seasons,  # Para mostrar las temporadas en el select
  }

  return render(request, 'pages/verClothes.html', context)

def FormularioClothes(request, ID_CLOTHES):
  try:
    clothe = Clothes.objects.get(ID_CLOTHES=ID_CLOTHES)
    kind_clothes_array = Kind_clothes.objects.all()
    season_array = Season.objects.all()
    data = {
      "clothe": clothe,
      'kind': kind_clothes_array,
      'season': season_array
    }
    return render(request, 'pages/formulario_Clothes.html', data)
  except ObjectDoesNotExist:
    error_message = f"La prenda con el id: {ID_CLOTHES} no existe"
    return render(request, 'pages/verClothes.html', {"error_message":error_message})
  
def actualizarClothes(request, ID_CLOTHES):
  try:
    if request.method == 'POST':
      kind_clothes_temp = request.POST.get('kind')
      season_temp = request.POST.get('season')
      kind_clothes_instance = get_object_or_404(Kind_clothes, ID_KIND=kind_clothes_temp)
      season_instance = get_object_or_404(Season, ID_SEASON=season_temp)


      clothe = Clothes.objects.get(ID_CLOTHES=ID_CLOTHES)

      clothe.COLOR = request.POST.get('color')
      clothe.BRAND = request.POST.get('brand')
      clothe.MATERIAL = request.POST.get('material')
      clothe.SEASON_FK = season_instance
      clothe.KIND_CLOTHES_FK = kind_clothes_instance

      if 'image' in request.FILES:
        # Actualiza la imagen solo si se proporciona en la solicitud
        clothe.IMAGE_CLOTHES = generate_unique_filename(
            request.FILES['image'])
      
      clothe.save()
    return redirect('verClothes')
  except ObjectDoesNotExist:
        error_message = f"La prenda con id: {ID_CLOTHES} no se actualizó."
        return render(request, "pages/verClothes.html", {"error_message": error_message})


