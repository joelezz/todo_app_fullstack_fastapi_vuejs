from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///mydb.db", echo=True)

with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            is_done INTEGER NOT NULL DEFAULT 0
        )
    """))
print("✅ Database initialized!")
