from django.shortcuts import redirect
from django.utils.http import url_has_allowed_host_and_scheme
from urllib.parse import quote

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print(request.session.get('customer'))
        returnUrl = request.META.get('PATH_INFO', '/')
        # Ensure returnUrl is a safe, local path
        if not isinstance(returnUrl, str) or not returnUrl.startswith('/'):
            returnUrl = '/'
        if not url_has_allowed_host_and_scheme(
            url=returnUrl,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure(),
        ):
            returnUrl = '/'
        safe_return_url = quote(returnUrl, safe="/")
        print(request.META.get('PATH_INFO', '/'))
        if not request.session.get('customer'):
            return redirect(f'login?return_url={safe_return_url}')

        response = get_response(request)
        return response

    return middleware