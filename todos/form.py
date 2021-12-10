from django.forms import ModelForm
from .models import Todos


class TodosForm(ModelForm):
    class Meta:

        model = Todos
        fields = ['name',]

# user form