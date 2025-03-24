from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'home.html')  # Hoặc HttpResponse

def chatbox_view(request):
    return render(request, 'chatbox.html')

def aboutpage(request):  # Thêm hàm này
    return render(request, 'about.html')  # Đảm bảo có template about.html