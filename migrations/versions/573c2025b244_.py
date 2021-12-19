"""empty message

Revision ID: 573c2025b244
Revises: b95b3949fbfb
Create Date: 2021-12-18 18:52:15.617512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '573c2025b244'
down_revision = 'b95b3949fbfb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=300), nullable=False),
    sa.Column('commentposter', sa.Integer(), nullable=False),
    sa.Column('postId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['commentposter'], ['user.id'], ),
    sa.ForeignKeyConstraint(['postId'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_comments')
    # ### end Alembic commands ###
