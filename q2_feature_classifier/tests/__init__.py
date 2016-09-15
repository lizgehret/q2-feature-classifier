# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Ben Kaehler
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import tempfile
import shutil

from q2_types.testing import TestPluginBase


class FeatureClassifierTestPluginBase(TestPluginBase):
    def setUp(self):
        try:
            from q2_feature_classifier.plugin_setup import plugin
        except ImportError:
            self.fail("Could not import plugin object.")

        self.plugin = plugin

        self.temp_dir = tempfile.TemporaryDirectory(
            prefix='q2-feature-classifier-test-temp-')

    def _setup_dir(self, filenames, dirfmt):
        for filename in filenames:
            filepath = self.get_data_path(filename)
            shutil.copy(filepath, self.temp_dir.name)

        return dirfmt(self.temp_dir.name, mode='r')