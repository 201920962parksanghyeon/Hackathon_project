from django.shortcuts import render
def landing(request):
    return render(
        request,
        'one_pages/landing.html'
    )

def about_me(request):
    return render(
        request,
        'one_pages/class.html'
    )
# Create your views here.
