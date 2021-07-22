import re
from dataclasses import dataclass


# 正規表現に用いる部分パターン
@dataclass
class Place:
    # abstime: 時間表現
    calendar_year: str = "(?P<calendar_year>[0-9]{,4})"  # 暦の年
    calendar_month: str = "(?P<calendar_month>0?[1-9]|1[0-2])"  # 暦の月
    calendar_day: str = "(?P<calendar_day>0?[1-9]|[12][0-9]|3[01])"  # 暦の日
    weekday: str = "(?P<weekday>[月火水木金土日])"
    season: str = "(?P<season>(春|夏|秋|冬))"
    quarter: str = "(?P<quarter>[1-4])"

    @property
    def weekday_with_suffix(self):
        # (日曜日)などの記号付きの表記
        return self.weekday + "(曜日|曜)?"

    @property
    def weekday_with_symbol(self):
        # (日曜日)などの記号付きの表記
        return "\s{,1}\(?\s{,1}" + self.weekday_with_suffix + "\s{,1}\)?"

    # duraton: 期間表現
    year: str = "(?P<year>[0-9]{,4})"
    month: str = "(?P<month>[0-9]+)"  # 日付における月とは異なり、18ヶ月など任意の数字を取れる
    day: str = "(?P<day>[0-9]+\.?[0-9]*)"
    century: str = "(?P<century>[1-9]?[0-9]{,2})"
    week: str = "(?P<week>[0-9]+\.?[0-9]*)"
    hour: str = "(?P<hour>[0-9]+\.?[0-9]*)"
    minutes: str = "(?P<minutes>[0-9]+\.?[0-9]*)"
    second: str = "(?P<second>[0-9]+\.?[0-9]*)"
    second_with_ms: str = "(?P<second_with_ms>[0-9]+[秒][0-9]+)"

    # reltime: 相対的な時間における曖昧表現
    around_prefix = "(以上|[くぐ]らい|ほど|程度|ばかり|近く|より(も)?)"

    # duration: 持続時間
    count: str = "(?P<count>[0-9]+\.?[0-9]*)"
    year_range: str = "(?P<year_range>[0-9]+\.?[0-9]*)"  # 期間としての月
    month_range: str = "(?P<month_range>[0-9]+\.?[0-9]*)"
    day_range: str = "(?P<day_range>[0-9]+\.?[0-9]*)"
    range: str = "(?P<range>[0-9]+\.?[0-9]*)"  # 頻度における数値としての表現

    def is_valid(self, target, text):
        # for tests
        re_pattern = getattr(self, target)
        if re.fullmatch(re_pattern, text):
            return True
        else:
            return False
