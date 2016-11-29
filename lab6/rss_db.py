import sqlite3

import rss_channel
import rss_post


class rss_db:
    connection = None
    cursor = None

    def __init__(self):
        self.connection = sqlite3.connect('rss.db')
        self.cursor = self.connection.cursor()

    def insert_post(self, post: rss_post):
        self.cursor.execute("Insert into rss_post VALUES (Null, ?, ?, ?, ?, ?)",
                            (post.channel_id,
                             post.title,
                             post.link,
                             post.data,
                             post.pub_date))
        id_ = self.cursor.lastrowid
        self.connection.commit()
        return id_

    def find_post(self, channel_id: int, link: str):
        self.cursor.execute("select * from rss_post where channel_id = ? and link=?", (channel_id, link))
        return self.posts_mapping()

    def find_posts(self, channel_id: int, count: int, page:int):
        self.cursor.execute("select * from rss_post where channel_id = ? limit ? offset ?", (channel_id, count, page*count))
        return self.posts_mapping()

    def posts_mapping(self):
        res_list = []
        for row in self.cursor:
            post = rss_post.rss_post()
            post.id = row[0]
            post.channel_id = row[1]
            post.title = row[2]
            post.link = row[3]
            post.data = row[4]
            post.pub_date = row[5]
            res_list.append(post)
        self.cursor.close()
        self.cursor = self.connection.cursor()
        return res_list

    def insert_channel(self, channel):
        self.cursor.execute("Insert into rss_channel VALUES (NULL, ?, ?, ?, ?)",
                            (channel.title,
                             channel.description,
                             channel.link,
                             channel.url))
        id_ = self.cursor.lastrowid
        self.connection.commit()
        return id_



    def find_channel(self, channel_url):
        self.cursor.execute("select * from rss_channel where url=?", [channel_url])
        return self.channel_mapping()

    def find_channel_by_id(self, id: int):
        self.cursor.execute("select * from rss_channel where id=?", [id])
        return self.channel_mapping()

    def find_channel_by_name(self, channel_name):
        self.cursor.execute("select * from rss_channel where title=?", [channel_name])
        return self.channel_mapping()

    def find_all_channels(self):
        self.cursor.execute("select * from rss_channel")
        return self.channel_mapping()

    def channel_mapping(self):
        res_list = []
        for row in self.cursor:
            channel = rss_channel.rss_channel()
            channel.id = row[0]
            channel.title = row[1]
            channel.description = row[2]
            channel.link = row[3]
            channel.url = row[4]
            res_list.append(channel)
        return res_list

    def find_all_urls(self):
        self.cursor.execute("select url from rss_channel")
        res_list = []
        for row in self.cursor:
            res_list.append(row[0])
        return res_list
