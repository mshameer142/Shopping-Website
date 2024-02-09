import datetime
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from.models import *
from django.contrib.auth.models import User, auth
from django import *
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.core.exceptions import MultipleObjectsReturned






def home(request):
    return render(request,'tem/index.html')


def about(request):
    return render(request,'tem/about.html')


def product(request):
    return render(request,'tem/products.html')


def sin_product(request):
    return render(request,'tem/single-product.html')


def contact(request):
    return render(request,'tem/contact.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request,username = username, password = password)
        if Registration.objects.filter(user = user, Password = password).exists():
            logs = Registration.objects.filter(user = user, Password = password)
            for value in logs:
                user_id = value.id
                usertype = value.User_role

            if usertype == 'staff':
                request.session['logg'] = user_id
                return redirect('staff_home')

            if usertype == 'client':
                request.session['logg1'] = user_id
                return redirect('client_home')

            if usertype == 'admin':
                request.session['logg3'] = user_id
                return redirect('admin_home')

    else:
        return render(request,'login.html')


def admin_rg(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mgn = Registration.objects.all()
        for w in mgn:
            if w.user.email == email and w.User_role == 'adminn':
                messages.success(request, 'You have already registered. Please login')
                return redirect('admin_rg')
        psw = request.POST.get('psw')
        user_name = request.POST.get('user_name')
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        fs.save(photo.name, photo)

        for t in User.objects.all():
            if t.username == user_name:
                messages.success(request, 'Username taken. Please try another')
                return redirect('admin_rg')

        user = User.objects.create_user(username=user_name, email=email, password=psw, first_name=first_name,last_name=last_name)
        user.save()

        reg = Registration()
        reg.Password = psw
        reg.Image = photo
        reg.User_role = 'adminn'
        reg.user = user
        reg.save()
        messages.success(request, 'You have successfully registered as admin')
        return redirect('home')
    else:
     return render(request,'Registeration_adminn.html')


def logout(request):
    auth.logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')


def staff_rg(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mgn = Registration.objects.all()
        for w in mgn:
            if w.user.email == email and w.User_role == 'staff':
                messages.success(request, 'You have already registered. Please login')
                return redirect('staff_rg')
        psw = request.POST.get('psw')
        user_name = request.POST.get('user_name')
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        fs.save(photo.name, photo)

        for t in User.objects.all():
            if t.username == user_name:
                messages.success(request, 'Username taken. Please try another')
                return redirect('staff_rg')

        user = User.objects.create_user(username=user_name, email=email, password=psw, first_name=first_name,last_name=last_name)
        user.save()

        reg = Registration()
        reg.Password = psw
        reg.Image = photo
        reg.User_role = 'staff'
        reg.user = user
        reg.save()
        messages.success(request, 'You have successfully registered as staff')
        return redirect('home')
    else:
     return render(request,'Registeration_staff.html')


def client_rg(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mgn = Registration.objects.all()
        for w in mgn:
            if w.user.email == email and w.User_role == 'client':
                messages.success(request, 'You have already registered. Please login')
                return redirect('client_rg')
        psw = request.POST.get('psw')
        user_name = request.POST.get('user_name')
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        fs.save(photo.name, photo)

        for t in User.objects.all():
            if t.username == user_name:
                messages.success(request, 'Username taken. Please try another')
                return redirect('client_rg')

        user = User.objects.create_user(username=user_name, email=email, password=psw, first_name=first_name,last_name=last_name)
        user.save()

        reg = Registration()
        reg.Password = psw
        reg.Image = photo
        reg.User_role = 'client'
        reg.user = user
        reg.save()
        messages.success(request, 'You have successfully registered as client')
        return redirect('home')
    else:
        return render(request,'Registeration_cus.html')


def ad_home(request):
    return render(request,'admin_home.html')


def st_home(request):
    return render(request,'staff_home.html')


def cl_home(request):
    return render(request,'client_home.html')


def adm_prof(request):
    gtt = Registration.objects.get(id = request.session['logg3'])
    return render(request, 'adm_prof.html',{'gtt':gtt})


def del_admin(request, id):
    bb1 = Registration.objects.get(id = id)
    bb1 = bb1.user.pk
    User.objects.get(id = bb1).delete()
    messages.success(request, 'You have successfully resigned from administration')
    return redirect('home')


def edit_admin(request):
    bb1 = Registration.objects.get(User_role = 'admin')
    return redirect('admin_home')
    rtrk = bb1.user.pk
    um = User.objects.get(id = rtrk)
    if request.method == 'POST':
        first = request.POST.get('first')
        last = request.POST.get('last')
        em = request.POST.get('em')
        psw = request.POST.get('psw')

        user_name = request.POST.get('user_name')
        m = User.objects.all().exclude(username=um.username)

        for t in m:
            if t.username == user_name:
                messages.success(request, 'Username taken. Please try another')
                return render(request, 'update_admin.html', {'bb1': bb1, 'um': um})

        passwor = make_password(psw)
        df = Registration.objects.get(id=request.session['logg3'])
        kmk = df.user.pk
        kmk = User.objects.get(id = kmk)
        kmk.username = user_name
        kmk.first_name = first
        kmk.last_name = last
        kmk.password = passwor
        kmk.email = em
        kmk.save()

        user = auth.authenticate(username = user_name, password = psw)
        auth.login(request, user)

        dcd = Registration.objects.get(User_role = 'admin')
        b = dcd.id
        m = int(b)
        request.session['logg3'] = m

        dcd = Registration.objects.get(id = request.session['logg3'])
        dcd.Password = psw
        dcd.user = kmk
        dcd.save()
        messages.success(request, 'You have successfully updated your profile')
        return redirect('adm_prof')
    else:
        return render(request, 'update_admin.html',{'bb1':bb1,'um':um})


def update_pr_st(request):
    b = Registration.objects.get(id = request.session['logg'])
    mjm = b.user.pk
    um = User.objects.get(id = mjm)
    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        email = request.POST.get('email')
        psw = request.POST.get('psw')
        user_name = request.POST.get('user_name')

        m = User.objects.all().exclude(username = um.username)

        for t in m:
            if t.username == user_name:
                messages.success(request, 'Username taken. Please try another')
                return render(request, 'update_pr_st.html', {'b': b, 'um': um})


        passwords = make_password(psw)
        u = User.objects.get(id = mjm)
        u.password = passwords
        u.username = user_name
        u.email = email
        u.first_name = f_name
        u.last_name = l_name
        u.save()

        user = auth.authenticate(username = user_name, password = psw)
        auth.login(request, user)

        bb = b.id
        m = int(bb)
        request.session['logg'] = m

        try:
            photo = request.FILES['imgg1']
            fs = FileSystemStorage()
            fs.save(photo.name, photo)
            b.Image = photo
            b.Password = psw
            b.user = u
            b.save()
            messages.success(request, 'Profile updated')
            return redirect('staff_home')
        except:
            photo = request.POST.get('imgg')
            b.Password = psw
            b.Image = photo
            b.user = u
            b.save()
            messages.success(request, 'Profile updated')
            return redirect('staff_home')
    return render(request, 'update_pr_st.html', {'b': b, 'um': um})


def update_pr_cl(request):
    aa = Registration.objects.get(id = request.session['logg1'])
    rfy = aa.user.pk
    um = User.objects.get(id = rfy)
    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pasw = request.POST.get('psw')
        user_name = request.POST.get('user_name')
        m = User.objects.all().exclude(username = um.username)

        for t in m:
            if t.username == user_name:
                messages.success(request, 'Username taken. Please try another')
                return redirect('update_pr_cl')


        passwords = make_password(pasw)
        u = User.objects.get(id = rfy)
        u.password = passwords
        u.username = user_name
        u.email = email
        u.first_name = f_name
        u.last_name = l_name
        u.save()

        user = auth.authenticate(username = user_name, password = pasw)
        auth.login(request, user)


        b = aa.id
        m = int(b)
        request.session['logg1'] = m

        try:
            imgg1 = request.FILES['imgg1']
            fs = FileSystemStorage()
            fs.save(imgg1.name,imgg1)
            aa.Password = pasw
            aa.Image = imgg1
            aa.user = u
            aa.save()
            messages.success(request, 'Updated successfully')
            return redirect('client_home')
        except:
            imgg2 = request.POST.get('imgg2')
            aa.Password = pasw
            aa.Image = imgg2
            aa.user = u
            aa.save()
            messages.success(request, 'Updated successfully')
            return redirect('client_home')
    return render(request, 'update_pr_cl.html', {'aa': aa,'um':um})


def ch_p(request):
    th = Registration.objects.get(id = request.session['logg'])
    trp = th.user.pk
    u = User.objects.get(id=trp)
    if request.method == 'POST':
        new_pass = request.POST.get('pssw')
        passwords = make_password(new_pass)
        u.password = passwords
        u.save()

        th.Password = new_pass
        th.save()
        messages.success(request, 'Password changed successfully. Login again with new password.')
        return redirect('logout')
    return render(request,'change_pass.html',{'th':th})


def ch_p2(request):
    th = Registration.objects.get(id = request.session['logg1'])
    trp = th.user.pk
    u = User.objects.get(id=trp)
    if request.method == 'POST':
        new_pass = request.POST.get('pssw')
        passwords = make_password(new_pass)
        u.password = passwords
        u.save()

        th.Password = new_pass
        th.save()
        messages.success(request, 'Password changed successfully. Login again with new password.')
        return redirect('logout')
    return render(request,'change_pass2.html',{'th':th})


def ch_p3(request):
    th = Registration.objects.get(id = request.session['logg3'])
    trp = th.user.pk
    u = User.objects.get(id=trp)
    if request.method == 'POST':
        new_pass = request.POST.get('pssw')
        passwords = make_password(new_pass)
        u.password = passwords
        u.save()

        th.Password = new_pass
        th.save()
        messages.success(request, 'Password changed successfully. Login again with new password.')
        return redirect('logout')
    return render(request,'change_pass3.html',{'th':th})


def m_m(request):
    p = Registration.objects.get(id = request.session['logg3'])
    bb = Messages.objects.filter(To_reg = p)
    return render(request,'message.html',{'bb':bb})


def del_msg_admin(request,id):
    Messages.objects.get(id = id).delete()
    messages.success(request, 'Message deleted successfully')
    return redirect('m_m')


def reply_msg_admin(request,id):
    pa = Messages.objects.get(id = id)
    toto = int(pa.From_reg.id)
    p_to = Registration.objects.get(id = toto)
    p = Registration.objects.get(id=request.session['logg3'])
    if request.method == 'POST':
        msg_cont = request.POST.get('msg_cont')
        pa1 = Messages()
        pa1.Message_content = msg_cont
        pa1.From_reg = p
        pa1.To_reg = p_to
        pa1.save()
        messages.success(request, 'Message reply successful')
        return redirect('m_m')
    return render(request,'reply_msg_admin.html',{'pa':pa})


def sent_msg_admin(request):
    kk = Registration.objects.all()
    p = Registration.objects.get(id = request.session['logg3'])
    if request.method == 'POST':
        to_em = request.POST.get('to_em')
        ddp = int(to_em)
        reg_to = Registration.objects.get(id = ddp)
        msg_cont = request.POST.get('msg_cont')
        nm = Messages()
        nm.Message_content = msg_cont
        nm.From_reg = p
        nm.To_reg = reg_to
        nm.save()
        messages.success(request, 'Message sent successfully')
        return redirect('m_m')
    return render(request,'sent_msg_admin.html',{'kk':kk})


def g_m(request):
    bb = Guest_messages.objects.all()
    return render(request,'guest_message.html',{'bb':bb})


def delete_g_msg(request,id):
    Guest_messages.objects.get(id=id).delete()
    messages.success(request, 'Message deleted successfully')
    return redirect('g_m')


def reply_g_msg(request, id):
    yt = Guest_messages.objects.get(id = id)
    if request.method == 'POST':
        email = "your@gmail.com"
        t_a = request.POST.get('t_a')
        emk = str(yt.Email)
        send_mail('Message reply from S.R Shopping website', t_a, email, [emk], fail_silently=False)
        redd = '/reply_g_msg/'+str(yt.id)
        messages.success(request, 'Email reply to guest done successfully')
        return redirect(redd)
    return render(request,'reply_g_msg.html',{'yt':yt})


def m_m2(request):
    p = Registration.objects.get(id=request.session['logg'])
    bb = Messages.objects.filter(To_reg = p)
    return render(request, 'msg2.html', {'bb': bb})


def del_msg_staff(request,id):
    Messages.objects.get(id = id).delete()
    messages.success(request, 'Message deleted successfully')
    return redirect('m_m2')


def reply_msg_staff(request,id):
    pa = Messages.objects.get(id = id)
    toto = int(pa.From_reg.id)
    p_to = Registration.objects.get(id=toto)
    p = Registration.objects.get(id=request.session['logg'])
    if request.method == 'POST':
        msg_cont = request.POST.get('msg_cont')
        pa1 = Messages()
        pa1.Message_content = msg_cont
        pa1.From_reg = p
        pa1.To_reg = p_to
        pa1.save()
        messages.success(request, 'Message reply successful')
        return redirect('m_m2')
    return render(request,'reply_msg_staff.html',{'pa':pa})


def sent_msg_staff(request):
    kk = Registration.objects.all()
    p = Registration.objects.get(id = request.session['logg'])
    if request.method == 'POST':
        to_em = request.POST.get('to_em')
        ddp = int(to_em)
        reg_to = Registration.objects.get(id=ddp)
        msg_cont = request.POST.get('msg_cont')
        nm = Messages()
        nm.Message_content = msg_cont
        nm.From_reg = p
        nm.To_reg = reg_to
        nm.save()
        messages.success(request, 'Message sent successfully')
        return redirect('m_m2')
    return render(request,'sent_msg_staff.html',{'kk':kk})


def m_m1(request):
    p = Registration.objects.get(id=request.session['logg1'])
    bb = Messages.objects.filter(To_reg = p)
    return render(request, 'msg1.html', {'bb': bb})


def del_msg_cl(request,id):
    Messages.objects.get(id = id).delete()
    messages.success(request, 'Message deleted successfully')
    return redirect('m_m1')


def reply_msg_cl(request,id):
    pa = Messages.objects.get(id=id)
    toto = int(pa.From_reg.id)
    p_to = Registration.objects.get(id=toto)
    p = Registration.objects.get(id=request.session['logg1'])
    if request.method == 'POST':
        msg_cont = request.POST.get('msg_cont')
        pa1 = Messages()
        pa1.Message_content = msg_cont
        pa1.From_reg = p
        pa1.To_reg = p_to
        pa1.save()
        messages.success(request, 'Message reply successful')
        return redirect('m_m1')
    return render(request,'reply_msg_cl.html',{'pa':pa})


def sent_msg_cl(request):
    kk = Registration.objects.all()
    p = Registration.objects.get(id = request.session['logg1'])
    if request.method == 'POST':
        to_em = request.POST.get('to_em')
        ddp = int(to_em)
        reg_to = Registration.objects.get(id=ddp)
        msg_cont = request.POST.get('msg_cont')
        nm = Messages()
        nm.Message_content = msg_cont
        nm.From_reg = p
        nm.To_reg = reg_to
        nm.save()
        messages.success(request, 'Message sent successfully')
        return redirect('m_m1')
    return render(request,'sent_msg_cl.html',{'kk':kk})


def cart(request):
    return render(request,'cart.html')


def cart2(request):
    return render(request,'cart2.html')


def cart3(request):
    return render(request,'cart3.html')


def cart4(request):
    return render(request,'cart4.html')


def cart5(request):
    return render(request,'cart5.html')


def cart6(request):
    return render(request,'cart6.html')


def cart7(request):
    return render(request,'cart7.html')


def cart8(request):
    return render(request,'cart8.html')


def cart9(request):
    return render(request,'cart9.html')


def payment(request):
    p = Registration.objects.get(id = request.session['logg1'])
    bb = Messages.objects.filter(To_reg = p)
    return render(request,'payment.html',{'bb': bb})


def submit(request):
    return render(request,'submit.html')


def add_to_cart(request):
    return render(request,'add-to-cart.html')


def add_to_cart_m(request):
    return render(request,'add_to_cart_m.html')


def add_to_cart_k(request):
    return render(request,'add_to_cart_k.html')






