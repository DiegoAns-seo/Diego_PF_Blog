from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'messages/inbox.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        recipient_id = request.POST['recipient']
        content = request.POST['content']
        Message.objects.create(
            sender=request.user,
            recipient=User.objects.get(id=recipient_id),
            content=content
        )
        return redirect('messages:inbox')
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'messages/send_message.html', {'users': users})