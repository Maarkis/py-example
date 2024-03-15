"""create snapshot_product table

Revision ID: e80eb50e7725
Revises: 0b0f909519be
Create Date: 2024-03-14 21:07:26.024980

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e80eb50e7725"
down_revision: Union[str, None] = "0b0f909519be"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "snapshot_product",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("product_id", sa.Integer(), nullable=False, unique=True),
        sa.Column("snapshot", sa.String(length=255), nullable=False),
    )

    op.create_foreign_key(
        "fk_snapshot_product_product",
        "snapshot_product",
        "product",
        ["product_id"],
        ["id"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    op.drop_constraint(
        "fk_snapshot_product_product", "snapshot_product", type_="foreignkey"
    )
    op.drop_table("snapshot_product")
