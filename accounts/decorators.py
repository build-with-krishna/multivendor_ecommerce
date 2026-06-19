from django.shortcuts import redirect


def superadmin_required(view_func):

    def wrapper(request,*args,**kwargs):

        if request.user.is_authenticated and request.user.role=="superadmin":
            return view_func(request,*args,**kwargs)

        return redirect('home')

    return wrapper


def vendor_required(view_func):

    def wrapper(request,*args,**kwargs):

        if request.user.is_authenticated and request.user.role=="vendor":
            return view_func(request,*args,**kwargs)

        return redirect('home')

    return wrapper


def customer_required(view_func):

    def wrapper(request,*args,**kwargs):

        if request.user.is_authenticated and request.user.role=="customer":
            return view_func(request,*args,**kwargs)

        return redirect('home')

    return wrapper