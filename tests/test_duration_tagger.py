import pytest

from ja_timex.tagger import DurationTagger


@pytest.fixture(scope="module")
def t():
    return DurationTagger()


def test_year(t):
    assert t.parse("1年間").value == "P1Y"
    assert t.parse("100年間").value == "P100Y"

    # abstimeともdurationとも取れる表現
    assert t.parse("1年").value == "P1Y"
    assert t.parse("2021年").value == "P2021Y"


def test_month(t):
    assert t.parse("1ヶ月間").value == "P1M"
    assert t.parse("100ヶ月間").value == "P100M"
    assert t.parse("1ヶ月").value == "P1M"

    # abstimeともdurationとも取れる表現
    assert t.parse("1月").value == "P1M"  # e.g. 1月もの間


def test_day(t):
    assert t.parse("1日間").value == "P1D"
    assert t.parse("100日間").value == "P100D"
    assert t.parse("1日").value == "P1D"


def test_hour(t):
    assert t.parse("1時間").value == "PT1H"
    assert t.parse("100時間").value == "PT100H"

    # 1時間のことを1時とは呼ばない
    assert t.parse("1時") is None


def test_minute(t):
    assert t.parse("1分間").value == "PT1M"
    assert t.parse("100分間").value == "PT100M"
    assert t.parse("1分").value == "PT1M"


def test_second(t):
    assert t.parse("1秒間").value == "PT1S"
    assert t.parse("100秒間").value == "PT100S"
    assert t.parse("1秒").value == "PT1S"


def test_second_with_ms(t):
    assert t.parse("1秒05").value == "PT1.05S"
    assert t.parse("100秒5").value == "PT100.5S"
    assert t.parse("1秒0").value == "PT1.0S"


def test_multiple_durations(t):
    assert t.parse("1年2ヶ月").value == "P1Y2M"
    assert t.parse("1年2ヶ月間").value == "P1Y2M"
    assert t.parse("1年2ヶ月10日").value == "P1Y2M10D"

    assert t.parse("1時間30分").value == "PT1H30M"
    assert t.parse("1時間30分間").value == "PT1H30M"
    assert t.parse("1時間30分25秒").value == "PT1H30M25S"


def test_multiple_durations_never_mixed_date_and_time(t):
    # 日付を表す持続時間表現と、時間を表す持続時間表現は、混ざらない
    assert t.parse("1年3時間") is None
    assert t.parse("3日10時間") is None
    assert t.parse("1日10分") is None  # 1日あたり10分という意味のため、DURATIONではなくSETとして扱う


def test_invalid_duration(t):
    assert t.parse("年を超す") is None
    assert t.parse("強化月間") is None
    assert t.parse("週またぎの行事") is None
    assert t.parse("日が変わる") is None


def test_half_suffix(t):
    # 半分を表す表記
    assert t.parse("1.5時間").value == "PT1.5H"
    assert t.parse("1時間半").value == "PT1.5H"
    assert t.parse("1時間半").text == "1時間半"

    # PT
    assert t.parse("10分半").value == "PT10.5M"
    assert t.parse("1秒半").value == "PT1.5S"

    # P
    assert t.parse("1年半").value == "P1.5Y"
    assert t.parse("5ヶ月半").value == "P5.5M"
    assert t.parse("2週間半").value == "P2.5W"  # 週だけは"間"を含むこともある
    assert t.parse("2週半").value == "P2.5W"
    assert t.parse("1日半").value == "P1.5D"
    assert t.parse("1日半").text == "1日半"


def test_only_half(t):
    # 数字がなく単に"半"だけの場合
    assert t.parse("半世紀").value == "P50Y"
    assert t.parse("四半世紀").value == "P25Y"
    assert t.parse("半年").value == "P0.5Y"
    assert t.parse("半月").value == "P0.5M"
    assert t.parse("半日").value == "P0.5D"
