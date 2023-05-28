"""New Migration

Revision ID: a43218b21e49
Revises: c323cccb0564
Create Date: 2023-05-12 20:18:09.614707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a43218b21e49'
down_revision = 'c323cccb0564'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('hashed_password', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'hashed_password')
    # ### end Alembic commands ###