from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from .decorators import validate_integers
from rest_framework import status

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
@api_view(['GET'])
def check_api(request):
    return Response("Hello world")

@api_view(['POST'])
@validate_integers
def try_decrotator(request):  
    try:
        result = request.data['a'] + request.data['b']  # Perform addition operation
        return Response({'result': result}, status=status.HTTP_200_OK)
    except ValueError:
        return Response({'error': 'Invalid input. Both "a" and "b" must be integers.'}, status=status.HTTP_400_BAD_REQUEST)
