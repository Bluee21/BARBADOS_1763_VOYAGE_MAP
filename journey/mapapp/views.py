from django.shortcuts import render

def journey_map(request):
    return render(request, 'journey_map.html')
