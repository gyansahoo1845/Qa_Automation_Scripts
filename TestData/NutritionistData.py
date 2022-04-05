import pytest


class NutritionistData:
    @pytest.fixture(
        params=[{"NutritionistReplyVerification": "Hi! We're here to support you and answer any questions you "
                                                  "may have. Feel free to leave your question below and we'll "
                                                  "get back to you as soon as possible - usually within an hour "
                                                  "during weekdays, 6am - 5pm PST. We'll get back to you within "
                                                  "24 - 48 hours on weekends.",
                 }])
    def nutritionistDataValidation(self, request):
        return request.param
