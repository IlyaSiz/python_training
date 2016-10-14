# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.coupon import Coupon


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test(app):
    app.session.login(email="demo@open-eshop.com", password="demo")
    app.coupon.add_new(Coupon(coupon_name="New great coupon", date="2016-09-15", number_of_coupons="5"))
    app.coupon.find_and_delete("New great coupon")
    app.session.logout()