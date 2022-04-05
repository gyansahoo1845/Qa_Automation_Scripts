from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# All the mobile locators

class MobileLocators:

    def __init__(self, driver):
        self.driver = driver

    createAccountButton = (MobileBy.ACCESSIBILITY_ID, "Create an Account")
    emailTextBox = (By.XPATH, "//XCUIElementTypeTextField")
    continueButton = (MobileBy.ACCESSIBILITY_ID, "Continue")
    nextButton = (MobileBy.ACCESSIBILITY_ID, "Next")
    finishButton = (MobileBy.ACCESSIBILITY_ID, "Finish")
    givenTestCardOption = (By.XPATH, "(//XCUIElementTypeButton)[1]")
    firstNameTextBox = (By.XPATH, "(//XCUIElementTypeTextField)[1]")
    lastNameTextBox = (By.XPATH, "(//XCUIElementTypeTextField)[2]")
    passwordTextBox = (By.XPATH, "//XCUIElementTypeSecureTextField")
    genderMale = (By.XPATH, "(//XCUIElementTypeButton)[1]")
    weightTextBox = (By.XPATH, "//XCUIElementTypeTextField")
    dateOfBirth = (By.XPATH, "//XCUIElementTypeImage")
    vegetarianDiet = (By.XPATH, "(//XCUIElementTypeButton)[1]")
    allergiesPeanuts = (By.XPATH, "(//XCUIElementTypeButton)[1]")
    energyGoals = (By.XPATH, "(//XCUIElementTypeButton)[5]")
    focusGoals = (By.XPATH, "(//XCUIElementTypeButton)[2]")
    calmGoals = (By.XPATH, "(//XCUIElementTypeButton)[3]")
    sadFocus = (MobileBy.ACCESSIBILITY_ID, "sad unselected")
    easilyDistracted = (By.XPATH, "(//XCUIElementTypeButton)[3]")
    selectBadHabits = (MobileBy.ACCESSIBILITY_ID, "I Don't Spend Time Outdoors")
    coolButton = (MobileBy.ACCESSIBILITY_ID, "Cool!")
    gotItButton = (MobileBy.ACCESSIBILITY_ID, "Got it")
    startCheckInButton = (MobileBy.ACCESSIBILITY_ID, "Start check-in")
    letsDoThisButton = (MobileBy.ACCESSIBILITY_ID, "Let's do this!")
    getStartedButton = (MobileBy.ACCESSIBILITY_ID, "Get started")
    moreButtonFooter = (MobileBy.ACCESSIBILITY_ID, "More")
    myAccountButton = (MobileBy.ACCESSIBILITY_ID, "My Account")
    logOutButton = (MobileBy.ACCESSIBILITY_ID, "Log Out")
    privacyPolicyURL = (MobileBy.ACCESSIBILITY_ID, "Privacy Policy")
    termsURL = (MobileBy.ACCESSIBILITY_ID, "Terms")

    # Validation Locators
    vesselCard = (MobileBy.ACCESSIBILITY_ID, "Please Select Answer")
    welcomeText = (MobileBy.ACCESSIBILITY_ID, "Welcome")
    wrongFirstName = (MobileBy.ACCESSIBILITY_ID, "Wrong First Name")
    wrongLastName = (MobileBy.ACCESSIBILITY_ID, "Wrong Last Name")
    wrongPassword = (MobileBy.ACCESSIBILITY_ID, "Wrong Password")
    weightValidation = (MobileBy.ACCESSIBILITY_ID, "Please enter your weight")
    goalsValidation = (MobileBy.ACCESSIBILITY_ID, "To proceed please select three goals")
    selectGoalValidation = (MobileBy.ACCESSIBILITY_ID, "Please select a goal")
    rateValidation = (MobileBy.ACCESSIBILITY_ID, "Please choose a rate")
    subGoalValidation = (MobileBy.ACCESSIBILITY_ID, "Please select a Subgoal")
    badHabitsValidation = (MobileBy.ACCESSIBILITY_ID, "Please select bad habits")
    emailValidation = (MobileBy.ACCESSIBILITY_ID, "Wrong Email")

    # Signup Page Data Verification
    welcomeMessageScreenValidation = (MobileBy.ACCESSIBILITY_ID, "Welcome! We’re glad you’re here.")
    vesselTestCardValidation = (MobileBy.ACCESSIBILITY_ID, "Do you have a Vessel test card?")
    welcomeTextFinishUpProfile = (MobileBy.ACCESSIBILITY_ID, "Welcome")
    genderScreenTextVerification = (MobileBy.ACCESSIBILITY_ID, "Gender")
    identifyWithGenderTextVerification = (MobileBy.ACCESSIBILITY_ID, "What gender do you identify with?")
    heightTextVerification = (MobileBy.ACCESSIBILITY_ID, "Height")
    howTallAreYouTextVerification = (MobileBy.ACCESSIBILITY_ID, "How tall are you?")
    weightTextVerification = (MobileBy.ACCESSIBILITY_ID, "Weight")
    whatIsYourWeightIbs = (MobileBy.ACCESSIBILITY_ID, "What is your weight (lbs)?")
    dateOfBirthTextVerification = (MobileBy.ACCESSIBILITY_ID, "Date of Birth")
    whatIsYourDateOfBirth = (MobileBy.ACCESSIBILITY_ID, "What is your date of birth?")
    dietTextVerification = (MobileBy.ACCESSIBILITY_ID, "Diet")
    selectTheDietTextVerification = (MobileBy.ACCESSIBILITY_ID, "Please select the diets that you are on.")
    preexistingConditionsNotification = (MobileBy.ACCESSIBILITY_ID, "Preexisting Conditions Notification")
    goalsTextVerification = (MobileBy.ACCESSIBILITY_ID, "Goals")
    selectThreeGoalsYouWouldLikeToFocusOn = (MobileBy.ACCESSIBILITY_ID, "Please select three goals you would like to focus on.")

    # Sign In Locators
    signInButton = (MobileBy.ACCESSIBILITY_ID, "Sign In")
    signInEmailTextBoxField = (By.XPATH, "//XCUIElementTypeTextField")
    signInPasswordTextBox = (By.XPATH, "//XCUIElementTypeSecureTextField")
    hideKeyBoard = (By.XPATH, "//XCUIElementTypeButton[@name='Done']")

    # Sign In Validation
    emailTextBoxValidation = (MobileBy.ACCESSIBILITY_ID, "Please enter a valid email address.")
    passwordTextBoxValidation = (MobileBy.ACCESSIBILITY_ID, "Please enter a valid password.")
    badUsernameOrPasswordValidation = (MobileBy.ACCESSIBILITY_ID, "Bad username or password.")
    backButton = (MobileBy.ACCESSIBILITY_ID, "Back")
    signInFocusCheckBoxDistracted = (By.XPATH, "(//XCUIElementTypeButton)[17]")

    # Forgot Password Validation
    forgotPasswordUrl = (MobileBy.ACCESSIBILITY_ID, "Forgot Password?")
    submitButton = (MobileBy.ACCESSIBILITY_ID, "Submit")
    successRequestText = (MobileBy.ACCESSIBILITY_ID, "Request sent successfully")
    loginButton = (MobileBy.ACCESSIBILITY_ID, "Login")

    # More Tab Locators
    myAccountButtonText = (MobileBy.ACCESSIBILITY_ID, "My Account")
    takeTestButtonText = (MobileBy.ACCESSIBILITY_ID, "Take a test")
    orderCardsButtonText = (MobileBy.ACCESSIBILITY_ID, "Order Cards")
    customSupplementsButtonText = (MobileBy.ACCESSIBILITY_ID, "Custom Supplements")
    chatWithANutritionistButtonText = (MobileBy.ACCESSIBILITY_ID, "Chat with a Nutritionist")
    backedByScienceButtonText = (MobileBy.ACCESSIBILITY_ID, "Backed by Science")
    supportButtonText = (MobileBy.ACCESSIBILITY_ID, "Support")

    # More Tab >> My Account Locators
    profileButtonText = (MobileBy.ACCESSIBILITY_ID, "Profile")
    manageMyGoalsButtonText = (MobileBy.ACCESSIBILITY_ID, "Manage my goals")
    manageMembershipButtonText = (MobileBy.ACCESSIBILITY_ID, "Manage Membership")
    manageMyDietAllergiesButtonText = (MobileBy.ACCESSIBILITY_ID, "Manage my Diet/Allergies")
    closeButton = (MobileBy.ACCESSIBILITY_ID, "close button")

    # Support Tab
    contactCustomerSupportButton = (MobileBy.ACCESSIBILITY_ID, "Contact Customer Support")
    searchAnswerSearchTextBox = (MobileBy.ACCESSIBILITY_ID, "Search for answers here")
    chatIcon = (MobileBy.ACCESSIBILITY_ID, "Support")
    typeMessageTextBox = (By.XPATH, "//XCUIElementTypeTextView")
    sendButton = (MobileBy.ACCESSIBILITY_ID, "Send")
    nameTextBoxSupport = (MobileBy.ACCESSIBILITY_ID, "Name")
    emailTextBoxSupport = (MobileBy.ACCESSIBILITY_ID, "Email")
    messageTextBoxSupport = (MobileBy.ACCESSIBILITY_ID, "Message")
    sendMessageButton = (MobileBy.ACCESSIBILITY_ID, "Send message")
    doneButton = (By.XPATH, "(//XCUIElementTypeButton[@name='Done'])[2]")
    successReachingOutMessage = (MobileBy.ACCESSIBILITY_ID, "Someone will get back to you soon")

    # Chat with a Nutritionist
    chatWithNutritionistButton = (MobileBy.ACCESSIBILITY_ID, "Chat with a Nutritionist")
    vesselNutritionistText = (MobileBy.ACCESSIBILITY_ID, "Vessel Nutritionist")
    startAChatButton = (MobileBy.ACCESSIBILITY_ID, "Start the chat")
    writeAMessage = (MobileBy.ACCESSIBILITY_ID, "Write a message…")
    sendAMessage = (MobileBy.ACCESSIBILITY_ID, "Send a message")
    replyTextVerification = (MobileBy.ACCESSIBILITY_ID, "Hi! We're here to support you and answer any questions you "
                                                        "may have. Feel free to leave your question below and we'll "
                                                        "get back to you as soon as possible - usually within an hour "
                                                        "during weekdays, 6am - 5pm PST. We'll get back to you within "
                                                        "24 - 48 hours on weekends.")
    closeChatButton = (MobileBy.ACCESSIBILITY_ID, "Close the chat")
    minimizeWindowButton = (MobileBy.ACCESSIBILITY_ID, "Minimize window")
    backButtonFromNutritionist = (MobileBy.ACCESSIBILITY_ID, "back button")

    # Add Program
    addToProgramButton = (MobileBy.ACCESSIBILITY_ID, "Add to program")
    joinAProgramButton = (MobileBy.ACCESSIBILITY_ID, "Join a Program")
    moodProgramButton = (MobileBy.XPATH, "(//XCUIElementTypeButton)[2]")
    leaveAndRemovePlanItems = (MobileBy.ACCESSIBILITY_ID, "Leave and remove plan items")

