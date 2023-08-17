from django.urls import include, path

from app1 import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
   path('api-auth/', include('rest_framework.urls')),
   path('createAccount',views.createAccount.as_view(),name='create_data'),
   path('authlog',views.authlog.as_view(),name='authlog'),
   
  

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)