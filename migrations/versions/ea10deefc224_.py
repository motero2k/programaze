"""empty message

Revision ID: ea10deefc224
Revises: 
Create Date: 2023-11-21 09:22:23.175732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea10deefc224'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('evidence',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('file_folder',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('parent_folder_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_folder_id'], ['file_folder.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('innosoft_day',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('subject', sa.String(length=100), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=256), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('token', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('coordinator',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event_manager',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('size_in_bytes', sa.BigInteger(), nullable=False),
    sa.Column('folder_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['folder_id'], ['file_folder.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lecturer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('president',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proposal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('subject', sa.String(length=100), nullable=False),
    sa.Column('proposal_type', sa.Enum('TALK', 'ACTIVITY', 'STAND', name='proposaltype'), nullable=False),
    sa.Column('state', sa.Enum('PENDING_OF_ADMISION', 'PENDING_OF_ACEPTATION', 'ON_PREPARATION', 'CONFIRMATED', 'REJECTED', 'CLOSED', name='state'), nullable=False),
    sa.Column('innosoft_day_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['innosoft_day_id'], ['innosoft_day.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviewer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('secretary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('token_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('num_token', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('token_state', sa.Enum('ACCEPTED', 'PENDING_OF_ACEPTATION', 'REJECTED', name='tokenstate'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_roles',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'role_id')
    )
    op.create_table('avatar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('votation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('state_votation', sa.Enum('ACCEPTED', 'REJECTED', 'IN_PROGRESS', name='statevotation'), nullable=False),
    sa.Column('proposal_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['proposal_id'], ['proposal.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('clean_name', sa.String(length=100), nullable=False),
    sa.Column('surname', sa.String(length=100), nullable=False),
    sa.Column('clean_surname', sa.String(length=100), nullable=False),
    sa.Column('dni', sa.String(length=20), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('avatar_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['avatar_id'], ['avatar.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    op.drop_table('votation')
    op.drop_table('avatar')
    op.drop_table('user_roles')
    op.drop_table('token_request')
    op.drop_table('student')
    op.drop_table('secretary')
    op.drop_table('reviewer')
    op.drop_table('proposal')
    op.drop_table('president')
    op.drop_table('lecturer')
    op.drop_table('file')
    op.drop_table('event_manager')
    op.drop_table('coordinator')
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('innosoft_day')
    op.drop_table('file_folder')
    op.drop_table('evidence')
    # ### end Alembic commands ###
