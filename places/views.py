from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Place


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append({
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.longitude, place.latitude]
          },
          "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
          }
        })
    template = 'index.html'
    json = {
      "type": "FeatureCollection",
      "features": features
    }

    context = {
        'json': json,
    }
    return render(request, template, context=context)


def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    response = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude
        }
    }
    
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})