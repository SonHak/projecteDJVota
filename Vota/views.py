from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,  Http404, HttpResponse
from django.urls import reverse
from django.views import generic


from .models import Consulta , Opcion , Votacion
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'Vota/index.html'
    context_object_name = 'consultas'

    def get_queryset(self):
        """Return the last five published questions."""
        return Consulta.objects.order_by('fechaInicio');


class ConsultaView(generic.DetailView):
    model = Consulta
    template_name = 'Vota/consulta.html'


class ResultsView(generic.DetailView):
    model = Consulta
    template_name = 'Vota/results.html'


def vota(request, consulta_id):
    question = get_object_or_404(Consulta, pk=consulta_id)
    try:
        selected_choice = question.opcion_set.get(pk=request.POST['opcion'])
    except (KeyError, Opcion.DoesNotExist):
        return render(request, 'Vota/consulta.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votaciones += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('Vota:results', args=(consulta_id,)))