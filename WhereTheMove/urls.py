"""WhereTheMove URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'What\'s The Move API'
API_DESCRIPTION = 'A Web API for connecting our amazing site to different client side.'
schema_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('Events.urls')),
    path('users/<username>/<pk>',user_views.user_events, name="user_events"),
    path('register/', user_views.register, name="register"),
    path('profile/', user_views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('Events.urls')),
    path('api/v1/', include('api.urls')),

    #third party
    path('tinymce/', include('tinymce.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')), 
    path('api-auth/', include('rest_framework.urls')), 
    path('api/v1/rest-auth/', include('rest_auth.urls')), 
    path('api/v1/rest-auth/registration/', # new
        include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('swagger-docs/', schema_view), # new

    #passowrd reset
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='users/change-password.html',
            success_url = '/'
        ),
        name='change_password'
        ),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), 
        name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
        name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), 
        name='password_reset_complete'),
    
    #comments
    path('comments/', include('django_comments_xtd.urls')),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.sites.AdminSite.index_title = 'WhereTheMoveIndex'
admin.site.site_header = "WTM|Admin" 

