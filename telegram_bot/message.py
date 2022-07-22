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

from typing import Dict

import openweather.requests


class Message:
	def __init__(self, local: str, data: Dict) -> None:
		self.__local: str = local
		self.__data: Dict = data

	def message_switch(self) -> Dict:
		if self.__data[1] == 'city not found':
			return self.__message_error()

		if self.__local == 'EN':
			return self.__message_local_en()
		elif self.__local == 'UA':
			return self.__message_local_ua()

	def __message_local_en(self) -> Dict:
		temp_dict: Dict = self.__data[2]
		gust_dict: Dict = self.__data[3]
		temp_text: str = f'In the city of {self.__data[1].capitalize()} now such weather conditions:\n'\
						 f'\U0001F31E temperature in the shade: ' \
						 f'{openweather.requests.Requests.kelvin_to_celsius(temp_dict["temp"])} ^C\n' \
						 f'\U0001F31E lowest temperature: ' \
						 f'{openweather.requests.Requests.kelvin_to_celsius(temp_dict["temp_min"])} ^C\n' \
						 f'\U0001F31E highest temperature: ' \
						 f'{openweather.requests.Requests.kelvin_to_celsius(temp_dict["temp_max"])} ^C\n' \
						 f'\U0001F300 Wind speed: {gust_dict.get("speed", "Calm")}\n' \
						 f'\U0001F4A8 Gusts of wind: {gust_dict.get("gust", "Almost none")}'

		message: Dict = {
			'chat_id': self.__data[0],
			'text': temp_text,
		}

		return message

	def __message_local_ua(self) -> Dict:
		temp_dict: Dict = self.__data[2]
		gust_dict: Dict = self.__data[3]
		temp_text: str = f'У місті {self.__data[1].capitalize()} зараз такі погодні умови:\n'\
						 f'\U0001F31E Температура в тіні: ' \
						 f'{openweather.requests.Requests.kelvin_to_celsius(temp_dict["temp"])} ^C\n' \
						 f'\U0001F31E Найнижча температура: ' \
						 f'{openweather.requests.Requests.kelvin_to_celsius(temp_dict["temp_min"])} ^C\n' \
						 f'\U0001F31E Найвища температура: ' \
						 f'{openweather.requests.Requests.kelvin_to_celsius(temp_dict["temp_max"])} ^C\n' \
						 f'\U0001F300 Швидкість вітру: {gust_dict.get("speed", "Штиль")}\n' \
						 f'\U0001F4A8 Пориви вітру: {gust_dict.get("gust", "Майже немає")}'

		message: Dict = {
			'chat_id': self.__data[0],
			'text': temp_text,
		}

		return message

	def __message_error(self) -> Dict:
		message: Dict = {}

		if self.__local == 'EN':
			message: Dict = {
				'chat_id': self.__data[0],
				'text': 'This city does not exist or there is a mistake in the names :(',
			}
		elif self.__local == 'UA':
			message: Dict = {
				'chat_id': self.__data[0],
				'text': 'Цього міста не існує або в назві помилка :(',
			}

		return message

	def __message_bad_cities(self) -> Dict:
		message: Dict = {
			'chat_id': self.__data[0],
			'text': 'Русский военный корабль, \U0001F4A3 иди нахуй! \U0001F4A9',
		}

		return message
