# Copyright 2016 Google Inc.
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

import webapp2
import cgi
#<h2>Enter some text to ROT13:</h2>
formData="""
<form method="post" action="/testform">

  <br>
  <textarea name='text' rows="20" cols="70" value="%(user_text)">
  </textarea>
  <br>
  <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(formData)

class TestHandler(webapp2.RequestHandler):
    def post(self):
        entered_text = self.request.get('text')
        escaped_text =  self.escape_text( entered_text )
        self.write_form(escaped_text)
#        self.response.headers['Content-Type'] = 'text/plain'
#        self.response.out.write(self.request)
##        self.redirect('/')

    def write_form(self, user_text=''):
#        self.response.out.write(user_text)
        self.response.out.write(formData % {"user_text": user_text})
##        self.response.out.write(formData)

    def escape_text(self, s):
        return cgi.escape(s, quote = True);

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform', TestHandler),
], debug=True)
