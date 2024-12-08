from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MessageForm

def messageplatform(request):  # Renamed the function
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('messageplatform') 
        else:
            messages.error(request, 'Failed to send the message. Please try again.')
    else:
        form = MessageForm()

    return render(request, 'messageplatform.html', {'form': form})
