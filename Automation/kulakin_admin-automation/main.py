from automation.TransactionEDXCOD import CreateTransactionEDXCOD
from automation.TransactionEDXBANK import CreateTransactionEDXBANK
from automation.TransactionEDMCOD import CreateTransactionEDMCOD
from automation.TransactionEDMBANK import CreateTransactionEDMBANK


def createtransactionedxcod():
    transactioncodedx = CreateTransactionEDXCOD()
    transactioncodedx.menu()
    transactioncodedx.fill_phone()
    transactioncodedx.fill_pin()
    transactioncodedx.button_login()
    transactioncodedx.transaction_menu()
    transactioncodedx.produk_edx()
    transactioncodedx.create_button()
    transactioncodedx.paste_button()
    transactioncodedx.textarea_create()
    transactioncodedx.add_template()
    transactioncodedx.simpan_button()
    transactioncodedx.sure_button()
    # transactioncodedx.publish_button()


def createtransactionedxbank():
    transactionbankedx = CreateTransactionEDXBANK()
    transactionbankedx.menu()
    transactionbankedx.fill_phone()
    transactionbankedx.fill_pin()
    transactionbankedx.button_login()
    transactionbankedx.transaction_menu()
    transactionbankedx.produk_edx()
    transactionbankedx.create_button()
    transactionbankedx.paste_button()
    transactionbankedx.textarea_create()
    transactionbankedx.add_template()
    transactionbankedx.bank_option()
    transactionbankedx.simpan_button()
    transactionbankedx.sure_button()


def createtransactionedmcod():
    transactioncodedm = CreateTransactionEDMCOD()
    transactioncodedm.menu()
    transactioncodedm.fill_phone()
    transactioncodedm.fill_pin()
    transactioncodedm.button_login()
    transactioncodedm.transaction_menu()
    transactioncodedm.produk_edm()
    transactioncodedm.create_button()
    transactioncodedm.paste_button()
    transactioncodedm.textarea_create()
    transactioncodedm.add_template()
    transactioncodedm.simpan_button()
    transactioncodedm.sure_button()


def createtransactionedmbank():
    transactionbankedm = CreateTransactionEDMBANK()
    transactionbankedm.menu()
    transactionbankedm.fill_phone()
    transactionbankedm.fill_pin()
    transactionbankedm.button_login()
    transactionbankedm.transaction_menu()
    transactionbankedm.produk_edm()
    transactionbankedm.create_button()
    transactionbankedm.paste_button()
    transactionbankedm.textarea_create()
    transactionbankedm.add_template()
    transactionbankedm.bank_option()
    transactionbankedm.simpan_button()
    transactionbankedm.sure_button()


# createtransactionedxcod()
# createtransactionedxbank()
# createtransactionedmcod()
createtransactionedmbank()
