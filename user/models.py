from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.
technologie =(
    ('Web Developer', 'Web Developer'),
    ('Mobile App Developer', 'Mobile App Developer'),
    ('Graphic Designer', 'Graphic Designer'),
    ('Content Writer', 'Content Writer'),
    ('Social Media Manager', 'Social Media Manager'),
    ('Virtual Assistant', 'Virtual Assistant'),
    ('Data Analyst', 'Data Analyst'),
    ('SEO Specialist', 'SEO Specialist'),
    ('Project Manager', 'Project Manager'),
    ('UI/UX Designer', 'UI/UX Designer'),
    ('iOS Developer', 'iOS Developer'),
    ('PHP Developer', 'PHP Developer'),
    ('Email Marketer', 'Email Marketer'),
    ('Paid Media Experts', 'Paid Media Expert'),
    ('E-commerce Developer', 'E-commerce Developer')
)
class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    whatsApp = models.CharField(max_length=12, null=True, unique=True)
    addresse = models.CharField(max_length=200, null=True)
    technologie = models.CharField(max_length=50, choices=technologie, null=True)
    lien_facebook = models.CharField(max_length=50, null=True, unique=True)
    lien_github = models.CharField(max_length=20, null=True, unique=True)
    discord = models.CharField(max_length=50, null=True, unique=True)
    upwork = models.CharField(max_length=100, null=True)
    apropos = models.TextField(null=True)
    photo = models.ImageField(default='avatar.jpg', upload_to='Profile_Images', validators=[FileExtensionValidator(['jpg', 'png'])])
    def __str__(self):
        return f'{self.staff.username}-Profile'