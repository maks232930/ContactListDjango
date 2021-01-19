from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Contact


class ContactListView(ListView):
    model = Contact
    context_object_name = 'contacts'
    template_name = 'contact/index.html'

    def get_queryset(self):
        search_input = self.request.GET.get('search-area')
        if search_input:
            return Contact.objects.filter(full_name__icontains=search_input)
        return Contact.objects.all()


def add_contact(request):
    if request.method == 'POST':
        new_contact = Contact(
            full_name=request.POST['fullname'],
            relationship=request.POST['relationship'],
            email=request.POST['e-mail'],
            phone_number=request.POST['phone-number'],
            address=request.POST['address']
        )
        new_contact.save()
        return redirect('index')
    return render(request, 'contact/new.html')


class ContactProfileDetailView(DetailView):
    model = Contact
    template_name = 'contact/contact-profile.html'
    context_object_name = 'contact'


def edit_contact(request, pk):
    contact = Contact.objects.get(pk=pk)

    if request.method == 'POST':
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['e-mail']
        contact.phone_number = request.POST['phone-number']
        contact.address = request.POST['address']
        contact.save()
        return redirect(contact.get_absolute_url())

    return render(request, 'contact/edit.html', {'contact': contact})


def delete_contact(request, pk):
    contact = Contact.objects.get(pk=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('index')

    return render(request, 'contact/delete.html', {'contact': contact})
