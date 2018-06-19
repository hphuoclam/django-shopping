from django.utils import translation

class LocaleMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language_code = 'vi' #TODO, your logic

        translation.activate(language_code)

        response = self.get_response(request)

        translation.deactivate()

        return response