from django.urls import path

from .views import ContactListView, ContactProfileDetailView,  add_contact, edit_contact, delete_contact

urlpatterns = [
    path('', ContactListView.as_view(), name='index'),
    path('add-contact/', add_contact, name='add-contact'),
    path('profile/<int:pk>/', ContactProfileDetailView.as_view(), name='profile'),
    path('edit-contact/<int:pk>/', edit_contact, name='edit_contact'),
    path('delete-contact/<int:pk>/', delete_contact, name='delete_contact')
]
