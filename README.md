# ToDoEveryDay0.6

概要==========================

前日に明日やること(todo)を書いて、今日のやるべきだったこと(todo)の評価を
カレンダーに記入する。

上記の、自分がやっている習慣をプログラムに落としこもうとしました。
※windowsのため、pyinstallerでexe化してあります。



使い方==========================

明日やることの設定のボタンをクリックすると設定画面へ（Max5個まで設定可能）

ここで一回プログラムを終了させて、もう一度起動すると設定した項目がトップページに出る。

todoが出来たかの評価はトップページのボタンから行う。

評価はコメントと記憶に残ったものをマークできるようになっている（今のところマーク機能は機能していない）

今のところはここまで。todoリストを作った時点でCドライブ直下にファイルが作られ、日にちごとに新しいファイルが追加される。

（問題点は山積みだけれど、区切りのいいところまでは開発をした）



今後の展望==========================

将来的には現実のカレンダーに近い形のUIにしたい。
具体的にはトップウィンドウにカレンダーを表示させて、クリック、もしくはカーソルを合わせると、その日のtodoリストや評価が見えたり、
マーク機能を使って思い出になった日付は強調表示させたい。


また問題点として、
・このままでは評価してコメントしたものが、アプリ上から見えない（Cドライブ直下のファイルを見ることになる）
・また、todoリストがきちんと設定されたかどうか確認がスムーズに行えていない。（更新のためにいちいち再起動する必要がある）
・前日や前々日のファイルにアプリ上からアクセスできない
・コア機能（機能があるものを作ること）の開発を優先したので、デザインを全く考慮していない
などがある


時間をかければ、上記の問題は必ず解決できると確信しているが、

現状、pythonのコマンドの使い方の確認検索に時間を食って、使ったことをまとめきれてないこと（多分忘れて、また検索ばかりに時間が取られるのでまとめたい）
日本企業全体としてJavaやCなど使っている、就活事情や、クラスでコードを書く関係上、ほかの言語でも検討してみたいこと、
などを考え、一回ここで開発を止めることにする。



ここまでやってきて==========================

完全に思い込みだろうけど、pythonの力不足を感じた。

書き方や処理が悪いのか、画面のリロード問題はすぐに解決できなかったり、変数に連番をつけて生成することが出来ない。
検索してもtkinterの独特の仕様が完全に理解できなかったなどを不便に感じた。

ここまでクラスを書くならjavaを使ったほうが、デザインの面や、参考資料の量などの点からいいのかなと感じた。
（もちろん参考資料が多くても理解できなければ意味がないが...)


また先にも言ったように、大まかな命令系統やpythonの仕様がうろ覚えのために、いちいち様々なサイトを巡ったので時間がかかった。
未来の自分が見るように一か所に情報をまとめておくのがいいかもしれない。







