"""rename department

Revision ID: 3037ad19df75
Revises: 14f58a4296ac
Create Date: 2024-04-03 18:25:16.378523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3037ad19df75'
down_revision = '14f58a4296ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
