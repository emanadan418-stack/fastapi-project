"""add user table
Revision ID: 426ca8dde49a
Revises: 1141d89d4dee
Create Date: 2026-01-10 08:07:30.415640
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '426ca8dde49a'
down_revision: Union[str, Sequence[str], None] = '1141d89d4dee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                )
    pass

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
