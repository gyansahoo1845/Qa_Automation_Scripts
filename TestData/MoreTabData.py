import pytest


class MoreTabData:
    @pytest.fixture(
        params=[{"MyAccountVerification": "My Account",
                 "TakeATestVerification": "Take a test",
                 "OrderCardsVerification": "Order Cards",
                 "CustomSupplementsVerification":"Custom Supplements",
                 "ChatWithANutritionistVerification":"Chat with a Nutritionist",
                 "BackedByScienceVerification":"Backed by Science",
                 "SupportVerification":"Support",
                 "ProfileButtonVerification":"Profile",
                 "ManageMyGoalsButtonVerification":"Manage my goals",
                 "ManageMembershipButtonVerification": "Manage Membership",
                 "ManageMyDietAllergiesButtonVerification": "Manage my Diet/Allergies",
                 }])
    def moreTabValidationData(self, request):
        return request.param