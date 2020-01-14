from django.contrib import admin
from.models import Post, Wisdom, Category, Tag, Comment
# from django_summernote.admin import SummernoteModelAdmin
admin.site.register(Wisdom)
admin.site.register(Category)

'''class WisdomAdmin(SummernoteModelAdmin):
    list_display = ('title', 'w_post', 'slug', 'published',)
    list_filter = ('title', 'w_post')
    prepopulated_fields = {'slug': ('title',)}'''

class Wisdom (admin.ModelAdmin):
    list_display = ('title', 'w_post', 'slug', 'published',)
    list_filter = ('title', 'w_post')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'author', 'published', 'status', 'image')
    list_filter = ('status', 'created', 'published', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published'
    ordering = ('status', 'published')


'''class BlogSummernote(SummernoteModelAdmin):
    summer_note_fields = ('text_min', 'body')
    list_display = ('title','slug', 'author', 'published', 'status', 'image')
    list_filter = ('status', 'created', 'published', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published'
    ordering = ('status', 'published')'''




@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    ordering = ["title", "slug"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ["title"]}



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Comment, CommentAdmin)
