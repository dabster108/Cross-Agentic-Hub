"""Test database insertion."""

import asyncio
import logging
from .connection import init_db, close_db, get_db_context

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def test_insert():
    """Test inserting a user into the database."""
    try:
        # Initialize database connection
        await init_db()
        logger.info("Database connected")
        
        # Insert a test user
        async with get_db_context() as conn:
            result = await conn.fetchrow(
                """
                INSERT INTO users (username, email)
                VALUES ($1, $2)
                RETURNING id, username, email, created_at
                """,
                "test_user",
                "test@example.com"
            )
            
            logger.info(f"✓ User inserted successfully:")
            logger.info(f"  ID: {result['id']}")
            logger.info(f"  Username: {result['username']}")
            logger.info(f"  Email: {result['email']}")
            logger.info(f"  Created: {result['created_at']}")
            
        # Verify the insertion
        async with get_db_context() as conn:
            count = await conn.fetchval("SELECT COUNT(*) FROM users")
            logger.info(f"✓ Total users in database: {count}")
            
    except Exception as e:
        logger.error(f"✗ Error: {e}")
        raise
    finally:
        await close_db()
        logger.info("Database connection closed")


if __name__ == "__main__":
    asyncio.run(test_insert())
