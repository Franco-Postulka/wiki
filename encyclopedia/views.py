from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
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

def compare_str(str1,str2):
    """_summary: compare 2 strings and returns true if there are coincidences
    Args:
        str1 (str)
        str2 (str)
    Returns:
        bool: if there are coincidences or not
    """
    import re
    if len(str1)<= len(str2):
        comparison = re.findall(str1.lower(),str2.lower())
        if len(comparison) > 0:
            return True
        else:
            return False
    else:
        comparison = re.findall(str2.lower(),str1.lower())
        if len(comparison) > 0:
            return True
        else:
            return False

def find_coincidences(list,string):
    """_summary: receives a list and a string, returns a list with elements of the list it received
    that matched the string
    Args:
        list (list):
        string (str)
    Returns:
        list: the elements that matched the string
    """
    new_list = []
    for element in list:
        coincidences = compare_str(string,element)
        if coincidences == True:
            new_list.append(element)
    return new_list

def search_bar(request):
    if request.method == "POST":
        search = request.POST['q']
        entry = util.get_entry(search)
        if entry != None:
            html_content = markdown2.markdown(entry)
            return render(request, "encyclopedia/entry.html", {
                "entry_content": html_content,
                "entry_title": search
            })
        else:
            entries = util.list_entries()
            coincidences = find_coincidences(entries,search)
            if len(coincidences) > 0:
                return render(request, "encyclopedia/index.html", {
                "entries": coincidences
                })
            else:
                return render(request,  "encyclopedia/notfound.html")


def new_page(request):
    return render(request, "encyclopedia/new_page.html")