# views.py

from django.shortcuts import render

from num2words import num2words
# utils.py

# utils.py

# utils.py

def numberToWords(n):
    ans= num2words(n)
    return ans.title() + "  Rupees Only"




def convert(request):
    if request.method == "POST":
        number = int(request.POST.get("number"))
        words = numberToWords(number)
        return render(request, 'app7/index.html', {'number': number, 'words': words, 'cheque': True})
    return render(request, 'app7/index.html')
