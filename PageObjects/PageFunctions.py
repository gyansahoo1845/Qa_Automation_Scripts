from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.MobileLocators import MobileLocators


# All the page functions and extend locators from Mobile Locators class.

class PageFunctions:

    def __init__(self, driver):
        self.driver = driver

    def expectedWait(self, locator):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def vesselCardValidation(self):
        return self.driver.find_element(*MobileLocators.vesselCard)

    def emailValidationMessage(self):
        return self.driver.find_element(*MobileLocators.emailValidation)

    def badHabitValidationMessage(self):
        return self.driver.find_element(*MobileLocators.badHabitsValidation)

    def subGoalValidationMessage(self):
        return self.driver.find_element(*MobileLocators.subGoalValidation)

    def rateValidationMessage(self):
        return self.driver.find_element(*MobileLocators.rateValidation)

    def selectGoalValidationMessage(self):
        return self.driver.find_element(*MobileLocators.selectGoalValidation)

    def getWelcomeText(self):
        return self.driver.find_element(*MobileLocators.welcomeText)

    def wrongFirstNameValidation(self):
        return self.driver.find_element(*MobileLocators.wrongFirstName)

    def wrongLastNameValidation(self):
        return self.driver.find_element(*MobileLocators.wrongLastName)

    def wrongPasswordValidation(self):
        return self.driver.find_element(*MobileLocators.wrongPassword)

    def weightValidationMessage(self):
        return self.driver.find_element(*MobileLocators.weightValidation)

    def goalsValidationMessage(self):
        return self.driver.find_element(*MobileLocators.goalsValidation)

    def clickOnSelectBadHabits(self):
        return self.expectedWait(MobileLocators.selectBadHabits)

    def clickOnCoolButton(self):
        return self.expectedWait(MobileLocators.coolButton)

    def clickOnCreateAnAccount(self):
        return self.expectedWait(MobileLocators.createAccountButton)

    def emailTextField(self):
        return self.driver.find_element(*MobileLocators.emailTextBox)

    def clickOnContinueButton(self):
        return self.expectedWait(MobileLocators.continueButton)

    def clickOnNextButton(self):
        return self.expectedWait(MobileLocators.nextButton)

    def clickOnFinishButton(self):
        return self.expectedWait(MobileLocators.finishButton)

    def clickOnYesIWasGivenTestCardOption(self):
        return self.driver.find_element(*MobileLocators.givenTestCardOption)

    def enterFirstName(self):
        return self.driver.find_element(*MobileLocators.firstNameTextBox)

    def enterLastName(self):
        return self.driver.find_element(*MobileLocators.lastNameTextBox)

    def enterPassword(self):
        return self.driver.find_element(*MobileLocators.passwordTextBox)

    def enterWeight(self):
        return self.driver.find_element(*MobileLocators.weightTextBox)

    def selectMaleGender(self):
        return self.driver.find_element(*MobileLocators.genderMale)

    def selectNotToSayDateOfBirth(self):
        return self.driver.find_element(*MobileLocators.dateOfBirth)

    def clickOnVegetarianDiet(self):
        return self.driver.find_element(*MobileLocators.vegetarianDiet)

    def clickOnAllergiesPeanuts(self):
        return self.driver.find_element(*MobileLocators.allergiesPeanuts)

    def clickOnEnergyGoals(self):
        return self.driver.find_element(*MobileLocators.energyGoals)

    def clickOnFocusGoals(self):
        return self.driver.find_element(*MobileLocators.focusGoals)

    def clickOnClamGoals(self):
        return self.driver.find_element(*MobileLocators.calmGoals)

    def clickOnSadFocus(self):
        return self.expectedWait(MobileLocators.sadFocus)

    def clickOnEasilyDistracted(self):
        return self.driver.find_element(*MobileLocators.easilyDistracted)

    def clickOnSignInEasilyDistracted(self):
        return self.driver.find_element(*MobileLocators.signInFocusCheckBoxDistracted)

    def clickOnGotItButton(self):
        return self.expectedWait(MobileLocators.gotItButton)

    def clickOnGetStartedButton(self):
        return self.expectedWait(MobileLocators.getStartedButton)

    def clickOnStartCheckIn(self):
        return self.expectedWait(MobileLocators.startCheckInButton)

    def startCheckInDisplay(self):
        return self.driver.find_element(*MobileLocators.startCheckInButton)

    def clickOnLetsDoThisButton(self):
        return self.expectedWait(MobileLocators.letsDoThisButton)

    def clickOnMoreButton(self):
        return self.expectedWait(MobileLocators.moreButtonFooter)

    def clickOnMyAccount(self):
        return self.expectedWait(MobileLocators.myAccountButton)

    def clickOnLogout(self):
        return self.expectedWait(MobileLocators.logOutButton)

    def clickOnSignInButton(self):
        return self.driver.find_element(*MobileLocators.signInButton)

    def signInEmailTextField(self):
        return self.driver.find_element(*MobileLocators.signInEmailTextBoxField)

    def signInPasswordTextField(self):
        return self.driver.find_element(*MobileLocators.signInPasswordTextBox)

    def hideKeyBoard(self):
        return self.driver.find_element(*MobileLocators.hideKeyBoard)

    def signInEmailVerificationText(self):
        return self.driver.find_element(*MobileLocators.emailTextBoxValidation)

    def signInPasswordVerificationText(self):
        return self.driver.find_element(*MobileLocators.passwordTextBoxValidation)

    def unRegisteredEmailOrPasswordVerificationText(self):
        return self.driver.find_element(*MobileLocators.badUsernameOrPasswordValidation)

    def clickOnBackButton(self):
        return self.driver.find_element(*MobileLocators.backButton)

    def clickOnForgotPasswordUrl(self):
        return self.driver.find_element(*MobileLocators.forgotPasswordUrl)

    def clickOnPrivacyPolicyUrl(self):
        return self.driver.find_element(*MobileLocators.privacyPolicyURL)

    def clickOnTermsUrl(self):
        return self.driver.find_element(*MobileLocators.termsURL)

    def clickOnSubmitButton(self):
        return self.driver.find_element(*MobileLocators.submitButton)

    def successRequestTextVerification(self):
        return self.driver.find_element(*MobileLocators.successRequestText)

    def clickOnLoginButton(self):
        return self.driver.find_element(*MobileLocators.loginButton)

    def myAccountButtonTextVerification(self):
        return self.driver.find_element(*MobileLocators.myAccountButtonText)

    def takeTestButtonTextVerification(self):
        return self.driver.find_element(*MobileLocators.takeTestButtonText)

    def orderCardsButtonTextVerification(self):
        return self.driver.find_element(*MobileLocators.orderCardsButtonText)

    def customSupplementsButtonTextVerification(self):
        return self.driver.find_element(*MobileLocators.customSupplementsButtonText)

    def chatWithANutritionistButtonTextVerification(self):
        return self.driver.find_element(*MobileLocators.chatWithANutritionistButtonText)

    def backedByScienceButtonTextVerification(self):
        return self.driver.find_element(*MobileLocators.backedByScienceButtonText)

    def supportButtonTextVerification(self):
        return self.driver.find_element(*MobileLocators.supportButtonText)

    def profileButtonTextVerification(self):
        return self.driver.find_element(*MobileLocators.profileButtonText)

    def manageMyGoalsButtonTextVerification(self):
        return self.driver.find_element(*MobileLocators.manageMyGoalsButtonText)

    def manageMembershipButtonTextVerification(self):
        return self.driver.find_element(*MobileLocators.manageMembershipButtonText)

    def manageMyDietAllergiesButtonTextVerification(self):
        return self.driver.find_element(*MobileLocators.manageMyDietAllergiesButtonText)

    def contactCustomerSupportButton(self):
        return self.driver.find_element(*MobileLocators.contactCustomerSupportButton)

    def searchAnswerCustomerSupportButton(self):
        return self.driver.find_element(*MobileLocators.searchAnswerSearchTextBox)

    def clickOnChatIconButton(self):
        return self.driver.find_element(*MobileLocators.chatIcon)

    def messageTypeTextBox(self):
        return self.driver.find_element(*MobileLocators.typeMessageTextBox)

    def clickOnMessageSendButton(self):
        return self.driver.find_element(*MobileLocators.sendButton)

    def nameTextBoxSupport(self):
        return self.driver.find_element(*MobileLocators.nameTextBoxSupport)

    def emailTextBoxSupport(self):
        return self.driver.find_element(*MobileLocators.emailTextBoxSupport)

    def messageTextBoxSupport(self):
        return self.driver.find_element(*MobileLocators.messageTextBoxSupport)

    def clickOnCloseButton(self):
        return self.driver.find_element(*MobileLocators.closeButton)

    def clickOnSendMessageButton(self):
        return self.driver.find_element(*MobileLocators.sendMessageButton)

    def clickOnDoneButton(self):
        return self.driver.find_element(*MobileLocators.doneButton)

    def successReachingOutMessage(self):
        return self.driver.find_element(*MobileLocators.successReachingOutMessage)

    def clickOnChatWithNutritionistButton(self):
        return self.driver.find_element(*MobileLocators.chatWithNutritionistButton)

    def vesselNutritionistTextVerification(self):
        return self.driver.find_element(*MobileLocators.vesselNutritionistText)

    def clickOnStartAChatButton(self):
        return self.expectedWait(MobileLocators.startAChatButton)

    def writeAMessageChatBox(self):
        return self.driver.find_element(*MobileLocators.writeAMessage)

    def sendAMessageButton(self):
        return self.driver.find_element(*MobileLocators.sendAMessage)

    def replyNutritionistTextVerification(self):
        return self.driver.find_element(*MobileLocators.replyTextVerification)

    def clicOnCloseChatButton(self):
        return self.driver.find_element(*MobileLocators.closeChatButton)

    def clickOnMinimizeWindowButton(self):
        return self.driver.find_element(*MobileLocators.minimizeWindowButton)

    def clickOnBackButtonFromNutritionist(self):
        return self.driver.find_element(*MobileLocators.backButtonFromNutritionist)

    def clickOnAddToProgramButton(self):
        return self.driver.find_element(*MobileLocators.addToProgramButton)

    def clickOnJoinAProgramButton(self):
        return self.driver.find_element(*MobileLocators.joinAProgramButton)

    def clickOnMoodProgramButton(self):
        return self.driver.find_element(*MobileLocators.moodProgramButton)