from django.db import models
from django.utils.text import slugify

# Create your models here.
class RecipeModel(models.Model):
  name = models.CharField(max_length=80)
  description = models.CharField(max_length=255)
  ingredients = models.CharField(max_length=255)
  duration= models.IntegerField()
  image = models.ImageField(default=None, blank=True, upload_to="images/")
  slug = models.SlugField(unique=True, blank=True)
  
  def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(RecipeModel, self).save(*args, **kwargs)

  def __str__(self):
    return self.name