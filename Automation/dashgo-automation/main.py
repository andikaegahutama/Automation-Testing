from automation.login import Login


def dashgo_login():
    login_dashgo = Login()
    login_dashgo.menu()
    login_dashgo.email()
    login_dashgo.password()
    login_dashgo.login_button()


dashgo_login()
