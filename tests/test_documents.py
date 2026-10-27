from app.documents import chunk_text, load_guide


def test_load_guide_contains_temperature_section():
    guide = load_guide()

    assert "Temperature:" in guide
    assert "Humidity:" in guide


def test_chunk_text_splits_paragraphs():
    text = "First paragraph.\n\nSecond paragraph.\n\nThird paragraph."

    chunks = chunk_text(text, max_chars=30)

    assert len(chunks) == 3
    assert "First paragraph." in chunks[0]
    assert "Second paragraph." in chunks[1]
    assert "Third paragraph." in chunks[2]


def test_chunk_text_handles_long_paragraph():
    text = "A" * 25

    chunks = chunk_text(text, max_chars=10)

    assert chunks == ["A" * 10, "A" * 10, "A" * 5]
