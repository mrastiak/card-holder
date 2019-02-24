from nanohttp import json, HTTPNotFound, int_or_notfound
from restfulpy.controllers import ModelRestController
from restfulpy.orm import DBSession

from ..models import Card


class CardController(ModelRestController):
    __model__ = Card

    @json(prevent_form=True)
    def get(self, id):
        id = int_or_notfound(id)

        card = DBSession.query(Card).get(id)
        if card is None:
            raise HTTPNotFound()

        return card

