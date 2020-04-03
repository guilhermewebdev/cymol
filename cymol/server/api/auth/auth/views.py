from django.http import HttpResponse, Http404
from . import settings
from django.utils.translation import gettext as _

def keys(request, key):
    l = {
        'private.pem': settings.PRIVATE_KEY,
        'public.pem': settings.PUBLIC_KEY,
        'secret.key': settings.SECRET_KEY,
    }
    if key in l:
        return HttpResponse(
            content=l[key],
            content_type='text/plain'
        )
    raise Http404(_('Chave não encontrada'))