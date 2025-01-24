"""
URL configuration for reservations project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

#Set the django admin site header and title
# Text to put at the top of the admin index page.
admin.site.index_title = "Projet Réservations"
# Text to put in each page's <div id="site-name">.
admin.site.site_header = "Projet Réservations HEADER"
# Text to put at the end of each page's <title>.
admin.site.site_title = "Spectacles"

#Set auth views header and title
auth_views.PasswordResetView.extra_context = {"site_header": admin.site.site_header,
                           "site_title": admin.site.site_title,
                           "index_title": admin.site.index_title,}
auth_views.PasswordResetDoneView.extra_context = {"site_header": admin.site.site_header,
                           "site_title": admin.site.site_title,
                           "index_title": admin.site.index_title,}
auth_views.PasswordResetConfirmView.extra_context = {"site_header": admin.site.site_header,
                           "site_title": admin.site.site_title,
                           "index_title": admin.site.index_title,}
auth_views.PasswordResetCompleteView.extra_context = {"site_header": admin.site.site_header,
                           "site_title": admin.site.site_title,
                           "index_title": admin.site.index_title,}
auth_views.PasswordChangeView.extra_context = {"site_header": admin.site.site_header,
                           "site_title": admin.site.site_title,
                           "index_title": admin.site.index_title,}
auth_views.PasswordChangeDoneView.extra_context = {"site_header": admin.site.site_header,
                           "site_title": admin.site.site_title,
                           "index_title": admin.site.index_title,}

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls'),),
    path('catalogue/', include('catalogue.urls')),
    path('admin/', admin.site.urls),
]

