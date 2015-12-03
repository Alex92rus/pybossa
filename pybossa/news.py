
# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2015 SciFabric LTD.
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.
import json
from time import time
from pybossa.core import sentinel
try:
    import cPickle as pickle
except ImportError:  # pragma: no cover
    import pickle


FEED_KEY = 'scifabricnews'

def get_news(score=None):
    """Return news list."""
    minscore = 0
    maxscore = 5
    if score:
        minscore = score
        maxscore = score
    data = sentinel.slave.zrangebyscore(FEED_KEY, minscore, maxscore,
                                        withscores=True)
    news = []
    for u in data:
        tmp = pickle.loads(u[0])
        news.append(tmp)
    return news
