from db_utils.db_declaration import Danmu, LiveStatus, Gift, SuperChat, Captain, View
from peewee import SqliteDatabase

path = "db/24393.db" 

db = SqliteDatabase(path, pragmas=(
            ('cache_size', -1024 * 64),  # 64MB page-cache.
            ('journal_mode', 'wal'))) # Use WAL-mode (you should always use this!).
db.connect()
db.bind([Danmu, LiveStatus, Gift, SuperChat, Captain, View])
db.create_tables([Danmu, LiveStatus, Gift, SuperChat, Captain, View])
