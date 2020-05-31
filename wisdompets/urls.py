
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic.list import ListView
from adoptioions.views import Pet_list
from django.views.generic import DetailView
from django.urls import reverse_lazy
from adoptioions import views
from adoptioions.views import Vaccine_detail
from adoptioions.views import Pet_update_time
from adoptioions.views import Pet_delete

from adoptioions.models import Pet

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^adoptions/(\d+)/', views.pet_detail, name='pet_detail'),
    # url(r'^create-pet/', views.create_pet, name='create_pet'),
    url(r'^create-pet/', CreateView.as_view(model=Pet, template_name='pet_form.html', success_url='home', fields='__all__'), name='create_pet'),
    # list view
    # url (r'^pets_list$', ListView.as_view(model=Pet, template_name="pet_list.html"), name="pet_list"),
    # extend listview
    # url (r'^pets_list$', Pet_list.as_view(), name="pet_list"),
    url (r'^pets_list$', views.page, name="pet_list"),
    # detailview
    url (r'^pet_detail_(?P<pk>\d+)$', DetailView.as_view(model=Pet,template_name="pet_details.html"), name="pet_detail"),
    # extend detailview
    url (r'^vac_detail_(?P<pk>\d+)$', Vaccine_detail.as_view(), name="vac_detail"),
    # update view
    # url (r'^update_pet_(?P<pk>\d+)$', UpdateView.as_view(model=Pet, template_name="update_pet.html",success_url=reverse_lazy('home'),fields='__all__'), name="update_pet"),
    # extend update
    url (r'^update_pet_time_(?P<pk>\d+)$', Pet_update_time.as_view(), name="update_pet_time"),
    # Delete view
    url(r'pet_delete(?P<pk>\d+)$', Pet_delete.as_view(), name="pet_delete")

]
