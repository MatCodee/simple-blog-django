from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_mod = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return self.title


class ContentTextBlog(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return  "Content Text " + self.blog.title


class ContentImageBlog(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return  "Content Image " + self.blog.title