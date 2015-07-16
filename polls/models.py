from django.db import models
import datetime
from django.db.models import permalink
from django.db.models.fields.files import ImageField
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
from PIL import Image, ImageOps
import sys


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, default='the-url', help_text='url for post')
    pub_date = models.DateField('date published')
    updated_date = models.DateField('date updated', default=datetime.date.today)
    is_enabled = models.BooleanField('is enabled')
    is_article = models.BooleanField('is article', default=True)
    is_guide = models.BooleanField('is guide', default=True)
    body = RichTextField(help_text='image url: /media/"url on image upload page"')
    meta_title = models.TextField(default='')
    meta_description = models.TextField(default='')
    meta_keywords = models.TextField(default='')
    meta_canonical = models.URLField(default='')
    categories = models.ManyToManyField('polls.Categories')
    quick1 = models.SlugField('quick1', help_text='url for post')
    quick1_title = models.CharField(max_length=200, default='')
    quick1_image = models.CharField(max_length="50", help_text='300 x 340')
    quick2 = models.SlugField('quick2', help_text='url for post')
    quick2_title = models.CharField(max_length=200, default='')
    quick2_image = models.CharField(max_length="50", help_text='300 x 340')
    quick3 = models.SlugField('quick3', help_text='url for post')
    quick3_title = models.CharField(max_length=200, default='')
    quick3_image = models.CharField(max_length="50", help_text='300 x 340', null=True)
    quick4 = models.SlugField('quick4', help_text='url for post')
    quick4_title = models.CharField(max_length=200, default='')
    quick4_image = models.CharField(max_length="50", help_text='300 x 340')

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_post', None, {'slug': self.slug})

    def get_absolute_url_quick(self, slug):
        # return ('view_post', None, {'slug': slug })
        return reverse('view_post', kwargs={'slug': str(slug)})


class Post_related_images(models.Model):
    post = models.ForeignKey('polls.Post', related_name='images')
    description = models.CharField(max_length=250)
    image = ImageField(upload_to='img/%Y/%m/%d')
    smallimage = models.CharField(max_length=250, blank=True)
    largeimage = models.CharField(max_length=250, blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.description

    class Meta:
        verbose_name_plural = "Post related images"

    def save(self):
        sizes = {'thumbnail': {'height': 340, 'width': 300},
                 'medium': {'height': 370, 'width': 635}}

        super(Post_related_images, self).save()
        photopath = str(self.image.path)  # this returns the full system path
        # to the original file
        im = Image.open(photopath)  # open the image using PIL
#         ins=ImageOps()
    # pull a few variables out of that full path
        extension = photopath.rsplit('.', 1)[1]  # the file extension
        filename = photopath.rsplit('/', 1)[-1].rsplit('.', 1)[:-1][0]  # the
        # file name only (minus path or extension)
        fullpath = photopath.rsplit('/', 1)[:-1][0]  # the path only (minus
        # the filename.extension)
        # use the file extension to determine if the image is valid
        # before proceeding
        if extension not in ['jpg', 'jpeg', 'gif', 'png']:
            sys.exit()

        # create medium image
        ins = ImageOps.fit(im, (sizes['medium']['width'], sizes['medium']['height']), Image.ANTIALIAS)
        medname = str(filename) + "_" + str(sizes['medium']['width']) + "x" + str(sizes['medium']['height']) + ".jpg"
        ins.save(str(fullpath) + '/' + medname)
        self.largeimage = self.image.url.rsplit('/', 1)[:-1][0] + '/' + medname

        # create thumbnail
        ins = ImageOps.fit(im, (sizes['thumbnail']['width'], sizes['thumbnail']['height']), Image.ANTIALIAS)
        thumbname = filename + "_" + str(sizes['thumbnail']['width']) + "x" + str(sizes['thumbnail']['height']) + ".jpg"
        ins.save(fullpath + '/' + thumbname)
        self.smallimage = self.image.url.rsplit('/', 1)[:-1][0] + '/' + thumbname

        super(Post_related_images, self).save()


class Index_quick_links(models.Model):
    title = models.CharField(max_length=200, default='')
    current = models.BooleanField('current', default=True)
    Iquick1 = models.SlugField('Iquick1', help_text='url for post')
    Iquick1_title = models.CharField(max_length=200, default='')
    Iquick1_image = models.CharField(max_length="50", help_text='300 x 340')
    Iquick2 = models.SlugField('Iquick2', help_text='url for post')
    Iquick2_title = models.CharField(max_length=200, default='')
    Iquick2_image = models.CharField(max_length="50", help_text='300 x 340')
    Iquick3 = models.SlugField('Iquick3', help_text='url for post')
    Iquick3_title = models.CharField(max_length=200, default='')
    Iquick3_image = models.CharField(max_length="50", help_text='300 x 340')
    Iquick4 = models.SlugField('Iquick4', help_text='url for post')
    Iquick4_title = models.CharField(max_length=200, default='')
    Iquick4_image = models.CharField(max_length="50", help_text='300 x 340')

    class Meta:
        verbose_name_plural = "Index quick links"

    def __str__(self):
        return self.title

    def get_absolute_url(self, slug):
        # return ('view_post', None, {'slug': slug })
        return reverse('view_post', kwargs={'slug': str(slug)})


class Categories(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, db_index=True, default='the-category')
    info = RichTextField()

    def __str__(self):  # __unicode__ on Python 2
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_categories', None, {'slug': self.slug})

    class Meta:
        verbose_name_plural = "Categories"
