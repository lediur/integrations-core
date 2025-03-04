# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import pytest


def pytest_addoption(parser):
    """Make sure the online part of the testsuite is parametrizable."""
    parser.addoption(
        "--distribution-name",
        action="store",
        default="datadog-active-directory",
        help="Standard distribution name of the desired Datadog check.",
    )
    parser.addoption(
        "--distribution-version",
        action="store",
        default="1.10.0",
        help="The version number of the desired Datadog check.",
    )
    parser.addoption(
        "--local-dir",
        action="store",
        default=None,
        help="Run tests against the given directory with TUF, in-toto and wheels.",
    )


def pytest_collection_modifyitems(config, items):
    if not config.getoption("--local-dir"):
        # No directory based tests requested.
        return

    skip_test = pytest.mark.skip(reason="running only tests that use local directory")
    for item in items:
        if "local_dir" not in item.keywords:
            item.add_marker(skip_test)


@pytest.fixture
def local_dir(request):
    """Provide local_dir fixture."""
    return request.config.getoption("--local-dir")


@pytest.fixture
def distribution_name(request):
    """Provide distribution_name fixture."""
    return request.config.getoption("--distribution-name")


@pytest.fixture
def distribution_version(request):
    """Provide distribution_version fixture."""
    return request.config.getoption("--distribution-version")


def pytest_configure(config):
    config.addinivalue_line("markers", "online: a test uses S3 to obtain targets, intoto and tuf metadata")
    config.addinivalue_line("markers", "offline: a test uses local targets, intoto and tuf metadata")
    config.addinivalue_line(
        "markers", "local_dir: a test uses explicitly supplied local directory with intoto, tuf and wheels"
    )
