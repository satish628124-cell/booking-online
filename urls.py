
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from bookstore.views import login, registration, logout, postProduct, getProducts, search, postComment, \
    likeOrDisLike, getRecentProducts, deleteProduct, getTrasactions, buyProduct, \
    buyProductAction, updatetrasaction, getuserinfo

urlpatterns = [

    path('admin/', admin.site.urls),

    path('',TemplateView.as_view(template_name = 'index.html'),name='login'),
    path('login/',TemplateView.as_view(template_name = 'index.html'),name='login'),
    path('loginaction/',login,name='loginaction'),

    path('registration/',TemplateView.as_view(template_name = 'registration.html'),name='registration'),
    path('regaction/',registration,name='regaction'),

    path('postproduct/',TemplateView.as_view(template_name = 'postproduct.html'),name='postproduct'),
    path('postproductaction/',postProduct,name='postproductaction'),

    path('getproducts/',getProducts,name='productlist'),
    path('search/',search,name='searchproducts'),
    path('postcomment/',postComment,name='postcomment'),
    path('likedislike/',likeOrDisLike,name='likedislike'),
    path('recentproducts/',getRecentProducts,name='recentproducts'),

    path('transactions/',getTrasactions,name='transactions'),

    path('buyproduct/',buyProduct,name='buyproduct'),
    path('buyproductaction/',buyProductAction,name='buyproductaction'),

    path('updatetransaction/',updatetrasaction,name='update transactions'),

    path('deleteproduct/',deleteProduct,name='deleteproducts'),
    path('getuser/',getuserinfo),

    path('logout/',logout,name='logout'),

]
