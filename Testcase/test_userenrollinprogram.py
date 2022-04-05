import time

from BaseUtilities.BaseClass import BaseClass
from BaseUtilities.LoggingClass import LogClass
from PageObjects.PageFunctions import PageFunctions
from TestData.LogInData import LogInData


class TestUserEnrollInProgramTestCases(BaseClass, LogClass, LogInData):
    def test_userenrollinprogram(self, logInCredentialData):

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

        # Click on Add To Program Button
        pagefunction.clickOnAddToProgramButton().click()
        time.sleep(2)

        # Click on Add To Program Button
        pagefunction.clickOnAddToProgramButton().click()
        time.sleep(2)

        # Click on clickOnJoinAProgramButton
        pagefunction.clickOnMoodProgramButton().click()
        time.sleep(2)

        # Click on Next Button
        pagefunction.clickOnNextButton()
        time.sleep(2)

