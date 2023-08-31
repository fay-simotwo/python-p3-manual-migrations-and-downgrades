from alembic import op
import sqlalchemy as sa

def upgrade():
    # Alter the column in the 'table_name' table
    op.alter_column('table_name', 'old_column', new_column_name='new_column')

def downgrade():
    # This is the opposite of the upgrade - you might need to define how to undo the change
    op.alter_column('table_name', 'new_column', new_column_name='old_column')
