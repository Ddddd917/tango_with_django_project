import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page

def populate():
    # 1. 创建一些字典，包含我们要添加的网页数据
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/'},
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/'},
        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/'}
    ]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/'},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/'}
    ]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/'},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org'}
    ]

    # 2. 创建分类字典
    cats = {
        'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
        'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
        'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16}
    }
    # 3. 遍历字典，将数据添加到数据库
    for cat, cat_data in cats.items():
        # 注意这里多了两个参数
        c = add_cat(cat, cat_data['views'], cat_data['likes'])

        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])
    # 打印添加结果
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


# 从这里开始执行
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()