from django.shortcuts import render, redirect
# from .models import front_banner, lower_banner
# from .forms import add_item_form, front_banner_form, coupon_form, lower_banner_form

# Create your views here.

def admindash(request):
    return render(request, "admindash/index.html")

def projects(request):
    
    # item_data = Item.objects.all().values()
    # print(item_data)
    return render(request, "admindash/current_items.html",{'item_data':item_data,'register_form':add_item_form})



# def carousel(request):
#     carousel_data = front_banner.objects.all().values()
#     print(carousel_data)
#     return render(request, "admindash/frontbanner.html",{'carousel_data':carousel_data,'register_form':front_banner_form})

# def lower_banner_view(request):
#     banner_data = lower_banner.objects.all()
#     print(banner_data)
#     return render(request, "admindash/lowerbanner.html",{'banner_data':banner_data,'register_form':lower_banner_form})

# def add_banner(request,pk):
#     s_obj = lower_banner.objects.get(id = pk)
#     itemform = lower_banner_form(request.POST, request.FILES, instance=s_obj)

#     if itemform.is_valid():
#         print('success')
#         itemformsave = itemform.save(commit=False)
#         # filesize = request.cookies.get("filesize")
#         itemformsave.image = request.FILES['image2']
#         itemform.save()

#     return redirect('lower_banner')


# def orders(request):
#     #order_item_data = OrderItem.objects.filter(ordered=True).order_by('created_at')
#     order_data = Order.objects.filter(ordered=True).order_by('ordered_date').reverse()
#     print(order_data)
#     return render(request, "admindash/orders.html",{'order_data':order_data})

# def order_item(request,pk):
#     print('here')
#     ref_id = pk
#     order_item_data = OrderItem.objects.filter(ref_code=ref_id)
#     print(order_item_data)
#     order_data = Order.objects.filter(ref_code=ref_id)
#     return render(request, "admindash/order_item.html",{"order_item_data":order_item_data,"order_data":order_data})

# def coupon(request):
#     coupon_data = Coupon.objects.all()
#     print(coupon_data)
#     return render(request, "admindash/coupon.html",{'coupon_data':coupon_data,'register_form':coupon_form})

# def add_coupon(request):
#     couponform = coupon_form(request.POST)

#     if couponform.is_valid():
#         print('Coupon added success')
#         couponform.save()

#     return redirect('coupon')

# def add_carousel(request,pk):
#     s_obj = front_banner.objects.get(id = pk)
#     itemform = front_banner_form(request.POST, request.FILES, instance=s_obj)

#     if itemform.is_valid():
#         print('success')
#         itemformsave = itemform.save(commit=False)
#         # filesize = request.cookies.get("filesize")
#         itemformsave.image = request.FILES['image']
#         itemform.save()

#     return redirect('carousel')

# def add_item(request):
#     itemform = add_item_form(request.POST, request.FILES)

#     if itemform.is_valid():
#         print('success')
#         itemformsave = itemform.save(commit=False)
#         # filesize = request.cookies.get("filesize")
#         itemformsave.image = request.FILES['image']
#         print(itemformsave.image2)
#         if itemformsave.image2 != 'abc.img' :
#             itemformsave.image2 = request.FILES['image2']
#         itemform.save()

#     return redirect('current_items')

# def edit_item(request, pk):
#     s_obj = Item.objects.get(id = pk)
#     print('here in edit view')

#     if request.method == "POST":
#         form = add_item_form(request.POST, instance=s_obj) #request.FILES
#         if form.is_valid():
#             print('success Edit')
#             # formsave = form.save(commit=False)
#             # formsave.image = request.FILES['image']
#             post = form.save()
#             return redirect('current_items')
#     else:
#         form = add_item_form(instance=s_obj)

#     context = {
#         'form' : form,
#         'form_id':pk
#     }

#     # return render(request,"admindash/edit_items.html",context)
#     return render(request, "admindash/edit_items.html",context)

# def delete_item(request, pk):
#     s_obj = Item.objects.get(id=pk)
#     s_obj.delete()
#     return redirect('current_items')

# def delete_coupon(request, pk):
#     s_obj = Coupon.objects.get(id=pk)
#     s_obj.delete()
#     return redirect('coupon')