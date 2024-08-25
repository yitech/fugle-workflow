from sqlalchemy.ext.declarative import declarative_base

# Define Base once
Base = declarative_base()

# Import your models
from .kline import KLine

# Make the models available for import
__all__ = ['KLine']