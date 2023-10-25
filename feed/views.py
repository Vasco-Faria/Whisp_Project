from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView,DeleteView,TemplateView
from django.contrib import messages

from followers.models import Follower
from .models import Post,Comment,Like
from .forms import PostForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

class HomePage(TemplateView):
    template_name = "feed/homepage.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        posts = Post.objects.all().order_by('-id')[:60]
        context['posts'] = posts
        context['form'] = PostForm()  
        return context

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(
                text=form.cleaned_data['text'],
                image=form.cleaned_data['image'],
                video=form.cleaned_data['video'],
                author=request.user
            )
            post.save()

            
            return redirect('/')
        posts = Post.objects.all().order_by('-id')[:60]
        return render(request, 'feed/homepage.html', {'form': form, 'posts': posts})

class DetailPostView(DetailView):
    http_method_names = ['get']
    template_name = "feed/detail.html"
    model = Post
    context_object_name = "post"
    
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    # Verificar se o usuário já deu "like" e excluir o "like" se necessário
    if not created:
        like.delete()

    post_likes = post.likes.count()

    # Exemplo de retorno de JSON com o status do "like"
    response_data = {'liked': created, 'like_count': post_likes}
    return JsonResponse(response_data)
    
class CreateNewPost(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "feed/new_post.html"
    fields = ['text','image','video']
    success_url = '/'

    def dispatch(self, request,*args,**kwargs):
        self.request = request
        return super().dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        
        return super().form_valid(form)

    def post(self, request,*args,**kwargs):
        post = Post.objects.create(
            text = request.POST.get("text"),
            author = request.user,
            image=request.FILES.get("image"), 
            video=request.FILES.get("video"), 
        )
        messages.add_message(self.request, messages.SUCCESS, "Your Post Is Submitted !!")
        return render(
            request,
            "includes/post.html",
            {
                'post':post,
                "show_detail_link" : True
            },
            content_type="application/html"
        )
    
    
class DeletePost(DeleteView):
    model = Post
    template = 'feed/post_confirm_delete.html'
    success_url = '/'
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        messages.add_message(self.request, messages.SUCCESS, "Your Post Is Deleted !!")
        return super().dispatch(request, *args, **kwargs)
    
    
    
class FollowingHomePage(TemplateView):
    http_method_names = ['get']
    template_name = "feed/followpost.html"
    def get_context_data(self, *args, **kwargs):
        friend_posts = ''
        context = super().get_context_data(*args, **kwargs)
        following = list(
            Follower.objects.filter(followed_by=self.request.user).values_list('following', flat=True)
        )
        if following:
            friend_posts = Post.objects.filter(author__in=following).order_by('-id')[0:60]
                
        context['friend_posts'] = friend_posts
        return context


class MyPostHomePage(TemplateView):
    http_method_names = ['get']
    template_name = "feed/detail.html"
    model = Post
    context_object_name = "posts"
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        posts = Post.objects.filter(author=self.request.user).order_by('-id')[0:60]    
        context['posts'] = posts
        return context