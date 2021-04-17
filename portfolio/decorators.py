from django.shortcuts import redirect, Http404

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_staff:
            raise Http404
        return view_func(request, *args, **kwargs)
    return wrapper_func