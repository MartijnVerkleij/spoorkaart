from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.template import RequestContext, loader

from railgraph.models import Station, Track

def index(request):

	stations = Station.objects.order_by('tel_code')
	tracks = Track.objects
	stations_map = []
	for station in stations:
		stations_map.append([station, ((53 - station.location_lat)*500) , ((station.location_lon - 5 )*500) ])

	therange = range(0,100,5)
	template = loader.get_template('spoorkaart/index.html')

	context = RequestContext(request, { 
		'therange': therange,
		'stations': stations,
		'stations_map': stations_map,
		'tracks': tracks,
	})

	return HttpResponse(template.render(context))
