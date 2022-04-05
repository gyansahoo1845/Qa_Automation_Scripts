import time

from BaseUtilities.BaseClass import BaseClass
from BaseUtilities.LoggingClass import LogClass
from PageObjects.PageFunctions import PageFunctions
from TestData.LogInData import LogInData


class TestGuestUserTestCases(BaseClass, LogClass, LogInData):

    def test_guestuseractions(self, logInValidationData, logInCredentialData):
        log = self.getLogger()  # Log function
        pagefunction = PageFunctions(self.driver)

        # Click on SignInButton
        pagefunction.clickOnSignInButton().click()

        # Click on Continue Button
        pagefunction.clickOnContinueButton()
        time.sleep(2)

        # Verify Blank email validation
        blankEmailValidation = pagefunction.signInEmailVerificationText().text
        assert blankEmailValidation == logInValidationData["LogInEmailVerification"]

        # Click on Email Textbox
        pagefunction.signInEmailTextField().click()
        pagefunction.signInEmailTextField().send_keys(logInCredentialData["Email"])

        time.sleep(2)
        # Click on Done button on IOS Keyword to Hide keyboard
        pagefunction.hideKeyBoard().click()
        time.sleep(1)

        # Click on Continue Button
        pagefunction.clickOnContinueButton()
        time.sleep(2)

        # Verify Blank email validation
        blankPasswordValidation = pagefunction.signInPasswordVerificationText().text
        assert blankPasswordValidation == logInValidationData["LogInPasswordVerification"]

        time.sleep(2)
        # Click on Done button on IOS Keyword to Hide keyboard
        pagefunction.hideKeyBoard().click()
        time.sleep(1)

        # Click on Email Textbox & Clear the textbox
        pagefunction.signInEmailTextField().click()
        pagefunction.signInEmailTextField().clear()

        time.sleep(2)
        # Click on Done button on IOS Keyword to Hide keyboard
        pagefunction.hideKeyBoard().click()
        time.sleep(1)

        # Click on Password text field
        pagefunction.signInPasswordTextField().click()
        # Send the Password in text field
        pagefunction.signInPasswordTextField().send_keys(logInCredentialData["Password"])

        time.sleep(2)
        # Click on Done button on IOS Keyword to Hide keyboard
        pagefunction.hideKeyBoard().click()
        time.sleep(1)

        # Click on Continue Button
        pagefunction.clickOnContinueButton()
        time.sleep(2)

        # Verify Blank email validation
        assert blankEmailValidation == logInValidationData["LogInEmailVerification"]

        # Click on Email Textbox & Enter the UnRegistered email in textbox
        pagefunction.signInEmailTextField().click()
        pagefunction.signInEmailTextField().send_keys(logInCredentialData["Email"])

        time.sleep(2)
        # Click on Done button on IOS Keyword to Hide keyboard
        pagefunction.hideKeyBoard().click()
        time.sleep(1)

        # Click on Password text field
        pagefunction.signInPasswordTextField().click()
        # Send the UnRegistered Password in text field
        pagefunction.signInPasswordTextField().send_keys(logInCredentialData["Password"])

        time.sleep(2)
        # Click on Done button on IOS Keyword to Hide keyboard
        pagefunction.hideKeyBoard().click()
        time.sleep(1)

        # Click on Continue Button
        pagefunction.clickOnContinueButton()
        time.sleep(2)

        # Verify UnRegistered Email OR Password validation
        unRegisteredEmailPasswordValidation = pagefunction.unRegisteredEmailOrPasswordVerificationText().text
        assert unRegisteredEmailPasswordValidation == logInValidationData["UnRegisteredEmailPassword"]

        # Click on Email Textbox & Clear the textbox
        pagefunction.signInEmailTextField().click()
        pagefunction.signInEmailTextField().clear()
        pagefunction.signInEmailTextField().send_keys(logInCredentialData["InValidEmail"])

        time.sleep(2)
        # Click on Done button on IOS Keyword to Hide keyboard
        pagefunction.hideKeyBoard().click()
        time.sleep(1)

        # Click on Password text field
        pagefunction.signInPasswordTextField().click()
        pagefunction.signInPasswordTextField().clear()
        # Send the UnRegistered Password in text field
        pagefunction.signInPasswordTextField().send_keys(logInCredentialData["Password"])

        time.sleep(2)
        # Click on Done button on IOS Keyword to Hide keyboard
        pagefunction.hideKeyBoard().click()
        time.sleep(1)

        # Click on Continue Button
        pagefunction.clickOnContinueButton()
        time.sleep(3)

        # Verify Invalid Email format
        inValidEmailFormatValidation = pagefunction.unRegisteredEmailOrPasswordVerificationText().text
        assert inValidEmailFormatValidation == logInValidationData["UnRegisteredEmailPassword"]

        # Click on Back Button
        pagefunction.clickOnBackButton().click()
        time.sleep(2)

        # Click on SignInButton
        pagefunction.clickOnSignInButton().click()

        # Click on Forgot Password URL
        pagefunction.clickOnForgotPasswordUrl().click()
        time.sleep(2)

        # Click on Submit Button
        pagefunction.clickOnSubmitButton().click()

        # Verify Blank email validation
        forgotBlankEmailValidation = pagefunction.signInEmailVerificationText().text
        assert forgotBlankEmailValidation == logInValidationData["LogInEmailVerification"]

        # Click on Email Textbox & Enter the UnRegistered email in textbox
        pagefunction.signInEmailTextField().click()
        pagefunction.signInEmailTextField().send_keys(logInCredentialData["Email"])

        time.sleep(2)
        # Click on Done button on IOS Keyword to Hide keyboard
        pagefunction.hideKeyBoard().click()
        time.sleep(1)

        # Click on Submit Button
        pagefunction.clickOnSubmitButton().click()
        time.sleep(2)

        # Verify Success request sent message
        successMessageText = pagefunction.successRequestTextVerification().text
        assert successMessageText == logInCredentialData["SuccessRequestMessage"]

        # Click on Login Button
        pagefunction.clickOnLoginButton().click()
        time.sleep(3)

        # Click on Back Button
        pagefunction.clickOnBackButton().click()
        time.sleep(2)

        # Click on Create An Account Button
        pagefunction.clickOnCreateAnAccount()
        time.sleep(2)

        pagefunction.clickOnPrivacyPolicyUrl().click()
        time.sleep(2)

        time.sleep(2)
        # Click on Done button on IOS Keyword to Hide keyboard
        pagefunction.hideKeyBoard().click()
        time.sleep(3)

        # Click on Term URL
        pagefunction.clickOnTermsUrl().click()
        time.sleep(2)

        # Click on Done button on IOS Keyword to Hide keyboard
        pagefunction.hideKeyBoard().click()
        time.sleep(3)