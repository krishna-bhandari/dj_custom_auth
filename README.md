
Auth_user
=====

auth_user is a Django app to which is used to serve user objects. It is used to authenticate and authorize user, create custom user types (roles) and assign them different permissions.

Detailed documentation is in the "docs" directory.

Quick start
-----------

Note**: This package must be used before running your first migrate command.

1. Add "auth_user" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'auth_user',
    ]

2. Also change the default user model for your project. To do that add this in settings.py ::

    AUTH_USER_MODEL = 'auth_user.User'


3. Include the polls URLconf in your project urls.py like this::

    path('auth_user/', include('auth_user.urls')),

4. Run ``python manage.py migrate`` to create the auth_user models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create permissions and other customizations (you'll need the Admin app enabled).

