from django.shortcuts import render


# fonction static style
def style(request):
    return render(request, 'portfolio_back//base.html')


def index(request):
    return render(request, 'portfolio_back/index.html')
