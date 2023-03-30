from django.shortcuts import render,redirect
from .models import Food,Consume

# Create your views here.
def index(request):
    consumed_food=""
    if request.method=="POST":
        food_consume=request.POST['food_consume']
        consume=Food.objects.get(name=food_consume)
        user=request.user
        consume=Consume(user=user,food_consume=consume)
        consume.save()
        foods=Food.objects.all()
    else:    
        foods=Food.objects.all()
    consumed_food=Consume.objects.filter(user=request.user)    
    return render(request,'myapp/index.html',{'foods':foods,'consumed_food':consumed_food})

def delete_food(request,id):
    consume_food=Consume.objects.get(pk=id)
    if request.method=="POST":
        consume_food.delete()
        return redirect('/')
    return render(request,'myapp/delete.html')