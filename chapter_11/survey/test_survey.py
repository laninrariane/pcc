import pytest
from survey import AnonymousServey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousServey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousServey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that multiple responses are stored properly"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousServey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for respon in responses:
        assert response in language_survey.responses