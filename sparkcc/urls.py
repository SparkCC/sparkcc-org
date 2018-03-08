from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from mezzanine.blog.views import blog_post_list

admin.autodiscover()

urlpatterns = [
    url("^admin/", include(admin.site.urls)),
    url("^$", blog_post_list, name="home"),
    url("^", include("mezzanine.urls")),
]

handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
