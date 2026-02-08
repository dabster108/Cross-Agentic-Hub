"""Quick test to insert and query data from the database."""

import asyncio
from database import init_db, close_db, get_db_context


async def test_insert():
    """Test inserting a user into the database."""
    try:
        await init_db()
        
        # Insert a test user
        async with get_db_context() as conn:
            user = await conn.fetchrow(
                """
                INSERT INTO users (username, email)
                VALUES ($1, $2)
                RETURNING id, username, email, created_at
                """,
                "test_user",
                "test@example.com"
            )
            print(f"✓ User created: {dict(user)}")
            
            # Query all users
            users = await conn.fetch("SELECT * FROM users")
            print(f"\n✓ Total users in database: {len(users)}")
            for u in users:
                print(f"  - {u['username']} ({u['email']})")
                
            # Show all tables
            tables = await conn.fetch(
                """
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name
                """
            )
            print(f"\n✓ Tables in database:")
            for t in tables:
                print(f"  - {t['table_name']}")
        
    finally:
        await close_db()


if __name__ == "__main__":
    asyncio.run(test_insert())
