from django.http import HttpResponseForbidden

def subscription_required(view):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.session['sub_state'] != 'active':
                return HttpResponseForbidden('Unauthorized')

        return view(request, *args, **kwargs)

    return _wrapped_view
