from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Ebook

class EbookForm(ModelForm):
    class Meta:
        model =  Ebook

        fields = ('title', 'author', 'release_date', 'category', 'score', 'description', 'status', 'photo')

        label = {
            'title' : _('Title'),
            'author' : _('Author'),
            'release_date' : _('Release Date'),
            'category' : _('Category'),
            'score' : _('Score'),
            'status' : _('Status'),
            'description' : _('Description'),
            'photo' : _('Photo'),
        }

        error_messages = {
            'title': {
                'required': _("Must fill this field"),
            },
            'status': {
                'required': _("Must fill this field"),
            },
        }