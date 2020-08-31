from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title="Chat API", description="Chat API description", public=True)

urlpatterns = [
    path('schema/', schema_view),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('chat/', include('chat.api.urls', namespace='chat')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title='API doc')),
    path('', TemplateView.as_view(template_name='index.html')),
    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
    # path('docs/', include_docs_urls(title='API doc', public=False)),
]


# from rest_framework.renderers import DocumentationRenderer
# class CustomRenderer(DocumentationRenderer):
#     languages = ['python', 'ruby', 'go']