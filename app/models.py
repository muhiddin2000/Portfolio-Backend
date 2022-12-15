from django.db import models
from django.utils.html import format_html


# Create your models here.
class SocialLink(models.Model):
    telegram = models.URLField(help_text="Enter telegram url", verbose_name="Telegram")
    instagram = models.URLField(help_text="Enter instagram url", verbose_name="Instagram")
    tiktok = models.URLField(help_text="Enter tiktok url", verbose_name="Tiktok")
    facebook = models.URLField(help_text="Enter facebook url", verbose_name="Facebook")
    youtube = models.URLField(help_text="Enter youtube url", verbose_name="Youtube")

    def __str__(self):
        return "Social Link"

    class Meta:
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"


class Profile(models.Model):
    name = models.CharField(max_length=30, help_text='Enter name', verbose_name='Name')
    image = models.ImageField(upload_to='profile-images', help_text='Upload images', verbose_name='Images')
    age = models.IntegerField(help_text="Enter age", verbose_name='Age')
    technologies = models.TextField(help_text='Enter technologies', verbose_name='technologies')
    job = models.CharField(max_length=100, help_text='enter job', verbose_name='Job')
    resume = models.FileField(upload_to='resumes', help_text='Upload resume', verbose_name='Resume')
    languages = models.CharField(max_length=30, default="O'zbek", help_text='Enter language', verbose_name='Language')
    portfolio = models.IntegerField(default='1', help_text='Enter portfolios count', verbose_name='Portfolio Count')
    profession = models.DecimalField(max_digits=10, decimal_places=1, default='1.5', help_text='Enter profession year',
                                     verbose_name='Profession Year')
    project = models.IntegerField(default='1', help_text='Enter project count', verbose_name='Project Count')

    def __str__(self):
        return self.name

    @property
    def photo(self):
        return format_html('<img src={} width="50"  height="50" style="border-radius:50%"'.format(self.image.url))


class Visitors(models.Model):
    count = models.IntegerField(default=1)


class Portfolio(models.Model):
    title = models.CharField(max_length=30, help_text='Enter title', verbose_name='Title')
    url = models.URLField(help_text="Enter url url", verbose_name="url")
    image = models.ImageField(upload_to='profile-images', help_text='Upload images', verbose_name='Images')

    def __str__(self):
        return self.title

    @property
    def photo(self):
        return format_html('<img src={} width="50"  height="50" style="border-radius:50%"'.format(self.image.url))


class Info(models.Model):
    gmail = models.EmailField(help_text='Enter gmail', verbose_name='Gmail')
    phone_number = models.CharField(max_length=30, help_text='Enter phone_number', verbose_name='Phone_number')
    adress = models.CharField(max_length=30, help_text='Enter adress', verbose_name='Adress')

    def __str__(self):
        return self.gmail
