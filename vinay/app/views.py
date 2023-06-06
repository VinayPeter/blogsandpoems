from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import PoemSubmissionForm

def app(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def second(request):
  template = loader.get_template('second.html')
  return HttpResponse(template.render())

def submit_poem(request):
    if request.method == 'POST':
        form = PoemSubmissionForm(request.POST)
        if form.is_valid():
            # Access the submitted form data
            poem_title = form.cleaned_data['poem_title']
            author_name = form.cleaned_data['author_name']
            poem_content = form.cleaned_data['poem_content']

            # Process the data (e.g., save it to the database)
            # Your logic goes here...

            # Optionally, you can redirect the user to a thank you page
            return render(request, 'thank_you.html')

    else:
        form = PoemSubmissionForm()

    return render(request, 'submit_poem.html', {'form': form})

def experiment(request):
  template = loader.get_template('experiment.html')
  return HttpResponse(template.render())
