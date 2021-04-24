from django.db.models.signals import post_save, pre_save, post_delete, pre_delete

from django.dispatch import receiver

from .models import Book, ISBN, User
from django.core.mail import send_mail

@receiver(post_save,sender=Book)
def after_book_creation(sender, instance, created, *args, **kwargs):
    if created:
        isbn_instance = ISBN.objects.create(author_title = instance.creator, book_title = instance.title)
        # isbn_instance.save()
        instance.isbn = isbn_instance
        instance.save()

        # send_mail('New Book {}'.format(instance.title), 'New book is created check it','',['suzannaim7@gmail.com'],fail_silently=False)

    else:
        print("updating")