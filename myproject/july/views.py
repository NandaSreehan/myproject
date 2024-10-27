from django.shortcuts import render
from django.http import HttpResponse
def johny(request,s):
    
    
    return HttpResponse (f"<p>father:{s}... {s}...<br> {s}: yes papa!<br>father: eating sugar<br>{s}: no papa!.. <br>father: telling lies <br>father: no papa open your mouth <br>{s} hah hah hah hah</p>")
