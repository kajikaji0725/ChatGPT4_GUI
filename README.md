# 起動方法 poetryいれてね
- poetry install
- poetry run python main.py
  - 実行する前に，main.pyがあるディレクトリに.envファイルを作ってください
    - 中身は，CHATGPT4_APIKEY=???としてください．(???のところに，各自のAPIキーを入れてください)

# 実行形式に変更
- poetry run pyinstaller main.py
- 結果は生成されたdistフォルダの中に入ってます
  - 引数を指定すると，いろいろと便利かもしれませんが，調べていないのでわかりません....
- 動かす際には，dist/mainの中に，.envを作って，main.pyをクリックしてください
  - 中身は上のやつと一緒です








# なんでpythonで書いてるんだろう..........................................
# わけのわからんパッケージ使うくらいなら，pythonじゃなくて，Go+Wails+React+Typescriptで作るべきだったな...................
