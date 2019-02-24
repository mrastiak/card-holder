from nanohttp import Controller, json
from restfulpy.controllers import RootController

import card_holder
from .foo import FooController
from .cards import CardController


class ApiV1(Controller):
    foos = FooController()
    cards = CardController()

    @json
    def version(self):
        return {
            'version': card_holder.__version__
        }


class Root(RootController):
    apiv1 = ApiV1()

