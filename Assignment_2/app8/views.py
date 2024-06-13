from django.shortcuts import render

import datetime

def encode_message(message):
    today = datetime.date.today()
    is_odd_day = today.day % 2 != 0

    odd_encoding = {chr(i + 64): f"{i:02d}" for i in range(1, 27)}
    even_encoding = {chr(i + 64): f"{i + 500}" for i in range(1, 27)}

    encoded_message = []

    for char in message.upper():
        if char in odd_encoding and is_odd_day:
            encoded_message.append(odd_encoding[char])
        elif char in even_encoding and not is_odd_day:
            encoded_message.append(even_encoding[char])
        else:
            encoded_message.append(char)

    return ' '.join(encoded_message)


def encode(request):
    encoded_message = ""
    if request.method == "POST":
        message = request.POST.get("message")
        encoded_message = encode_message(message)
    return render(request, 'app8/index.html', {'encoded_message': encoded_message})
# Create your views here.
