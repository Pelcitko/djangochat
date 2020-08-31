from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('chat/', include('chat.api.urls', namespace='chat')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]


# schéma
schema = get_schema_view(
    title="Chat API",
    description="""Chat API description""",
    public=True
)

# api dokumentace
title='API Documentation'
description="""
This application was created for the WEAP course. Originally according to a tutorial on [YouTube](https://www.youtube.com/playlist?list=PLLRM7ROnmA9EnQmnfTgUzCfzbbnc-oEbZ).
"""


urlpatterns += [
    path('schema/', schema),
    path('docs/', include_docs_urls(title, description)),
]


# from rest_framework.renderers import DocumentationRenderer
# class CustomRenderer(DocumentationRenderer):
#     languages = ['python', 'ruby', 'go']