"""empty message

Revision ID: 532e487a994e
Revises: 
Create Date: 2024-11-04 15:44:20.008926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '532e487a994e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alert',
    sa.Column('alert_id', sa.Integer(), nullable=False),
    sa.Column('alert_time', sa.DateTime(), nullable=True),
    sa.Column('alert_type', sa.String(length=50), nullable=False),
    sa.Column('messege', sa.String(length=50), nullable=False),
    sa.Column('alert_status', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('alert_id')
    )
    op.create_table('location',
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.Column('state', sa.String(length=30), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('zipcode', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('location_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('house',
    sa.Column('house_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('house_no', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['location_id'], ['location.location_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('house_id'),
    sa.UniqueConstraint('room_id')
    )
    op.create_table('device',
    sa.Column('house_id', sa.Integer(), nullable=False),
    sa.Column('device_id', sa.Integer(), nullable=False),
    sa.Column('device_name', sa.String(length=50), nullable=False),
    sa.Column('device_type', sa.String(length=50), nullable=False),
    sa.Column('device_status', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['house_id'], ['house.house_id'], ),
    sa.PrimaryKeyConstraint('device_id')
    )
    op.create_table('sensor',
    sa.Column('sensor_id', sa.Integer(), nullable=False),
    sa.Column('device_id', sa.Integer(), nullable=False),
    sa.Column('sensor_type', sa.String(length=50), nullable=False),
    sa.Column('sensor_status', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['device_id'], ['device.device_id'], ),
    sa.PrimaryKeyConstraint('sensor_id')
    )
    op.create_table('sensor_data',
    sa.Column('sensor_data_id', sa.Integer(), nullable=False),
    sa.Column('sensor_id', sa.Integer(), nullable=False),
    sa.Column('data_value', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sensor_id'], ['sensor.sensor_id'], ),
    sa.PrimaryKeyConstraint('sensor_data_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sensor_data')
    op.drop_table('sensor')
    op.drop_table('device')
    op.drop_table('house')
    op.drop_table('user')
    op.drop_table('location')
    op.drop_table('alert')
    # ### end Alembic commands ###
