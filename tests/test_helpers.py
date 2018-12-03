# -*- coding: utf-8 -*-

import pytest

from sceptre.exceptions import PathConversionError
from sceptre.helpers import get_external_stack_name
from sceptre.helpers import normalise_path


class TestHelpers(object):

    def test_get_external_stack_name(self):
        result = get_external_stack_name("prj", "dev/ew1/jump-host")
        assert result == "prj-dev-ew1-jump-host"

    def test_normalise_path_with_valid_path(self):
        path = normalise_path("valid/path")
        assert path == "valid/path"

    def test_normalise_path_with_backslashes_in_path(self):
        path = normalise_path("valid\path")
        assert path == "valid/path"

    def test_normalise_path_with_double_backslashes_in_path(self):
        path = normalise_path('valid\\path')
        assert path == "valid/path"

    def test_normalise_path_with_leading_slash(self):
        path = normalise_path("/this/is/valid")
        assert path == "/this/is/valid"

    def test_normalise_path_with_leading_backslash(self):
        path = normalise_path('\\this\path\is\\valid')
        assert path == "/this/path/is/valid"

    def test_normalise_path_with_trailing_slash(self):
        with pytest.raises(PathConversionError):
            normalise_path(
                "this/path/is/invalid/"
            )

    def test_normalise_path_with_trailing_backslash(self):
        with pytest.raises(PathConversionError):
            normalise_path(
                'this\path\is\invalid\\'
            )
