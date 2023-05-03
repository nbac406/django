from django.shortcuts import render,get_object_or_404 
from django.shortcuts import redirect
from .models import Category, Post
from django.views import generic
from .forms import QuestionForm
from django.utils import timezone
#from .models import Test

# Create your views here.

def index(req) : 
    post_list = Post.objects.order_by('-createDate')
    context = {
        'post_list' : post_list
    }
    return render(req, 'index.html', context = context)

def post(req, post_id) : 
    question = get_object_or_404(Post, pk=post_id)
    #question = Post.objects
    context = {
        'question' : question
    }
    return render(req, 'post.html', context = context)


#class PostDetailView(generic.DetailView) :
    #model = Post

#class PostCreate(LoginRequiredMixin, CreateView) : 
#   model = Post
#    fields = ['title', 'title_image', 'content', 'category']
#
def post_create(req):
    if req.method == 'POST':
        form = QuestionForm(req.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(req, 'post_form.html', context)