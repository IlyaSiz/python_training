import pytest
from fixture.application import Application

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    fixture.session.login(email="demo@open-eshop.com", password="demo")
    def fin():  
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture