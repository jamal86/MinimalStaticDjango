"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import django

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Microsoft Code Challege',
            'year':datetime.now().year,
	    'version':django.VERSION,
        })
    )

def anotherpage(request):
    assert isinstance(request, HttpRequest)
    return render(
        request, 
        'app/anotherpage.html',
        context_instance = RequestContext(request, 
            {
                'name': 'Timothy',
                'twitter': '@timmyreilly',
                'year': datetime.now().year,
            })
    )
