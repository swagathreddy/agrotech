from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('farmer/', views.farmer_view, name='farmer'),
    path('tourists/', views.tourists_view, name='tourists'),
    path('register/', views.register_farmer, name='register_farmer'),
    path('login/', views.login, name='login'),  # URL mapping for login page
    path('lendafarm/', views.lend_a_farm, name='lend_a_farm'),
    path('tourists/centres/', views.centres, name='centres'),
     path('blog/', views.blog_view, name='blog'),
     path('writeblog/', views.write_blog_view, name='write_blog'),
     path('courses/', views.courses_view, name='courses'),
     path('products/', views.products_view, name='products'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
