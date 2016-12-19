from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib import messages

def count_rate(like, dislike):
    rate = 0
    if like > 5:
        star = like*2 - dislike
        if star < 0 or star == 0 :
            rate = 0
        elif star > 0 and star < 2:
            rate = 1
        elif star >= 2 and star < 4:
            rate = 2
        elif star >= 4 and star < 6:
            rate = 3
        elif star >= 6 and star < 8:
            rate = 4
        elif star >= 8 :
            rate = 5
        else :
            rate = 5
    else :
        rate = 0
    return rate

# Create your models here.
class PostType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):              # __unicode__ voi Python 2
        return self.name
    
class PostSubType(models.Model):
    main_type = models.ForeignKey(PostType)
    name = models.CharField(max_length=100)
    def __str__(self):              # __unicode__ voi Python 2
        return  self.name  + " - " + self.main_type.name
    
# class FollowList(models.Model):l
#     user = models.ForeignKey(User)
#     follow_user = models.ForeignKey(User)

class Post(models.Model):
    author = models.ForeignKey(User)
    sub_type = models.ForeignKey(PostSubType)
    title = models.CharField(max_length=200)
    description = models.TextField(default=' ', null=True)
    image_description = models.ImageField(upload_to="image_description/%Y/%m/%d")
    content = RichTextUploadingField()
    commit_date = models.DateTimeField('Date commit')
    def __str__(self):              # __unicode__ voi Python 2
        return self.title 
    
    def was_commit_recently(self):
        return self.commit_date >= timezone.now() - datetime.timedelta(days=1)
    was_commit_recently.admin_order_field = 'commit_date'
    was_commit_recently.boolean = True
    was_commit_recently.short_description = 'Published recently?'
    
    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs) # Call the "real" save() method.
        list_post_accpect = PostAccept.objects.filter(post=self.pk)
        if len(list_post_accpect)  == 0:
            new_post_accept = PostAccept.objects.create(post=self, is_accept=False)
            new_post_accept.save()
    def change(self, *args, **kwargs):
        super(Post, self).change(*args, **kwargs) # Call the "real" change() method.
        list_post_accept = PostAccept.objects.filter(post=self.pk)
        if len(list_post_accept)  == 0:
            new_post_accept = PostAccept.objects.create(post=self, is_accept=False)
            new_post_accept.save()
    def delete(self, *args, **kwargs):
        super(Post, self).delete(*args, **kwargs) # Call the "real" delete() method.
        list_post_accpect = PostAccept.objects.filter(post=self.pk)
        for post in list_post_accpect :
            post.delete()
            
class PostAccept(models.Model):
    post = models.ForeignKey(Post)
    is_accept = models.BooleanField(default=False)
    is_hot = models.BooleanField(default=False)
    accept_date = models.DateTimeField(default=timezone.now())
    def __str__(self):              # __unicode__ voi Python 2
        return self.post.title + " - " + self.post.author.username
    def save(self, *args, **kwargs):
        super(PostAccept, self).save(*args, **kwargs) # Call the "real" change() method.
        if self.is_accept == True:
            list_post_accepted = PostAccepted.objects.filter(relate_post_accept=self.pk)
            if len(list_post_accepted) == 0:
                new_post_accepted = PostAccepted.objects.create(relate_post_accept=self,
                                                                is_hot = self.is_hot,
                                                                author=self.post.author,
                                                                sub_type=self.post.sub_type,
                                                                title=self.post.title,
                                                                description=self.post.description,
                                                                image_description=self.post.image_description,
                                                                content=self.post.content,
                                                                commit_date=self.post.commit_date,
                                                                accept_date=self.accept_date
                                                                )
                new_post_accepted.save()
            else :
                for post_accepted in list_post_accepted:
                    post_accepted.is_hot = self.is_hot
                    post_accepted.author = self.post.author
                    post_accepted.sub_type = self.post.sub_type
                    post_accepted.title = self.post.title
                    post_accepted.description = self.post.description
                    post_accepted.image_description = self.post.image_description
                    post_accepted.content = self.post.content
                    post_accepted.commit_date = self.post.commit_date
                    post_accepted.accept_date = self.accept_date
                    post_accepted.save()
        

class Tournaments(models.Model):
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Team(models.Model):
    tournament = models.ForeignKey(Tournaments)
    icon = models.ImageField(upload_to="icon_team")
    name = models.CharField(max_length=400)
    def __str__(self):
        return self.name
class LiveNews(models.Model):
    host = models.ForeignKey(Team, related_name='host_team')
    quest = models.ForeignKey(Team, related_name='quest_team')
    round = models.IntegerField(null=True)
    host_point = models.IntegerField(null=True)
    quest_point = models.IntegerField(null=True)
    pub_time = models.DateTimeField(null=True)
    def save(self, *args, **kwargs):
        objects=LiveNews.objects.all()
        if objects.count() == 4:
            objects[0].delete()
        super(LiveNews, self).save(*args, **kwargs)
    def was_commit_recently(self):
        return self.pub_time >= timezone.now() - datetime.timedelta(days=0.08)
    was_commit_recently.admin_order_field = 'pub_time'
    was_commit_recently.boolean = True
    was_commit_recently.short_description = 'Published recently?'
    
class Music(models.Model):
    link_download = models.CharField(max_length=300)
    name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=2000)
    def __str__(self):
        return self.name
    
class PostAccepted(models.Model):
    relate_post_accept = models.ForeignKey(PostAccept)
    is_hot = models.BooleanField(default=False)
    author = models.ForeignKey(User)
    sub_type = models.ForeignKey(PostSubType)
    title = models.CharField(max_length=200)
    description = models.TextField(default=' ', null=True)
    image_description = models.ImageField()
    content = RichTextUploadingField()
    commit_date = models.DateTimeField('Date commit')
    accept_date = models.DateTimeField('Date accept')
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        super(PostAccepted, self).save(*args, **kwargs) # Call the "real" save() method.
        list_post_rate = PostRate.objects.filter(post=self)
        if len(list_post_rate) == 0:
            new_post_rate = PostRate.objects.create(post=self)
            new_post_rate.save()
            
    def delete(self, *args, **kwargs):
        super(PostAccepted, self).delete(*args, **kwargs) # Call the "real" delete() method.
        list_post_rate = PostRate.objects.filter(post=self)
        for post in list_post_rate :
            post.delete()
class PostRate(models.Model):
    post = models.ForeignKey(PostAccepted)
    num_like = models.IntegerField(default=0)
    num_dislike = models.IntegerField(default=0)
    def rate(self):
        return count_rate(self.num_like, self.num_dislike)
    rate.admin_order_field = 'Rate'
    def __str__(self):
        return self.post.title 
class Infor(models.Model):
    tumble = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    youtube = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    email_password = models.CharField(max_length=200)
    page_infor = models.CharField(max_length=2000)
    def __str__(self):
        return "Page Information"
    def delete(self, *args, **kwargs):
        return None
        super(Infor, self).delete(*args, **kwargs) # Call the "real" delete() method.
