from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


# Create your models here.
class Author(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)

    def update_rating(self):
        for post in Post.objects.filter(author=self):
            self.rate += post.rate * 3
            for comment in Comment.objects.filter(post=post):
                self.rate += comment.rate
        for comment in Comment.objects.filter(user=self.user):
            self.rate += comment.rate
        self.save()


class Category(BaseModel):
    category_name = models.CharField(max_length=16, unique=True)


class Post(BaseModel):
    TYPES_LIST = (('AR', 'article'), ('NW', 'news'))

    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default="UNKNOWN")
    type = models.CharField(max_length=8, choices=TYPES_LIST)
    create_time = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.TextField()
    text = models.TextField()
    rate = models.IntegerField(default=0)

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()

    def preview(self):
        return f"{self.text[:125]}..."


class PostCategory(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    create_time = models.DateField(auto_now_add=True)
    rate = models.IntegerField(default=0)

    def like(self):
        self.rate += 1
        self.save()

    def dislike(self):
        self.rate -= 1
        self.save()