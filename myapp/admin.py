from django.contrib import admin
from .models import Bus, User, Book, terminals, counter

# Register your models here.

admin.site.register(Bus)
admin.site.register(User)
admin.site.register(Book)
admin.site.register(terminals)
admin.site.register(counter)


