from django.shortcuts import render,redirect,reverse
from django.urls import reverse_lazy
from .models import Product,BillingAddress,OrderItem,Order,Payment,Comment
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import CheckoutForm,CommentForm,ContactForm

class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    paginate_by = 2
    template_name = 'products/product_list.html'
    context_object_name = 'product'


# class ProductDetailView(generic.DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'

def product_detail_view(request, pk):
    products = get_object_or_404(Product, pk=pk)
    product_comments = products.comments.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment= comment_form.save(commit=False)
            new_comment.new_comment = products
            new_comment.user = request.user
            new_comment.save()
            comment_form=CommentForm()
    else:
        comment_form = CommentForm()

    context = {
        'product': products,
        'comments':product_comments,
        'comment_form':comment_form,
    }
    return render(request, 'products/product_detail.html',context)



class ProductUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Product
    fields = ['title','description','price','active','size','wear','discount_price','image']
    template_name = "products/product_update.html"

class ProductDeleteView(LoginRequiredMixin , generic.DeleteView):
    model = Product
    template_name = "products/product_delete.html"
    success_url = reverse_lazy('product-list')

class ProductCreateView(LoginRequiredMixin , generic.CreateView):
    model = Product
    fields = ['title','description','price','size','wear','discount_price','image',]
    template_name = "products/product_create.html"

class ContactView(generic.CreateView):
    form_class = ContactForm
    template_name = "products/product_contact.html"
    success_url = reverse_lazy('feedback')


class OrderSummery(LoginRequiredMixin , generic.View):
    def get(self, *args,**kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object':order
            }
            return render(self.request,'products/order_summary.html',context)
        except ObjectDoesNotExist:
            messages.error(self.request,'you do not have active order')
            return redirect('/')


class ChekoutView(generic.View):
    def get(self , *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form' : form
        }
        return render(self.request,'products/checkout.html',context)
    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        print(self.request.POST)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                print(self.request.POST)
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')
                # save_info = form.cleaned_data.get('save_info')
                descript = form.cleaned_data.get('descript')
                payment_option = form.cleaned_data.get('payment_option')
                number = form.cleaned_data.get('number')
                f_name = form.cleaned_data.get('f_name')
                l_name = form.cleaned_data.get('l_name')
                billing_address = BillingAddress(
                    user = self.request.user,
                    apartment_address = apartment_address,
                    country = country,
                    # save_info = save_info,
                    number = number,
                    f_name = f_name,
                    l_name = l_name,
                    descript = descript
                )
                print(self.request.POST)
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                #TODO add redirect to payment option
                return redirect('checkout')
            messages.warning(self.request,'Failed checkout')
            return redirect('checkout')
        except ObjectDoesNotExist:
            message.error(self.request,'dont have active order')
            return redirect('order-summary')




@login_required
def add_to_cart(request,pk):
    item = get_object_or_404(Product,pk=pk)
    order_item,create = OrderItem.objects.get_or_create(
        user=request.user,
        item=item,
        )
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item=item).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request,'this item was updated')
            return redirect("order-summary")
        else:
            messages.info(request,'this item was added')
            order.items.add(order_item)
    else:
        order = Order.objects.create(user= request.user)
        order.items.add(order_item)
    return redirect("product-list")
        



# def add_to_cart(request,pk):
#     product = get_object_or_404(Product, pk=pk)#product ro begir
#     order_item , created = OrderItem.get_or_create(#user sefaresh dard ya kheyr (check mikone)
#         user=request.user,
#         item=item,#user sefaresh dard ya kheyr (check mikone)
#         ordered = False
#     )#va agar sefaresh dasht quantity ro kamo ziad mikonim
#     order_qs = Order.objects.filter(user=request.user,ordered=False)#sefareshi ro migirm k takmil nashode
#     if order_qs.exist():
#         order = order_qs[0]
#         #check the orderItem in the Order
#         if order.items.filter(item=item).exists():
#             order_item.quantity += 1
#             order_item.save()
#             messages.info(request, "This item quantity was updated.")
#             return redirect('product-list')
#         else:
#             order.items.add(order_item)
#             messages.info(request, "This item was added to your cart.")
#             return redirect('product-list')
#     else:
#         order = Order.objects.create(user=request.user)
#         order.items.add(order_item)
#     return redirect('product-list')


@login_required
def remove_from_cart(request,pk):
    order_item = get_object_or_404(OrderItem, item__id=pk , order__user = request.user, order__ordered=False)
    order_item.delete()
    messages.info(request,'this item was removed')
    return redirect("order-summary")


    # item = get_object_or_404(Product,pk=pk)
    # order_qs = Order.objects.filter(
    #     user=request.user,
    #     ordered=False
    # )
    # if order_qs.exists():
    #     order = order_qs[0]
    #     if order.items.filter(item=item).exists():
    #         order_item = OrderItem.objects.filter(
    #             item = item,
    #             user = request.user,
    #             ordered = False
    #         )[0]
    #         order.items.remove(order_item)
            
    #     else:
    #         messages.info(request,'this item was not in your cart ')
    #         return redirect("order-summary")
    # else:
    #     messages.info(request,'you do not have an active order')
    #     return redirect("order-summary")
    # return redirect("order-summary")

@login_required()
def remove_single_item_from_cart(request, pk):
    item= get_object_or_404(Product,pk=pk)
    order =Order.objects.filter(
        user=request.user,
        ordered=False
    ).last()
    result = order.reduce_order_item_quantity(pk)
    if not result:
        messages.info(request, "This item was not in your cart")
    return redirect('order-summary')
    

def feedback(request):
    return render(request,'products/feedback.html')
    
    
    # if order_qs.exists():
    
    # if order.items.filter(item=item).exists():
    #     order_item = OrderItem.objects.filter(
    #         item=item,
    #         user=request.user,
    #         ordered=False
    #     )[0]
    #     if order_item.quantity > 1:
    #         order_item.quantity -= 1
    #         order_item.save()
    #         return redirect("order-summary")
    #     else:
    #         order.items.remove(order_item)
    #         return redirect("order-summary")
    # else:
    #     messages.info(request, "This item was not in your cart")
    #     return redirect("order-summary")
  




# class PaymentView(generic.View):
    # pass



    

