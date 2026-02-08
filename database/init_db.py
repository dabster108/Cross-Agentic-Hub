"""Database initialization script."""

import asyncio
import logging
from .connection import init_db, close_db, get_db_context
from .models import CREATE_TABLES, DROP_TABLES

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def create_tables():
    """Create all database tables."""
    try:
        async with get_db_context() as conn:
            await conn.execute(CREATE_TABLES)
            logger.info("✓ All tables created successfully")
    except Exception as e:
        logger.error(f"✗ Failed to create tables: {e}")
        raise


async def drop_tables():
    """Drop all database tables (use with caution!)."""
    try:
        async with get_db_context() as conn:
            await conn.execute(DROP_TABLES)
            logger.info("✓ All tables dropped successfully")
    except Exception as e:
        logger.error(f"✗ Failed to drop tables: {e}")
        raise


async def reset_database():
    """Drop and recreate all tables."""
    logger.warning("⚠️  Resetting database - all data will be lost!")
    await drop_tables()
    await create_tables()
    logger.info("✓ Database reset complete")


async def main():
    """Main initialization function."""
    logger.info("Starting database initialization...")
    
    try:
        # Initialize connection pool
        await init_db()
        
        # Create tables
        await create_tables()
        
        logger.info("✓ Database initialization completed successfully")
        
    except Exception as e:
        logger.error(f"✗ Database initialization failed: {e}")
        raise
    finally:
        await close_db()


if __name__ == "__main__":
    asyncio.run(main())
