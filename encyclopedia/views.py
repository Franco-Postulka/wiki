from django.shortcuts import render
import markdown2
from . import util
from django import forms


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request, entry):
    entry_content = util.get_entry(entry)
    if  entry_content == None:
        # The entry does not exist
        return render(request, "encyclopedia/notfound.html")
    else:
        # The entry does exist
        html_content = markdown2.markdown(entry_content)
        return render(request, "encyclopedia/entry.html", {
            "entry_content": html_content,
            "entry_title": entry
        })

class NewTaskForm(forms.Form):
    task = forms.CharField(label='New Task')



