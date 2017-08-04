#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import os
import webapp2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/main.html')
        self.response.write(template.render())

    def post(self):
        r_template = jinja_environment.get_template('templates/results.html')
        # mascot, establish, parking
        answer_one = self.request.get('mascot')
        answer_two = self.request.get('establish')
        answer_three = self.request.get('parking')

        if answer_one.lower() == 'oscar':
            msg1 = 'Correct!'
        else:
            msg1 = 'Wrong! You lose!'

        if answer_two == '1920':
            msg2 = 'Correct'
        else:
            msg2 = 'Wrong'

        if answer_three.lower() == 'president':
            msg3 = 'Correct'
        else:
            msg3 = 'Wrong'


        template_variables = {
            'answer1' : answer_one,
            'answer2' : answer_two,
            'answer3' : answer_three,
            'msg1' : msg1,
            'msg2' : msg2,
            'msg3' : msg3
        }

        self.response.write(r_template.render(template_variables))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
