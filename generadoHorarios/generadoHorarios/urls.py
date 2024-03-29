"""generadoHorarios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from pages.urls import pages_patterns #se importa la tupla de pages
from institucion.urls import planteles_patterns
from django.conf import settings

urlpatterns = [
    #admin paths
    path('admin/', admin.site.urls),
    #core paths
    path('',include('core.urls')),
    #aulas
    path('insti/',include(planteles_patterns)),
    #pages paths
    path('mate/',include(pages_patterns)),
    #Paths de auth
    path('accounts/',include('django.contrib.auth.urls')),
    path('usuarios/',include('usuarios.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)#SI TENEMOS EL DEBUG EN TRUE TODOS LOS ARCHIVOS MEDIA IRAN A BUSCARLOS EN LA MEDIA ROOT QUE SE ENCUENTRA EN SETTINGS
