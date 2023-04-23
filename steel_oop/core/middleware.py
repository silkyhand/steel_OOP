from datetime import datetime, timedelta
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse


class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Convert datetime to string
            last_activity_time = request.session.get('last_activity_time')
            if last_activity_time and (datetime.now() - datetime.strptime(last_activity_time, '%Y-%m-%d %H:%M:%S')) > timedelta(seconds=settings.SESSION_COOKIE_AGE):
                # User's session has expired
                del request.session['last_activity_time']
                logout_url = reverse('users:logout')  # Replace 'logout' with your actual logout URL name
                return redirect(logout_url)

            # Update the last activity time in the session
            request.session['last_activity_time'] = current_time

        return self.get_response(request)

        