from restfulpy.testing import ApplicableTestCase

from card_holder import Cardholder


class LocalApplicationTestCase(ApplicableTestCase):
    __application_factory__ = Cardholder

