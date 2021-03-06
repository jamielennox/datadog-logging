# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import logging
import uuid

from datadog_logging.tests.unit import base


class SimpleGoodLogs(base.StatsdTestCase):

    def test_simple_logging_levels(self):
        logger = self.getStatsdLogger(level=logging.WARNING)

        logger.debug('This should not be passed')
        self.assertFalse(self.called)

        logger.warning('This should be passed')
        self.assertTrue(self.called_once)

        self.assertElement('text', 'This should be passed')
        self.assertElement('title', 'This should be passed')
        self.assertElement('alert_type', 'warning')
