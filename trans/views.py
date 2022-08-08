from django.shortcuts import render
import googletrans
from googletrans import Translator

# Create your views here.
def index(request):
    context = {
        "ndict" : googletrans.LANGUAGES
    }
    if request.method == "POST":
        b = request.POST.get("bf")
        f = request.POST.get("fr")
        t = request.POST.get("to")

        tr = Translator()
        af = tr.translate(b, src=f, dest=t)
        context.update({
            "bf" : b,
            "fr" : f,
            "to" : t,
            "af" : af.text
        })
    return render(request, "trans/index.html", context)





