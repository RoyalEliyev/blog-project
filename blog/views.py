from django.shortcuts import render, redirect
from django.views.generic import View
from blog.models import BlogModel, AboutModel, ContactModel
from django.db.models import Q


class IndexView(View):
    def get(self, request, *args, **kwags):
        blogs = BlogModel.objects.all()
        context = {
           "blogs":blogs,
        }
        # query = request.GET.get("blog")
        # context = {}
        # if query:
        #     blogs = blogs.filter(
        #         Q(name__contains=query) | Q(about__contains=query)
        #         )
        #     abouts = []
        #     for blog in blogs:
        #         abouts.append(blog.about)

        #     Abouts = []
        #     for about in abouts:
        #         About = about.replace(query, "<span style='background-color:yellow;'>" + query +"</span>")
        #         Abouts.append(About)
        #     context["Abouts"] = Abouts

        # context["blogs"] = blogs
        # context["query"] = query
        return render(request, "index.html", context)
    
    # def post(self, request, *args, **kwargs):
    #     name = request.POST.get("name")
    #     pub_date = request.POST.get("pub_date")
    #     about = request.POST.get("about")
    #     poster = request.POST.get("posters")
    #     BlogModel.objects.create(
    #         user = request.user,
    #         name = name,
    #         pub_date = pub_date,
    #         about = about,
    #         poster = poster,
    #     )
    #     return redirect("about")

class AboutView(View):
    def get(self, request, *args, **kwags):
        abouts = AboutModel.objects.all()
        context = {
            "about":abouts,
        }
        return render(request, "about.html", context)
    # def post(self, request, *args, **kwags):
    #     name = request.POST.get("name")
    #     title = request.POST.get("title")
    #     text = request.POST.get("text")
    #     AboutModel.objects.create(
    #         name = name,
    #         title = title,
    #         text = text,
    #     )
    #     return redirect("about")
    
class PostView(View):
    def get(self, request, *args, **kwags):
        posts = BlogModel.objects.filter(
            user = request.user,
        )
        context = {
            "posts":posts,
        }
        return render(request, "post.html", context)
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        pub_date = request.POST.get("pub_date")
        about = request.POST.get("about")
        poster = request.POST.get("posters")
        BlogModel.objects.create(
            user = request.user,
            name = name,
            pub_date = pub_date,
            about = about,
            poster = poster,
        )
        return redirect("index")
    
class ContactView(View):
    def get(self, request, *args, **kwags):
        contacts = ContactModel.objects.all()
        context = {
            "contacts":contacts,
        }
        return render(request, "contact.html", context)
    def post(self, request, *args, **kwags):
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        BlogModel.objects.create(
            user = request.user,
            name = name,
            email = email,
            phone_number = phone_number,
            subject = subject,
            message = message,
        )
        return redirect("post")

class DetailView(View):
    def get(self, request, *args, **kwags):
        return render(request, "detail.html")
    
class BlogView(View):
    def get(self, request, *args, **kwags):
        return render(request, "blog.html")