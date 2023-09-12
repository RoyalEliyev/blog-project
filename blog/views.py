from django.shortcuts import render, redirect
from django.views.generic import View
from blog.models import BlogModel, AboutModel, ContactModel, SosialMediaModel, CommentModel
from django.db.models import Q
from django.http import Http404

class IndexView(View):
    def get(self, request, *args, **kwags):
        blogs = BlogModel.objects.all()
        sosial_medias = SosialMediaModel.objects.all()
        context = {
           "blogs":blogs,
           "sosial_medias":sosial_medias,
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
        sosial_medias = SosialMediaModel.objects.all()
        context = {
            "about":abouts,
            "sosial_medias":sosial_medias,
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
    def get(self, request, id, *args, **kwargs):
        post = BlogModel.objects.get(id=id)
        sosial_medias = SosialMediaModel.objects.all()
        context = {
            "post":post,
            "sosial_medias":sosial_medias,
        }
        return render(request, "post.html", context)
    
    def post(self, request,id, *args, **kwargs):
        blog = BlogModel.objects.get(id=id)
        content = request.POST.get("content")  

        CommentModel.objects.create(
            user = request.user,
            blog =blog,
            content=content,
        )
        return redirect("post", id=id)
    
class ContactView(View):
    def get(self, request, *args, **kwags):
        blogs = ContactModel.objects.all()
        sosial_medias = SosialMediaModel.objects.all()
        context = {
            "blogs":blogs,
            "sosial_medias":sosial_medias,
        }
        return render(request, "contact.html", context)
    def post(self, request, *args, **kwags):
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        ContactModel.objects.create(
            user = request.user,
            name = name,
            email = email,
            phone_number = phone_number,
            subject = subject,
            message = message,
        )


class BlogView(View):
    def get(self, request, *args, **kwags):
        blogs = BlogModel.objects.all()
        sosial_medias = SosialMediaModel.objects.all()
        context = {
            "blogs":blogs,
            "sosial_medias":sosial_medias,
        }
        return render(request, "blog.html", context)
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

    

class SosialMedia(View):
    def get(self, request, *args, **kwags):
        sosial_medias = SosialMediaModel.objects.all()
        context = {
            "sosial_medias":sosial_medias,
        }
        return render(request, "base.html", context)
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        link = request.POST.get("link")

        SosialMedia.objects.create(
            name = name,
            link = link,
        )



    