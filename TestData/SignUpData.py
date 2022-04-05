import pytest
import string
import random


# Import the data from this class. Added dictionary for data, added data in key & value anf access the value with the help of Key.

class SignUpData:
    ranData = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(4))
    email = "gyansahoo333+{0}@gmail.com".format(ranData)
    print(email)

    @pytest.fixture(params=[("Gyan", "Sahoo", "Huck@1845")])
    def getData(self, request):
        return request.param

    @pytest.fixture(
        params=[{"Email": email, "FirstName": "Gyan", "LastName": "Sahoo", "Password": "Huck@1845", "Weight": "65"}])
    def getDataDict(self, request):
        return request.param

    @pytest.fixture(
        params=[{"VesselCardValidation": "Please Select Answer", "wrongFirstName": "Wrong First Name",
                 "wrongLastName": "Wrong Last Name",
                 "wrongPassword": "Wrong Password",
                 "weightValidation": "Please enter your weight",
                 "goalsValidation": "To proceed please select three goals",
                 "goalsOneValidation": "Please select a goal",
                 "rateValidation": "Please choose a rate",
                 "subGoalValidation": "Please select a Subgoal",
                 "badHabitsValidation": "Please select bad habits",
                 "emailValidation": "Wrong Email"
                 }])
    def validationData(self, request):
        return request.param

    @pytest.fixture(
        params=[{"vesselCardTextVerification": "Do you have a Vessel test card?",
                 "welcomeScreen": "Welcome! We’re glad you’re here.",
                 "welcomeTextSettingUpProfile": "Welcome",
                 "genderScreenText": "Gender",
                 "genderIdentifyWithText": "What gender do you identify with?",
                 "heightScreenValidation": "Height",
                 "howTallAreYouTextValidation": "How tall are you?",
                 "weightTextVerification": "Weight",
                 "whatIsYourWeight": "What is your weight (lbs)?",
                 "dateOfBirthTextVerification": "Date of Birth",
                 "whatIsYourDateOfBirth": "What is your date of birth?",
                 "dietTextVerification": "Diet",
                 "selectTheDietTextVerification": "Please select the diets that you are on.",
                 "allergiesTextVerification": "Allergies",
                 "selectAnyAllergiesText": "Please select any food allergies you have.",
                 "preexistingConditionsNotification": "Preexisting Conditions Notification",
                 "goalsTextVerification": "Goals",
                 "selectThreeGoalsYouWouldLikeToFocusOnValidation": "Please select three goals you would like to focus on.",
                 "howWasYourMoodTextVerification": "How was your Mood?"}])
    def pageDataVerification(self, request):
        return request.param
