from django.shortcuts import render,get_object_or_404
from .models import Category,Regions,Blog
from taggit.models import Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
def index(request):
    categories = Category.objects.all()
    regions=Regions.objects.all()
    blog=Blog.objects.all()
    tag=Tag.objects.all()
    
    
    # users_in_group = Group.objects.get(name="Admin").user_set.all()
    # is_member = request.user in users_in_group
 
    
    page = request.GET.get('page',1)
    paginator = Paginator(blog,2)
    # comments_count=posts.Comment_set.all()

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator,2)
    

    return render(request,"index.html", {
        "categories":categories,
        "regions":regions,
        'blog':posts,
        'tag':tag
    })
    
def region_filter(request, slug):
    region = get_object_or_404(Regions, slug=slug)
    posts = Blog.objects.filter(region=region)
    categories = Category.objects.all()
    regions=Regions.objects.all()
    tag=Tag.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(posts,3)
    # comments_count=posts.Comment_set.all()

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator,1)
    

    return render(request,"index.html", {
        "categories":categories,
        "regions":regions,
        'blog':posts,
        'tag':tag
    })

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Blog.objects.filter(category=category)
    categories = Category.objects.all()
    regions=Regions.objects.all()
    tag=Tag.objects.all()
    context = {
        'blog':posts,
        'categories':categories,
        "regions":regions,
        'tag':tag
    }
    return render(request, 'index.html', context)   

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Blog.objects.filter(tags=tag)
    categories = Category.objects.all()
    regions=Regions.objects.all()
    context = {
        'blog':posts,
        'categories':categories,
        "regions":regions,
    }
    return render(request, 'index.html', context)    

def detail(request,slug):
    tag=Tag.objects.all()
    detail=get_object_or_404(Blog,slug=slug)
    print(detail,'tagkar')
    return render(request,'video-page.html',{'detail':detail,'tag':tag})