from django.shortcuts import render
from .models import FeedBack
from .forms import FeedBackForm
import telebot

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        message = f'{request.POST["name"]}\n{request.POST["email"]}\n{request.POST["phone"]}\n{request.POST["message"]}'
        if form.is_valid():
            bot = telebot.TeleBot('5292944836:AAHAE2mxZglIglvV_9hSbaZyQU0i6kb4SKg')
            bot.send_message(1437957160, message)
            form.save()

    form = FeedBackForm()
    feedbacks = FeedBack.objects.all()
    content = {
        'feedbacks': feedbacks,
        'form': form,
    }
    return render(request, 'main/index.html', content)