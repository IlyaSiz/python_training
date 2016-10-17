# -*- coding: utf-8 -*-
from model.coupon import Coupon

def test_add_and_del_coupon(app):
    app.coupon.add_new(Coupon(coupon_name="New great coupon", date="2016-09-15", number_of_coupons="5"))
    app.coupon.find_and_delete("New great coupon")

def test2(app):
    app.coupon.add_new(Coupon(coupon_name="Other coupon", date="2017-08-08", number_of_coupons="3"))
    app.coupon.find_and_delete("Other coupon")

