from django.shortcuts import render

posts = [
    {
        'author': 'Wood',
        'title': 'Wood vs dog or wood and dog',
        'content': 'First post content',
        'date_posted': 'Fed 23, 2021'
    },
    {
        'author': 'Goat',
        'title': 'The pycologogical aspects of bullying',
        'content': 'Second post content',
        'date_posted': 'July 2, 2021'
    },
    {
        'author': 'Gaef',
        'title': 'Living with makeup addiction',
        'content': 'Second post content',
        'date_posted': 'July 2, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})