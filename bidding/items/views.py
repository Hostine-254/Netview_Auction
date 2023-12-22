from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Item
from django.core.mail import send_mail  

@csrf_exempt
@login_required(login_url='login')
def additem(request):
    if request.method == 'POST':
        img1 = ' '; img2 = ' '; img3= ' '; img4 = ' '
        iname = request.POST['iname']
        prof = request.FILES['img']
        img1 = request.FILES.get('img1')
        img2 = request.FILES.get('img2')
        img3 = request.FILES.get('img3')
        img4 = request.FILES.get('img4')
        itag = request.POST['itag']
        cond = request.POST['cond']
        sdisc = request.POST['sdis']
        ldisc = request.POST['ldis']
        disc = request.POST['disc']
        price = request.POST['iprice']
        sdate=request.POST['s_date']
        omail = request.user.email

        item = Item(ownermail=omail,start_date=sdate,currentPrice=price,img1=img1,img2=img2,img3=img3,img4=img4,name=iname,profile=prof,tag=itag,condition=cond,short_description=sdisc,long_description=ldisc,discount=disc,basePrice=price)
        item.save()
        return redirect("home")
    else:
        return render(request,'upload.html')

def sub_product(request):
    id=request.GET['id']
    
    item = Item.objects.get(id=id)

    lstatus="live"

    if item.status ==lstatus:
        return render(request,"common.html",{'item':item})
    else:
        return redirect("home")  
    #print(type(item)) 
    
def sub_product_main(request):
    value = request.GET.get('value')
    
    
    if value == 'plot':
        Item.objects.filter(tag=value)
        return render(request,"view_all.html")
    elif value == 'Automobiles':
        items = Item.objects.filter(tag="Automobiles").filter(status="live")
        categ = Item.objects.filter(tag="Automobiles").filter(status="live").first()
        print(items)
        return render(request,"view_all_2.html", {'items':items,'categ':categ})
    elif value == 'electronics':
        item = Item.objects.filter(tag=value)
        return render(request,"view_all.html")
    elif value == 'furniture':
        item = Item.objects.filter(tag=value)
        print('This is the returned vlalue %s' % value)
    elif value == 'art':
        item = Item.objects.filter(tag=value)
        print('This is the returned vlalue %s' % value)
    elif value == 'machines':
        item = Item.objects.filter(tag=value)
        print('This is the returned vlalue %s' % value)
    else :
        print('Got nothing')
    return HttpResponse("good")

@login_required(login_url='login')
def biditem(request):
    id=request.GET['id']
    
    item = Item.objects.get(id=id)
    print(item)
    lstatus="live"

    if item.status ==lstatus:
        return render(request,"item_bids.html",{'item':item})
    else:
        return redirect("home")

def validate(request):
    value = request.GET.get('bidrs')
    
    iid = request.GET.get('iid')
    item = Item.objects.get(id=iid)
    if value == '':return render(request, "biditem.html",{'item':item})
    # print (iid)

    bidder = request.user
    bidderEmail = bidder.email
    # print (bidder.id)
    item_obj = Item.objects.get(id=iid)

    itemownerEmail = item_obj.ownermail

    if bidderEmail==itemownerEmail:
        return render(request,"notification.html")
    else:
        mail = item_obj.ownermail
        subject = "Online Bidding"  
        msg     = "Congratulations your item is bidded by "+bidder.email+", at Shs = "+value+". Contact your buyer by email Thank You for bidding with us."
        to      = mail  
        res     = send_mail(subject, msg, "hostineamwata2020@gmail.com", [to])


        Item.objects.filter(id=iid).update(currentPrice=value)
        Item.objects.filter(id=iid).update(highest_bidder=bidder.id)
        return redirect("home")