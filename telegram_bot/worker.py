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

from json import loads
from typing import Dict, Any

import requests

from sources_db.sqlite_worker import SQLiteWorker


class Worker:
	URL: str = 'https://api.telegram.org/bot'

	def __init__(self, const: Any) -> None:
		self.db_connect = SQLiteWorker('telegram_chats.db')
		self.db_connect.get_db_id([1275569537, 941332901])

		self.__const: Any = const
		self.__counter: int = 0

	def request_by_update_bot(self) -> Dict:
		request_url = f'{self.URL}{self.__const.telegram_token}/getUpdates'
		res = requests.get(request_url, proxies=self.__const.proxies_requests if self.__const.proxy_on else None)

		return loads(res.text)

	def parser_update_bot(self):
		res: Dict = self.request_by_update_bot()
		update_id: int = 0

		if len(res['result']) > self.__counter:
			self.__counter =  len(res['result'])

			for result_row in res['result']:
				for result_one_key, result_one_value in result_row.items():
					if result_one_key == 'update_id':
						update_id = result_one_value
					elif result_one_key == 'message':
						for result_two_key, result_two_value in result_one_value.items():
							if result_two_key == 'from':
								for result_tree_key, result_tree_value in result_two_value.items():
									if result_tree_key == 'id':
										print(result_tree_value, update_id)
										print(self.db_connect.get_db_id([result_tree_value, update_id]))
										self.db_connect.close_db()
								print('from => ', result_two_value)
							elif result_two_key == 'chat':
								print('chat => ', result_two_value)
							elif result_two_key == 'text':
								print('text => ', result_two_value)
		else:
			pass
