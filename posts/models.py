from django.db import models
from cloudinary.models import CloudinaryField

#from django_forum.posts.views import likes


# Create your models here.


class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=100, db_index=True, default='Anonymous'
    )

    body = models.CharField(
        'Body', blank=True, null=True, max_length=1400, db_index=True
    )

    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )

    likes = models.PositiveIntegerField(
        'like', default=0, db_index=True, blank=True
    )

    image = CloudinaryField('image', blank= True, db_index=True)

    def __str__(self):
            return self.name
