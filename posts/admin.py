from django.contrib import admin

from .models import Post, PostAccept, PostRate, PostSubType, PostType, PostAccepted, LiveNews, Music, Tournaments, Team, Infor

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'author', 'sub_type','was_commit_recently') # thu tu hien thi cac attribute 
    list_filter = ['commit_date'] # bo loc
    search_fields = ['title','author__username'] #bo search
class PostAcceptAdmin(admin.ModelAdmin):
    list_display = ('get_title','get_author','get_commit_date','is_accept', 'is_hot')
    def get_title(self, obj):
        return obj.post.title
    get_title.short_description = "Title"
    def get_author(self, obj):
        return obj.post.author.username
    get_author.short_description = "Author"
    def get_commit_date(self, obj):
        return obj.post.commit_date
    get_commit_date.short_description = "Date commit"
    list_filter = ['post__commit_date', 'is_accept', 'is_hot']
    search_fields = ['post__title', 'get_author']
class PostRateAdmin(admin.ModelAdmin):
    list_display = ('get_title','get_author')
    def get_title(self, obj):
        return obj.post.title
    get_title.short_description = "Title"
    def get_author(self, obj):
        return obj.post.author.username
    get_author.short_description = "Author"
class PostAcceptedAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'sub_type','commit_date','accept_date','is_hot') # thu tu hien thi trong question
    list_filter = ['commit_date','accept_date','is_hot'] # bo loc
    search_fields = ['title','author__username']
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'tournament', 'icon')
    search_fields = ['name','tournament__name']
class LiveNewsAdmin(admin.ModelAdmin):
    list_display = ('host', 'host_point', 'quest_point','quest','round','was_commit_recently')
class TypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
admin.site.register(PostType, TypeAdmin)
admin.site.register(PostSubType)
admin.site.register(Post, PostAdmin)
admin.site.register(PostAccept, PostAcceptAdmin)
admin.site.register(PostRate)
admin.site.register(PostAccepted, PostAcceptedAdmin)
admin.site.register(LiveNews, LiveNewsAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Tournaments)
admin.site.register(Infor)