"""
utils.py

Copyright 2018 Andres Riancho

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
import logging


class AllLoggingDisabled(object):
    """
    A context manager that will prevent any logging messages
    triggered during the body from being processed.
    """
    def __init__(self):
        self.previous_level = logging.INFO

    def __enter__(self, highest_level=logging.CRITICAL):
        """
        :param highest_level: The maximum logging level in use.
                              This would only need to be changed if a custom level
                              greater than CRITICAL is defined.
        :return: None
        """
        # two kind-of hacks here:
        #    * can't get the highest logging level in effect => delegate to the user
        #    * can't get the current module-level override => use an undocumented
        #       (but non-private!) interface
        self.previous_level = logging.root.manager.disable
        logging.disable(highest_level)

    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.disable(self.previous_level)

        # If we returned True here, any exception would be suppressed!
        return False

