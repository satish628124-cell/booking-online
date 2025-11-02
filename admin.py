from django.contrib import admin

# Register your models here.
from bookstore.models import RegistrationModel, ProductModel,CommentModel,LikeOrDisLikeModel

admin.site.register(RegistrationModel)
admin.site.register(ProductModel)
admin.site.register(CommentModel)
admin.site.register(LikeOrDisLikeModel)
