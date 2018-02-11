"""empty message

Revision ID: a23d52153936
Revises: 
Create Date: 2018-02-08 13:38:42.971931

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a23d52153936'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cheapest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('extension', sa.String(length=20), nullable=True),
    sa.Column('reg_registrar', sa.String(length=20), nullable=True),
    sa.Column('reg_price', sa.Float(), nullable=True),
    sa.Column('renew_registrar', sa.String(length=20), nullable=True),
    sa.Column('renew_price', sa.Float(), nullable=True),
    sa.Column('tran_registrar', sa.String(length=20), nullable=True),
    sa.Column('tran_price', sa.Float(), nullable=True),
    sa.Column('popularity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('test')
    op.drop_index('ix_domains_name', table_name='domains')
    op.create_index(op.f('ix_domains_name'), 'domains', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_domains_name'), table_name='domains')
    op.create_index('ix_domains_name', 'domains', ['name'], unique=False)
    op.create_table('test',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('info', mysql.VARCHAR(length=20), nullable=True),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('cheapest')
    # ### end Alembic commands ###
