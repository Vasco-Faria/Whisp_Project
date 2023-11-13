from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView,DeleteView,TemplateView
from django.contrib import messages
from notifications.signals import notify
from django.db.models import Q

from followers.models import Follower
from .models import Post,Like,Comment
from .forms import PostForm,CommentForm, SearchForm


class HomePage(TemplateView):
    template_name = "feed/homepage.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        search_query = self.request.GET.get('search', '')
        search_form = SearchForm(initial={'search': search_query})
        
        if search_query:
            
            posts = Post.objects.filter(Q(text__icontains=search_query)).order_by('-id')[:60]
        else:
            
            posts = Post.objects.all().order_by('-id')[:60]
            
        context['posts'] = posts
        context['form'] = PostForm()
        context['search_form'] = search_form
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
            messages.add_message(self.request, messages.SUCCESS, "Your Post Is Submitted !!")

            notify.send(request.user, recipient=request.user, verb=f"O seu post foi realizado com sucesso.")
        
            return redirect('/')
        posts = Post.objects.all().order_by('-id')[:60]
        
        return render(request, 'feed/homepage.html', {'form': form, 'posts': posts})
    

def like_post(request):
    user=request.user
    if request.method=="POST":
        post_id=request.POST.get('post_id')
        post_obj=Post.objects.get(id=post_id)
        
        if user in post_obj.likes.all():
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        post_owner = post_obj.author
        
        notify.send(request.user, recipient=post_owner, verb=f"Your post has received a like by {user.username} .")
        
        like.save()
                
    post_detail_url = reverse('feed:detail', args=[post_id])

    return redirect(post_detail_url)

class DetailPostView(DetailView):
    http_method_names = ['get', 'post']
    template_name = "feed/detail.html"
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = context['post']

        comments = Comment.objects.filter(post=post)

        context['comments'] = comments
        context['comment_form'] = CommentForm()

        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        print('Reached post method')  

        if comment_form.is_valid():
            print('Form is valid') 
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = self.get_object()
            new_comment.save()
            messages.add_message(self.request, messages.SUCCESS, "Your Comment is Submitted !!")

        post_owner = self.get_object().author 
        
        notify.send(request.user, recipient=post_owner, verb=f"Your post has received a comment by {request.user.username} .")

        return redirect(f'/{new_comment.post.id}')

    
    
    


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
    template_name = 'feed/post_confirm_delete.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        messages.success(self.request, "Your Post Is Deleted !!")
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')

        if action == 'Yes':
            user = request.user
            post = self.get_object()
            post_owner = post.author
            notify.send(user, recipient=post_owner, verb=f"Your post was deleted by the admin, {user.username} .")
            post.delete()  # Delete the post

        return HttpResponseRedirect(self.success_url)


        
    

class DeleteComment(DeleteView):
    model = Comment
    template_name = 'feed/comment_confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        messages.add_message(self.request, messages.SUCCESS, "Your Comment Is Deleted !!")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        post_id = self.object.post_id 
        return f'/{post_id}'
    
    
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
        comments = Comment.objects.filter()
        context['comments']=comments
        context['posts'] = posts
        return context