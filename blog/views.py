from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.



# importing models and libraries
from .forms import commentForm
from .models import post, Category
from django.views import generic
from django.views.decorators.http import require_GET
from django.http import HttpResponse

def detail(request, category_slug, slug):
    Post = get_object_or_404(post, slug=slug, status=post.ACTIVE)
    
    if request.method == 'POST':
    
        form = commentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post
            comment.save()
            
            return redirect('post_detail', slug=slug)
    else:
        
        form = commentForm()
    
    return render(request, 'blog/detail.html', {'post': Post, 'form': form})
 
def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=post.ACTIVE)
    
    return render(request, 'blog/category.html', {'category': category, 'posts': posts})

def search(request):
    query = request.GET.get('query', '')
    posts = post.objects.filter(status=post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))
    
    return render(request, 'blog/search.html', {'posts': posts, 'query': query})
    
# class based views for posts
#class postslist(generic.ListView):
#    queryset = post.objects.filter(status=1).order_by('-created_on')
#    template_name = 'blog/home.html'
#    paginate_by = 4
 
# class based view for each post
#class postdetail(generic.DetailView):
#    model = post
#    template_name = "blog/posts_list.html"

#def home(request):
#    return HttpResponse('Hello, World!')

