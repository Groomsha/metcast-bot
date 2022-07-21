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
			return self.__local_en_message()
		elif self.__local == 'UA':
			pass

	def __local_en_message(self) -> Dict:
		temp_dict: Dict = self.__data[2]
		temp_text: str = f'In the city of {self.__data[1]} now such weather conditions:\n'\
					f'temperature in the shade: {openweather.requests.Requests.kelvin_to_celsius(temp_dict["temp"])} ^C\n' \
					f'lowest temperature: {openweather.requests.Requests.kelvin_to_celsius(temp_dict["temp_min"])} ^C\n' \
					f'highest temperature: {openweather.requests.Requests.kelvin_to_celsius(temp_dict["temp_max"])} ^C'

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

		return message
