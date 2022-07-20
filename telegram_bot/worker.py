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
from typing import Dict, List, Any

import requests
import openweather.requests as tem
# from sources_db.sqlite_worker import SQLiteWorker


class Worker:
	URL: str = 'https://api.telegram.org/bot'

	def __init__(self, const: Any) -> None:
		# self.db_connect = SQLiteWorker('telegram_chats.db')

		self.__bot_start = False
		self.__const: Any = const
		self.__counter: int = 0

	def __request_by_update_bot(self) -> Dict:
		request_url = f'{self.URL}{self.__const.telegram_token}/getUpdates'
		res = requests.get(request_url, proxies=self.__const.proxies_requests if self.__const.proxy_on else None)

		return loads(res.text)

	def __parser_update_bot(self) -> None:
		res: Dict = self.__request_by_update_bot()
		data: List = []

		# if len(res['result']) > self.__counter:
		# 	self.__counter =  len(res['result'])

		for result_row in res['result']:
			request: Dict = {}
			temp: List = []

			request['update_id'] = result_row.get('update_id')
			temp.append(result_row.get('update_id'))

			for result_one_key, result_one_value in result_row.get('message').items():
				if result_one_key == 'from':
					for result_two_key, result_two_value in result_one_value.items():
						if result_two_key == 'id':
							temp.append(result_two_value)
							request['chat_id'] = result_two_value
						elif result_two_key == 'first_name':
							request['first_name'] = result_two_value
						elif result_two_key == 'last_name':
							request['last_name'] = result_two_value
						elif result_two_key == 'username':
							request['username'] = result_two_value
				elif result_one_key == 'text':
					request['text'] = result_one_value

				# self.__sql_save_user(request)
			temp.append(request['text'])
			data.append(temp)
		else:
			pass

		if self.__bot_start:
			if self.__const.update_id != data[-1][0]:
				self.__const.update_id = data[-1][0]
				return data[-1]
		else:
			self.__const.update_id = data[-1][0]
			self.__bot_start = True

	# def __sql_save_user(self, request) -> str:
	# 	res = self.db_connect.get_db_id([request['chat_id'], request['update_id']])
	#
	#
	# 	if not res[0]:
	# 		self.db_connect.save_user_chat_row([request['chat_id'], request['update_id']])
	# 		self.db_connect.save_user_data_row([request['chat_id'], request['username'], request['first_name'], request['last_name']])
	#
	# 		return request['text']
	# 	else:
	# 		if not res[1]:
	# 			return request['text']

	def check_new_message(self) -> str:
		return self.__parser_update_bot()

	def sending_message(self, data: Dict) -> None:
		if not data[1] == 'city not found':
			temp_dict:Dict = data[2]
			temp_text: str = f'In the city of {data[1]} now such weather conditions:\n'\
						f'temperature in the shade: {tem.Requests.kelvin_to_celsius(temp_dict["temp"])} ^C\n' \
						f'lowest temperature: {tem.Requests.kelvin_to_celsius(temp_dict["temp_min"])} ^C\n' \
						f'highest temperature: {tem.Requests.kelvin_to_celsius(temp_dict["temp_max"])} ^C'

			message: Dict = {
				'chat_id': data[0],
				'text': temp_text,
			}
		else:
			message: Dict = {
				'chat_id': data[0],
				'text': 'This city does not exist or there is a mistake in the names :(',
			}

		request_url: str = f'{self.URL}{self.__const.telegram_token}/sendMessage'
		requests.post(request_url, proxies=self.__const.proxies_requests if self.__const.proxy_on else None, data=message)
