"""criando tabela orders

Revision ID: 6079fbba8754
Revises: 1e2a882777ba
Create Date: 2022-04-28 17:23:23.213860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6079fbba8754"
down_revision = "1e2a882777ba"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "orders",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("date", sa.DateTime(), nullable=True),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("orders")
    # ### end Alembic commands ###