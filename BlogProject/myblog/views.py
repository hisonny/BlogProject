from django.shortcuts import render,redirect,HttpResponse
from .models import Album,Photo,Blog

# Create your views here.

def home(request):

    return render(request, template_name='blog/index.html')

def list(request):
    album = Album.objects.filter(author=request.user)
    return render(request, template_name='blog/list.html', context={"albums": album})

def delete(request,pk):
   blog = Blog.objects.get(pk=pk)
   blog.delete()
   return redirect(myblog)

def update(request,pk):
    if request.method == 'GET':
        blog = Blog.objects.get(pk=pk)
        return render(request,'blog/update.html',{'blog':blog})
    elif request.method == 'POST':
        blog = Blog.objects.get(pk=pk)
        data = request.POST
        blog.title = data.get('title')
        blog.maincontent = data.get('maincontent')
        blog.description = data.get('description')
        blog.save()
        return redirect(myblog)


def create_blog(request):
    if request.method == 'GET':
        return render(request,'blog/create_blog.html')
    elif request.method =='POST':
        data = request.POST
        title = data.get('title')
        maincontent = data.get('maincontent')
        description = data.get('description')
        blog = Blog(author=request.user,title=title,maincontent=maincontent,description=description)
        blog.save()
        return redirect(myblog)

def myoneblog(request,pk):
    blog = Blog.objects.get(pk=pk)

    return render(request, 'blog/show_myoneblog.html', {'blog':blog})

def myblog(request):
    blog = Blog.objects.filter(author=request.user)
    return render(request, template_name='blog/myblog.html', context={"blogs": blog})

def alloneblog(request,pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog/show_alloneblog.html', {'blog':blog})

def allblog(request):
    blog = Blog.objects.all()
    return render(request, template_name='blog/allblog.html', context={"blogs": blog})

def detail(request):
    photos = Photo.objects.filter(author=request.user)
    return render(request,'blog/show_photo.html',{'photos':photos})

def create_question(request):
    if request.method == 'GET':
        return render(request,'blog/create.html')
    elif request.method == 'POST':
        # 获取提交的POST数据
        data = request.POST
        title = data.get('title')
        # print(title)
        description = data.get('description')
        f = request.FILES['img']
        question = Album(author=request.user,title=title,description=description,img=f)
        question.save()
        return redirect(home)