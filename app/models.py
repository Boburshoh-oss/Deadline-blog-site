from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _


class Regions(TranslatableModel):
    translation = TranslatedFields(
        name=models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Name'))
    )
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.safe_translation_getter('name') or ''

    def get_absolute_url(self):
        return f'regions/{self.slug}'


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'categories/{self.slug}'


class Blog(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name=_('Title')),
        description=models.TextField(verbose_name=_('Description')))
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True,)
    image = models.ImageField(upload_to='blogimages')
    region = models.ForeignKey(Regions, on_delete=models.CASCADE, )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, )

    class Meta:
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.safe_translation_getter('title') or ''

    def get_absolute_url(self):
        return f'blog/{self.slug}'


class Hashtags(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    posts = models.ManyToManyField(Blog,)

    class Meta:
        verbose_name_plural = 'Hashtags'

    def __str__(self):
        return self.name


class PicturesFromTheBlog(models.Model):
    owner = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shotsinblogs')

    class Meta:
        verbose_name_plural = 'Pictures from the blog'

    def __str__(self):
        return self.owner.safe_translation_getter('title') or ''
