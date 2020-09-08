from django.contrib import admin

class AdminSite(admin.AdminSite):

    def has_permission(self, request):
        return request.user.is_active

cymol = AdminSite(name='cymol')