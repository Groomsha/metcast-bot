#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

"""
Project Name: 'Metcast Bot'
Description: Створення гри BlackJack для курсового проекту у CyberBionic Systematics
Ihor Cheberiak (c) 2022
https://www.linkedin.com/in/ihor-cheberiak/
"""

import sqlite3


def create_table(db_connect: sqlite3, db_cursor: sqlite3) -> None:
	create_table_id_user_chat: str = '''CREATE TABLE IF NOT EXISTS id_user_chat (
		id_chat INTEGER PRIMARY KEY, 
		id_update INTEGER);'''

	create_table_id_user_data: str = '''CREATE TABLE IF NOT EXISTS id_user_data (
		id_data INTEGER PRIMARY KEY, 
		username TEXT, 
		first_name TEXT,
		last_name TEXT,
		language TEXT);'''

	db_cursor.execute(create_table_id_user_chat)
	db_cursor.execute(create_table_id_user_data)
	db_connect.commit()


if __name__ == '__main__':
	connect: sqlite3 = sqlite3.connect('../telegram_chats.db')
	cursor: sqlite3 = connect.cursor()

	create_table(connect, cursor)

	sqlite_select_query: str = "select sqlite_version();"
	cursor.execute(sqlite_select_query)
	record = cursor.fetchall()

	print("Версия базы данных SQLite: ", record)
	connect.close()
