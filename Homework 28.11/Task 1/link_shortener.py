import shelve

DATABASE_FILE = "links_db"

class LinkShortener:
    def __init__(self):
        self.db_file = DATABASE_FILE

    def add_link(self, original_url, short_name):
        with shelve.open(self.db_file) as db:
            if short_name in db:
                return f"Назва '{short_name}' вже використовується!"
            db[short_name] = original_url
            return f"Додано: {original_url} -> {short_name}"

    def get_link(self, short_name):
        with shelve.open(self.db_file) as db:
            if short_name in db:
                return db[short_name]
            return f"Посилання для назви '{short_name}' не знайдено!"

    def delete_link(self, short_name):
        with shelve.open(self.db_file) as db:
            if short_name in db:
                del db[short_name]
                return f"Посилання '{short_name}' успішно видалено!"
            return f"Посилання '{short_name}' не знайдено!"

    def list_links(self):
        with shelve.open(self.db_file) as db:
            return {key: db[key] for key in db}
