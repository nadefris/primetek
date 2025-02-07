from django.db import models

# Create your models here.


# importing django models and users
from django.contrib.auth.models import User
 
 
# creating an django model class
class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField()
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '%s' % self.slug

class post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'
    
    CHOICES_STATUS = (
        (ACTIVE, 'active'),
        (DRAFT, 'Draft')
    )
    
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    # title field using charfield constraint with unique constraint
    title = models.CharField(max_length=255, unique=True)
    # slug field auto populated using title with unique constraint
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    # author field populated using users database
    #author = models.ForeignKey(User, on_delete= models.CASCADE)
    # and date time fields automatically populated using system time
    #updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add= True)
    # content field to store our post
    #content = models.TextField()
    # meta description for SEO benefits
    #metades = models.CharField(max_length=300, default="new post")
    # status of post
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
 
    # meta for the class
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '%s/%s' % (self.category.slug, self.slug)


    # used while managing models from terminal
    #def __str__(self):
    #    return self.title
class comment(models.Model):
    post = models.ForeignKey(post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return self.name

    
