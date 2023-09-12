from django.contrib import admin
from django.http.request import HttpRequest
from blog.models import CategoryModel,TagModel,SettingsModel,ContactModel,SosialMediaModel,BlogModel,CommentModel,LikeModel, AboutModel

admin.site.register(CategoryModel)
admin.site.register(TagModel)
# admin.site.register(SettingsModel)
@admin.register(SettingsModel)
class SettingsModel(admin.ModelAdmin):
    def has_add_permission(self, request) -> bool:
        if self.model.objects.count() >= 1:
            return False
        return super(SettingsModel, self).has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None) -> bool:
        if self.model.objects.count() <= 1:
            return False
        return super(SettingsModel, self).has_delete_permission(request, obj)

admin.site.register(ContactModel)
admin.site.register(SosialMediaModel)
admin.site.register(BlogModel)
admin.site.register(CommentModel)
admin.site.register(LikeModel)
admin.site.register(AboutModel)


