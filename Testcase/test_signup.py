import time
from BaseUtilities.BaseClass import BaseClass
from PageObjects.MobileLocators import MobileLocators
from PageObjects.PageFunctions import PageFunctions
from TestData.SignUpData import SignUpData
from BaseUtilities.LoggingClass import LogClass


# Testcase class - Added test script for signup page with verification.

class TestSignUpTestCases(BaseClass, LogClass, SignUpData):

    def test_signup(self, getDataDict, validationData):
        mobileLocators = MobileLocators(self.driver)
        log = self.getLogger() # Log function
        pagefunction = PageFunctions(self.driver)

        # Click on create an account button
        pagefunction.clickOnCreateAnAccount()
        log.info("Click on Create an account button")
        time.sleep(2)

        # Verify validation message if user click on continue button without any email
        pagefunction.clickOnContinueButton()
        log.info("Click on Click on Continue Button")
        emailValidationText = pagefunction.emailValidationMessage().text
        assert emailValidationText == validationData["emailValidation"]
        log.info("Verify validation message if user click on continue button without any email")

        # Click on email text box & enter the email from dictionary
        pagefunction.emailTextField().click()
        emailAddress = getDataDict["Email"]
        pagefunction.emailTextField().send_keys(emailAddress)
        log.info("Click on email text box & enter the email from dictionary")

        # Click on continue button
        pagefunction.clickOnContinueButton()
        time.sleep(3)
        log.info("Click on continue button")

        # Vessel Card Verification
        pagefunction.clickOnContinueButton()
        vesselMessage = pagefunction.vesselCardValidation().text
        assert vesselMessage == validationData["VesselCardValidation"]
        log.info("Verify the vessel card verification message")

        # Click on Yes I Was Given Test Card Option
        pagefunction.clickOnYesIWasGivenTestCardOption().click()
        time.sleep(3)
        log.info("Click on Yes I Was Given Test Card Option")

        # Click on continue button
        pagefunction.clickOnContinueButton()
        time.sleep(3)
        log.info("Click on continue button")

        # Click on continue button
        pagefunction.clickOnContinueButton()
        time.sleep(3)
        log.info("Click on continue button")

        # Validation for blank First name.
        pagefunction.clickOnContinueButton()
        firstNameValidation = pagefunction.wrongFirstNameValidation().text
        assert firstNameValidation == validationData["wrongFirstName"]
        log.info("Verify the message for blank First name.")

        # Enter the first name
        pagefunction.enterFirstName().click()
        pagefunction.enterFirstName().send_keys(getDataDict["FirstName"])
        log.info("Enter the First Name in Textbox")

        # Validation for blank last name field
        pagefunction.enterLastName().click()
        time.sleep(1)
        pagefunction.enterPassword().click()
        pagefunction.clickOnContinueButton()
        lastNameValidation = pagefunction.wrongLastNameValidation().text
        assert lastNameValidation == validationData["wrongLastName"]
        log.info("Verify the message for blank Last name.")

        # Enter the last name
        pagefunction.enterLastName().click()
        pagefunction.enterLastName().send_keys(getDataDict["LastName"])
        log.info("Enter the Last Name in Textbox")

        # Validation for blank password field
        pagefunction.enterPassword().click()
        pagefunction.clickOnContinueButton()
        passwordValidation = pagefunction.wrongPasswordValidation().text
        assert passwordValidation == validationData["wrongPassword"]
        log.info("Verify the message for blank password field.")

        # Enter the password
        pagefunction.enterPassword().click()
        pagefunction.enterPassword().send_keys(getDataDict["Password"])
        pagefunction.clickOnContinueButton()
        log.info("Enter the password in textbox")

        # Select Gender
        pagefunction.selectMaleGender().click()
        time.sleep(2)
        log.info("Select Male Gender")

        # Click on Next button
        pagefunction.clickOnNextButton()
        time.sleep(2)
        log.info("Click on next button")

        pagefunction.clickOnNextButton()
        time.sleep(2)
        log.info("Click on next button")

        pagefunction.clickOnNextButton()
        time.sleep(2)
        log.info("Click on next button")

        # Verify validation for blank weight validation
        pagefunction.clickOnNextButton()
        time.sleep(1)
        weightValidation = pagefunction.weightValidationMessage().text
        assert weightValidation == validationData["weightValidation"]
        log.info("Verify validation for blank weight validation")

        # Enter the weight
        pagefunction.enterWeight().click()
        pagefunction.enterWeight().send_keys(getDataDict["Weight"])
        log.info("Enter the weight in textbox")

        # Click on next button
        pagefunction.clickOnNextButton()
        time.sleep(2)
        log.info("Click on next button")

        # Select not to say date of birth button
        pagefunction.selectNotToSayDateOfBirth().click()
        log.info("Select not to say date of birth button")

        # Click on finish button
        pagefunction.clickOnFinishButton()
        time.sleep(5)
        log.info("Click on finish button")

        # Click on vegetarian diet button
        pagefunction.clickOnVegetarianDiet().click()
        pagefunction.clickOnNextButton()
        time.sleep(2)
        log.info("Click on vegetarian diet button")

        # Click on allergies peanuts option
        pagefunction.clickOnAllergiesPeanuts().click()
        pagefunction.clickOnNextButton()
        time.sleep(2)
        log.info("Click on allergies peanuts option")

        # Click on continue button
        pagefunction.clickOnContinueButton()
        time.sleep(3)
        log.info("Click on continue button")

        # Verify validation message if user click on next button without select any option
        pagefunction.clickOnNextButton()
        goalsValidation = pagefunction.goalsValidationMessage().text
        assert goalsValidation == validationData["goalsValidation"]
        log.info("Verify validation message if user click on next button without select any option")

        # Click on Focus goal option
        pagefunction.clickOnFocusGoals().click()
        time.sleep(2)
        log.info("Click on Focus goal option")

        # Click on calm goal option
        pagefunction.clickOnClamGoals().click()
        time.sleep(2)
        log.info("Click on calm goal option")

        # Click on energy option
        pagefunction.clickOnEnergyGoals().click()
        time.sleep(2)
        log.info("Click on energy option")

        # Click on next button
        pagefunction.clickOnNextButton()
        time.sleep(5)
        log.info("Click on next button")

        # Verify validation message if user click on next button without select any option
        pagefunction.clickOnNextButton()
        goalsOneValidation = pagefunction.selectGoalValidationMessage().text
        assert goalsOneValidation == validationData["goalsOneValidation"]
        log.info("Verify validation message if user click on next button without select any option")

        # Click on Focus goal option
        pagefunction.clickOnFocusGoals().click()
        pagefunction.clickOnNextButton()
        time.sleep(6)
        log.info("Click on Focus goal option")

        # Verify the rate validation if user click on next button without select any option
        pagefunction.clickOnNextButton()
        rateMessage = pagefunction.rateValidationMessage().text
        assert rateMessage == validationData["rateValidation"]
        log.info("Verify the rate validation if user click on next button without select any option")

        # Click on sad focus option
        pagefunction.clickOnSadFocus()
        log.info("Click on sad focus option")
        # Click on next button
        pagefunction.clickOnNextButton()
        time.sleep(5)
        log.info("Click on next button")

        # Verify validation message if user click on next button without select any sub goal
        pagefunction.clickOnNextButton()
        subGoalMessage = pagefunction.subGoalValidationMessage().text
        assert subGoalMessage == validationData["subGoalValidation"]
        log.info("Verify validation message if user click on next button without select any sub goal")

        # Click on easily distracted option
        pagefunction.clickOnEasilyDistracted().click()
        log.info("Click on easily distracted option")
        # Click on next button
        pagefunction.clickOnNextButton()
        time.sleep(5)
        log.info("Click on next button")

        # Verify the validation message if user click on next button without select any option
        pagefunction.clickOnNextButton()
        badHabitMessage = pagefunction.badHabitValidationMessage().text
        assert badHabitMessage == validationData["badHabitsValidation"]
        log.info("Verify the validation message if user click on next button without select any option")

        # Click on bad habit option
        pagefunction.clickOnSelectBadHabits()
        log.info("Click on bad habit option")
        # Click on next button
        pagefunction.clickOnNextButton()
        time.sleep(2)
        log.info("Click on next button")

        # Click on cool button
        pagefunction.clickOnCoolButton()
        time.sleep(2)
        log.info("Click on cool button")

        # Click on cool button
        pagefunction.clickOnCoolButton()
        time.sleep(5)
        log.info("Click on cool button")

        # Click on cool button
        pagefunction.clickOnCoolButton()
        time.sleep(5)
        log.info("Click on cool button")

        # Click on Got it button
        pagefunction.clickOnGotItButton()
        time.sleep(2)
        log.info("Click on Got it button")

        # Click on Got it button
        pagefunction.clickOnGotItButton()
        time.sleep(2)
        log.info("Click on Got it button")

        # Click on Let's do this button
        pagefunction.clickOnLetsDoThisButton()
        time.sleep(2)
        log.info("Click on Let's do this button")

        # Click on Let's do this button
        pagefunction.clickOnLetsDoThisButton()
        time.sleep(2)
        log.info("Click on Let's do this button")

        # Click on Got it button
        pagefunction.clickOnGotItButton()
        time.sleep(2)
        log.info("Click on Got it button")

        # Click on More Button on footer
        pagefunction.clickOnMoreButton()
        log.info("Click on More button")

        # Click on My Account Button
        pagefunction.clickOnMyAccount()
        log.info("Click on More button")

        # Click on Logout Button
        pagefunction.clickOnLogout()
        time.sleep(2)
        log.info("Click on Logout button")

        # Sign In Flow
        # Click on SignInButton
        pagefunction.clickOnSignInButton().click()
        log.info("Click on Sign In button")

        # Click on Email text field
        pagefunction.signInEmailTextField().click()
        pagefunction.signInEmailTextField().send_keys(emailAddress)
        log.info("Enter the email address which was created while signing up.")

        time.sleep(2)
        # Click on Done button on IOS Keyword to Hide keyboard
        pagefunction.hideKeyBoard().click()
        time.sleep(1)
        log.info("Hide the Ios Keyboard")

        # Click on Password text field
        pagefunction.signInPasswordTextField().click()
        # Send the Password in text field
        pagefunction.signInPasswordTextField().send_keys(getDataDict["Password"])
        log.info("Enter the password which was created while signing up.")

        # Click on Continue Button
        pagefunction.clickOnContinueButton()
        time.sleep(3)
        log.info("Click on Continue Button")

        # Click on More Button on footer
        pagefunction.clickOnMoreButton()
        log.info("Click on More Button on footer")

        # Click on My Account Button
        pagefunction.clickOnMyAccount()
        log.info("Click on My Account Button")

        # Click on Logout Button
        pagefunction.clickOnLogout()
        time.sleep(2)
        log.info("Click on Logout Button")