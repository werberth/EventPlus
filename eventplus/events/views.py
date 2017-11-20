from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy as r

from .models import Event, Supporters
from .forms import CreateEventForm, SupporterForm


class KwargsEventView(object):

    """
        classe que sobrescreve o methodo get_form_kwargs
        para adicionar o evento ao formulário.
        Essa classe deverá ser herdada pro todas as views
        que utilizaram formulários que nescessitaram adicionar
        o evento automaticamente a alguma instancia de um model
        no momento de sua criação.
    """

    def get_form_kwargs(self):
        kwargs = super(KwargsEventView, self).get_form_kwargs()
        kwargs['event'] = get_object_or_404(Event, pk=self.kwargs['event'])
        return kwargs


class KwargsUserView(object):

    """
        classe que sobrescreve o methodo get_form_kwargs
        para adicionar o usuario ao formulário.
        Essa classe deverá ser herdada pro todas as views
        que utilizaram formulários que nescessitaram adicionar
        o usuario automaticamente a alguma instancia de um model
        no momento de sua criação.
    """

    def get_form_kwargs(self):
        kwargs = super(KwargsUserView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CreateEventView(LoginRequiredMixin, KwargsUserView, generic.CreateView):

    """
        View de criação do evento.
    """

    model = Event
    form_class = CreateEventForm
    template_name = 'events/crud_event.html'

    def form_valid(self, form):
        event = form.save()
        url = r(
            'events:edit',
            kwargs={
                'slug': event.slug
            }
        )
        return HttpResponseRedirect(url)


class UpdateEventView(
        LoginRequiredMixin,
        KwargsUserView,
        generic.UpdateView):

    """
        View de edição dos dados do evento.
    """

    model = Event
    form_class = CreateEventForm
    template_name = 'events/crud_event.html'

    def get_success_url(self):
        url = r(
            'events:edit',
            kwargs={
                'slug': self.kwargs['slug']
            }
        )
        return url


class DeleteEventView(LoginRequiredMixin, generic.DeleteView):

    """
        View de exclusão de um evento dado. (passado pela url)
    """

    model = Event
    success_url = r('events:myevents')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ListEventView(generic.ListView):

    """
        View de listagem dos eventos, que servirá também
        como pagina inicial da aplicação.
    """

    model = Event

    queryset = Event.objects.filter(
        end_date__gte=datetime.today()
    ).order_by('-start_date')

    template_name = 'events/list_events.html'
    context_object_name = 'events'
    paginate_by = 5


class MyEventsView(LoginRequiredMixin, generic.ListView):

    """
        View de listagem dos eventos criados pelo usuário autenticado.
        O usuário ao efetuar login será redirecionado para a url dessa view
    """

    model = Event
    template_name = 'events/my_events.html'
    context_object_name = 'events'
    paginate_by = 5

    def get_queryset(self):
        queryset = Event.objects.filter(
            user=self.request.user
        ).order_by('-start_date')
        return queryset


class EventView(generic.TemplateView):

    """
        View de visualĩzação de um evento, por um usuário
        não autenticado, ou que não é o dono (moderador) do evento.
    """

    template_name = 'events/event.html'

    def get_context_data(self, **kwargs):
        context = super(EventView, self).get_context_data(**kwargs)
        event = get_object_or_404(Event, slug=kwargs['slug'])
        context['event'] = event
        context['all_talks'] = self.select_talks_by_day(event)
        context = self.get_supporters(context, event)
        return context

    def get_supporters(self, context, event):
        context['sponsors'] = event.supporters.filter(
            types="sponsors"
        )
        context['promoters'] = event.supporters.filter(
            types="promoters"
        )
        context['organizers'] = event.supporters.filter(
            types="organizers"
        )
        return context

    def select_talks_by_day(self, event):
        date = event.start_date
        talks_list = []
        while date <= event.end_date:
            talks = event.talks.filter(date=date).order_by('start_at')
            talks_list.append(talks)
            date += timedelta(days=1)
        return talks_list


class EventEditView(LoginRequiredMixin, EventView):

    """
        View de visualização e organização (edição) de um dado evento
        pelo seu criador. Após criar um determinado evento, o
        usuário será redirecionado para essa pagina.
    """

    template_name = 'events/event_edit.html'

    def get_context_data(self, **kwargs):
        context = super(EventEditView, self).get_context_data(**kwargs)
        event = get_object_or_404(
            Event,
            user=self.request.user,
            slug=kwargs['slug']
        )
        context['event'] = event
        context['all_talks'] = self.select_talks_by_day(event)
        context = self.get_supporters(context, event)
        return context


class CreateSupporterView(
        LoginRequiredMixin,
        KwargsEventView,
        generic.CreateView):

    """
        View de criação de um colaborador
    """

    model = Supporters
    form_class = SupporterForm
    template_name = 'events/crud_supporter.html'

    def get_success_url(self):
        event = get_object_or_404(Event, pk=self.kwargs['event'])
        url = r(
            'events:edit',
            kwargs={
                'slug': event.slug
            }
        )
        return url


class UpdateSupporterView(
        LoginRequiredMixin,
        KwargsEventView,
        generic.UpdateView):

    """
        View de edição de um colaborador
    """

    model = Supporters
    form_class = SupporterForm
    template_name = 'events/crud_supporter.html'

    def get_success_url(self):
        event = get_object_or_404(Event, pk=self.kwargs['event'])
        url = r(
            'events:edit',
            kwargs={
                'slug': event.slug
            }
        )
        return url


class DeleteSupporterView(LoginRequiredMixin, generic.DeleteView):
    """
        View de exclusão de um dado colaborador
    """

    model = Supporters
    success_url = r('events:supporter_create')

    def get_success_url(self):
        url = r(
            'events:edit',
            kwargs={
                'slug': self.kwargs['event']
            }
        )
        return url

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
