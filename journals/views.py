from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from .models import Title, Entry
from .forms import TitleForm, EntryForm, TitleChangeForm, EntryChangeForm


def home(request):
    # Return all journal titles
    titles = Title.objects.all()
    context = {'titles': titles }
    return render(request, template_name='journals/home.html', context=context)

def journal_detail(request, title_id):
    # Return the details of a specific journal entry
    # This is a GET request
    try:
        title = Title.objects.get(id=title_id)
    except Title.DoesNotExist:
        return HTTPResponseNotFound('Sorry, The requested object does not exist on our server.')
    entries = Entry.objects.filter(title=title)
    context = {
        'title': title,
        'entries': entries
    }
    return render(request, template_name='journals/details.html', context=context)


def add_title(request):
    # Add a new title object
    if request.method == 'POST':
        form = TitleForm(data=request.POST)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.author = request.user
            save_form.save()
            return redirect('home')
    form = TitleForm()
    context = {'form': form}
    return render(request, template_name='journals/add-title.html', context={'form': form})

def add_entry(request, title_id):
    # Add a new entry object
    if request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.title = title
            save_form.save()
            return redirect('details', title_id=title_id)
    form = EntryForm()
    context = {'form': form}
    return render(request, template_name='journals/add-entry.html', context=context)

def edit_title(request, title_id):
    # Edit a title
    # This is a POST request
    title = get_object_or_404(Title, id=title_id)
    if request.method == 'POST':
        form = TitleChangeForm(data=request.POST, instance=title)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = TitleChangeForm(instance=title)
    context = {'form': form}
    return render(request, template_name='journals/edit-title.html', context=context)


def edit_entry(request, entry_id):
    # Edit an entry
    # This is a POST request
    entry = get_object_or_404(Entry, id=entry_id)
    if request.method == 'POST':
        form = EntryChangeForm(data=request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = EntryChangeForm(instance=entry)
    context = {'form': form}
    return render(request, template_name='journals/edit-entry.html', context=context)


def delete_title(request, title_id):
    # Delete a specific title
    title = get_object_or_404(Title, id=title_id)
    if request.method == 'POST':
        title.delete()
        return redirect('home')
    form = TitleChangeForm(instance=title)
    context = {'form': form}
    return render(request, template_name='journals/delete-title.html', context=context)


def delete_entry(request, entry_id):
    # Delete a specific entry
    entry = get_object_or_404(Entry, id=entry_id)
    if request.method == 'POST':
        entry.delete()
        return redirect('home')
    form = EntryChangeForm(instance=entry)
    context = {'form': form}
    return render(request, template_name='journals/delete-entry.html', context=context)
