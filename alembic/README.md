
# Project Name

This project uses SQLAlchemy and Alembic for database migrations. Below are some common commands and usage patterns for managing your database schema with Alembic.

## Prerequisites

- **Python** (version 3.x)
- **PostgreSQL** (or any other SQLAlchemy-supported database)
- **SQLAlchemy** (for defining models)
- **Alembic** (for managing migrations)

## Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize Alembic:**
   ```bash
   alembic init alembic
   ```

3. **Configure Alembic:**
   Update the `sqlalchemy.url` in `alembic.ini` with your database connection string:
   ```ini
   sqlalchemy.url = postgresql://user:password@localhost/dbname
   ```

## Common Usage

### 1. Create a New Table

To create a new table, define a model in your `models/` directory.

**Example: `models/kline.py`**
```python
from sqlalchemy import Column, Integer, String, Float, Date
from . import Base

class KLine(Base):
    __tablename__ = 'kline'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)
```

**Generate the migration:**
```bash
alembic revision --autogenerate -m "Create kline table"
```

**Apply the migration:**
```bash
alembic upgrade head
```

### 2. Add a New Column

To add a new column to an existing table, update the corresponding model.

**Example: Adding an `adjusted_close` column to the `KLine` model:**
```python
class KLine(Base):
    __tablename__ = 'kline'

    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    adjusted_close = Column(Float)  # New column added
    volume = Column(Float, nullable=False)
```

**Generate the migration:**
```bash
alembic revision --autogenerate -m "Add adjusted_close column to kline table"
```

**Apply the migration:**
```bash
alembic upgrade head
```

### 3. Add a Foreign Key

To add a foreign key, update your model to include a relationship.

**Example: Adding a `user_id` foreign key to a `Trades` table:**

First, define the `User` model if not already defined:
```python
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
```

Next, define the `Trades` model with a foreign key to the `User` table:
```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Trade(Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
    
    user = relationship("User")
```

**Generate the migration:**
```bash
alembic revision --autogenerate -m "Add trades table with user_id foreign key"
```

**Apply the migration:**
```bash
alembic upgrade head
```

## Reverting Migrations

To undo the last migration:

```bash
alembic downgrade -1
```

To revert all migrations:

```bash
alembic downgrade base
```

## Checking the Database State

To check the current revision of the database:

```bash
alembic current
```

To view the migration history:

```bash
alembic history
```

## Troubleshooting

- **Target database is not up to date:** Ensure you've applied all migrations with `alembic upgrade head`.
- **Can't proceed with `--autogenerate` option:** Ensure `Base.metadata` is correctly referenced in `env.py`.

## License

This project is licensed under the MIT License.
