from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from .models import Categories, Post, Index_quick_links
from forms import ContactForm, EnquiryForm, contactform
from mfabrik.zoho.crm import CRM
import datetime

crm = CRM(authtoken="c5e226a5dabe938839005601a94844eb",scope="crmapi")
# crm.open()

recipient = ['reservations@houseofmoli.com','']

#recipient = ['warunhasija@gmail.com']


def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EnquiryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['query']
            sender = form.cleaned_data['email']
            recipients = recipient
            from django.core.mail import send_mail
            send_mail('Query through pvr', form.cleaned_data['contact'] + subject, sender, recipients,fail_silently=False)
#             process the data in form.cleaned_data as required
#             ...
#             redirect to a new URL:
             lead = {
                 u"Last Name": name,
                 u"Email": sender,
                 u"Phone": form.cleaned_data['contact'],
                 u"Source": u"PVR",
                 u"Description": subject,
                 u"Query Date": datetime.date.today
             }
             responses = crm.insert_records('Leads', [lead])
            return HttpResponseRedirect('thanks.html')
    elif request.method == 'GET':
        form = EnquiryForm()
    quicklinks = Index_quick_links.objects.get(current=True)
    quick1url = quicklinks.get_absolute_url(quicklinks.Iquick1)
    quick2url = quicklinks.get_absolute_url(quicklinks.Iquick2)
    quick3url = quicklinks.get_absolute_url(quicklinks.Iquick3)
    quick4url = quicklinks.get_absolute_url(quicklinks.Iquick4)
    return render(request, 'index.html', {
        'quicklinks': quicklinks,
        'categories': Categories.objects.all(),
        'posts': Post.objects.all()[: 5],
        'form': form,
        'quick1url': quick1url,
        'quick2url': quick2url,
        'quick3url': quick3url,
        'quick4url': quick4url,
    })


def wheretostay(request):
    return render_to_response('wheretostay.html')


def story(request):
    return render_to_response('story.html')


def specialoffers(request):
    return render_to_response('specialoffers.html')


def parisguide(request):
    posts = Post.objects.filter(is_guide=True)
    images = [post.images.all() for post in posts]
    categories = [post.categories.all() for post in posts]
    data = zip(posts, images, categories)
#     import pdb;pdb.set_trace()
#     for post in posts:
#         categories = Categories.objects.filter(post=post)
    return render(request, 'parisguide.html', {'data': data})


def articles(request):
    posts = Post.objects.filter(is_article=True)
    images = [post.images.all() for post in posts]
    categories = [post.categories.all() for post in posts]
    data = zip(posts, images, categories)
#     import pdb;pdb.set_trace()
#     for post in posts:
#         categories = Categories.objects.filter(post=post)
    return render(request, 'articles.html', {'data': data})


def thanks(request):
    return render_to_response('thanks.html')


def contact(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['email']
            recipients = recipient
            from django.core.mail import send_mail
            send_mail('Query through pvr', subject, sender, recipients)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
             lead = {
                 u"Last Name": name,
                 u"Email": sender,
                 u"Source": u"PVR",
                 u"Description": subject,
                 u"Query Date": datetime.date.today
             }
             responses = crm.insert_records('Leads', [lead])
            return HttpResponseRedirect('thanks.html')
    elif request.method == 'GET':
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
    # return render_to_response('contact.html', form=form)


def view_post(request, slug):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = contactform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['email']
            recipients = recipient
            from django.core.mail import send_mail
            send_mail('Query through pvr', subject, sender, recipients)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
             lead = {
                 u"Last Name": name,
                 u"Email": sender,
                 u"Source": u"PVR",
                 u"Description": subject,
                 u"Query Date": datetime.date.today
             }
             responses = crm.insert_records('Leads', [lead])
             return HttpResponseRedirect('thanks.html')
    elif request.method == 'GET':
        form = contactform()
    post = get_object_or_404(Post, slug=slug)
    quick1url = post.get_absolute_url_quick(post.quick1)
    quick2url = post.get_absolute_url_quick(post.quick2)
    quick3url = post.get_absolute_url_quick(post.quick3)
    quick4url = post.get_absolute_url_quick(post.quick4)
    categories = Categories.objects.filter(post=post)[:5]
    if post.is_enabled:
        return render(request, 'view_post.html', {
            'categories': categories,
            'post': post,
            'form': form,
            'quick1url': quick1url,
            'quick2url': quick2url,
            'quick3url': quick3url,
            'quick4url': quick4url,
        })
    else:
        return render_to_response('404.html')


def view_categories(request, slug):
    category = get_object_or_404(Categories, slug=slug)
    return render_to_response('view_categories.html', {
        'category': category,
        'categories': Categories.objects.all(),
        'posts': Post.objects.filter(categories=category)
    })
