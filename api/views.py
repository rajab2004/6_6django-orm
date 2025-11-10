from django.http import HttpRequest, JsonResponse


def products_view(request: HttpRequest) -> JsonResponse:
    
    return JsonResponse(data={})

