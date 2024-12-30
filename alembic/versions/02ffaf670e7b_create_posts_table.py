"""create posts table

Revision ID: 02ffaf670e7b
Revises: 
Create Date: 2024-12-24 15:00:38.569640

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02ffaf670e7b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("Post",sa.Column("id",sa.Integer(),nullable=False,primary_key=True)
                    ,sa.Column("title",sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('Post')
    pass
