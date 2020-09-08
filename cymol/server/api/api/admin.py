from django.contrib import admin

class AdminSite(admin.AdminSite):

    def has_permission(self, request):
        return request.user.is_active

cymol = AdminSite(name='cymol')

def register(model_or_iterator):
    def decorator(admin_class):
        cymol.register(model_or_iterator, admin_class)
    return decorator