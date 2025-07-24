from django.shortcuts import render
from .models import Post
from django.core.paginator import EmptyPage, PageNotAnInteger,    Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .forms import EmailPostForm
# Create your views here.
def post_list(request):
    post_list = Post.published.all()
    # pagination of 5 posts per page
    paginator = Paginator(post_list,4)
    page_number = request.GET.get('page',1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )

# shows details of each post
def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day 
    )    
    return render(
        request,
        'blog/post/detail.html',
        {'post':post}
    )

# using class to view
# class PostListView(ListView):
#     """ Alternative post list view """
#     queryset = Post.published.all()
#     context_object_name = "posts"
#     paginate_by = 4
#     template_name = 'blog/post/list.html'

# email validation
def post_share(request, post_id):
    # to retrieve posts by their id
    post = get_object_or_404(
        Post,
        id = post_id,
        status = Post.Status.PUBLISHED
    )
    
    if request.method == "POST":
        # submitting a form
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = EmailPostForm()
        return render(
            request,
            "blog/post/share.html",
            {
                'post': post,
                'form': form
            }
        )    