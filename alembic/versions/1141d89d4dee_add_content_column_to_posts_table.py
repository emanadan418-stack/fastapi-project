"""add content column to posts table
Revision ID: 1141d89d4dee
Revises: 747f20c53cfd
Create Date: 2026-01-10 07:59:48.495192
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision: str = '1141d89d4dee'
down_revision: Union[str, Sequence[str], None] = '747f20c53cfd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
