from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VendorForm
from .models import Vendor


@login_required
def create_store(request):

    if request.user.role != "vendor":
        return redirect('profile')

    if request.method == "POST":

        form = VendorForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            vendor = form.save(commit=False)

            vendor.user = request.user

            vendor.save()

            return redirect('vendor_dashboard')

    else:

        form = VendorForm()

    return render(
        request,
        'vendors/create_store.html',
        {'form': form}
    )


@login_required
def vendor_dashboard(request):

    vendor = Vendor.objects.get(user=request.user)

    return render(
        request,
        'vendors/vendor_dashboard.html',
        {'vendor': vendor}
    )