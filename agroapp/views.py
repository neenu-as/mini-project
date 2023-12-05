import datetime

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from agroapp.models import *


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def logout(request):
    auth.logout(request)
    return render(request,"loginindex.html")



def home(request):
    return render(request,"homeindex.html")
def aboutus(request):
    return render(request, 'ABOUT_US.html')
def contactus(request):
    return render(request, 'CONTACT_US.html')

def login(request):
    return render(request, 'loginindex.html')

def logincheck(request):
    uname=request.POST['textfield']
    pswd=request.POST['textfield2']
    try:

        ob=login_table.objects.get(Username=uname, password=pswd)
        if ob.type == "admin":
            ob1=auth.authenticate(username='admin',password='admin')
            if ob1 is not None:
                auth.login(request,ob1)
            request.session['lid'] = ob.id
            return HttpResponse('''<script>window.location='/hmpg'</script>''')
        elif ob.type == "farmer":
            ob1 = auth.authenticate(username='admin', password='admin')
            if ob1 is not None:
               auth.login(request,ob1)
            request.session['fid'] = ob.id
            return HttpResponse('''<script>window.location='/hompg'</script>''')
        elif ob.type == "staff":
          ob1 = auth.authenticate(username='admin', password='admin')
          if ob1 is not None:
              auth.login(request,ob1)
          request.session['oid'] = ob.id
          return HttpResponse('''<script>window.location='/homepg'</script>''')
        # elif ob.type == "shops":
        #     ob1 = auth.authenticate(username='admin', password='admin')
        #     if ob1 is not None:
        #         auth.login(request.ob1)
        #     request.session['sid'] = ob.id
        #     return HttpResponse('''<script>window.location='/hmpage'</script>''')
        elif ob.type == "user":
            ob1 = auth.authenticate(username='admin', password='admin')
            if ob1 is not None:
                auth.login(request,ob1)
            request.session['uid'] = ob.id
            return HttpResponse('''<script>window.location='/hompage'</script>''')

        else :
          return HttpResponse('''<script>alert('INVALID');window.location='/'</script>''')
    except:
        return HttpResponse('''<script>alert('INVALID USER NAME OR PASSWORD');window.location='/'</script>''')


def freg(request):
    return render(request, 'farmerregisterindex.html')

def farmer_reg(request):
    nm=request.POST['textfield']
    gd=request.POST['radiobutton']
    dob=request.POST['date']
    wrd=request.POST['select2']
    pl=request.POST['textfield4']
    pst = request.POST['textfield5']
    pin = request.POST['textfield6']
    phn = request.POST['textfield7']
    eml = request.POST['textfield8']
    img = request.FILES['file']
    fs = FileSystemStorage()
    fn = fs.save(img.name, img)
    adhr=request.POST['textfield9']
    unm = request.POST['textfield10']
    psd = request.POST['textfield11']

    ob=login_table()
    ob.Username=unm
    ob.password=psd
    ob.type="farmer"
    ob.save()

    obu=farmer()
    obu.name=nm
    obu.gender=gd
    obu.DOB=dob
    obu.ward=wrd
    obu.place=pl
    obu.post = pst
    obu.pin=pin
    obu.phon = phn
    obu.email = eml
    obu.photo = fn
    obu.Adhaar=adhr
    obu.LOGINID=ob
    obu.save()
    return HttpResponse('''<script>alert('Registerd');window.location='login'</script>''')
@login_required(login_url="/")
def manageproduct(request):
    ob=product.objects.filter(FARMER__LOGINID__id=request.session['fid']).order_by('-id')
    date = timezone.now().date()
    print(date, "iiiiiiiiiiiii")
    for i in ob:
        if i.date == date:
            i.delete()
    return render(request, 'farmer/sell product.html',{'val':ob})
@login_required(login_url="/")
def addnewproduct(request):
    today = timezone.now().date()
    return render(request, 'farmer/insert product.html',{'today':str(today)})
@login_required(login_url="/")
def addproduct(request):
    nm = request.POST['textfield']
    qnty = request.POST['textfield2']
    priz = request.POST['textfield3']
    date = request.POST['textfield4']
    img = request.FILES['file']
    fs = FileSystemStorage()
    fn = fs.save(img.name, img)
    obu = product()
    obu.name = nm
    obu.quantity = qnty
    obu.price = priz
    obu.date=date
    obu.image= fn
    obu.FARMER=farmer.objects.get(LOGINID__id=request.session['fid'])

    obu.save()
    return HttpResponse('''<script>alert('Added');window.location='/manageproduct'</script>''')


@login_required(login_url="/")
def edit_prdct(request,id):
    ob2=product.objects.get(id=id)
    request.session['ffid']=id
    today = timezone.now().date()
    return render(request,'farmer/edit_fproduct.html',{'val':ob2 ,'date':str(ob2.date),"today":str(today)})

@login_required(login_url="/")
def edit_fprdct(request):
    if 'file' in request.FILES:
        nm = request._post['textfield']
        qnty = request._post['textfield2']
        prz =request._post['textfield3']
        date=request._post['textfield4']
        img =request.FILES['file']
        fs = FileSystemStorage()
        fsave =fs.save(img.name,img)
        ob = product.objects.get(id=request.session['ffid'])
        ob.name = nm
        ob.quantity = qnty
        ob.price =  prz
        ob.date= date
        ob. image = fsave
        ob.save()

    else:
         nm = request._post['textfield']
         qnty= request._post['textfield2']
         prz  = request._post['textfield3']
         date= request._post['textfield4']
         ob = product.objects.get(id=request.session['ffid'])
         ob.name = nm
         ob.quantity = qnty
         ob.price =  prz
         ob.date=date
         ob.save()
    return HttpResponse('''<script>alert("edited");window.location="/manageproduct"</script>''')

def dltprdct(request,id):
    ob2=product.objects.get(id=id)
    ob2.delete()

    return HttpResponse('''<script>alert("Deleted");window.location="/manageproduct"</script>''')






def ureg(request):
    return render(request, 'userregisterindex.html')


def user_reg(request):
    nm = request.POST['textfield']
    gd = request.POST['radiobutton']
    dob = request.POST['date']
    pl = request.POST['textfield2']
    pst = request.POST['textfield5']
    pin = request.POST['textfield6']
    phn = request.POST['textfield7']
    eml = request.POST['textfield8']
    img = request.FILES['file']
    fs = FileSystemStorage()
    fn = fs.save(img.name, img)
    unm = request.POST['textfield9']
    psd = request.POST['textfield10']

    ob = login_table()
    ob.Username = unm
    ob.password = psd
    ob.type = "user"
    ob.save()

    obu = user()
    obu.name = nm
    obu.gender = gd
    obu.age = dob
    obu.place = pl
    obu.post = pst
    obu.pin = pin
    obu.phon = phn
    obu.email = eml
    obu.photo = fn
    obu.LOGINID = ob
    obu.save()
    return HttpResponse('''<script>alert('Registerd');window.location='login'</script>''')
@login_required(login_url="/")
def viewshops(request):
    ob = shops.objects.all()
    return render(request, 'admin/view shops.html',{'val':ob})
@login_required(login_url="/")
def search_shp(request):
    name =request.POST['textfield']
    ob1 =shops.objects.filter(name__icontains=name)
    return render(request,'admin/view shops.html',{'val':ob1})
def dltshp(request,id):
    ob2=login_table.objects.get(id=id)
    ob2.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/viewshops"</script>''')
@login_required(login_url="/")
def edit_shop(request,id):
    ob2=shops.objects.get(id=id)
    request.session['sid']=id
    return render(request,'admin/edit_shop.html',{'val':ob2})@login_required(login_url="/")
def edit_shp(request):
    if 'file' in request.FILES :
        nm = request._post['textfield']
        pl = request._post['textfield2']
        pst =request._post['textfield3']
        pin =request._post['textfield4']
        phn =request._post['textfield5']
        eml =request._post['textfield6']
        img =request.FILES['file']
        fs = FileSystemStorage()
        fsave =fs.save(img.name,img)
        ob = shops.objects.get(id=request.session['sid'])
        ob.name = nm
        ob.place = pl
        ob.post = pst
        ob.pin = pin
        ob.phon = phn
        ob.email = eml
        ob.photo = fsave
        ob.save()
        return HttpResponse('''<script>alert("edited");window.location="/viewshops"</script>''')
    else:
        nm = request._post['textfield']
        pl = request._post['textfield2']
        pst = request._post['textfield3']
        pin = request._post['textfield4']
        phn = request._post['textfield5']
        eml = request._post['textfield6']

        ob = shops.objects.get(id=request.session['sid'])
        ob.name = nm
        ob.place = pl
        ob.post = pst
        ob.pin = pin
        ob.phon = phn
        ob.email = eml
        ob.save()
        return HttpResponse('''<script>alert("edited");window.location="/viewshops"</script>''')








@login_required(login_url="/")
def addshp(request):
    return render(request, 'admin/Add new shops.html')@login_required(login_url="/")
def addedshop(request):
    nm = request.POST['textfield']
    pl = request.POST['textfield2']
    pst = request.POST['textfield3']
    pin = request.POST['textfield4']
    img = request.FILES['file']
    fs = FileSystemStorage()
    fn = fs.save(img.name, img)
    phn = request.POST['textfield5']
    eml = request.POST['textfield6']
    unm = request.POST['textfield7']
    psd = request.POST['textfield8']
    ob = login_table()
    ob.Username = unm
    ob.password = psd
    ob.type = "shop"
    ob.save()
    obu = shops()
    obu.name = nm
    obu.place = pl
    obu.post = pst
    obu.pin = pin
    obu.place = pl
    obu.phon = phn
    obu.email = eml
    obu.photo = fn
    obu.LOGINID = ob
    obu.save()
    return HttpResponse('''<script>alert('Added');window.location='/viewshops'</script>''')
@login_required(login_url="/")
def viewstf(request):
    ob=officer.objects.all().order_by('-id')
    return render(request,'admin/vie staff.html',{'val':ob})
@login_required(login_url="/")
def search_stf(request):
    name = request.POST['textfield']
    ob1 = officer.objects.filter(name__icontains=name)
    return render(request, 'admin/vie staff.html',{'val':ob1})
@login_required(login_url="/")
def dltstf(request,id):
    ob2 = login_table.objects.get(id=id)
    ob2.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/viewstf"</script>''')
@login_required(login_url="/")
def edit_staff(request,id):
    ob2=officer.objects.get(id=id)
    request.session['oid'] = id
    return render(request,'admin/edit_staff.html',{'val':ob2})
@login_required(login_url="/")
def edit_stf(request):
    if 'file' in request.FILES:
        nm = request.POST['textfield']
        gd = request.POST['radiobutton']
        pl = request.POST['textfield2']
        pst = request.POST['textfield3']
        pin = request.POST['textfield4']
        img = request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(img.name, img)
        phn = request.POST['textfield5']
        eml = request.POST['textfield6']

        ob = officer.objects.get(id=request.session['oid'])
        ob.name = nm
        ob.gender = gd
        ob.place= pl
        ob.post= pst
        ob.pin=pin
        ob.photo=fsave
        ob.phon=phn
        ob.email=eml
        ob.save()
        return HttpResponse(''' <script>alert("edited");window.location="/viewstf"</script>''')
    else:
        nm = request.POST['textfield']
        gd = request.POST['radiobutton']
        pl = request.POST['textfield2']
        pst = request.POST['textfield3']
        pin = request.POST['textfield4']
        phn = request.POST['textfield5']
        eml = request.POST['textfield6']

        ob = officer.objects.get(id=request.session['oid'])
        ob.name = nm
        ob.gender = gd
        ob.place = pl
        ob.post = pst
        ob.pin = pin
        ob.phon=phn
        ob.email = eml
        ob.save()
        return HttpResponse(''' <script>alert("edited");window.location="/viewstf"</script>''')
@login_required(login_url="/")
def addstf(request):
    return render(request, 'admin/ADD NEW STAFF.html')

@login_required(login_url="/")
def addedstaff(request):
    nm=request.POST['textfield']
    gd=request.POST['radiobutton']
    pl=request.POST['textfield2']
    pst = request.POST['textfield3']
    pin = request.POST['textfield4']
    img = request.FILES['file']
    fs=FileSystemStorage()
    fn=fs.save(img.name,img)
    phn = request.POST['textfield5']
    eml = request.POST['textfield6']
    unm = request.POST['textfield7']
    psd = request.POST['textfield8']

    ob=login_table()
    ob.Username=unm
    ob.password=psd
    ob.type="staff"
    ob.save()

    obu=officer()
    obu.name=nm
    obu.gender=gd
    obu.place=pl
    obu.post = pst
    obu.pin = pin
    obu.place = pl
    obu.phon = phn
    obu.email = eml
    obu.photo = fn
    obu.LOGINID=ob
    obu.save()
    return HttpResponse('''<script>alert('Added');window.location='/viewstf'</script>''')


@login_required(login_url="/")
def hmpg(request):
    return render(request, 'admin/admi_2_index.html')
    # return render(request, 'admin/Admin_new_index.html')
@login_required(login_url="/")
def sndrply(request,id):
    request.session['rid']=id
    return render(request, 'admin/send reply.html')
@login_required(login_url="/")
def sendedreply(request):
    re=request.POST['textfield2']
    ob=complaint.objects.get(id=request.session['rid'])
    ob.reply=re
    ob.save()
    return HttpResponse('''<script>alert('Sent');window.location='/viewcmpnt'</script>''')
@login_required(login_url="/")
def viewcmpnt(request):
    ob = complaint.objects.all()
    return render(request, 'admin/view complaint.html',{'val':ob})
@login_required(login_url="/")
def search_cmpnt(request):
    date = request.POST['textfield']
    ob1 = complaint.objects.filter(date=date)
    return render(request, 'admin/view complaint.html', {'val': ob1,"d":date})

@login_required(login_url="/")
def viewusers(request):
    my_objects = user.objects.all( ).order_by('-id')
    # Set the number of items per page
    items_per_page = 4

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request, 'admin/view users.html',{'my_objects':my_objects})


@login_required(login_url="/")


def search_user(request):
    name = request.POST['textfield']
    my_objects = user.objects.filter(name__icontains=name)

    # Set the number of items per page
    items_per_page = 5

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request, 'admin/view users.html',{'my_objects':my_objects})

from django.utils import timezone
@login_required(login_url="/")
def aplschms(request):
    ob=schemes.objects.filter(tdate__gte=datetime.datetime.today())
    print(ob,"kkkkkkkkkkkkk")
    date=timezone.now().date()
    print(date,"iiiiiiiiiiiii")
    for i in ob:
        if i.tdate == date:
            i.delete()
    return render(request, 'farmer/apply schems.html',{'val':ob})





@login_required(login_url="/")
def hompg(request):
    return render(request,'farmer/farmerindex.html')
@login_required(login_url="/")
def inrtprdct(request):
    return render(request, 'farmer/insert product.html')

@login_required(login_url="/")
def snddbtvwrply(request):
    ob = doubts.objects.filter(FARMER__LOGINID__id=request.session['fid'])
    return render(request,'farmer/send doubt and view reply.html',{'val':ob})
@login_required(login_url="/")
def srchsnddbtvwrply(request):
    dt=request.POST['textfield']
    ob = doubts.objects.filter(FARMER__LOGINID__id=request.session['fid'],date=dt)
    return render(request,'farmer/send doubt and view reply.html',{'val':ob})
@login_required(login_url="/")
def snddbt(request):
    ob=officer.objects.all()
    return render(request,'farmer/send doubts.html',{'v':ob})
@login_required(login_url="/")
def snd_dobt(request):
    dbt=request.POST['textfield2']
    ofc=request.POST['select']
    ob=doubts()
    ob.doubt=dbt
    ob.FARMER=farmer.objects.get(LOGINID__id=request.session['fid'])
    ob.OFFICER=officer.objects.get(id=ofc)
    ob.date=datetime.datetime.today()
    ob.reply='pending'
    ob.save()
    return HttpResponse('''<script>alert('send successfully....');window.location='/snddbtvwrply'</script>''')
#










# def viwfrtzr(request):
#     ob = fertilizer.objects.all()
#
#     return render(request, 'farmer/view fertilizer.html',{'val':ob})
#
# def search_viewfertilizer(request):
#     name =request.POST['textfield']
#     ob1 =fertilizer.objects.filter(name__icontains=name)
#     return render(request,'farmer/view fertilizer.html',{'val':ob1})
@login_required(login_url="/")
def viwordr(request):
    ob=order.objects.filter(status="pending")
    return render(request, 'farmer/view order.html',{'val':ob})
@login_required(login_url="/")
def viwordr_details(request,id):
    request.session['oid']=id
    ob=order_details.objects.filter(ORDER__id=id)
    tp=0
    for i in ob:
        i.total=int(i.quantity)*int(i.PRODUCT.price)
        tp=tp+i.total
    return render(request,'farmer/view order details.html',{'val':ob,"tp":tp})
@login_required(login_url="/")
def ordr_accept(request):
    return render(request,'farmer/view order details.html')
@login_required(login_url="/")
def ordr_reject(request):
    return render(request,'farmer/view order details.html')
@login_required(login_url="/")
def viwschms(request):
    return render(request, 'farmer/view schem status.html')

@login_required(login_url="/")
def view_s_product(request):
    my_objects = subsidy_product.objects.all()

    # Set the number of items per page
    items_per_page = 5

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)
    return render(request, 'farmer/view subsidy products.html',{'my_objects': my_objects})







@login_required(login_url="/")

def srchsbsdy_prodcts(request):
    n=request.POST['select']
    my_objects=subsidy_product.objects.filter(category=n)

    # Set the number of items per page
    items_per_page = 5

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)
    return render(request, 'farmer/view subsidy products.html', {'my_objects': my_objects})
@login_required(login_url="/")

def ordr_s_product(request,id):
    ob = subsidy_product.objects.get(id=id)
    request.session['g']=id
    return render(request, 'farmer/order subsidy product.html',{'val':ob})
@login_required(login_url="/")
def ordr_subsdy_product(request):
    from datetime import date
    qty=request.POST['textfield4']
    print(qty)
    pob=subsidy_product.objects.get(id=request.session['g'])
    if int(qty) <= int(pob.quantity):
        ob=s_product_request()
        ob.SPRODUCT=subsidy_product.objects.get(id=request.session['g'])
        ob.FARMER=farmer.objects.get(LOGINID_id=request.session['fid'])
        ob.status="pending"
        ob.quantity=qty
        ob.date=datetime.today()
        ob.save()
        ob1=subsidy_product.objects.get(id=request.session['g'])
        ob1.quantity=int(ob1.quantity)-int(qty)
        ob1.save()
        print(ob.quantity)
        return HttpResponse('''<script>alert('Sent');window.location='/view_s_product#about'</script>''')
    else:
        return HttpResponse('''<script>alert('Out of stock');window.location='/view_s_product#about'</script>''')
@login_required(login_url="/")
def S_order_history(request,id):
    ob = sorder_details.objects.filter(ORDER__id=id)
    return render(request,'farmer/order_s_history.html',{'val': ob})
@login_required(login_url="/")
def view_s_order(request):
    ob=s_product_request.objects.filter(status='ordered',FARMER__LOGINID__id=request.session['fid'])
    print(ob,"=====================")
    return render(request,'farmer/my_s_orders.html',{'val':ob})
@login_required(login_url="/")
def ordrsprdctcode(request):
    btn=request.POST['Submit']
    if btn == 'ORDER NOW':
            print(request.session['g'],"kiiiiiiiiiiiiiiiiiii")
            qty=request.POST['textfield4']
            qq=subsidy_product.objects.get(id=request.session['g'])
            tt = float(qq.price)* float(qty)
            stock = float(qq.quantity)
            print(stock,qty,"jjjjjjjjjjjjjjjjjjjjjj")
            nstk = float(stock) - float(qty)
            if stock >= float(qty):
                up=subsidy_product.objects.get(id=request.session['g'])
                up.quantity=nstk
                up.save()
                qt=s_product_request()
                qt.date=datetime.datetime.today()
                qt.FARMER=farmer.objects.get(LOGINID=request.session['fid'])
                qt.status='pending'
                qt.price=tt
                qt.save()
                qty1=sorder_details()
                qty1.quantity=qty
                qty1.PRODUCT=subsidy_product.objects.get(id=request.session['g'])
                qty1.ORDER=qt
                qty1.date=datetime.datetime.today()
                qty1.save()
                return HttpResponse('''<script>alert('placed order successfuly');window.location='/view_s_product#main'</script>''')
            else:
                return HttpResponse('''<script>alert('out of stock');window.location='/view_s_product#main'</script>''')
    else:

        qty=request.POST['textfield4']
        qq=subsidy_product.objects.get(id=request.session['g'])
        tt = float(qq.price)* float(qty)
        stock = float(qq.quantity)
        print(stock,qty,"jjjjjjjjjjjjjjjjjjjjjj")
        nstk = float(stock) - float(qty)
        if stock >= float(qty):
            up=subsidy_product.objects.get(id=request.session['g'])
            up.quantity=nstk
            up.save()
            q=s_product_request.objects.filter(FARMER=farmer.objects.get(LOGINID__id=request.session['fid']),status='CART')
            if len(q)==0:
                qt=s_product_request()
                qt.date=datetime.datetime.today()
                qt.FARMER=farmer.objects.get(LOGINID=request.session['fid'])
                qt.status='CART'
                qt.price=tt
                qt.save()
                qty1=sorder_details()
                qty1.quantity=qty
                qty1.PRODUCT=subsidy_product.objects.get(id=request.session['g'])
                qty1.ORDER=qt
                qty1.date = datetime.datetime.today()
                qty1.save()
                return HttpResponse('''<script>alert('ADD TO CART');window.location='/view_s_product#main'</script>''')
            else:
                total = float(q[0].price) + float(tt)
                qt=s_product_request.objects.get(id=q[0].id)
                qt.price=total
                qt.save()
                qty1=sorder_details.objects.filter(PRODUCT__id=request.session['g'],ORDER__id=q[0].id)
                if len(qty1)==0:
                    qqt=sorder_details()
                    qqt.ORDER=q[0]
                    qqt.PRODUCT=subsidy_product.objects.get(id=request.session['g'])
                    qqt.quantity=qty
                    qqt.date=datetime.datetime.today()
                    qqt.save()
                else:
                    qry1=sorder_details.objects.get(id=qty1[0].id)
                    quty=float(qty1[0].quantity) + float(qty)
                    qry1.quantity=qty
                    qry1.date=datetime.datetime.today()
                    qry1.save()
                return HttpResponse('''<script>alert('ADD TO CART');window.location='/view_s_product#main'</script>''')
        else:
            return HttpResponse('''<script>alert('OUT OF STOCK');window.location='/view_s_product#main'</script>''')


@login_required(login_url="/")
def cancel_s_order(request, id, qty):
        obd = sorder_details.objects.get(id=id)
        request.session['oid']=obd.ORDER.id
        obp = subsidy_product.objects.get(id=obd.PRODUCT.id)
        obp.quantity = float(obp.quantity) + float(qty)
        obp.save()
        obd.delete()
        ob2 = sorder_details.objects.filter(ORDER__id=request.session['oid'])
        if len(ob2) == 0:
            ob1=s_product_request.objects.get(id=request.session['oid'])
            ob1.delete()
        return redirect('/view_s_order')


@login_required(login_url="/")
def view_s_cart(request):
    try:
        OB1 = s_product_request.objects.get(FARMER__LOGINID__id=request.session['fid'], status='CART')
        ob = sorder_details.objects.filter(ORDER__FARMER__LOGINID__id=request.session['fid'], ORDER__status='CART')
        return render(request, 'farmer/view_s_ cart.html', {'val': ob, 'total': OB1})
    except:
        ob = sorder_details.objects.filter(ORDER__FARMER__LOGINID__id=request.session['fid'], ORDER__status='CART')
        return render(request, 'farmer/view_s_ cart.html', {'val': ob, 'total': 0})

@login_required(login_url="/")
def add_to_cart(request):
    return render(request, 'farmer/view_s_ cart.html')

@login_required(login_url="/")
def S_orderstatus(request):
    ob = s_product_request.objects.filter(FARMER__LOGINID__id=request.session['fid'])
    return render(request, 'farmer/Subsidyorder status.html',{'val':ob})
@login_required(login_url="/")
def S_order_status(request,id):
    ob = sorder_details.objects.filter(ORDER__id=id)
    return render(request, 'farmer/Subsid_item_ status.html',{'val':ob})
@login_required(login_url="/")
def addschms(request):
    today = timezone.now().date()
    return render(request, 'officer/add schems.htmll',{'today':str(today)})
@login_required(login_url="/")
def homepg(request):
    return render(request, 'officer/officer_2_index.html')
@login_required(login_url="/")
def rply(request):
    return render(request, 'officer/reply.html')



@login_required(login_url="/")
def updtschms(request):
    ob = schemes.objects.all().order_by('-id')
    return render(request, 'officer/update upcomming schems.html', {'val': ob})


@login_required(login_url="/")
def addschemes(request):
    today = timezone.now().date()
    return render(request, 'officer/add schems.html',{'today':str(today)})
@login_required(login_url="/")
def add_schms(request):
    nm = request.POST['textfield']
    documents = request.POST['textfield2']
    fdate = request.POST['textfield3']
    tdate = request.POST['textfield4']
    details = request.POST['textfield5']
    obu =schemes()
    obu.name= nm
    obu.documents=  documents
    obu.fdate= fdate
    obu.tdate= tdate
    obu.details= details
#     obu.OFFICER = officer.objects.get(LOGINID__id=request.session['oid'])
    obu.save()
    return HttpResponse('''<script>alert('Added');window.location='/updtschms'</script>''')
@login_required(login_url="/")
def edit_schemes(request,id):
    ob = schemes.objects.get(id=id)
    request.session['schid']=id
    today = timezone.now().date()
    return render(request, 'officer/edit_schemes.html', {'val': ob,'fdate':str(ob.fdate),'tdate':str(ob.tdate),'today':str(today)})
@login_required(login_url="/")
def edit_schemescode(request):
    nm = request.POST['textfield']
    documents = request.POST['textfield2']
    fdate = request.POST['textfield3']
    tdate = request.POST['textfield4']
    details = request.POST['textfield5']
    obu = schemes.objects.get(id=request.session['schid'])
    obu.name = nm
    obu.documents = documents
    obu.fdate = fdate
    obu.tdate = tdate
    obu.details = details
    #     obu.OFFICER = officer.objects.get(LOGINID__id=request.session['oid'])
    obu.save()

    return HttpResponse('''<script>alert('edited');window.location='/updtschms'</script>''')



# def editschem(request):
#     return render(request, 'officer/edit_schemes.html')
@login_required(login_url="/")
def dlt_schms(request,id):
    ob=schemes.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('deleted');window.location='/updtschms'</script>''')

@login_required(login_url="/")
def viwdbtrply(request):
    print(request.session['oid'],"llllllllllllllllll")
    ob=doubts.objects.filter(OFFICER__LOGINID__id=request.session['oid'])
    return render(request,'officer/view doubts & send reply.html',{'val':ob})

@login_required(login_url="/")
def viwdbtrplysearch(request):
    date=request.POST['date']
    print(request.session['oid'],"llllllllllllllllll")
    ob=doubts.objects.filter(OFFICER__LOGINID__id=request.session['oid'],date=date)
    return render(request,'officer/view doubts & send reply.html',{'val':ob})



@login_required(login_url="/")
def sendrply(request,id):
    request.session['rid'] = id
    return render(request, 'officer/reply.html')

@login_required(login_url="/")
def sendedreplytodoubt(request):
    re=request.POST['textfield']
    ob=doubts.objects.get(id=request.session['rid'])
    ob.reply=re
    ob.save()
    return HttpResponse('''<script>alert('Sent');window.location='/viwdbtrply'</script>''')




@login_required(login_url="/")
def viwschmverfy(request):
    return render(request, 'officer/view schem request & verify.html')
@login_required(login_url="/")

def add_manage_s_prdt(request):
    ob=subsidy_product.objects.all().order_by('-id')
    return render(request, 'officer/add &manage subsidy product.html',{'val':ob})
@login_required(login_url="/")
def srchsbsdy_products(request):
    n=request.POST['select']
    ob=subsidy_product.objects.filter(category=n)
    return render(request, 'officer/add &manage subsidy product.html', {'val': ob})

@login_required(login_url="/")
def addsubsidy_product(request):
    return render(request,'officer/Add subsidy product.html')

@login_required(login_url="/")
def add_s_prdt(request):
    nm = request.POST['textfield']
    stock = request.POST['textfield2']
    category = request.POST['select']
    details = request.POST['textfield3']
    price = request.POST['textfield4']
    img = request.FILES['file']
    fs = FileSystemStorage()
    fn = fs.save(img.name,img)
    obu =subsidy_product()
    obu. sproduct= nm
    obu. details= details
    obu. category= category
    obu. price= price
    obu. quantity= stock
    obu.image= fn
    obu.OFFICER = officer.objects.get(LOGINID__id=request.session['oid'])
    obu.save()
    return HttpResponse('''<script>alert('Added');window.location='/add_manage_s_prdt'</script>''')

#
#
@login_required(login_url="/")
def edit_sprdct(request,id):
    ob2=subsidy_product.objects.get(id=id)
    request.session['spid']=id
    # print(ob2.sproduct,"Rrrrrrrr")
    return render(request,'officer/edit_sproduct.html',{'val':ob2})
@login_required(login_url="/")
def edit_subsidyprdct(request):
    if 'file' in request.FILES:
        nm = request._post['textfield']
        img =request.FILES['file']
        price=request.POST['textfield4']
        fs = FileSystemStorage()
        fsave =fs.save(img.name,img)
        # catgry = request._post['select']
        stck = request._post['textfield2']
        detls = request._post['textfield3']
        ob =subsidy_product.objects.get(id=request.session['spid'])
        ob.sproduct= nm
        ob.image= img
        ob.details =detls
        ob.price = price
        ob.quantity= stck
        ob. image = fsave
        ob.save()
#
    else:
         nm = request._post['textfield']
         stck = request._post['textfield2']
         detls = request._post['textfield3']
         price = request._post['textfield4']
         ob = subsidy_product.objects.get(id=request.session['spid'])
         ob.sproduct = nm
         ob.details =detls
         ob.quantity= stck
         ob.price= price
         ob.save()
    return HttpResponse('''<script>alert("edited");window.location="/add_manage_s_prdt"</script>''')

@login_required(login_url="/")
def dltsprdct(request,id):
    ob2=subsidy_product.objects.get(id=id)
    ob2.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/add_manage_s_prdt"</script>''')
@login_required(login_url="/")
def s_prdct_order(request):
    ob1=s_product_request.objects.all().order_by('-id')
    # ob=sorder_details.objects.filter(ORDER__status='pending',PRODUCT__OFFICER__LOGINID__id=request.session['oid'])
    # print(ob,"======================")
    return render(request, 'officer/order from farmer.html',{'val':ob1})
@login_required(login_url="/")
def s_prdct_order1(request,id):
    ob1=sorder_details.objects.filter(ORDER__id=id)
    # ob=sorder_details.objects.filter(ORDER__status='pending',PRODUCT__OFFICER__LOGINID__id=request.session['oid'])
    # print(ob,"======================")
    return render(request, 'officer/order_s_history.html',{'val':ob1})

@login_required(login_url="/")
def accept_s_order(request,id):
    ob=s_product_request.objects.get(id=id)
    ob.status='ordered'
    ob.save()
    return HttpResponse('''<script>alert("Accepted....");window.location="/s_prdct_order"</script>''')

@login_required(login_url="/")
def reject_s_order(request,id):
    ob = s_product_request.objects.get(id=id)
    ob.status = 'rejected'
    ob.save()
    obd = sorder_details.objects.filter(ORDER__id=id)
    for i in obd:
        obp = subsidy_product.objects.get(id=i.PRODUCT.id)
        obp.quantity = float(obp.quantity) + float(i.quantity)
        obp.save()
    return HttpResponse('''<script>alert("Rejected...");window.location="/s_prdct_order"</script>''')


@login_required(login_url="/")
def viewfarmerinfo(request):
    ob = farmer.objects.all()
    obo=order.objects.filter(status='ORDER')
    olist=[]
    for i in obo:
        olist.append(i.id)
    for i in ob:
        obnum=order_details.objects.filter(PRODUCT__FARMER__id=i.id,ORDER__id__in=olist)
        oclist=[]
        for j in obnum:
            if j.ORDER.id not in oclist:
                oclist.append(j.ORDER.id)
        i.pin=len(oclist)
    for i in ob:
        print(i.pin)
    # ob=ob.order_by('-pin')
    # for i in ob:
    #     print(i.pin)
    return render(request, 'officer/view farmer info.html', {'val': ob})

@login_required(login_url="/")
def srchfarmerinfo(request):
    n=request.POST['textfield']
    ob = farmer.objects.filter(name__icontains=n)
    obo = order.objects.filter(status='ORDER')
    olist = []
    for i in obo:
        olist.append(i.id)
    for i in ob:
        obnum = order_details.objects.filter(PRODUCT__FARMER__id=i.id, ORDER__id__in=olist)
        oclist = []
        for j in obnum:
            if j.ORDER.id not in oclist:
                oclist.append(j.ORDER.id)
        i.pin = len(oclist)
    for i in ob:
        print(i.pin)
    return render(request, 'officer/view farmer info.html', {'val': ob})

@login_required(login_url="/")
def viwprdct(request,id):
    ob = product.objects.filter(FARMER__id=id)
    for i in ob:
        obnum= order_details.objects.filter(PRODUCT__id=id)
        oclist = []
        for j in obnum:
            if j.id not in oclist:
                oclist.append(j.id)
        i.pin = len(oclist)
    for i in ob:
        print(i.pin)
    return render(request, 'officer/view product for sale.html',{'val':ob})


@login_required(login_url="/")
def ordrrqst(request,id):
    ob= order_details.objects.filter(PRODUCT__id=id)
    for i in ob:
        i.tp=float(i.quantity)*float(i.PRODUCT.price)
    return render(request, 'officer/view ordr rqst.html',{'val':ob})


@login_required(login_url="/")
def acceptorder(request,id):
    ob=order.objects.get(id=id)
    ob.status='Accepted'
    ob.save()
    return HttpResponse('''<script>alert('Accepted');window.location='/homepg'</script>''')

@login_required(login_url="/")
def rejectorder(request,id):
    ob=order.objects.get(id=id)
    ob.status='Rejected'
    ob.save()
    obd=order_details.objects.filter(ORDER__id=id)
    for i in obd:
        obp=i.PRODUCT
        obp.quantity=float(i.quantity)+float(obp.quantity)
        obp.save()
    return HttpResponse('''<script>alert('Rejected');window.location='/homepg'</script>''')



def updtinfoferlzr(request):
    ob = fertilizer.objects.all()
    return render(request, 'shop/update info fertilizer.html',{'val':ob})


def dlt_frtzr(request,id):
    ob2=fertilizer.objects.get(id=id)
    ob2.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/updtinfoferlzr"</script>''')

def search_ftlzr(request):
    name =request.POST['textfield']
    ob1 =fertilizer.objects.filter(name__icontains=name)
    return render(request,'shop/update info fertilizer.html',{'val':ob1})



def edit_fertlzr(request,id):
    ob2=fertilizer.objects.get(id=id)
    request.session['fid']=id
    return render(request,'shop/edit fertilizer.html',{'val':ob2})


def edit_ftlzr(request):
    nm = request.POST['textfield']
    prz = request.POST['textfield2']
    qty = request.POST['textfield3']
    dtls = request.POST['textfield4']
    ob = fertilizer.objects.get(id=request.session['fid'])
    ob.name = nm
    ob.price = prz
    ob.quantity=qty
    ob.details=dtls
    ob.save()
    return HttpResponse('''<script>alert("edited");window.location="updtinfoferlzr"</script>''')




def addferlzr(request):
    return render(request, 'shop/add fertilizer.html')

def fertilizer_info(request):
    nm = request.POST['textfield']
    prz = request.POST['textfield2']
    qty = request.POST['textfield3']
    dtls = request.POST['textfield4']
    obu = fertilizer()
    obu.name = nm
    obu.price = prz
    obu.quantity = qty
    obu.details =dtls
    obu.SHOPS=shops.objects.get(LOGINID=request.session['sid'])
    obu.save()
    return HttpResponse('''<script>alert('Added');window.location='/updtinfoferlzr'</script>''')



def hmpage(request):
    return render(request, 'shop/home page.html')

def sbsidy(request):
    ob = subsidy.objects.all()
    return render(request, 'shop/subsidy.html',{'val':ob})


def search_subsidy(request):
    name =request.POST['textfield']
    ob1 =subsidy.objects.filter(name__icontains=name)
    return render(request,'shop/subsidy.html',{'val':ob1})


def dlt_subsidy(request,id):
    ob2=subsidy.objects.get(id=id)
    ob2.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/sbsidy"</script>''')





def edit_subsidy(request,id):
    ob2=subsidy.objects.get(id=id)
    request.session['shid']=id
    return render(request,'shop/edit subsidy.html',{'val':ob2})


def edit_sbsdy(request):
    snm = request.POST['textfield']
    amnt = request.POST['textfield3']
    ob = subsidy.objects.get(id=request.session['shid'])
    ob.name = snm
    ob.amount=amnt
    ob.save()
    return HttpResponse('''<script>alert("edited");window.location="sbsidy"</script>''')

def addsbsidy(request):
    ob= fertilizer.objects.all()
    return render(request, 'shop/add subsidy.html',{'val':ob})

def add_subsidy(request):
    snm = request.POST['textfield']
    amnt = request.POST['textfield3']
    fer = request.POST['select']
    obu = subsidy()
    obu.name = snm
    obu.amount = amnt
    obu.FERTILIZER=fertilizer.objects.get(id=fer)
    obu.save()
    return HttpResponse('''<script>alert('Added');window.location='/sbsidy'</script>''')




def addviwprdctratng(request):
    return render(request, 'user/add & view product rating.html')
def addprdctratng(request):
    return render(request, 'user/Add product rating.html')

@login_required(login_url="/")
def hompage(request):
    return render(request, 'user/userindex.html')

@login_required(login_url="/")
def ordrdtls(request,id):
    request.session['pid']=id
    ob=product.objects.get(id=id)
    return render(request, 'user/order details.html',{'val':ob})

@login_required(login_url="/")
def ordrprdct(request):

    my_objects = product.objects.filter(date__gte=datetime.datetime.today()).order_by('-id')
    date = timezone.now().date()
    print(date, "iiiiiiiiiiiii")
    for i in my_objects:
        if i.date == date:
            i.delete()
    # Set the number of items per page
    items_per_page = 5

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

        return render(request, 'user/order products.html',{'my_objects':my_objects})
    return render(request, 'user/order products.html', {'my_objects': my_objects})

@login_required(login_url="/")
def ordrprdctcode(request):
    btn=request.POST['Submit']
    if btn == 'ORDER NOW':
            print(request.session['pid'],"kiiiiiiiiiiiiiiiiiii")
            qty=request.POST['textfield3']
            qq=product.objects.get(id=request.session['pid'])
            tt = float(qq.price)* float(qty)
            stock = float(qq.quantity)
            print(stock,qty,"jjjjjjjjjjjjjjjjjjjjjj")
            nstk = float(stock) - float(qty)
            if stock >= float(qty):
                up=product.objects.get(id=request.session['pid'])
                up.quantity=nstk
                up.save()
                qt=order()
                qt.date=datetime.datetime.today()
                qt.USER=user.objects.get(LOGINID=request.session['uid'])
                qt.status='ORDER'
                qt.price=tt
                qt.save()
                qty1=order_details()
                qty1.quantity=qty
                qty1.PRODUCT=product.objects.get(id=request.session['pid'])
                qty1.ORDER=qt
                qty1.date=datetime.datetime.today()
                qty1.save()
                return HttpResponse('''<script>alert('placed order successfuly');window.location='/ordrprdct'</script>''')
            else:
                return HttpResponse('''<script>alert('out of stock');window.location='/ordrprdct'</script>''')
    else:

        qty=request.POST['textfield3']
        qq=product.objects.get(id=request.session['pid'])
        tt = float(qq.price)* float(qty)
        stock = float(qq.quantity)
        print(stock,qty,"jjjjjjjjjjjjjjjjjjjjjj")
        nstk = float(stock) - float(qty)
        if stock >= float(qty):
            up=product.objects.get(id=request.session['pid'])
            up.quantity=nstk
            up.save()
            q=order.objects.filter(USER=user.objects.get(LOGINID__id=request.session['uid']),status='CART')
            if len(q)==0:
                qt=order()
                qt.date=datetime.datetime.today()
                qt.USER=user.objects.get(LOGINID=request.session['uid'])
                qt.status='CART'
                qt.price=tt
                qt.save()
                qty1=order_details()
                qty1.quantity=qty
                qty1.PRODUCT=product.objects.get(id=request.session['pid'])
                qty1.ORDER=qt
                qty1.date = datetime.datetime.today()
                qty1.save()
                return HttpResponse('''<script>alert('ADD TO CART');window.location='/ordrprdct'</script>''')
            else:
                total = float(q[0].price) + float(tt)
                qt=order.objects.get(id=q[0].id)
                qt.price=total
                qt.save()
                qty1=order_details.objects.filter(PRODUCT__id=request.session['pid'],ORDER__id=q[0].id)
                if len(qty1)==0:
                    qqt=order_details()
                    qqt.ORDER=q[0]
                    qqt.PRODUCT=product.objects.get(id=request.session['pid'])
                    qqt.quantity=qty
                    qqt.date=datetime.datetime.today()
                    qqt.save()
                else:
                    qry1=order_details.objects.get(id=qty1[0].id)
                    quty=float(qty1[0].quantity) + float(qty)
                    qry1.quantity=quty
                    qry1.date=datetime.datetime.today()
                    qry1.save()
                return HttpResponse('''<script>alert('ADD TO CART');window.location='/hompage'</script>''')
        else:
            return HttpResponse('''<script>alert('OUT OF STOCK');window.location='/hompage'</script>''')

@login_required(login_url="/")
def viewmycart(request):
    try:
        OB1=order.objects.get(USER__LOGINID__id=request.session['uid'],status='CART')
        ob = order_details.objects.filter(ORDER__USER__LOGINID__id=request.session['uid'],ORDER__status='CART')
        return render(request,'user/view my cart.html',{'val': ob,'total':OB1})
    except:
        ob = order_details.objects.filter(ORDER__USER__LOGINID__id=request.session['uid'],ORDER__status='CART')
        return render(request,'user/view my cart.html',{'val': ob,'total':0})

@login_required(login_url="/")
def viewhistory(request):
    ob = order_details.objects.filter(ORDER__USER__LOGINID__id=request.session['uid'],ORDER__status='Accepted')
    return render(request,'user/order_history.html',{'val': ob})
@login_required(login_url="/")
def deleteorder(request,id,qty):
    obd=order_details.objects.get(id=id)

    # ob1=product.objects.get(id=pid)
    # tt = int(ob1.quantity) + int(qty)
    # ob1.quantity=tt
    # ob1.save()
    # obd = order_details.objects.filter(ORDER__id=id)
    # o=product.objects.get(id=int(obd.PRODUCT))
    obp = obd.PRODUCT
    obp.quantity = float(obp.quantity) +float(qty)
    obp.save()
    obd.delete()
    return redirect('/viewhistory')
@login_required(login_url="/")
def orderfromcart(request,id):
    ob=order.objects.get(id=id)
    ob.status='ORDER'
    ob.save()
    return render(request,'user/view my cart.html')

@login_required(login_url="/")
def sorderfromcart(request,id):
    ob=s_product_request.objects.get(id=id)
    ob.status='pending'
    ob.save()
    return HttpResponse('''<script>alert('Ordered successfully....');window.location='/hompg'</script>''')

@login_required(login_url="/")
def srchordr_products(request):
    n = request.POST['textfield']
    my_objects = product.objects.filter(name__icontains=n)

    # Set the number of items per page
    items_per_page = 5

    # Create a Paginator instance
    paginator = Paginator(my_objects, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        my_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        my_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        my_objects = paginator.page(paginator.num_pages)

    return render(request, 'user/order products.html', {'my_objects': my_objects})



@login_required(login_url="/")
def ordr_status(request):
    ob = order.objects.filter(USER__LOGINID__id=request.session['uid'])
    return render(request, 'user/order_status.html',{'val': ob})


@login_required(login_url="/")
def view_item_ordr_status(request,id):
    ob = order_details.objects.filter(ORDER__id=id)
    return render(request, 'user/view_order_items.html', {'val': ob})



@login_required(login_url="/")
def sndcmplntviwrply(request):
    ob=complaint.objects.filter(USER__LOGINID__id=request.session['uid'])
    return render(request, 'user/send complaint& view reply.html',{'val':ob})
@login_required(login_url="/")
def sndcmpnt(request):
    return render(request, 'user/send complaint.html')

@login_required(login_url="/")
def snd_cmpnt(request):
    cmp=request.POST['textfield']
    ob=complaint()
    ob.complaint=cmp
    ob.USER=user.objects.get(LOGINID__id=request.session['uid'])
    ob.date=datetime.datetime.today()
    ob.reply='pending'
    ob.save()
    return HttpResponse('''<script>alert('send successfully....');window.location='/sndcmplntviwrply'</script>''')




@login_required(login_url="/")
def viwrviw(request):
    return render(request, 'user/view review.html')



from django.http import JsonResponse


def uncheck(request):
    un = request.GET['un']
    data = {
        'is_taken': login_table.objects.filter(Username__iexact=un).exists()
    }
    if data['is_taken']:
        data['error_message'] = "A user with this username already exists."
        # return HttpResponse("A user with this username already exists.")
    return JsonResponse(data)















