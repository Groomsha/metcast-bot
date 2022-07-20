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


class Requests:
	URL: str = 'http://api.openweathermap.org/data/2.5/weather?'

	def __init__(self, const: Any) -> None:
		"""Клас створює запит та повертає дані від API погоди"""
		self.__const: Any = const

	def request_by_city(self, req: str) -> Dict:
		"""Метод робить запит API погоди за вказаним містом"""
		request_url = f'{self.URL}q={req.capitalize()}&appid={self.__const.weather_token}'
		res = requests.get(request_url, proxies=self.__const.proxies_requests if self.__const.proxy_on else None)

		return loads(res.text)

	def check_new_map_city(self, city: List) -> List:
		"""Метод повертає оброблені дані щодо погоди"""
		data: List = [city[1], city[2]]
		request = self.request_by_city(city[2])

		if request['cod'] == '404':
			data: List = [city[1], request['message']]
		else:
			data.append(request['main'])
			data.append(request['wind'])

		return data

	@staticmethod
	def kelvin_to_celsius(temp: float) -> float:
		"""Метод для переведення кельвіни в цельсій"""
		celsius = temp - 273.15
		return round(celsius, 4)
