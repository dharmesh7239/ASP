
from django.test import TestCase
from .models import JobListing

class JobListingTests(TestCase):
    def setUp(self):
        
        JobListing.objects.create(title='Python Developer', company='ABC Inc', location='City A', salary='$100,000')

    def test_job_listing_title(self):
    
        job = JobListing.objects.get(title='Python Developer')
        
        self.assertEqual(job.title, 'Python Developer')

    def test_job_listing_salary(self):
        job = JobListing.objects.get(title='Python Developer')
        
        self.assertEqual(job.salary, '$100,000')
