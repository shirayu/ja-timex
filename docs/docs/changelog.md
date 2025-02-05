# 更新履歴

## v0.1.7(2021-08-15)

### 🚀 Features

* 漢数字を変換しない`ignore_kansuji`パラメータを追加 (#44) @yagays
* 末日という表現をサポート (#42) @yagays
* 16世紀頃, 紀元前2世紀近くといった表現をサポート (#40) @yagays
* 早朝6時や10時半といった表現をサポート (#36) @yagays
* 深夜0時や深夜25時といった表現をサポート (#35) @yagays
* 3日ぶりや10年ぶりといった表現をサポート (#32) @yagays
* 8日目や30年もの間といった表現をサポート (#30) @yagays

### 🐛 Bug Fixes

* 一時代を時間として取得してしまう問題を修正 (#45) @yagays
* 翌週28日が週28日と取得される問題を修正 (#39) @yagays
* remove JUST mod (#38) @yagays
* 数字が複数含まれるときに桁数のコンマ処理がされない問題を修正 (#37) @yagays
* 12：30といった全角コロンの時間表記を取得できるように修正 (#34) @yagays
* 時刻表現の後にスペースがある際にTimex.textに含まれないように修正 (#33) @yagays
* 東京・千代田区や千春,千夏,千秋,千冬といった表現を取得してしまうバグを修正 (#31) @yagays
* 全角括弧の囲みを取得するように修正 (#29) @yagays

### 📖 Documentation and examples

* update docs (#41) @yagays

## v0.1.6(2021-08-09)

### 🚀 Features

* `to_datetime()`でデフォルトのtimezoneを設定可能にする (#27) @yagays
* 1年半後や1時間半前、半年といった表現をサポート (#23) @yagays
* "半"という表現をサポート (#22) @yagays

### 🐛 Bug Fixes

* 先月や半年前などの数字を伴わない表現でto\_duration()の計算を修正 (#25) @yagays
* "世紀"の前に数字が無いとエラーが出る問題を修正 (#24) @yagays

### 📖 Documentation and examples

* 日付型/時間型への変換方法の説明を追加 (#28) @yagays
* typoを修正 (#18) @yagays

### 🚧 Maintenance

* テストを追加 (#26) @yagays
* enable to trigger with release drafter (#17) @yagays

## v0.1.5(2021-08-06)

### 🚀 Features

* 基準日を設定できるようにする (#14) @yagays
* 夜9時・今夜9時のような表現をサポート (#13) @yagays

### 📖 Documentation and examples

* 基準日時の説明を追加 (#16) @yagays

### 🚧 Maintenance

* streamlitのアプリでto\_datetime/to\_durationに対応 (#15) @yagays
* add release-drafter (#12) @yagays

## v0.1.4 (2021-08-05)

### 🐛 Bug fixes

* "毎年6月"が"年6月"と判定されるバグを修正 #4
* Windows環境でテストが通らないエラーを修正 #8

### 🚧 Maintenance

* CIを整備 #6 #10

## v0.1.3 (2021-08-01)

* バグ修正

## v0.1.2 (2021-08-01)

* 「先月」「一昨年」といった表現を追加

## v0.1.1 (2021-08-01)

* `ja-timex`リリース
* `ja-timex/docs`でドキュメント公開