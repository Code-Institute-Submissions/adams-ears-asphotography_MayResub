from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def view_basket(request):

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    This function ..
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})
    # This does.....
    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += quantity
            else:
                basket[item_id]['items_by_size'][size] = quantity
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}

    if item_id in list(basket.keys()):
        basket[item_id] = quantity
    else:
        basket[item_id] = quantity
    request.session['basket'] = basket
    return redirect(redirect_url)


def remove_from_basket(request, item_id):
    """
    Remove the item from the shopping bag.
    """

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        basket = request.session.get('basket', {})

        if size:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
        else:
            basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception:
        return HttpResponse(status=500)
