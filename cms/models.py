from django.db import models

class SiteContent(models.Model):
    """
    A simple key-value store for site-wide content (e.g. Hero title, tagline)
    """
    key = models.CharField(max_length=100, unique=True, help_text="e.g., 'home_hero_title'")
    value = models.TextField(blank=True)
    image = models.ImageField(upload_to='site_images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True, help_text="Link to external video (e.g., YouTube)")
    file_upload = models.FileField(upload_to='site_media/', blank=True, null=True, help_text="Direct upload for image or video")

    def __str__(self):
        return self.key

class ClassProgram(models.Model):
    """
    For Sweat Pilates, Sweat Bootcamp, etc.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=[('Pilates', 'Pilates'), ('Bootcamp', 'Bootcamp'), ('Online', 'Online')])
    image = models.ImageField(upload_to='program_images/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.category} - {self.title}"

class FAQCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class FAQItem(models.Model):
    category = models.ForeignKey(FAQCategory, related_name='items', on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.question

class Enquiry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    newsletter = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"

class Transformation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video_upload = models.FileField(upload_to='transformations/')
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
