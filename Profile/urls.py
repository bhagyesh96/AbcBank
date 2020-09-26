
from . import views
from django.urls import path

app_name = "profiles"

urlpatterns = [
    path("account_status/", views.index, name = "account_status"),
    path("account_service/", views.account_service, name = "account_service"),
    path("add_fund/", views.add_fund, name = "add_fund"),
    path("statement/", views.statement, name = "statement"),
    path("manager_dashboard/", views.managerBank, name = "manager_dash"),
    path("manager_statement/", views.managerBank, name = "manager_statement"),
]