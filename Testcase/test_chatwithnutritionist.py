import time

from BaseUtilities.BaseClass import BaseClass
from BaseUtilities.LoggingClass import LogClass
from PageObjects.PageFunctions import PageFunctions
from TestData.CustSupportData import CustSupportData
from TestData.LogInData import LogInData
from TestData.NutritionistData import NutritionistData


class TestChatWithNutritionistTestCases(BaseClass, LogClass, LogInData, CustSupportData, NutritionistData):
    def test_chatwithnutritionist(self, logInCredentialData, nutritionistDataValidation):

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

        time.sleep(2)
        # Click on Done button on IOS Keyword to Hide keyboard
        pagefunction.hideKeyBoard().click()
        time.sleep(1)

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

        # Click on Chat With A Nutritionist Button
        pagefunction.chatWithANutritionistButtonTextVerification().click()
        time.sleep(2)

        # Click on Chat With A Nutritionist Button
        pagefunction.clickOnChatWithNutritionistButton().click()
        time.sleep(5)

        # Click on Start A Chat Button
        pagefunction.clickOnStartAChatButton()
        time.sleep(2)

        # Click on Write A Message Chat Box
        pagefunction.writeAMessageChatBox().click()
        time.sleep(2)
        pagefunction.writeAMessageChatBox().send_keys("Hi Vessel Nutritionist")
        time.sleep(2)

        # Click on Send Message button
        pagefunction.sendAMessageButton().click()
        time.sleep(2)
        # Click on Done button on IOS Keyword to Hide keyboard
        pagefunction.hideKeyBoard().click()
        time.sleep(5)

        # Click on close chat icon
        pagefunction.clicOnCloseChatButton().click()
        time.sleep(2)

        # Click on close chat button
        pagefunction.clicOnCloseChatButton().click()
        time.sleep(2)

        # Click on Minimize button
        pagefunction.clickOnMinimizeWindowButton().click()
        time.sleep(2)

        # Click on back button
        pagefunction.clickOnBackButtonFromNutritionist().click()
        time.sleep(2)

        # Click on My Account Button
        pagefunction.clickOnMyAccount()
        time.sleep(2)

        # Click on Logout Button
        pagefunction.clickOnLogout()
        time.sleep(2)