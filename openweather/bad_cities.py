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

from typing import List


class BadCities:
	def __init__(self, local: str = 'RU') -> None:
		self.__local = local
		self.__bad_cities_ru: List = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Нижний Новгород',
									  'Казань', 'Самара', 'Челябинск', 'Омск', 'Ростов-на-Дону', 'Уфа', 'Красноярск',
									  'Пермь', 'Волгоград', 'Воронеж', 'Саратов', 'Краснодар', 'Тольятти', 'Тюмень',
									  'Ижевск', 'Барнаул', 'Ульяновск', 'Иркутск', 'Владивосток', 'Ярославль',
									  'Хабаровск', 'Ахачкала', 'Оренбург', 'Томск', 'Новокузнецк', 'Кемерово',
									  'Астрахань', 'Рязань', 'Набережные Челны', 'Пенза', 'Липецк', 'Тула', 'Киров',
									  'Чебоксары', 'Калининград', 'Курск', 'Улан-Удэ', 'Ставрополь', 'Магнитогорск',
									  'Тверь', 'Иваново', 'Брянск', 'Сочи', 'Белгород', 'Сургут']

	def check_city(self, name: str) -> bool:
		for c in self.__bad_cities_ru:
			if name == c:
				return True
			else:
				return False
