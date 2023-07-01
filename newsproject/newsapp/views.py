from django.shortcuts import render
def index(request):
    return render(request,'newsapp/index.html')
def moviesinfo(request):
    head_msg="LATEST MOVIE INFORMATION"
    msg1="RRR Movie got oscar award"
    msg2="Dasara movie public talk is superhit"
    msg3="Prabhas Movie remuneration is very high"
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)
def sportsinfo(request):
    head_msg="LATEST SPORTS INFORMATION"
    msg1="Virat Kohli to decide separate from Captain"
    msg2="Dhoni is also known as Mr cool Captain"
    msg3="IPL starts from march 31"
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)
def politicsinfo(request):
    head_msg="LATEST POLITICS INFORMATION"
    msg1="YS Jagan is the CM of Andhra Pradesh"
    msg2="KTR is one of the best minister in telangana"
    msg3="Narendra Modi is our PrimeMinister"
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)
# Create your views here.
