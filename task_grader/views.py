from django.db.models import Avg
from django.http import HttpResponse
from django.http import JsonResponse


from django.views import View
from django.views.generic import FormView

from task_grader.forms import AddMarkForm
from task_grader.models import Grade, Candidate


class AddMarkView(FormView):
    template_name = 'task_grader/add-mark.html'
    form_class = AddMarkForm
    success_url = '/'

    def form_valid(self, form):
        try:
            Grade.objects.get(task_id=form.cleaned_data['task'], candidate_id=form.cleaned_data['candidate'])
            return HttpResponse("Already graded!")
        except Grade.DoesNotExist:
            form.save()
            return super().form_valid(form)


class ShowAllView(View):

    def get(self, request):
        candidates = Candidate.objects.all()
        responseData = []
        for candidate in candidates:
            grades = list(Grade.objects.filter(candidate_id=candidate.id).values_list('value', flat=True).distinct())
            average = Grade.objects.filter(candidate_id=candidate.id).aggregate(Avg('value'))["value__avg"]
            data = {
                'data': [
                    {
                'pk': candidate.id,
                'full_name': candidate.name,
                'avg_grade': average,
                'grades': grades
                    }
                ]
                }
            responseData.append(data)

        return JsonResponse(responseData, safe=False, json_dumps_params={'indent': 2})
