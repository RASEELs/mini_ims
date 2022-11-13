from django.shortcuts import render

# Create your views here.
def item_index(request):
    return render(request, 'items/index.html')