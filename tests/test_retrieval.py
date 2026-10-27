from app.retrieval import retrieve_passages


def test_retrieves_temperature_guidance():
    passages = retrieve_passages("What is the temperature range?")

    assert passages
    assert any("18–26 degrees Celsius" in passage for passage in passages)


def test_retrieves_humidity_guidance():
    passages = retrieve_passages("What humidity range is mentioned?")

    assert passages
    assert any("30–60 percent" in passage for passage in passages)


def test_irrelevant_question_returns_no_passages():
    passages = retrieve_passages("Who won the football match?")

    assert passages == []
