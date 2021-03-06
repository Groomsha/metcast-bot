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

import const

from telegram_bot.worker import Worker
from openweather.requests import Requests


def check_bot(bot, weather) -> None:
	"""Функція перевіряє наявність нового повідомлення у чаті"""
	city = bot.check_new_message()

	if city != None:
		telegram_bot.sending_message(weather.check_new_map_city(city))


if __name__ == '__main__':
	"""Точка входу до програми"""
	telegram_bot = Worker(const)
	openweather = Requests(const)

	while True:
		check_bot(telegram_bot, openweather)
