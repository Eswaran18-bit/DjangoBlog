from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.urls import reverse
import logging
from blog.models import Post 
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm 

def index(request):
    blog_name = "Eswaran Page"
    document_name ="Blog Page"
    """ Posts = [
        {
            "id": 1,
            "title": 'Getting Started with Django',
            "content": 'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It handles common web development tasks like authentication, routing, and database management, allowing developers to focus on building features instead of boilerplate code.'
        },
        {
            "id": 2,
            "title": 'Why React is Popular in Modern Web Apps',
            "content": 'React is a JavaScript library used to build fast and interactive user interfaces. It follows a component-based architecture, making code reusable, maintainable, and easier to test. React is widely used for single-page applications.'
        },
        {
            "id": 3,
            "title": 'Django vs Flask: Which One to Choose?',
            "content": 'Django is best suited for large-scale applications with built-in features, while Flask offers flexibility and simplicity for smaller projects. The choice depends on project size, complexity, and developer preference.'
        },
        {
            "id": 4,
            "title": 'Tips to Become a Better Python Developer',
            "content": 'To improve as a Python developer, focus on writing clean code, understanding core concepts, practicing problem-solving, learning frameworks like Django or FastAPI, and contributing to real-world projects.'
        }
    ] """
    Posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(Posts, 5)  # 5 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "blog/index.html",{"blog_title":blog_name,"document_title":document_name,"Posts":page_obj})

    
logger = logging.getLogger("Tester")

def detail(request, slug):
    logger.debug("Detail page accessed")
    logger.info(f"Post ID: {slug}")
    

    try: 
        PostData = Post.objects.get(slug=slug)
        relatedPost = Post.objects.filter(categories_id = PostData.categories_id ).exclude(id=PostData.id)
    except Post.DoesNotExist:
         raise Http404("Post Does not Exist")
                 
    return render(request, "blog/detail.html",{'Post':PostData,"relatedPost":relatedPost})
    #return HttpResponse(f"give the Python With React Join Please{Post_id}")

def old_url(request):
    return redirect(reverse("blog:new_url"))

def new_url(request):
    return HttpResponse("this new URL Page ")

def newAbout(request):
    return render(request,"blog/normal.html")

def contact(request):
    logger = logging.getLogger("Testing")
    success_message = None

    if request.method == "POST":
        formData = ContactForm(request.POST)

        if formData.is_valid():
            name = formData.cleaned_data['name']
            email = formData.cleaned_data['email']
            message = formData.cleaned_data['message']

            logger.debug(f"POST Data {name} {email} {message}")

            success_message = "Form submitted successfully!"
            formData = ContactForm()  # reset form
        else:
            logger.debug("Form validation failed")
    else:
        formData = ContactForm()

    return render(
        request,
        "blog/contact.html",
        {
            "form": formData,
            "success_message": success_message,
          
        }
    )

def about(request):
    return render(request,"blog/about.html")