"""add_content_column

Revision ID: e00b767730ab
Revises: 97e1359c521f
Create Date: 2024-12-30 10:27:07.944518

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e00b767730ab'
down_revision: Union[str, None] = '97e1359c521f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass

