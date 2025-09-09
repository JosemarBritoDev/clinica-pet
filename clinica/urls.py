from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', include('clinica.base.urls')),  # Isso aplica o prefixo /base/ às rotas da app
]
