"""Reusable safe URL-only feature extraction helpers.

These functions do not visit or fetch a destination webpage.
"""

from __future__ import annotations

import ipaddress
import math
from collections import Counter
from urllib.parse import parse_qsl, urlsplit

SUSPICIOUS_TOKENS = (
    "login", "verify", "verification", "secure", "account", "update",
    "signin", "bank", "confirm", "password", "wallet", "crypto",
    "invoice", "payment", "support", "recover", "unlock",
)


def shannon_entropy(text: str) -> float:
    text = "" if text is None else str(text)
    if not text:
        return 0.0
    counts = Counter(text)
    n = len(text)
    return -sum((count / n) * math.log2(count / n) for count in counts.values())


def host_is_ip(host: str) -> int:
    if not host:
        return 0
    try:
        ipaddress.ip_address(host)
        return 1
    except ValueError:
        return 0


def extract_safe_url_features(url: str) -> dict[str, float]:
    raw = "" if url is None else str(url).strip()
    parse_text = raw if "://" in raw else "http://" + raw

    try:
        parsed = urlsplit(parse_text)
        host = parsed.hostname or ""
        path = parsed.path or ""
        query = parsed.query or ""
        scheme = (parsed.scheme or "").lower()
    except Exception:
        host, path, query, scheme = "", "", "", ""

    letters = sum(ch.isalpha() for ch in raw)
    digits = sum(ch.isdigit() for ch in raw)
    punctuation_chars = ".-_~:/?#[]@!$&'()*+,;=%"
    punctuation_count = sum(ch in punctuation_chars for ch in raw)
    lower = raw.lower()

    return {
        "eng_url_char_len": len(raw),
        "eng_hostname_len": len(host),
        "eng_path_len": len(path),
        "eng_query_len": len(query),
        "eng_dot_count": raw.count("."),
        "eng_hyphen_count": raw.count("-"),
        "eng_at_count": raw.count("@"),
        "eng_slash_count": raw.count("/"),
        "eng_question_count": raw.count("?"),
        "eng_equal_count": raw.count("="),
        "eng_ampersand_count": raw.count("&"),
        "eng_percent_count": raw.count("%"),
        "eng_digit_count": digits,
        "eng_letter_count": letters,
        "eng_digit_letter_ratio": digits / max(letters, 1),
        "eng_punctuation_count": punctuation_count,
        "eng_punctuation_ratio": punctuation_count / max(len(raw), 1),
        "eng_path_depth": len([p for p in path.split("/") if p]),
        "eng_query_param_count": len(parse_qsl(query, keep_blank_values=True)),
        "eng_entropy": shannon_entropy(raw),
        "eng_suspicious_token_count": sum(token in lower for token in SUSPICIOUS_TOKENS),
        "eng_uses_https": int(scheme == "https"),
        "eng_host_is_ip": host_is_ip(host),
    }
