"""Add is_admin column

Revision ID: 27458e6e6c1d
Revises: 927ce54614a1
Create Date: 2024-02-14 15:09:29.868812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27458e6e6c1d'
down_revision = '927ce54614a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_admin')

    # ### end Alembic commands ###
