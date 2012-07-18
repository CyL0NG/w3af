'''
unittest_coverage.py

Copyright 2012 Andres Riancho

This file is part of w3af, w3af.sourceforge.net .

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
'''
import os
import unittest

from core.controllers.w3afCore import w3afCore

TEST_PATH = os.path.join('plugins', 'tests')


class TestUnittestCoverage(unittest.TestCase):

    def setUp(self):
        self.w3afcore = w3afCore()
        
    def test_audit(self):
        self._analyze_unittests('audit')
        
    def test_discovery(self):
        self._analyze_unittests('discovery')

    def test_grep(self):
        self._analyze_unittests('grep')
        
    def _analyze_unittests(self, plugin_type):
        plugins = self.w3afcore.plugins.getPluginList(plugin_type)
        
        missing = []
        
        for plugin in plugins:
            if not self._has_test(plugin_type, plugin):
                missing.append(plugin)
        
        if missing:
            msg = 'The following %s plugins dont have unittests: %s' %  \
                  (plugin_type, ', '.join(missing) )
            self.assertTrue( False, msg )
    
    def _has_test(self, plugin_type, plugin_name):
        tests = os.listdir(os.path.join(TEST_PATH, plugin_type))
        
        
        fname = 'test_%s.py' % plugin_name
        return fname in tests
        