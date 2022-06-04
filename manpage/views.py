from django.shortcuts import render

# Create your views here.
#from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from .models import ManpagePost


class BlackarchView(ListView):
    template_name = 'blackarch.html'
    model = ManpagePost
    context_object_name = 'blackarch_records'
    queryset = ManpagePost.objects.filter( distro='blackarch' ).order_by('?')
    paginate_by = 20


class CentosView(ListView):
    template_name = 'centos.html'
    model = ManpagePost
    context_object_name = 'centos_records'
    queryset = ManpagePost.objects.filter( distro='centos' ).order_by('?')
    paginate_by = 20
    
    
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    
    def form_valid(self, form):
        form.send_email()
        messages.success( self.request, 'お問い合わせは正常に送信されました。' )
        return super().form_valid(form)
    
    
class DebianView(ListView):
    template_name = 'debian.html'
    model = ManpagePost
    context_object_name = 'debian_records'
    queryset = ManpagePost.objects.filter( distro='debian' ).order_by('?')
    paginate_by = 20
    
    
class DeepinView(ListView):
    template_name = 'deepin.html'
    model = ManpagePost
    context_object_name = 'deepin_records'
    queryset = ManpagePost.objects.filter( distro='deepin' ).order_by('?')
    paginate_by = 20
    
    
class FreebsdView(ListView):
    template_name = 'freebsd.html'
    model = ManpagePost
    context_object_name = 'freebsd_records'
    queryset = ManpagePost.objects.filter( distro='freebsd' ).order_by('?')
    paginate_by = 20


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'orderby_records'
    queryset = ManpagePost.objects.order_by('?')
    paginate_by = 20


class KaliView(ListView):
    template_name = 'kali.html'
    model = ManpagePost
    context_object_name = 'kali_records'
    queryset = ManpagePost.objects.filter( distro='kali' ).order_by('?')
    paginate_by = 20
    
    
class MacosView(ListView):
    template_name = 'macos.html'
    model = ManpagePost
    context_object_name = 'macos_records'
    queryset = ManpagePost.objects.filter( distro='macos' ).order_by('?')
    paginate_by = 20
    
    
class ManpageDetail(DetailView):
    template_name = 'post.html'
    model = ManpagePost
    
    
class ParrotView(ListView):
    template_name = 'parrot.html'
    model = ManpagePost
    context_object_name = 'parrot_records'
    queryset = ManpagePost.objects.filter( distro='parrot' ).order_by('?')
    paginate_by = 20
    
    
class QubesView(ListView):
    template_name = 'qubes.html'
    model = ManpagePost
    context_object_name = 'qubes_records'
    queryset = ManpagePost.objects.filter( distro='qubes' ).order_by('?')
    paginate_by = 20
    
    
class RaspberrypiView(ListView):
    template_name = 'raspberrypi.html'
    model = ManpagePost
    context_object_name = 'raspberrypi_records'
    queryset = ManpagePost.objects.filter( distro='raspberrypi' ).order_by('?')
    paginate_by = 20
    
    
class RhelView(ListView):
    template_name = 'rhel.html'
    model = ManpagePost
    context_object_name = 'rhel_records'
    queryset = ManpagePost.objects.filter( distro='rhel' ).order_by('?')
    paginate_by = 20
    
    
class SlackwareView(ListView):
    template_name = 'slackware.html'
    model = ManpagePost
    context_object_name = 'slackware_records'
    queryset = ManpagePost.objects.filter( distro='slackware' ).order_by('?')
    paginate_by = 20


class UbuntuView(ListView):
    template_name = 'ubuntu.html'
    model = ManpagePost
    context_object_name = 'ubuntu_records'
    queryset = ManpagePost.objects.filter( distro='ubuntu' ).order_by('?')
    paginate_by = 20
    
    
class WindowsView(ListView):
    template_name = 'windows.html'
    model = ManpagePost
    context_object_name = 'windows_records'
    queryset = ManpagePost.objects.filter( distro='windows' ).order_by('?')
    paginate_by = 20
    
    
