from django.contrib import admin
from blog.models import CategoryModel,TagModel,SettingsModel,ContactModel,SosialMediaModel,BlogModel,CommentModel,LikeModel, AboutModel

admin.site.register(CategoryModel)
admin.site.register(TagModel)
admin.site.register(SettingsModel)
admin.site.register(ContactModel)
admin.site.register(SosialMediaModel)
admin.site.register(BlogModel)
admin.site.register(CommentModel)
admin.site.register(LikeModel)
admin.site.register(AboutModel)


