# -*- coding: utf-8 -*-
"""Test for License classes."""
import unittest
from xmodule.license import parse_license, License, ARRLicense, CCLicense


def assert_equal_license(self, lic_1, lic_2):
    """
    Asserts that lic_1 and lic_2 are both licenses of the same
    type, with the same versions as applicable.
    """
    # Assert that lic_1 and lic_2 are both License types,
    # otherwise further checks will fail
    self.assertTrue(isinstance(lic_1, License))
    self.assertTrue(isinstance(lic_2, License))
    # Assert licenses are of the same type
    self.assertEqual(lic_1.kind, lic_2.kind)
    # If they're not of the ARR type license, they're versioned, so
    # assert that their versions are also equal
    if not lic_1.kind == "ARR":
        self.assertEqual(lic_1.version, lic_2.version)


class LicenseTest(unittest.TestCase):
    """Tests for License class."""

    def setUp(self):
        self.no_license = License()
        self.default_license = ARRLicense()
        self.random_license = License('RAND', "v2.56")
        self.random_dict = {"kind": "RAND", "version": "v2.56"}
        self.invalid_dict = {"kind": "RAND"}

    def test_html(self):
        """Should never be called in production, but otherwise say it's not licensed."""
        self.assertEqual(self.no_license.html, u"<p>This resource is not licensed.</p>")

    def test_to_json(self):
        self.assertEqual(License().to_json(None)["kind"], "ARR")
        self.assertEqual(License().to_json(self.random_license), {"kind": "RAND", "version": "v2.56"})
        self.assertEqual(License().to_json(self.random_dict), {"kind": "RAND", "version": "v2.56"})
        with self.assertRaises(TypeError):
            License().to_json(self.invalid_dict)

    def test_from_json(self):
        assert_equal_license(self, License().from_json(None), self.default_license)
        assert_equal_license(self, License().from_json(""), self.default_license)


class ARRLicenseTest(unittest.TestCase):
    """Tests for All Rights Reserved License class."""

    def setUp(self):
        self.arr_license = ARRLicense()

    def test_html(self):
        self.assertEqual(self.arr_license.html, "&copy;<span class='license-text'>All rights reserved</span>")

    def test_from_json(self):
        assert_equal_license(self, License().from_json("ARR"), self.arr_license)


class CCLicenseTest(unittest.TestCase):
    """Tests for Creative Commons License class."""

    def setUp(self):
        self.cc0_license = CCLicense("CC0")
        self.cc_by_license = CCLicense("CC-BY")
        self.cc_by_sa_license = CCLicense("CC-BY-SA")
        self.cc_by_nd_license = CCLicense("CC-BY-ND")
        self.cc_by_nc_license = CCLicense("CC-BY-NC")
        self.cc_by_nc_sa_license = CCLicense("CC-BY-NC-SA")
        self.cc_by_nc_nd_license = CCLicense("CC-BY-NC-ND")

    def test_version(self):
        self.assertEqual(self.cc0_license.version, "4.0")

    def test_html(self):
        # URL should be correct
        self.assertTrue("creativecommons.org/licenses/by-nc-sa/4.0/" in self.cc_by_nc_sa_license.html)

        # CC icon should be there
        self.assertTrue("class='icon-cc" in self.cc0_license.html)

        # ZERO icon should be there
        self.assertTrue("icon-cc-zero" in self.cc0_license.html)

        # BY icon should be there
        self.assertTrue("icon-cc-by" in self.cc_by_license.html)
        self.assertTrue("icon-cc-by" in self.cc_by_sa_license.html)
        self.assertTrue("icon-cc-by" in self.cc_by_nd_license.html)
        self.assertTrue("icon-cc-by" in self.cc_by_nc_license.html)
        self.assertTrue("icon-cc-by" in self.cc_by_nc_sa_license.html)
        self.assertTrue("icon-cc-by" in self.cc_by_nc_nd_license.html)

        # NC icon should be there
        self.assertTrue("icon-cc-nc" in self.cc_by_nc_license.html)
        self.assertTrue("icon-cc-nc" in self.cc_by_nc_nd_license.html)

        # SA icon should be there
        self.assertTrue("icon-cc-sa" in self.cc_by_sa_license.html)
        self.assertTrue("icon-cc-sa" in self.cc_by_nc_sa_license.html)

        # ND icon should be there
        self.assertTrue("icon-cc-by" in self.cc_by_nd_license.html)
        self.assertTrue("icon-cc-by" in self.cc_by_nc_nd_license.html)

    def test_from_json(self):
        assert_equal_license(self, License().from_json("CC0"), self.cc0_license)
        assert_equal_license(self, License().from_json("CC-BY"), self.cc_by_license)
        assert_equal_license(self, License().from_json("CC-BY-SA"), self.cc_by_sa_license)
        assert_equal_license(self, License().from_json("CC-BY-ND"), self.cc_by_nd_license)
        assert_equal_license(self, License().from_json("CC-BY-NC"), self.cc_by_nc_license)
        assert_equal_license(self, License().from_json("CC-BY-NC-SA"), self.cc_by_nc_sa_license)
        assert_equal_license(self, License().from_json("CC-BY-NC-ND"), self.cc_by_nc_nd_license)

    def test_description(self):
        # BY text should be there
        self.assertTrue("Attribution" in self.cc_by_license.description)
        self.assertTrue("Attribution" in self.cc_by_sa_license.description)
        self.assertTrue("Attribution" in self.cc_by_nd_license.description)
        self.assertTrue("Attribution" in self.cc_by_nc_license.description)
        self.assertTrue("Attribution" in self.cc_by_nc_sa_license.description)
        self.assertTrue("Attribution" in self.cc_by_nc_nd_license.description)

        # NC text should be there
        self.assertTrue("NonCommercial" in self.cc_by_nc_license.description)
        self.assertTrue("NonCommercial" in self.cc_by_nc_nd_license.description)

        # SA text should be there
        self.assertTrue("ShareAlike" in self.cc_by_sa_license.description)
        self.assertTrue("ShareAlike" in self.cc_by_nc_sa_license.description)

        # ND text should be there
        self.assertTrue("NonDerivatives" in self.cc_by_nd_license.description)
        self.assertTrue("NonDerivatives" in self.cc_by_nc_nd_license.description)


class ParseLicenseTest(unittest.TestCase):
    """Tests for license parser."""

    def test_parse_license(self):
        assert_equal_license(self, parse_license(None), ARRLicense())
        assert_equal_license(self, parse_license(""), ARRLicense())
        assert_equal_license(self, parse_license("ARR"), ARRLicense())
        assert_equal_license(self, parse_license("CC0"), CCLicense("CC0", "4.0"))
        assert_equal_license(self, parse_license("CC-BY"), CCLicense("CC-BY", "4.0"))
        assert_equal_license(self, parse_license({"license": "CC-BY", "version": "4.0"}), CCLicense("CC-BY", "4.0"))
        assert_equal_license(self, parse_license({"kind": "CC-BY", "version": "4.0"}), CCLicense("CC-BY", "4.0"))
        with self.assertRaises(ValueError):
            parse_license({"kind": "CC-BY"})
