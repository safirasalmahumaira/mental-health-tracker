from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245850',
        'name': 'Safira Salma Huamira',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)