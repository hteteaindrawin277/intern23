# from django.views import generic
# from .models import Post
#
# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'
#
# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

'''def index(request):
    if request.method=="POST":
        files=request.FILES.getlist('files')
        file_list=[]
        for file in files:
            new_file=Files(file=file)
            new_file.save()
            file_list.append(new_file.file.url)


        #new_file=Files(file=request.FILES['name'])
        #new_file.save()
        return  render(request,'home.html',{'new.urls':file_list})
    else:
        return render(request,'home.html')

'''

from django.shortcuts import render, get_object_or_404
from .models import Post, PostImage
from django.views import generic
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


# class DetailView(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'post_detail.html', {
        'post':post,
        'photos':photos
    })




