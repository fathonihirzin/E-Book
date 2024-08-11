from django.db import models
from django.utils.translation import gettext_lazy as _

class Ebook(models.Model):

    class EbookStatus(models.TextChoices):
        COMPLETED = 'completed', _('Completed')
        READING = 'reading', _('Reading')
        NOT_YET = 'not_yet', _('Not_Yet')

    class EbookCategory(models.TextChoices):
        ACTION = 'action', _('Action')
        FANTACY = 'fantacy', _('Fantacy')
        TECHNOLOGY = 'technology', _('Technology')



    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    release_date = models.DateField()
    category = models.CharField(max_length=20)
    score = models.FloatField()
    description = models.TextField()
    photo=models.ImageField(upload_to="uploads")

    status = models.CharField(
        max_length=20,
        choices=EbookStatus.choices,
        default=EbookStatus.NOT_YET
    )

    category = models.CharField(
        max_length=20,
        choices=EbookCategory.choices
    )

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ebooks'
