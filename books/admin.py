from django.contrib import admin
from .models import Book, Category, ISBN, Tag, Metric
from .forms import BookForm                 # 3shan validatin ytb2 3la Admin panel
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    form = BookForm                         # 3shan validatin ytb2 3la Admin panel      
    list_display = ("title","creator","description")
    list_filter = ("category", )
    search_fields = ("title", )

class BookInLine(admin.StackedInline):     #for more customization , tublarInline 3shn yb2o inline gnb b3d 
    model = Book
    max_num = 3
    extra = 1

class TagAdmin(admin.ModelAdmin):     #for relation one to many 3shan yzhr posts(many) in tag_page(one)
    inlines = [BookInLine]


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(ISBN)
admin.site.register(Metric)
admin.site.register(Tag, TagAdmin)