from django.contrib import admin
from .models import Blog,ContentImageBlog,ContentTextBlog
# Register your models here.

admin.site.register(Blog)
admin.site.register(ContentImageBlog)
admin.site.register(ContentTextBlog)

