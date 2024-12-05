from django.shortcuts import render

def base_view(request):
    return render(request,'testapp/base.html')

def movie_view(request):
    return render(request,'testapp/movie.html')

def sport_view(request):
    return render(request,'testapp/sport.html')
def politics_view(request):
    return render(request,'testapp/politics.html')