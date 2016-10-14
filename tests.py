# -*- coding: utf-8 -*-
import pytest
from application import Application
from coupon import Coupon


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_login(app):
    app.login(email="demo@open-eshop.com", password="demo")
    app.add_new_coupon(Coupon(coupon_name="New great coupon", date="2016-09-15", number_of_coupons="5"))
    app.find_and_delete_coupon("New great coupon")
    app.logout()