"""adding new column to person model

Revision ID: 53bb9b9ee007
Revises: bbd4d6b41a93
Create Date: 2021-11-28 17:58:28.402864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53bb9b9ee007'
down_revision = 'bbd4d6b41a93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('phone_number', sa.String(length=120), nullable=False))
    op.create_unique_constraint(None, 'person', ['phone_number'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'person', type_='unique')
    op.drop_column('person', 'phone_number')
    # ### end Alembic commands ###