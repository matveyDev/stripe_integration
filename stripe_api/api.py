import stripe

from item.models import Item
from .config import API_KEY


stripe.api_key = API_KEY


class StripeAPI:

    @staticmethod
    def _get_session_id(item_id: int) -> str:
        item = Item.objects.get(id=item_id)
        session = stripe.checkout.Session.create(
            line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price),
            },
            'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/cancel',
        )

        return session.id
