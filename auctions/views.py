from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User,AuctionList,Comments


def index(request):
    if(request.method == 'POST'):
        user = User.objects.get(username=request.user)
        title = request.POST['title']
        description = request.POST['description']
        current_price = request.POST['bids']
        photo = request.POST['photo']
        categories = request.POST['categories']
        auction = AuctionList.objects.create(username = user, title=title, description=description, current_price=current_price,photo=photo,categories=categories)
        auction.save()
    return render(request, "auctions/index.html",{
        "auctionslist": AuctionList.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
 
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    return render(request, "auctions/createlist.html")\
    
def details(request, product_id):
    product_details = AuctionList.objects.get(id=product_id)
    if(request.method == 'POST'):
        comment = request.POST["comment"]
        comment_details = Comments.objects.create(username=request.user, product=product_details, text = comment)
        comment_details.save()
    comment = product_details.comments.all()
    return render(request, "auctions/details.html",{
        "details": product_details,
        "product_comments": comment
    })

def category(request):
    all_product = AuctionList.objects.all()
    all_products = set()
    for product in all_product:
        all_products.add(product.categories)
    return render(request, "auctions/categories.html",{
        "all_products":all_products,
        
    })

def details_category(request, product_category):
    products = AuctionList.objects.filter(categories=product_category)
    return render(request, "auctions/index.html", {
        "auctionslist":products
    })