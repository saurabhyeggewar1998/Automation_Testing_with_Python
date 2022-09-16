import warnings


# def api_v1():
#     #warnings.filterwarnings('ignore','.*api.*')
#     warnings.warn(UserWarning("api v1, should use functions from v2"))
#     warnings.warn("mohit good mornig")
#     return 1
#
#
# def test_one():
#     assert api_v1() == 1

#2nd
import pytest


# def api_v1():
#     warnings.warn("api v1, should use functions from v2; use api_v2",deprecated:DeprecationWarning)
#     warnings.warn("mohit")
#     return 1
#
#
# @pytest.mark.filterwarnings("ignore:api v1")
# def test_one():
#     assert api_v1() == 1
# def myfunction(n):
#     return n
#
#
#
# def test_myfunction_deprecated():
#     with pytest.deprecated_call():
#         myfunction(17)

# import warnings
# import pytest
#
#
# def test_warning():
#     with pytest.warns(UserWarning):
#         warnings.warn("my warning", UserWarning)

