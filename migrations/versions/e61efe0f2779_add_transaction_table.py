"""add transaction table

Revision ID: e61efe0f2779
Revises: bc6c672cfd3f
Create Date: 2022-08-05 22:45:38.107570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e61efe0f2779'
down_revision = 'bc6c672cfd3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quote_id', sa.String(length=255), nullable=False),
    sa.Column('recipient_id', sa.String(length=255), nullable=False),
    sa.Column('transfer_id', sa.String(length=255), nullable=False),
    sa.Column('target_account_id', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('complaint_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['complaint_id'], ['complainers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    # ### end Alembic commands ###
