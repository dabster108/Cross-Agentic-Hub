"""Database connection management for Neon PostgreSQL."""

import asyncpg
from typing import Optional
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_7gtqkuHF4LXb@ep-patient-rice-ai7k18a9-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

logger = logging.getLogger(__name__)

# Global connection pool
_pool: Optional[asyncpg.Pool] = None


async def init_db() -> None:
    """Initialize database connection pool."""
    global _pool
    try:
        _pool = await asyncpg.create_pool(
            dsn=DATABASE_URL,
            min_size=2,
            max_size=10,
            command_timeout=60,
        )
        logger.info("Database connection pool initialized successfully")
        
        # Test the connection
        async with _pool.acquire() as conn:
            version = await conn.fetchval("SELECT version()")
            logger.info(f"Connected to PostgreSQL: {version}")
            
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise


async def close_db() -> None:
    """Close database connection pool."""
    global _pool
    if _pool:
        await _pool.close()
        logger.info("Database connection pool closed")
        _pool = None


async def get_db() -> asyncpg.Connection:
    """
    Get a database connection from the pool.
    
    Usage:
        conn = await get_db()
        try:
            result = await conn.fetch("SELECT * FROM users")
        finally:
            await conn.close()
    """
    if not _pool:
        raise RuntimeError("Database pool not initialized. Call init_db() first.")
    
    return await _pool.acquire()


def get_db_context():
    """
    Get a database connection context manager from the pool.
    
    Usage:
        async with get_db_context() as conn:
            result = await conn.fetch("SELECT * FROM users")
    """
    if not _pool:
        raise RuntimeError("Database pool not initialized. Call init_db() first.")
    
    return _pool.acquire()


async def execute_query(query: str, *args) -> None:
    """Execute a query without returning results."""
    async with get_db_context() as conn:
        await conn.execute(query, *args)


async def fetch_one(query: str, *args):
    """Fetch a single row."""
    async with get_db_context() as conn:
        return await conn.fetchrow(query, *args)


async def fetch_all(query: str, *args):
    """Fetch all rows."""
    async with get_db_context() as conn:
        return await conn.fetch(query, *args)


async def fetch_val(query: str, *args):
    """Fetch a single value."""
    async with get_db_context() as conn:
        return await conn.fetchval(query, *args)
