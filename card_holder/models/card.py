from restfulpy.orm import DeclarativeBase, Field, FilteringMixin, \
    PaginationMixin, OrderingMixin

from sqlalchemy import Unicode, Integer


class Card(FilteringMixin, PaginationMixin, OrderingMixin, DeclarativeBase):
    __tablename__ = 'card'

    type_ = Field(String(100), readonly=True)
    __mapper_args__ = {
        'polymorphic_on': type_,
        'polymorphic_identity': __tablename__
    }

    id = Field(Integer, primary_key=True)
    name = Field(
        Unicode(50),
        readonly=False,
        max_length=50,
        min_length=3,
        not_none=True,
        nullable=False,
        required=True,
        python_type=str,
    )
    pan = Field(
        Unicode(19),
        readonly=False,
        max_length=19,
        min_length=16,
        not_none=True,
        nullable=False,
        required=True,
        python_type=str,
    )
    owner = Field(
        Unicode(50),
        readonly=False,
        max_length=50,
        min_length=3,
        not_none=True,
        nullable=False,
        required=True,
        python_type=str,
    )

class MyCard(Card):
    __mapper_args__ = {'polymorphic_identity': __tablename__}

     cvv2 = Field(
         Integer,
         readonly=False,
         minimum=100,
         maximum=9999,
         not_none=False,
         nullable=True,
         required=False,
         python_type=int,
     )
     pin1 = Field(
         Unicode(4),
         readonly=False,
         min_length=4,
         max_length=4,
         not_none=False,
         nullable=True,
         required=False,
         python_type=str,
     )
     pin2= Field(
         Uncicode(12),
         readonly=False,
         min_length=5,
         max_length=12,
         not_none=False,
         nullable=True,
         required=False,
         python_type=str,
     )

