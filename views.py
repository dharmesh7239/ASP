
from django.shortcuts import render
from django.http import HttpResponse
from .models import JobListing

def job_listings(request):
   
    job_listings = JobListing.objects.all()
    context = {'job_listings': job_listings}
    return render(request, 'myapp/job_listings.html', context)

def job_detail(request, job_id):
  
    job = JobListing.objects.get(id=job_id)
    context = {'job': job}
    return render(request, 'myapp/job_detail.html', context)
