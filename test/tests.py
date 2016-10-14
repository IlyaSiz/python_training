# -*- coding: utf-8 -*-
from model.coupon import Coupon

def test_add_and_del_coupon(app):
    app.session.login(email="demo@open-eshop.com", password="demo")
    app.coupon.add_new(Coupon(coupon_name="New great coupon", date="2016-09-15", number_of_coupons="5"))
    app.coupon.find_and_delete("New great coupon")
    app.session.logout()