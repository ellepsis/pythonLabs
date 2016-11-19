import feedparser

from rss_db import rss_db
import rss_worker

"""
Простой RSS reader

При добавлении ленты (например https://habrahabr.ru/rss/interesting/)
записи из добавленной ленты сканируются и заносятся в базу (например sqlite)

При нажатии на кнопку обновить - новое сканирование и добавление новых записей (без дублрования существующих)

Отображение ленты начиная с самых свежих записей с пагинацией (несколько записей на странице)

Записи из разных лент хранить и показывать отдельно (по названию ленты).
"""


def main():
    rss_db_connection = rss_db()
    rss_worker.add_new_channel(rss_db_connection, "https://habrahabr.ru/rss/interesting/")
    rss_worker.update_all_channels(rss_db_connection)


if __name__ == "__main__":
    main()
