# -*- coding: utf8 -*-
# SDAPS - Scripts for data acquisition with paper based surveys
# Copyright (C) 2008, Christoph Simon <christoph.simon@gmx.eu>
# Copyright (C) 2008, Benjamin Berg <benjamin@sipsolutions.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or   
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the  
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from sdaps import model


def parse (survey, additionalqobjects) :
	
	document = file(additionalqobjects, 'r')
	
	for line in document :
		line = line.decode('utf-8')
		args = line.strip().split('\t')
		qobject = getattr(model.questionnaire, 'Additional_%s' % args.pop(0))
		assert issubclass(qobject, model.questionnaire.QObject)
		qobject = qobject()
		survey.questionnaire.add_qobject(qobject)
		qobject.setup.setup(args)

