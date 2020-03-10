from rest_framework import throttling


class QuestionCreationThrottleSustained(throttling.UserRateThrottle):
    scope = 'question.create.sustained'

class QuestionThrottleSustained(throttling.UserRateThrottle):
    scope = 'question.sustained'