import stripe

from config.settings import STRIPE_API_KEY
from materials.models import Course

stripe.api_key = 'sk_test_51OwlwuD6YDI1PfPLy21tsj9vFtQyB94lj8ymzvJBTwxCAakovP0Vp0P90ZtWkltoBxxA9HrLhuriECdFS4wDuUz000ztcLB6jE'

def create_product(pk):
    course = Course.objects.get(pk=pk)
    product = stripe.Product.create(name=course.title)
    amount = course.price
    return product['id'], amount


def create_pay_course(product, amount):
    pay_course = stripe.Price.create(
        currency="usd",
        unit_amount=amount,
        product=product,
    )
    return pay_course

def create_pay_session(pay_course):
    pay_session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/courses/",
        line_items=[{"price": pay_course, "quantity": 1}],
        mode="payment",
    )
    return pay_session['id'], pay_session['url']
