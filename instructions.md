To run app:
uvicorn main:app --reload

To run sqlite:
sqlite3 todosapp.db

To read jwt:
http://jwt.io/

1 command integrate alembic:
alembic init alembic

2 command to migrate:
alembic revision --autogenerate -m "initial migration"
alembic upgrade head

Downgrade migration:
alembic downgrade -1

1. we do revision that what changes will be done 
* alembic revision -m "Create phone number for user column"
2. change upgrade section
* def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(length=12), nullable=True))
3. run upgrade command
* alembic upgrade "revision_id"

For downgrade:
in alembic python file:
def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')

alembic downgrade -1


 pytest --disable-warnings
