from django.urls import path
from.import views
import shop.views

urlpatterns = [
    path('',shop.views.home,name='home'),
    path('home',shop.views.home,name='home'),
    path('about',shop.views.about,name='about'),
    path('product',shop.views.product,name='product'),
    path('sin-product',shop.views.sin_product,name='sin-product'),
    path('contact',shop.views.contact,name='contact'),
    path('login',shop.views.login,name='login'),
    path('adminn',shop.views.admin_rg,name='adminn'),
    path('logout',shop.views.logout,name='logout'),
    path('staff',shop.views.staff_rg,name='staff'),
    path('client',shop.views.client_rg,name='client'),
    path('admin_home',shop.views.ad_home,name='admin_home'),
    path('staff_home',shop.views.st_home,name='staff_home'),
    path('client_home',shop.views.cl_home,name='client_home'),
    path('update_pr_st/',shop.views.update_pr_st,name='update_pr_st'),
    path('update_pr_cl/',shop.views.update_pr_cl,name='update_pr_cl'),
    path('del_admin/<id>',shop.views.del_admin,name='del_admin'),
    path('edit_admin/',shop.views.edit_admin,name='edit_admin'),
    path('adm_prof/',shop.views.adm_prof,name='adm_prof'),
    path('ch_p', shop.views.ch_p, name='ch_p'),
    path('ch_p2', shop.views.ch_p2, name='ch_p2'),
    path('ch_p3', shop.views.ch_p3, name='ch_p3'),
    path('m_m', shop.views.m_m, name='m_m'),
    path('del_msg_admin/<id>', shop.views.del_msg_admin, name='del_msg_admin'),
    path('reply_msg_admin/<id>', shop.views.reply_msg_admin, name='reply_msg_admin'),
    path('sent_msg_admin', shop.views.sent_msg_admin, name='sent_msg_admin'),
    path('g_m',shop.views.g_m,name='g_m'),
    path('delete_g_msg/<id>',shop.views.delete_g_msg,name='delete_g_msg'),
    path('reply_g_msg/<id>',shop.views.reply_g_msg,name='reply_g_msg'),
    path('m_m2', shop.views.m_m2, name='m_m2'),
    path('del_msg_staff/<id>', shop.views.del_msg_staff, name='del_msg_staff'),
    path('reply_msg_staff/<id>', shop.views.reply_msg_staff, name='reply_msg_staff'),
    path('sent_msg_staff', shop.views.sent_msg_staff, name='sent_msg_staff'),
    path('m_m1', shop.views.m_m1, name='m_m1'),
    path('del_msg_cl/<id>', shop.views.del_msg_cl, name='del_msg_cl'),
    path('reply_msg_cl/<id>', shop.views.reply_msg_cl, name='reply_msg_cl'),
    path('sent_msg_cl', shop.views.sent_msg_cl, name='sent_msg_cl'),
    path('cart',shop.views.cart,name='cart'),
    path('cart2',shop.views.cart2,name='cart2'),
    path('cart3',shop.views.cart3,name='cart3'),
    path('cart4',shop.views.cart4,name='cart4'),
    path('cart5',shop.views.cart5,name='cart5'),
    path('cart6',shop.views.cart6,name='cart6'),
    path('cart7',shop.views.cart7,name='cart7'),
    path('cart8',shop.views.cart8,name='cart8'),
    path('cart9',shop.views.cart9,name='cart9'),
    path('payment',shop.views.payment,name='payment'),
    path('submit',shop.views.submit,name='submit'),
    path('add_to_cart',shop.views.add_to_cart,name='add_to_cart'),
    path('add_to_cart_m',shop.views.add_to_cart_m,name='add_to_cart_m'),
    path('add_to_cart_k',shop.views.add_to_cart_k,name='add_to_cart_k'),






]










