from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from braces.views import CsrfExemptMixin
from predict.object_detection_runner import main

import base64


def index(request):
    return HttpResponse("Hello, world. You're at the predict index.")

@require_POST
@csrf_exempt
def predict(request):
    image = request.body

    # Armar imagen
    img = base64.decodestring(image)

    # Guardar Image
    open('predict/test_images/temp.jpg', 'wb').write(img)

    # Predicciones de la imagen
    prediction = {}
    prediction['saludos'] = "hola"
    prediction['prediction'] = main()
    prediction['imagen'] = base64.encodestring(open('predict/output/temp.jpg', 'rb').read()).decode('ascii')

    return JsonResponse(prediction)
