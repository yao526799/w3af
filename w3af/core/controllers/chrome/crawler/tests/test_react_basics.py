"""
test_react_basics.py

Copyright 2019 Andres Riancho

This file is part of w3af, http://w3af.org/ .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
from w3af.core.controllers.chrome.crawler.tests.base import BaseChromeCrawlerTest


class ReactBasicTest(BaseChromeCrawlerTest):
    def test_react_hello_world_app(self):
        url = 'http://react-hello-world-app.surge.sh/'
        found_uris = self._crawl(url)

        expected_uris = {
            'http://react-hello-world-app.surge.sh/static/js/main.d78accb8.js',
            'http://react-hello-world-app.surge.sh/static/css/main.4b51051d.css',
            'http://react-hello-world-app.surge.sh/'
        }

        self.assertEqual(found_uris, expected_uris)

        expected_messages = '''
        Dispatching "click" on CSS selector "!document"
        Dispatching "click" on CSS selector ".AddGreeter button"
        Dispatching "click" on CSS selector ".HelloWorldList .HelloWorld:nth-of-type(2) button:nth-child(2)"
        Dispatching "click" on CSS selector ".HelloWorldList .HelloWorld:nth-of-type(2) button:nth-child(2) [role]"
        Dispatching "click" on CSS selector ".HelloWorldList .HelloWorld:nth-of-type(2) button:nth-child(3)"
        Dispatching "click" on CSS selector ".HelloWorldList .HelloWorld:nth-of-type(2) button:nth-child(3) [role]"
        Dispatching "click" on CSS selector ".HelloWorldList .HelloWorld:nth-of-type(2) button:nth-child(5)"
        Dispatching "click" on CSS selector ".HelloWorldList .HelloWorld:nth-of-type(2) button:nth-child(5) [role]"
        The JS crawler noticed a big change in the DOM.
        Dispatching "click" on CSS selector "!document"
        Dispatching "click" on CSS selector ".HelloWorldList .HelloWorld:nth-of-type(3) button:nth-child(2)"
        Dispatching "click" on CSS selector ".HelloWorldList .HelloWorld:nth-of-type(3) button:nth-child(2) [role]"
        Dispatching "click" on CSS selector ".HelloWorldList .HelloWorld:nth-of-type(3) button:nth-child(3)"
        Dispatching "click" on CSS selector ".HelloWorldList .HelloWorld:nth-of-type(3) button:nth-child(3) [role]"
        Dispatching "click" on CSS selector ".HelloWorldList .HelloWorld:nth-of-type(3) button:nth-child(5)"
        The JS crawler noticed a big change in the DOM.
        Dispatching "click" on CSS selector "!document"
        Dispatching "click" on CSS selector ".HelloWorldList .HelloWorld:nth-of-type(3) button:nth-child(5) [role]"
        Processing event 13 out of (unknown) for http://react-hello-world-app.surge.sh/. Event dispatch error count is 0. Already processed 16 events with types: {u'click': 35}
        The JS crawler noticed a big change in the DOM.
        '''

        found, not_found = self._log_contains(expected_messages)
        self.assertEqual(not_found, [])

    def test_react_autosuggest(self):
        url = 'https://dist-usikpayhrn.now.sh/'
        found_uris = self._crawl(url)

        expected_uris = {
            'https://dist-usikpayhrn.now.sh/autosuggest.css',
            'https://fonts.googleapis.com/css?family=Open%20Sans:300|Open%20Sans:400',
            'https://fonts.gstatic.com/s/opensans/v17/mem8YaGs126MiZpBA-UFVZ0e.ttf',
            'https://api.github.com/repos/moroshko/react-autosuggest',
            'https://dist-usikpayhrn.now.sh/',
            'https://dist-usikpayhrn.now.sh/app.css',
            'https://dist-usikpayhrn.now.sh/index.js',
            'https://fonts.gstatic.com/s/opensans/v17/mem5YaGs126MiZpBA-UN_r8OUuhs.ttf'
        }

        self.assertEqual(found_uris, expected_uris)

        expected_messages = '''
        The JS crawler found a total of 0 event listeners
        '''

        found, not_found = self._log_contains(expected_messages)
        self.assertEqual(not_found, [])

    def test_react_icons_menu(self):
        url = 'https://react-icons-kit.now.sh/'
        found_uris = self._crawl(url)

        expected_uris = {
            'https://api.github.com/repos/wmira/react-icons-kit',
            'https://react-icons-kit.now.sh/static/js/main.883b6669.chunk.js',
            'https://react-icons-kit.now.sh/static/css/main.1969ec6f.chunk.css',
            'https://fonts.googleapis.com/css?family=Roboto',
            'https://buttons.github.io/buttons.js',
            'https://react-icons-kit.now.sh/static/js/12.bb39441f.chunk.js',
            'https://react-icons-kit.now.sh/static/js/6.82dd2a0d.chunk.js',
            'https://react-icons-kit.now.sh/static/js/7.8a170409.chunk.js',
            'https://fonts.gstatic.com/s/roboto/v20/KFOmCnqEu92Fr1Mu4mxP.ttf',
            'https://react-icons-kit.now.sh/static/js/5.61059cf1.chunk.js',
            'https://react-icons-kit.now.sh/static/js/3.53088ee4.chunk.js',
            'https://react-icons-kit.now.sh/static/js/2.7fcf3a64.chunk.js',
            'https://react-icons-kit.now.sh/static/js/9.09bf1d7f.chunk.js',
            'https://react-icons-kit.now.sh/static/js/14.896ea694.chunk.js',
            'https://react-icons-kit.now.sh/static/js/11.231df52c.chunk.js',
            'https://react-icons-kit.now.sh/',
            'https://react-icons-kit.now.sh/static/js/13.b15ad13e.chunk.js',
            'https://react-icons-kit.now.sh/static/js/10.8540d94c.chunk.js',
            'https://react-icons-kit.now.sh/static/js/8.98e8b840.chunk.js',
            'https://react-icons-kit.now.sh/static/js/4.3cc6d30f.chunk.js',
        }

        self.assertEqual(found_uris, expected_uris)

        expected_messages = '''
        Dispatching "click" on CSS selector ".sc-hSdWYo div:nth-of-type(2)"
        Processing event 32 out of (unknown) for https://react-icons-kit.now.sh/.
        Event dispatch error count is 0.
        Already processed 34 events with types: {u'click': 34}.
        Ignoring "click" event on selector
        '''

        found, not_found = self._log_contains(expected_messages)
        self.assertEqual(not_found, [])
