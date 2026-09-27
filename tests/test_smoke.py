from src.features import extract_safe_url_features
from src.metrics import false_positive_rate


def test_feature_extraction_smoke():
    x = extract_safe_url_features("https://example.com/login?id=123")
    assert x["eng_uses_https"] == 1
    assert x["eng_url_char_len"] > 0
    assert x["eng_query_param_count"] == 1


def test_false_positive_rate():
    y_true = [0, 0, 1, 1]
    y_pred = [0, 1, 1, 1]
    assert false_positive_rate(y_true, y_pred) == 0.5
