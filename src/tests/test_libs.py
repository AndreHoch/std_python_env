# test_libs.py

import pytest
import importlib

# List of all the libraries to be checked.
# You can easily add or remove libraries from this list.
LIBRARIES_TO_CHECK = [
    "numpy",
    "pandas",
    "matplotlib",
    "scipy",
    "jupyterlab",
    "pytest",
]

@pytest.mark.parametrize("library_name", LIBRARIES_TO_CHECK)
def test_library_exists(library_name):
    """
    This test function checks if a given Python library exists in the
    current environment.

    The @pytest.mark.parametrize decorator runs this test once for each
    item in the `LIBRARIES_TO_CHECK` list.

    Args:
        library_name (str): The name of the library to check for.
    """
    try:
        # importlib.util.find_spec is the recommended way to check
        # for a library's existence without actually importing it.
        # It returns a spec object if the library is found, otherwise None.
        spec = importlib.util.find_spec(library_name)
        assert spec is not None, f"Library '{library_name}' was not found."
    except ImportError:
        # This is a fallback check, but find_spec is more direct.
        # An ImportError is raised if the module cannot be imported.
        pytest.fail(f"ImportError: Library '{library_name}' could not be imported.")
