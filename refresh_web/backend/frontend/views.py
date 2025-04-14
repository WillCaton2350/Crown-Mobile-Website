from django.shortcuts import render
from .forms import ReviewForm

class index_view: 
    def index(request):
        return render(request,'index.html')
    
    def about(request):
        return render(request,'about.html')
    
    def contact(request):
        return render(request,'contact.html')
    
    def subscribe(request):
        return render(request,'subscribe.html')
    
    def unsubscribe(request):
        return render(request,'unsubscribe.html')
    
    def socials(request):
        return render(request,'socials.html')
    
    def careers(request):
        return render(request,'careers.html')
    
    def reviewForm(request):
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'home.html')
        else:
            form = ReviewForm()
            return render(request, 'contact.html', {'form': form})