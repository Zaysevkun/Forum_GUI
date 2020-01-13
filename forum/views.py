from django.db.models.functions import datetime
from django.shortcuts import render , get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from forum.models import Categories, Messages, Users


# Create your views here.


def index(request):
    categories = Categories.objects.filter(parent_id__isnull=True)

    return render(request, "index.html", {"categories": categories})


def create(request):
    if request.method == "POST":
        tom = Categories()
        tom.name = request.POST.get("name")
        #tom.id = request.POST.get("id")
        tom.parent_id = None

        tom.save()
    return HttpResponseRedirect("/")


def category_page(request, pk):
    categories = Categories.objects.filter(parent_id__isnull=False)
    messages = Messages.objects.filter(categories_id__exact=pk)
    return render(request, 'messages.html', {'messages': messages, 'pk': pk, 'categories': categories})


def send_message(request):
    user = Users.objects.get(pk='04cd6c85-05c6-4c31-b8d7-e61bd528bae3')
    if request.method == "POST":
        tom = Messages()
        tom.text = request.POST.get("text")
        tom.author = user
        tom.posted_at = datetime.datetime.now()
        tom.categories_id = request.POST.get("category")

        tom.save()
    return HttpResponseRedirect("/category/" + tom.categories_id)


def zapros(request):
    #name_map = {'Id': 'id', 'name': 'category_name', 'text': 'text', 'name': 'name', 'posted_at': 'posted_at'}
    output = Messages.objects.raw('''SELECT DISTINCT ON (categories_id) forum_categories.id,forum_categories.name as categ, text, 
    forum_users.name, posted_at FROM forum_messages INNER JOIN forum_categories ON forum_categories.id = 
    forum_messages.categories_id INNER JOIN forum_users ON forum_users.id = forum_messages.author_id WHERE 
    categories_id IN (SELECT msg.categories_id FROM (SELECT DISTINCT ON (categories_id, author_id) categories_id FROM 
    forum_messages ORDER BY categories_id, author_id, posted_at) AS msg GROUP BY (msg.categories_id) HAVING COUNT(*) 
    > 2 LIMIT 10) ORDER BY categories_id, posted_at DESC;''')
    return render(request, 'zapros.html', {'output': output, 'test': output.columns})
