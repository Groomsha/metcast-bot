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
from typing import List, Tuple


class SQLiteWorker:
	def __init__(self, db_name: str) -> None:
		self.__connect: sqlite3 = sqlite3.connect(db_name)
		self.__cursor: sqlite3 = self.__connect.cursor()

	def save_new_row(self, row: str) -> None:
		self.__cursor.execute(f'INSERT INTO id_user_chat (id_chat, id_update)VALUES{row[0]},{row[1]}')

		self.__cursor.execute(f'''INSERT INTO id_user_data 
		(id_data, username, first_name, last_name, language)VALUES{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}''')

	def get_db_id(self, row: List[int]) -> Tuple[bool, bool]:
		record: sqlite3 = self.__cursor.execute(f'SELECT id_chat, id_update FROM id_user_chat WHERE id_chat = {row[0]}')
		res_record: Tuple = record.fetchall()

		if len(res_record) != 0:
			if res_record[0][1] == row[1]:
				return (True, False)
			else:
				return (True, True)
		else:
			return (False, False)

	def close_db(self) -> None:
		self.__connect.close()
