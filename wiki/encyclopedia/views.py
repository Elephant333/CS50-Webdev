from django.shortcuts import render

from . import util

from markdown import Markdown
markdown = Markdown()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if title in util.list_entries():
        body = util.get_entry(title)
        body_converted = markdown.convert(body)

        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "body": body_converted
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested page was not found."
        })
