"""empty message

Revision ID: 8c1d746f5f13
Revises: 4020d08ee63b
Create Date: 2023-09-06 19:13:29.440787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c1d746f5f13'
down_revision = '4020d08ee63b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('profile_picture_link', sa.String(length=1000), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_column('profile_picture_link')

    # ### end Alembic commands ###
