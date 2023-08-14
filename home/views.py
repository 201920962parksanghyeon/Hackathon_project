from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']



    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')
def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'home/post_list.html',
        {
            'posts': posts,
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'home/single_post_page.html',
        {
            'post': post,
        }
    )
# Create your views here.
