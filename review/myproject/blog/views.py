from django.shortcuts import redirect,render, get_object_or_404
from .models import Blog,Intro
from django.utils import timezone
from .forms import BlogUpdate
# Create your views here.
def hello(request):
    return render(request,'hello.html')

#개발자 소개글
#1단계 간단한 글
#2단계 이미지 붙여보기

def intro(request):
    intro = Intro.objects
    return render(request,'intro.html',{'intro':intro})

def blog(request):
    blogs = Blog.objects
    return render(request,'blog.html',{'blogs':blogs})

def new(request):     
    return render(request,'new.html')


def create(request):
    blog = Blog()#Blog의 객체를 하나 생성
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    #image
    blog.images  = request.FILES['images']
    blog.pub_date = timezone.datetime.now()
   
    blog.save()
    return redirect('/blog/'+str(blog.id))

'''
def create(request):
    blog = Blog()#Blog의 객체를 하나 생성
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
   
    blog.save()
    return redirect('/blog/'+str(blog.id))
'''
def delete(request,blog_id):
    Blog.objects.get(id=blog_id).delete()
    return redirect('/')

def update(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    if request.method =='POST':
        form = BlogUpdate(request.POST)
            
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.body= form.cleaned_data['body']
            blog.images = form.cleaned_data['images']
            blog.images = request.FILES['images']
            blog.pub_date = timezone.datetime.now()
            blog.save()#DB에 반영하기
            return redirect('/blog/'+str(blog.id))
            #redirect를 호출해서 객채를 호출해서 detail로 이동

    else:
        form = BlogUpdate(instance = blog)
        return render(request,'update.html',{'form':form})




def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html',{'blog' : blog_detail})