import pytest


class LogInData:

    @pytest.fixture(
        params=[{"LogInEmailVerification": "Please enter a valid email address.",
                 "LogInPasswordVerification": "Please enter a valid password.",
                 "UnRegisteredEmailPassword": "Bad username or password.",
                 }])
    def logInValidationData(self, request):
        return request.param

    @pytest.fixture(
        params=[{"Email": "gyansahoo333302@gmail.com",
                 "Password": "Huck@18456",
                 "InValidEmail": "abc.def@mail.c",
                 "ForgotEmail": "gyansahoo1112@gmail.com",
                 "SuccessRequestMessage": "Request sent successfully",
                 "SignInEmail": "gyansahoo333+1els@gmail.com",
                 "SignInPassword": "Huck@1845",
                 }])
    def logInCredentialData(self, request):
        return request.param
