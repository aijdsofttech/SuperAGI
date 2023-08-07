"""updated_tool_configs

Revision ID: d8315244ea43
Revises: 71e3980d55f5
Create Date: 2023-08-01 11:11:32.725355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8315244ea43'
down_revision = '5d5f801f28e7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tool_configs', sa.Column('key_type', sa.String(), nullable=True))
    op.add_column('tool_configs', sa.Column('is_secret', sa.Boolean(), nullable=True))
    op.add_column('tool_configs', sa.Column('is_required', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tool_configs', 'is_required')
    op.drop_column('tool_configs', 'is_secret')
    op.drop_column('tool_configs', 'key_type')
    # ### end Alembic commands ###
