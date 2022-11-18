from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from item.models import Item
from stripe_api.api import StripeAPI

API = StripeAPI()


@api_view(['GET'])
def get_session_id(request, id: int):
    session_id = API._get_session_id(id)
    return Response({'session_id': session_id})


class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'item_buy.html'

    def get(self, request, id: int):
        item = Item.objects.get(id=id)
        return Response({'item': item})
