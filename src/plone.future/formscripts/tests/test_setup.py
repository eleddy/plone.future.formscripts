# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from plone.future.formscripts.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of plone.future.formscripts into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plone.future.formscripts is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('plone.future.formscripts'))

    def test_uninstall(self):
        """Test if plone.future.formscripts is cleanly uninstalled."""
        self.installer.uninstallProducts(['plone.future.formscripts'])
        self.assertFalse(self.installer.isProductInstalled('plone.future.formscripts'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IPlone.futureFormscriptsLayer is registered."""
        from plone.future.formscripts.interfaces import IPlone.futureFormscriptsLayer
        from plone.browserlayer import utils
        self.failUnless(IPlone.futureFormscriptsLayer in utils.registered_layers())
