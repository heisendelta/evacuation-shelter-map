from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
import folium
from .models import City

def main(request):
    return HttpResponse("Hello world!")

def city(request, city_name):
    try:
        city = City.objects.get(name=city_name)

        my_map = folium.Map(location=[city.lat_center, city.lon_center], zoom_start=10)
        map_html = my_map.get_root().render()

        context = {'map_html': map_html}
        return render(request, 'map_template.html', context)
    
    except city.DoesNotExist:
        return HttpResponseNotFound('City not in database.')
