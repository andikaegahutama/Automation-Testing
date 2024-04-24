import time

from automation.Transaction import CreateTransaction
from automation.Customer import CreateCustomer
from automation.Customer_Service import CreateCustomerService
from automation.Partner import CreatePartner


def createtransaction():
    my_transaction = CreateTransaction()
    my_transaction.login_menu()
    my_transaction.fill_username()
    my_transaction.fill_password()
    my_transaction.submit_login()
    time.sleep(2)
    my_transaction.transaction_menu()
    my_transaction.create_button()
    my_transaction.customer_general()
    my_transaction.pickup_general()
    time.sleep(1)
    my_transaction.addorder_general()
    my_transaction.set_general()
    my_transaction.typeservice_general()
    my_transaction.submit_general()
    time.sleep(1)
    my_transaction.partner_pesanan()
    my_transaction.pickup_pesanan()
    my_transaction.distance_pesanan()
    my_transaction.shippingcost_pesanan()
    my_transaction.servicecost_pesanan()
    my_transaction.servicefee_pesanan()
    my_transaction.payment_pesanan()
    my_transaction.addrecepient_pesanan()
    my_transaction.customer_recepient()
    my_transaction.dropoff_recepient()
    my_transaction.ordertype_recepient()
    my_transaction.ordername_recepient()
    my_transaction.quantity_recepient()
    my_transaction.add_recepient()
    my_transaction.add_pesanan()
    my_transaction.submit_order()


def createpartner():
    my_partner = CreatePartner()
    my_partner.login_menu()
    my_partner.fill_username()
    my_partner.fill_password()
    my_partner.submit_login()
    my_partner.partner_menu()
    my_partner.create_button()
    my_partner.create_fullname()
    my_partner.create_phone()
    my_partner.create_gender()
    my_partner.create_date()
    my_partner.create_servicetype()
    my_partner.create_submit()


def createcustomer():
    my_customer = CreateCustomer()
    my_customer.login_menu()
    my_customer.fill_username()
    my_customer.fill_password()
    my_customer.submit_login()
    my_customer.customer_menu()
    my_customer.create_button()
    my_customer.create_firstname()
    my_customer.create_lastname()
    my_customer.create_phone()
    my_customer.create_email()
    my_customer.create_submit()


def createcustomerservice():
    my_customerservice = CreateCustomerService()
    my_customerservice.login_menu()
    my_customerservice.fill_username()
    my_customerservice.fill_password()
    my_customerservice.submit_login()
    my_customerservice.customerservice_menu()
    my_customerservice.create_button()
    my_customerservice.create_fullname()
    my_customerservice.create_email()
    my_customerservice.create_password()
    my_customerservice.create_role()
    my_customerservice.create_submit()


# def createmerchant():
#     my_merchant = CreateMerchant("firefox")
#     my_merchant.login_menu()
#     my_merchant.fill_username()
#     my_merchant.fill_password()
#     my_merchant.submit_login()
#     my_merchant.merchant_menu()
#     my_merchant.create_button()
#     my_merchant.create_fullname()
#     my_merchant.create_phone()
#     my_merchant.create_phone2()
#     my_merchant.create_latitude()
#     my_merchant.create_longitude()
#     my_merchant.create_alamat()
#     my_merchant.create_submit()

# createtransaction()
# createtransactiondone()
# createpartner()
# createcustomer()
# createcustomerservice()

# createmerchant()
createtransaction()
