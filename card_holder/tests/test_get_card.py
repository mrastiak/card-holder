from bddrest import status, when, response

from card_holder.tests.helpers import LocalApplicationTestCase
from card_holder.models import Card


class TestCard(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        session = cls.create_session()

        cls.card = Card(
            name='Card',
            pan='1234567890123456',
            owner='John Doe',
        )
        session.add(cls.card)
        session.commit()

    def test_get(self):
        with self.given(
            'Get a Card',
            f'/apiv1/cards/id: {self.card.id}',
        ):
            assert status == 200
            assert response.json['id'] == self.card.id
            assert response.json['name'] == self.card.name
            assert response.json['pan'] == self.card.pan

            when(
                'Passing chert o pert ID',
                url_parameters=dict(id=0)
            )
            assert status == 404

            when(
                'Passing invalid type ID',
                url_parameters=dict(id='baghali')
            )
            assert status == 404

            when(
                'Passing form',
                form=dict(a='b'),
            )
            assert status == 400


