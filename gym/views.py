from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import Enquiry, Equipment, GymPlan, Member


# Create your views here.
@staff_member_required(login_url='admin_login')
def index(request):
    stats = {
        'enquiries_count': Enquiry.objects.count(),
        'equipment_count': Equipment.objects.count(),
        'plans_count': GymPlan.objects.count(),
        'members_count': Member.objects.count(),
    }
    return render(request, 'index.html', stats)


def about(request):
    return render(request, 'about.html')


def contact(request):
    hours = [
        {'day': 'Friday', 'sessions': ['6:30 AM - 9:00 AM', '5:30 PM - 11:00 PM']},
        {'day': 'Saturday', 'sessions': ['6:30 AM - 9:00 AM', '5:30 PM - 11:00 PM']},
        {'day': 'Sunday', 'sessions': [], 'closed': True},
        {'day': 'Monday (Iqbal Day)', 'day_key': 'Monday', 'sessions': ['6:30 AM - 9:00 AM', '5:30 PM - 11:00 PM']},
        {'day': 'Tuesday', 'sessions': ['6:30 AM - 9:00 AM', '5:30 PM - 11:00 PM']},
        {'day': 'Wednesday', 'sessions': ['6:30 AM - 9:00 AM', '5:30 PM - 11:00 PM']},
        {'day': 'Thursday', 'sessions': ['6:30 AM - 9:00 AM', '5:30 PM - 11:00 PM']},
    ]
    today = timezone.localtime().strftime('%A')
    return render(request, 'contact.html', {'hours': hours, 'today': today})


def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('uname', '').strip()
        password = request.POST.get('pwd', '')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            auth_login(request, user)
            return redirect('index')

        return render(request, 'login.html', {'error': 'Invalid username or password.'})

    return render(request, 'login.html')


def admin_logout(request):
    auth_logout(request)
    return redirect('admin_login')


@staff_member_required(login_url='admin_login')
def enquiry_add(request):
    if request.method == 'POST':
        Enquiry.objects.create(
            name=request.POST.get('name', '').strip(),
            email=request.POST.get('email', '').strip(),
            phone=request.POST.get('phone', '').strip(),
            age=request.POST.get('age') or None,
            gender=request.POST.get('gender', '').strip(),
            message=request.POST.get('message', '').strip(),
        )
        return redirect('enquiry_list')
    return render(request, 'enquiry_form.html')


@staff_member_required(login_url='admin_login')
def enquiry_list(request):
    return render(request, 'enquiry_list.html', {'enquiries': Enquiry.objects.all()})


@staff_member_required(login_url='admin_login')
def enquiry_delete(request, enquiry_id):
    if request.method == 'POST':
        enquiry = get_object_or_404(Enquiry, id=enquiry_id)
        enquiry.delete()
    return redirect('enquiry_list')


@staff_member_required(login_url='admin_login')
def plan_add(request):
    if request.method == 'POST':
        GymPlan.objects.create(
            name=request.POST.get('name', '').strip(),
            duration_months=request.POST.get('duration_months', 0),
            price=request.POST.get('price', 0),
            description=request.POST.get('description', '').strip(),
        )
        return redirect('plan_list')
    return render(request, 'plan_form.html')


@staff_member_required(login_url='admin_login')
def plan_list(request):
    return render(request, 'plan_list.html', {'plans': GymPlan.objects.all()})


@staff_member_required(login_url='admin_login')
def plan_delete(request, plan_id):
    if request.method == 'POST':
        plan = get_object_or_404(GymPlan, id=plan_id)
        try:
            plan.delete()
            messages.success(request, 'Plan deleted successfully.')
        except ProtectedError:
            messages.error(request, 'This plan cannot be deleted while members are using it.')
    return redirect('plan_list')


@staff_member_required(login_url='admin_login')
def equipment_add(request):
    if request.method == 'POST':
        Equipment.objects.create(
            name=request.POST.get('name', '').strip(),
            price=request.POST.get('price') or 0,
            quantity=request.POST.get('quantity', 1),
            unit=request.POST.get('unit', 'Piece').strip(),
            purchase_date=request.POST.get('purchase_date') or None,
            description=request.POST.get('description', '').strip(),
            condition=request.POST.get('condition', 'Good').strip(),
        )
        return redirect('equipment_list')
    return render(request, 'equipment_form.html')


@staff_member_required(login_url='admin_login')
def equipment_list(request):
    return render(request, 'equipment_list.html', {'equipment': Equipment.objects.all()})


@staff_member_required(login_url='admin_login')
def equipment_delete(request, equipment_id):
    if request.method == 'POST':
        equipment = get_object_or_404(Equipment, id=equipment_id)
        equipment.delete()
        messages.success(request, 'Equipment deleted successfully.')
    return redirect('equipment_list')


@staff_member_required(login_url='admin_login')
def member_add(request):
    plans = GymPlan.objects.filter(is_active=True)
    if request.method == 'POST':
        Member.objects.create(
            name=request.POST.get('name', '').strip(),
            phone=request.POST.get('phone', '').strip(),
            email=request.POST.get('email', '').strip(),
            age=request.POST.get('age') or None,
            gender=request.POST.get('gender', '').strip(),
            plan_id=request.POST.get('plan') or None,
            join_date=request.POST.get('join_date') or timezone.localdate(),
            expiry_date=request.POST.get('expiry_date') or None,
            initial_amount=request.POST.get('initial_amount') or 0,
        )
        return redirect('member_list')
    return render(request, 'member_form.html', {'plans': plans})


@staff_member_required(login_url='admin_login')
def member_list(request):
    members = Member.objects.select_related('plan').all()
    return render(request, 'member_list.html', {'members': members})


@staff_member_required(login_url='admin_login')
def member_delete(request, member_id):
    if request.method == 'POST':
        member = get_object_or_404(Member, id=member_id)
        member.delete()
        messages.success(request, 'Member deleted successfully.')
    return redirect('member_list')