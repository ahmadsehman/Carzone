from django.shortcuts import get_object_or_404, render
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def cars(request):
    cars  = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4) # Show 4 car per page.
    page_number = request.GET.get('page')
    page_car = paginator.get_page(page_number)

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    context = {
        'cars': page_car,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/cars.html', context)


def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    context = {
        'single_car': single_car
    }
    return render(request, 'cars/car_detail.html', context)


def search(request):
    cars  = Car.objects.order_by('-created_date')

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

    # البحث عن طريق مايتم كتابته في مربع النص
    if 'keyword' in request.GET: # 'keyword' : هو الاسم الذي تم استخدامه في مربع النص الخاص بالبحث في الفورم
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword) # وهي تعني ان الحقل يحتوي على __icontains  وتمت عن طريق استخدام  description  تم عمل فلتره بواسطة حقل 

    # Model البحث عن طريق مايتم اختياره من قائمة 
    if 'model' in request.GET: # 'model' : Model هو الاسم الذي تم استخدامه لقائمة  
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model) # __iexact : - تعني المطابقة في كل شيء

    # Location البحث عن طريق مايتم اختياره من قائمة 
    if 'city' in request.GET: # 'city' : Location هو الاسم الذي تم استخدامه لقائمة  
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    # Year البحث عن طريق مايتم اختياره من قائمة 
    if 'year' in request.GET: # 'year' : Year هو الاسم الذي تم استخدامه لقائمة  
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    # Select Type Of Car البحث عن طريق مايتم اختياره من قائمة 
    if 'body_style' in request.GET: # 'body_style' : Select Type Of Car هو الاسم الذي تم استخدامه لقائمة  
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    #  البحث عن طريق مايتم اختياره من السعر
    if 'min_price' in request.GET: # 'min_price' : هو الاسم الخاص بالسعر  
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price) # __lte : تعني أصغر من أو يساوي  __gte : تعني أكبر من أويساوي

    if 'transmission' in request.GET: # 'transmission' : Transmission هو الاسم الذي تم استخدامه لقائمة  
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(transmission__iexact=transmission)
    

    context = {
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search
    }
    return render(request, 'cars/search.html', context)
