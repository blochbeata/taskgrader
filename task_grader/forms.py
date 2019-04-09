from django.forms import ModelForm

from task_grader.models import Grade


class AddMarkForm(ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'
