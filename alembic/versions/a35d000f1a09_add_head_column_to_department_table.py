"""Add head column to Department table

Revision ID: a35d000f1a09
Revises: 69a382117b53
Create Date: 2024-12-18 15:19:09.054338

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a35d000f1a09'
down_revision: Union[str, None] = '69a382117b53'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('head', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('departments', 'head')
    # ### end Alembic commands ###