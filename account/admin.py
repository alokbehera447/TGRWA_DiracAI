from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from account.models import Account, UserType, UserTitle, FutureCustomerContacts, Institute, DegreeName, DocumentCopy, MarkSheet, Certificate, EduDegree,Achievements, Address

from django.core.paginator import Paginator


class NoCountPaginator(Paginator):
    @property
    def count(self):
        return 999999999




class AccountAdmin(UserAdmin):
        list_select_related = True
        list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff','usertype')
        search_fields = ('email','username',)
        readonly_fields=('id', 'date_joined', 'last_login')
        filter_horizontal = ()
        list_filter = ()
        fieldsets = ()
        show_full_result_count = False



admin.site.register(Account, AccountAdmin)

admin.site.register(UserType)
admin.site.register(UserTitle)
admin.site.register(FutureCustomerContacts)
admin.site.register(Institute)
admin.site.register(DegreeName)
admin.site.register(DocumentCopy)
admin.site.register(MarkSheet)
admin.site.register(Certificate)
admin.site.register(EduDegree)
admin.site.register(Achievements)
admin.site.register(Address)











