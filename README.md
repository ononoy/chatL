##ブラウザ上かアプリで、GitWikiにメモ残しておくか...
# ①ユーザ同士でチャットが出来る部屋がある(1対1のみ、グループも作りたい)
# ②ユーザAとユーザBのチャットルームは他の人からは見れない
# ③ユーザ同士のチャット履歴はいつでも復元される(サーバ側に保存されている)
# ④ユーザ登録画面はあってもなくても
# ⑤チャットはリアルタイムで更新されてなくても、更新したい

# ・AWSのEC2とRDSを使ってインフラ構築
# ・EC2のOSはUbuntuまたはAmazon Linuxを使用
# ・RDSのDBMSにはMySQLを使用
# ・サーバ側はPythonで実装
# ・PythonのWebフレームワークにはTornadoを使用
# ・DBのORMにはsqlalchemyを使用
# ・マイグレーションにはalembicを使用
# ・コーディング規約はpycodestyle(pep8)に従う(atomなどのパッケージにあるのでそれを使用すると規約に沿っていない書き方を注意してくれるから便利)
