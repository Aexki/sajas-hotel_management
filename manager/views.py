from django.shortcuts import render,redirect
from accounts.models import cabservice,roomservice,complaintservice

# Create your views here.

def manager(request):
    all_cabservice=cabservice.objects.all()
    all_roomservice=roomservice.objects.all()
    all_complaintservice=complaintservice.objects.all()
    
    context={
        "all_cabservice":all_cabservice,
        "all_roomservice":all_roomservice,
        "all_complaintservice":all_complaintservice
    }
    
    return render(request, 'manager.html', context)

def manager1(request):
    all_roomservice=roomservice.objects.all()
    
    context={
        "all_roomservice":all_roomservice
    }
    
    return render(request, 'manager1.html', context)

def manager2(request):
    all_cabservice=cabservice.objects.all()
    
    context={
        "all_cabservice":all_cabservice
    }
    
    return render(request, 'manager2.html', context)

def manager3(request):
    all_complaintservice=complaintservice.objects.all()
    
    context={
        "all_complaintservice":all_complaintservice
    }
    
    return render(request, 'manager3.html', context)

def delete1(request, room_id):
    item= roomservice.objects.get(pk=room_id)
    item.delete()
    return redirect('1')

def delete2(request, cab_id):
    item= cabservice.objects.get(pk=cab_id)
    item.delete()
    return redirect('2')

def delete3(request, com_id):
    item= complaintservice.objects.get(pk=com_id)
    item.delete()
    return redirect('3')

def cross_off1(request, room_id):
    item= roomservice.objects.get(pk=room_id)
    item.completed=True
    item.save()
    return redirect('1')

def cross_off2(request, cab_id):
    item= cabservice.objects.get(pk=cab_id)
    item.completed=True
    item.save()
    return redirect('2')

def cross_off3(request, com_id):
    item= complaintservice.objects.get(pk=com_id)
    item.completed=True
    item.save()
    return redirect('3')

def uncross1(request, room_id):
    item= roomservice.objects.get(pk=room_id)
    item.completed=False
    item.save()
    return redirect('1')

def uncross2(request, cab_id):
    item= cabservice.objects.get(pk=cab_id)
    item.completed=False
    item.save() 
    return redirect('2')

def uncross3(request, com_id):
    item= complaintservice.objects.get(pk=com_id)
    item.completed=False
    item.save()
    return redirect('3')