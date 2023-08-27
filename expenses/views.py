from django.shortcuts import render
from .models import ExpenseRecord  # Import your models here


def dashboard_view(request):
    # Add logic to generate data for your charts
    context = {
        'current_tab': 'dashboard',
        # Add other context data here
    }
    return render(request, 'templates/dashboard.html', context)


def records_view(request):
    # Fetch expense records from the database
    expense_records = ExpenseRecord.objects.all()
    context = {
        'current_tab': 'records',
        'expense_records': expense_records,
    }
    return render(request, 'templates/records.html', context)


def imports_view(request):
    # Add logic to fetch import history from the database
    context = {
        'current_tab': 'imports',
        # Add other context data here
    }
    return render(request, 'templates/imports.html', context)

def analytics_view(request):
    # Add logic to handle analytics functionality
    context = {
        'current_tab': 'analytics',
        # Add other context data here
    }
    return render(request, 'templates/analytics.html', context)
