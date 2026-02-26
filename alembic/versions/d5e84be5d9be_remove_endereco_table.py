"""remove endereco table

Revision ID: d5e84be5d9be
Revises: e76a67f61b8d
Create Date: 2026-02-26 15:13:53.733170

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5e84be5d9be'
down_revision: Union[str, Sequence[str], None] = 'e76a67f61b8d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.drop_table("enderecos")

def downgrade():
    pass
