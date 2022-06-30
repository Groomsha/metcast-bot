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


class Worker:
	URL: str = 'https://api.telegram.org/bot'

	def __init__(self, const: Any, db: Any) -> None:
		self.__const: Any = const
		self.__db_data: Any = db
		self.__counter: int = 0

	def request_by_update_bot(self) -> Dict:
		request_url = f'{self.URL}{self.__const.telegram_token}/getUpdates'
		res = requests.get(request_url, proxies=self.__const.proxies_requests if self.__const.proxy_on else None)

		return loads(res.text)

	def parser_update_bot(self):
		res: Dict = self.request_by_update_bot()

		if len(res['result']) > self.__counter:
			self.__counter =  len(res['result'])

			for result_row in res['result']:
				for result_row_key, result_row_value in result_row.items():
					if result_row_key == 'update_id':
						print('update_id => ', result_row_value)
					elif result_row_key == 'message':
						for key, value in result_row_value.items():
							if key == 'from':
								print('from => ', value)
							elif key == 'chat':
								print('chat => ', value)
							elif key == 'text':
								print('text => ', value)
		else:
			pass
