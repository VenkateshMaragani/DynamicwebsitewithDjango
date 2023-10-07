from django.db import models

class Contact(models.Model):
    # Fields for collecting contact information
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    country = models.CharField(max_length=30)
    ph = models.CharField(max_length=13) 
    # Additional fields if needed, such as phone number, date, etc.
    # Timestamps for when the contact was made
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name  # Display the full name in admin panel, change as needed
    from django.db import models

class Contact_details(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    company_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    # Additional fields
    service_interested_in = models.CharField(max_length=100, choices=[
        ('Web Development', 'Web Development'),
        ('App Development', 'App Development'),
        ('Consulting', 'Consulting'),
        ('Other', 'Other'),
    ])
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    project_description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


