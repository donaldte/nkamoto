from django.shortcuts import render
from django.views import View


class IndexView(View):
    """
    Name: IndexView
    Description: This class is used to render the index page.
    Author: DonaldProgrammeur 
    """
    def get(self, request):
        return render(request, 'index.html')
