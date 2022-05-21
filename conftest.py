import pytest

def pytest_addoption(parser):
    parser.addoption("--inputfile", action="store", default=None)
    parser.addoption("--date", action="store", default=None)
    parser.addoption("--datetime", action="store", default=None)
    parser.addoption("--latitude", action="store", default=None)
    parser.addoption("--longitude", action="store", default=None)
    parser.addoption("--depth", action="store", default=None)
    parser.addoption("--time", action="store", default=None)
    parser.addoption("--depthmargin", action="store", default="0")
    parser.addoption("--depthmonotonic", action="store", default="False")
    parser.addoption("--salinity", action="store", default=None)
    parser.addoption("--watertemperature", action="store", default=None)
    
@pytest.fixture(scope="session")
def inputfile(pytestconfig):
    return  pytestconfig.getoption("inputfile")
    
@pytest.fixture(scope="session")
def date(pytestconfig):
    return  pytestconfig.getoption("date")
    
@pytest.fixture(scope="session")
def dattim(pytestconfig):
    return  pytestconfig.getoption("datetime")
    
@pytest.fixture(scope="session")
def latitude(pytestconfig):
    return  pytestconfig.getoption("latitude")
    
@pytest.fixture(scope="session")
def longitude(pytestconfig):
    return  pytestconfig.getoption("longitude")
    
@pytest.fixture(scope="session")
def depth(pytestconfig):
    return  pytestconfig.getoption("depth")

@pytest.fixture(scope="session")
def time(pytestconfig):
    return  pytestconfig.getoption("time")

@pytest.fixture(scope="session")
def depthmargin(pytestconfig):
    return pytestconfig.getoption("depthmargin")

@pytest.fixture(scope="session")
def depthmonotonic(pytestconfig):
    return pytestconfig.getoption("depthmonotonic")

@pytest.fixture(scope="session")
def salinity(pytestconfig):
    return pytestconfig.getoption("salinity")

@pytest.fixture(scope="session")
def watertemperature(pytestconfig):
    return pytestconfig.getoption("watertemperature")