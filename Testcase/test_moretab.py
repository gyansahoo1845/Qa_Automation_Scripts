import time

from BaseUtilities.BaseClass import BaseClass
from BaseUtilities.LoggingClass import LogClass
from PageObjects.PageFunctions import PageFunctions
from TestData.LogInData import LogInData
from TestData.MoreTabData import MoreTabData


class TestMoreTabTestCases(BaseClass, LogClass, LogInData, MoreTabData):

    def test_verifymoretab(self, logInCredentialData, moreTabValidationData):
        log = self.getLogger()  # Log function
        pagefunction = PageFunctions(self.driver)
        # Sign In Flow
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

        # Verify My Account Text validation
        myAccountTextValidation = pagefunction.myAccountButtonTextVerification().text
        assert myAccountTextValidation == moreTabValidationData["MyAccountVerification"]

        # Verify Take Test Button Text validation
        takeTestButtonTextValidation = pagefunction.takeTestButtonTextVerification().text
        assert takeTestButtonTextValidation == moreTabValidationData["TakeATestVerification"]

        # Verify Order Cards Button Text validation
        orderCardsButtonTextValidation = pagefunction.orderCardsButtonTextVerification().text
        assert orderCardsButtonTextValidation == moreTabValidationData["OrderCardsVerification"]

        # Verify Custom Supplements Text validation
        customSupplementsButtonTextValidation = pagefunction.customSupplementsButtonTextVerification().text
        assert customSupplementsButtonTextValidation == moreTabValidationData["CustomSupplementsVerification"]

        # Verify Chat With A Nutritionist Text validation
        chatWithANutritionistButtonTextValidation = pagefunction.chatWithANutritionistButtonTextVerification().text
        assert chatWithANutritionistButtonTextValidation == moreTabValidationData["ChatWithANutritionistVerification"]

        # Verify Backed By Science Text validation
        backedByScienceButtonTextValidation = pagefunction.backedByScienceButtonTextVerification().text
        assert backedByScienceButtonTextValidation == moreTabValidationData["BackedByScienceVerification"]

        # Verify Support Text validation
        supportButtonTextValidation = pagefunction.supportButtonTextVerification().text
        assert supportButtonTextValidation == moreTabValidationData["SupportVerification"]

        # Click on My Account Button
        pagefunction.clickOnMyAccount()

        # Verify Support Text validation
        profileButtonTextValidation = pagefunction.profileButtonTextVerification().text
        assert profileButtonTextValidation == moreTabValidationData["ProfileButtonVerification"]

        # Verify Manage My Goals Text validation
        manageMyGoalsButtonTextValidation = pagefunction.manageMyGoalsButtonTextVerification().text
        assert manageMyGoalsButtonTextValidation == moreTabValidationData["ManageMyGoalsButtonVerification"]

        # Verify Manage Membership Button Text validation
        manageMembershipButtonTextValidation = pagefunction.manageMembershipButtonTextVerification().text
        assert manageMembershipButtonTextValidation == moreTabValidationData["ManageMembershipButtonVerification"]

        # Verify Manage My Diet/Allergies Text validation
        manageMyDietAllergiesButtonTextValidation = pagefunction.manageMyDietAllergiesButtonTextVerification().text
        assert manageMyDietAllergiesButtonTextValidation == moreTabValidationData["ManageMyDietAllergiesButtonVerification"]

        # Click on Logout Button
        pagefunction.clickOnLogout()
        time.sleep(2)