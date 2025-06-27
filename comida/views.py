from django.shortcuts import render

def menu(request):
    comidas = [
        {'nombre': 'Pollo a la brasa', 'imagen': 'images/pollo.jpg'},
        {'nombre': 'Broaster', 'imagen': 'images/broaster.jpg'},
        {'nombre': 'Chaufa', 'imagen': 'images/chaufa.jpg'},
        {'nombre': 'Pizza', 'imagen': 'images/pizza.jpg'}
    ]
    return render(request, 'comida/menu.html', {'comidas': comidas})