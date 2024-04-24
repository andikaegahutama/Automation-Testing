from automation.createtransaction import CreateTransaction


def createtransactiondone():
    mytransaction = CreateTransaction()
    mytransaction.login_menu()
    mytransaction.fill_username()
    mytransaction.fill_password()
    mytransaction.submit_login()
    mytransaction.transaction_create()
    mytransaction.textarea_create()
    # mytransaction.ethix_edx()
    mytransaction.submit_textarea()
    mytransaction.warehouse_type()
    mytransaction.courir_type()
    mytransaction.review_button()
    mytransaction.publish_button()


createtransactiondone()
