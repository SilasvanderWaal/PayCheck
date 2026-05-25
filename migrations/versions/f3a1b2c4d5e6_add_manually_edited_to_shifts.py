"""add manually_edited to shifts

Revision ID: f3a1b2c4d5e6
Revises: a8eafe753f15
Create Date: 2026-05-25 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f3a1b2c4d5e6'
down_revision = 'a8eafe753f15'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('shifts', schema=None) as batch_op:
        batch_op.add_column(sa.Column(
            'manually_edited',
            sa.Boolean(),
            nullable=False,
            server_default=sa.false()
        ))


def downgrade():
    with op.batch_alter_table('shifts', schema=None) as batch_op:
        batch_op.drop_column('manually_edited')
