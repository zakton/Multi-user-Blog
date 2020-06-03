from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from autoslug import AutoSlugField

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published', restriction='public')

'''
class RestrictedManager(models.Manager):
    def get_queryset(self):
        return super(RestrictedManager, self).get_queryset().filter(status='published', restriction='restricted', subscribers__username=self.request.user)
'''

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    RESTRICTION_CHOICES = (
        ('restricted', 'Restricted'),
        ('public', 'Public'),
    )
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from=('title'), unique_with=('publish'))
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    restriction = models.CharField(max_length=10,
                                choices=RESTRICTION_CHOICES,
                                default='restricted')
    subscribers = models.ManyToManyField(User)

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    #restricted = RestrictedManager()

    ### zakton
    # must have a subscriber field, i.e. subscribers allowed to view this post ... many to many


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
