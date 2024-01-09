from django.shortcuts import render

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })

finches = [
{'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
{'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
]