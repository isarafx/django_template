from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Blog(models.Model):
    slug = models.SlugField(max_length=120, unique=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_pub = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    cover_pic = models.ImageField(upload_to='blogcover/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('singleblog', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

class Staff(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.CharField(max_length=25)
    pic = models.ImageField(upload_to='staff_pic/')
    description = models.TextField()

    def __str__(self):
        return self.name

class ContactUs(models.Model):
    name = models.CharField(max_length=80, help_text="Name of the sender")
    subject = models.CharField(max_length=100)
    message = models.TextField()
    cont_email = models.EmailField()

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" + self.cont_email