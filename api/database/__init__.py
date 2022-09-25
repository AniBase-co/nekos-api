from playhouse.sqlite_ext import SqliteExtDatabase

db = SqliteExtDatabase(
    'db.sqlite3', 
    pragmas={
        'journal_mode': 'wal',
        'cache_size': -64 * 1000,      # 64 MB cache
        'synchronous': 0,              # Managed by OS
        'foreign_keys': 1,             # Enforce foreign key constraints
        'ignore_check_constraints': 0, # Enforce constraint checks
    }
)
