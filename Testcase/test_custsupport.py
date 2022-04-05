import time

from BaseUtilities.BaseClass import BaseClass
from BaseUtilities.LoggingClass import LogClass
from PageObjects.PageFunctions import PageFunctions
from TestData.CustSupportData import CustSupportData
from TestData.LogInData import LogInData


class TestCustomerSupportTestCases(BaseClass, LogClass, LogInData, CustSupportData):

    def test_verifycustomersupport(self, logInCredentialData, customerSupportData):

        log = self.getLogger()  # Log function
        pagefunction = PageFunctions(self.driver)

        # Click on SignInButton
        pagefunction.clickOnSignInButton().click()

        # Click on Email text field
        pagefunction.signInEmailTextField().click()
        pagefunction.signInEmailTextField().send_keys(logInCredentialData["SignInEmail"])

        time.sleep(2)
        # Click on Done button on IOS Keyword to Hide keyboard
        pagefunction.hideKeyBoard().click()
        time.sleep(1)

        # Click on Password text field
        pagefunction.signInPasswordTextField().click()
        # Send the Password in text field
        pagefunction.signInPasswordTextField().send_keys(logInCredentialData["SignInPassword"])

        # Click on Continue Button
        pagefunction.clickOnContinueButton()
        time.sleep(3)

        # Click on Got it button
        pagefunction.clickOnGotItButton()
        time.sleep(2)

        # Click on Got it button
        pagefunction.clickOnGotItButton()
        time.sleep(2)

        # Click on Button as
        getStartCheckInText = pagefunction.startCheckInDisplay().text

        if getStartCheckInText == "Start check-in":
            pagefunction.clickOnStartCheckIn()
            time.sleep(2)
        else:
            pagefunction.clickOnGetStartedButton()
            time.sleep(2)

        # Click on sad focus option
        pagefunction.clickOnSadFocus()
        # Click on next button
        pagefunction.clickOnNextButton()
        time.sleep(5)

        # Click on easily distracted option
        pagefunction.clickOnSignInEasilyDistracted().click()
        # Click on next button
        pagefunction.clickOnNextButton()
        time.sleep(5)

        # Click on bad habit option
        pagefunction.clickOnSelectBadHabits()
        # Click on next button
        pagefunction.clickOnNextButton()
        time.sleep(2)

        # Click on Got it button
        pagefunction.clickOnGotItButton()
        time.sleep(2)

        # Click on Got it button
        pagefunction.clickOnGotItButton()
        time.sleep(2)

        # Click on Let's do this button
        pagefunction.clickOnLetsDoThisButton()
        time.sleep(2)

        # Click on Let's do this button
        pagefunction.clickOnLetsDoThisButton()
        time.sleep(2)

        # Click on Got it button
        pagefunction.clickOnGotItButton()
        time.sleep(2)

        # Click on More Button on footer
        pagefunction.clickOnMoreButton()
        time.sleep(2)

        # Click on Support Button
        pagefunction.supportButtonTextVerification().click()
        time.sleep(2)

        # Click on Customer Support Button
        pagefunction.contactCustomerSupportButton().click()
        time.sleep(7)

        # Click on Chat Icon
        pagefunction.clickOnChatIconButton().click()
        time.sleep(4)

        pagefunction.nameTextBoxSupport().click()
        pagefunction.nameTextBoxSupport().send_keys("Gyan Sahoo")

        pagefunction.emailTextBoxSupport().click()
        pagefunction.emailTextBoxSupport().send_keys(logInCredentialData["SignInEmail"])

        pagefunction.messageTextBoxSupport().click()
        pagefunction.messageTextBoxSupport().send_keys("Hi, I am Gyan.")
        time.sleep(2)

        pagefunction.clickOnSendMessageButton().click()
        time.sleep(2)

        reachingOutMessage = pagefunction.successReachingOutMessage().text
        assert reachingOutMessage == customerSupportData["ReachingOutMessage"]
        time.sleep(2)

        # Click on Done button on browser to close browser screen
        pagefunction.hideKeyBoard().click()
        time.sleep(3)

        # Click on Back Button
        pagefunction.clickOnCloseButton().click()
        time.sleep(2)

        # Click on My Account Button
        pagefunction.clickOnMyAccount()

        # Click on Logout Button
        pagefunction.clickOnLogout()
        time.sleep(2)