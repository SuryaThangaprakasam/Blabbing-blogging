from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import *
from .forms import CustomUserForm,CustomUserChangeForm
from django.contrib.auth import authenticate, login, logout ,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

def index(request):
    blogs = Blog.objects.all()
    return render(request,'index.html', {'blogs': blogs})

def register(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    else:
        form = CustomUserForm()
        if request.method == 'POST':
            form = CustomUserForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Registered Successfully")
                return redirect('/login')
        return render(request, 'register.html', {'form':form})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=username, password=pwd)
            if user is not None:
                if user.is_blocked:
                    messages.error(request, "Your account has been temporarily blocked")
                else:
                    login(request, user)
                    messages.success(request, "Logged in Successfully")
                    return redirect('/profile')
            else:
                messages.error(request, "Invalid Credentials")
    return render(request, 'login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Successfully")
    return redirect('/')

def profile(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(author=request.user)
        return render(request, 'profile.html', {'blogs': blogs})
    else:
        messages.success(request, "Login to access profile")
        return redirect('/login')

def update_profile(request):
    if request.user.is_authenticated:
        form = CustomUserChangeForm(instance = request.user)
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Updated Successfully")
                return redirect('/profile')
            else:
                messages.warning(request, f"{form.errors}")
        return render(request, 'update_profile.html', {'form':form})
    else:
        return redirect('/')

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important: Keeps the user logged in after password change
                messages.success(request, 'Your password was successfully updated!')
                return redirect('/profile')  # Replace 'profile' with your desired redirect URL
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {'form': form})
    else:
        return redirect('/')

def blog_editor(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            author = request.user
            title = request.POST.get('title')
            content = request.POST.get('content')
            blog_img = request.FILES.get('blog_img') #always get by input name
            Blog.objects.create(author=author, title=title, content=content, blog_img=blog_img)
            messages.success(request, "Blog created successfully")
            return redirect('/myblogs')  # Redirect to a blog list page or success page
        return render(request, 'blog_editor.html')
    else:
        messages.error(request, "Login to Create blog")
        return redirect('/login')

def edit_blog(request, b_id):
    the_blog = Blog.objects.get(id=b_id)
    if request.user == the_blog.author:
        if request.method == 'POST':
            author = request.user
            title = request.POST.get('title')
            content = request.POST.get('content')
            blog_img = request.FILES.get('blog_img')

            the_blog.author = author
            the_blog.title = title
            the_blog.content = content
            if blog_img: #update img only if new file is provided
                the_blog.blog_img = blog_img
            the_blog.save()

            messages.success(request, "Blog Updated Successfully")
            return redirect(f'/theblog/{the_blog.id}')
        return render(request, 'edit_blog.html', {'the_blog':the_blog})
    else:
        messages.warning(request, "Only the author can edit their blogs")
        return redirect(f'/theblog/{the_blog.id}')
        
def my_blogs(request):
    blogs = Blog.objects.filter(author=request.user)
    return render(request, 'my_blogs.html', {'blogs': blogs})

def the_blog(request, id):
    blog = Blog.objects.get(id=id)
    comment = Comment.objects.filter(blog=blog)
    return render(request, 'the_blog.html', {'blog':blog, 'comment':comment})

def delete_blog(request, b_id):
    if request.user.is_authenticated:
        blog = Blog.objects.get(id=b_id)
        blog.delete()
        messages.success(request, "Blog deleted successfully")
        return redirect("/myblogs")
    else:
        messages.warning(request, "Need access to delete a blog")
        return redirect('/login')

def add_comments(request, b_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            author = request.user
            blog = get_object_or_404(Blog, id=b_id)
            comment_text = request.POST.get('comment_text')
            if comment_text:
                Comment.objects.create(author=author, blog=blog, comment_text=comment_text)
                messages.success(request, "Comment added successfully")
            else:
                messages.error(request, "Comment cannot be empty")
            return redirect(f'/theblog/{b_id}')
    else:
        messages.error(request, "Login to add comment")
        return redirect('/login')

