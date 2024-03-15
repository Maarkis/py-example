"""create product table

Revision ID: 0b0f909519be
Revises: 
Create Date: 2024-03-14 17:26:42.200264

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0b0f909519be"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "product",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column(
            "sku", sa.String(length=255), nullable=False, unique=True, index=True
        ),
        sa.Column("provider", sa.String(length=100), nullable=False),
        sa.Column("machine_name", sa.String(length=255), nullable=False),
        sa.Column("value", sa.Numeric(precision=5, scale=3), nullable=False),
        sa.Column("cpu", sa.Integer(), nullable=False),
        sa.Column("ram", sa.Integer(), nullable=False),
        sa.Column("disk", sa.Integer(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("product")
