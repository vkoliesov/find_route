from django.shortcuts import render, get_object_or_404

from cities.models import City


def home(request, id=None):
    if id:

        city = get_object_or_404(City, id=id)
        context = {'object': city}
        return render(request, 'cities/detail.html', context)

    qs = City.objects.all()
    context = {'objects_list': qs}
    return render(request, 'cities/home.html', context)
