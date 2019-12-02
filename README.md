# ShikokuSoubun2019

四国地区総合文化祭2019 ミニプロコンの色々をまとめるところです

## Board

### コマンド

```
// 盤面検証(配下ディレクトリ全て)
make test

// 盤面検証(ディレクトリ指定)
make test TARGET_DIR=dir_name
```

### 注意

- 作成した人の名前をディレクトリ名にし、その中に盤面JSONを保存してください
- テストが通過した盤面のみをcommitしてください
- ファイル名は分かりやすいものにしてください
- 編集に関して、特に必要なgit操作はありません
    - 競合を避けるため、管理者以外は他人のディレクトリ・ファイルを操作しないでください
- 盤面JSONはofficial/内のものを参考に作成してください

### 必要盤面

<table border="2" width="700" height="200">
<tr>
<th>試合</th>
<th>サイズ</th>
<th>エージェント数/チーム</th>
<th>必要数</th>
<th>備考</th>
</tr>
<tr>
<td>予選</td>
<td>10 x 10</td>
<td>3</td>
<td>2つ</td>
<td></td>
</tr>
<tr>
<td>敗者復活</td>
<td>10 x 10</td>
<td>3</td>
<td>2</td>
<td></td>
</tr>
<tr>
<td>準決勝</td>
<td>15 x 15</td>
<td>5</td>
<td>2</td>
<td></td>
</tr>
<tr>
<td>3位決定戦</td>
<td>17 x 17</td>
<td>6</td>
<td>2</td>
<td>マイナスを密集させる、など難しい盤面</td>
</tr>
<tr>
<td>決勝</td>
<td>20x20</td>
<td>8</td>
<td>2</td>
<td>特徴的で盛り上がりそうな盤面</td>
</tr>
</table>

