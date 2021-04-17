from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.template.defaultfilters import slugify
from PIL import Image
from ckeditor_uploader.fields import RichTextUploadingField

def upload_image(instance, filename):
    """A function used in the Image field to change the name of the image to ID of the project"""
    _ , extension = filename.split('.')
    return f"projects_pics/{instance.pk}.{extension}"

class Project(models.Model):
    title       = models.CharField(max_length=200, null=True, blank=True)
    description = RichTextUploadingField(max_length=5000, null=True, blank=True)
    category    = models.CharField(max_length=200, null=True, blank=True)
    image       = models.ImageField(default='projects_pics/default.jpg', upload_to=upload_image, null=True, blank=True)
    author      = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at  = models.DateTimeField(default=now)
    active      = models.BooleanField(default=True)
    slug        = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """overriding a save function to make a slug and resize a large image"""

        # fix a some a rename image problem
        if self.pk is None:
            img = self.image
            self.image = None
            super().save(self, *args, **kwargs)
            self.image = img

        self.slug = slugify(f"{self.title} {self.category} {self.pk}")
        
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.width > 500 or img.height > 500:
            img.thumbnail((500, 500))
            img.save(self.image.path)

    def __str__(self):
        return self.title

class ActiveSections(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))


    about    = models.BooleanField(choices=BOOL_CHOICES, default=True)
    services = models.BooleanField(choices=BOOL_CHOICES, default=True)
    portfolio    = models.BooleanField(choices=BOOL_CHOICES, default=True)
    experience    = models.BooleanField(choices=BOOL_CHOICES, default=True)
    contact    = models.BooleanField(choices=BOOL_CHOICES, default=True)
