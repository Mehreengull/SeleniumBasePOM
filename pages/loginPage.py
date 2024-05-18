class LoginPage:
    def test_login(self, sb, username, password):
        sb.open("https://the-internet.herokuapp.com/login")
        sb.type("#username", username)
        sb.type("#password", password)
        sb.click("//button[@type='submit']")

