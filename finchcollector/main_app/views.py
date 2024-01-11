from django.shortcuts import render

from.models import Finch

from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {
    'finches': finches
  })

# finches = [
# {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
# {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
# ]

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch })


class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'

class FinchUpdate(UpdateView):
  model = Finch
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'