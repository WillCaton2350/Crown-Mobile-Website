from django.shortcuts import render

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
