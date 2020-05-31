from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django import forms
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView 
from django.views.generic import DetailView 
from django.views.generic import UpdateView
from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views.generic import DeleteView


from .models import Pet,Vaccine

# list view
def page(request):
    pets_list = Pet.objects.all()
    last_pet = 0
    if 'last_pet' in request.session:
        last_pet = Pet.objects.get(id = request.session['last_pet'])
        pets_list = pets_list.exclude(id = request.session['last_pet'])
    return render(request, 'pet_list.html', {'pets_list': pets_list, 'last_pet' : last_pet})

class Pet_list(ListView):
    model = Pet
    template_name = 'pet_list.html'
    paginate_by = 5
    def get_queryset(self):
        queryset= Pet.objects.all().order_by("name")
        return queryset

# extend detailview
class Vaccine_detail(DetailView):
    model = Vaccine
    template_name = 'pet_details.html'
    
    def get_context_data(self, **kwargs):
        context = super(Vaccine_detail, self).get_context_data(**kwargs)
        pet_vac = Pet.objects.filter(vaccinations = self.object)
        context['pet_vac'] = pet_vac
        return context

# extend updateview
class Form_pet_time(ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'submission_date']

class Pet_update_time(UpdateView):
    model = Pet
    template_name = 'update_pet.html'
    form_class = Form_pet_time
    success_url = 'home'  

    def get_success_url(self):
        return reverse(self.success_url)


# Delete Pet
class Pet_delete(DeleteView):
    model = Pet
    template_name = 'confirm_delete_pet.html'
    success_url = 'home'
    # fields = ['name', 'sex']
    form_class = Form_pet_time
    def get_success_url(self):
        return reverse(self.success_url)


# create form 

# class Form_inscription(forms.Form):
#     name = forms.CharField(label="Name", max_length=50)
#     species = forms.CharField(label="Species", max_length=30)
#     breed = forms.CharField(label="Breed", max_length=30, )
#     sex = forms.CharField(label="sex", max_length=1, )
#     age = forms.IntegerField(label="Age")
#     submitter = forms.CharField(label="submitter")
#     submission_date = forms.DateTimeField()
#     # vaccinations = forms.Ma(label='Vaccine',queryset= Vaccine.objects.all())


# class Form_pet(forms.ModelForm):
#     class Meta:
#         model = Pet
#         fields = ['name', 'species', 'breed', 'sex', 'age', 'submitter', 'submission_date']
#         # exclude = ('description','age')


def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets': pets})

def pet_detail(request, id):
    try:
        pet = Pet.objects.get(id=id)
        request.session['last_pet'] = pet.id
        print("///////// : ", request.session['last_pet'])
    except Pet.DoesNotExist:
        raise Http404('Pet Does Not Exit')
    return render(request, 'pet_detail.html', {'pet': pet})

# def create_pet(request):
#     if len(request.POST):
#         form = Form_pet(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('home'))
#         else:
#             return render(request, 'pet_form.html', {'form':form})
#     else:
#         form = Form_pet()
#         return render(request, 'pet_form.html', {'form':form})


# def create_pet1(request):
#     if request.POST:
#         form = Form_inscription(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             species = form.cleaned_data['species']
#             breed = form.cleaned_data['breed']
#             sex = form.cleaned_data['sex']
#             age = form.cleaned_data['age']
#             submitter = form.cleaned_data['submitter']
#             submission_date = form.cleaned_data['submission_date']
#             # vaccinations = form.cleaned_data['vaccinations']

#             new_pet = Pet(name=name,species= species,breed= breed,sex= sex,age=age,submitter=submitter,
#             submission_date=submission_date)
            
#             new_pet.save()
#             print(">>>>>>>>>")
#             return HttpResponse("Pet added")
#         else:
#             print("<<<<<<<<<<")
#             return render(request,'pet_form.html' ,{'form':form})
#     else:
#         # va/cs_list = Vaccine.objects.all()
#         form = Form_inscription()
#         return render(request,'pet_form.html' , {'form':form})        


