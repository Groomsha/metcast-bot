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

from threading import Timer

import const

from telegram_bot.worker import Worker
from openweather.requests import Requests


def check_bot():
	city = telegram_bot.check_new_message()

	for get in city:
		telegram_bot.sending_message(openweather.check_new_map_city(get))

if __name__ == '__main__':
	telegram_bot = Worker(const)
	openweather = Requests(const)

	check_bot()
	# timer_to_new_game = Timer(2, check_bot)
	# timer_to_new_game.start()

# while True:
# 	check_bot()
# 	timer_to_new_game = Timer(2, check_bot)
# 	timer_to_new_game.start()
