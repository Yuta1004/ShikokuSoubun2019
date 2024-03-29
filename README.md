# ShikokuSoubun2019

四国地区総合文化祭2019 ミニプロコンの色々をまとめるところです

## Board

![](https://github.com/Yuta1004/ShikokuSoubun2019/workflows/Validate%20the%20Board/badge.svg)

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

### 当日実際に使った盤面

<table>
    <tr>
        <th>試合</th>
        <th>サイズ</th>
        <th>エージェント数</th>
        <th>公開盤面</th>
        <th>非公開盤面</th>
        <th>備考</th>
    </tr>
    <tr>
        <td>予行演習</td>
        <td>10 x 10</td>
        <td>3</td>
        <td>official/A-1.json</td>
        <td>official/A-1.json</td>
        <td></td>
    </tr>
    <tr>
        <td>予選</td>
        <td>10 x 10</td>
        <td>3</td>
        <td>official/A-3.json</td>
        <td>kishida/Qualifying1.json</td>
        <td></td>
    </tr>
    <tr>
        <td>エキシビション</td>
        <td>10 x 10</td>
        <td>3</td>
        <td>official/A-2.json</td>
        <td>MoriGod_maketile/yosenM.json</td>
        <td>一番盛り上がった</td>
    </tr>
    <tr>
        <td>3, 5位決定戦</td>
        <td>14 x 14</td>
        <td>5</td>
        <td>official/C-2.json</td>
        <td>kishida/SemiFinal2.json</td>
        <td></td>
    </tr>
    <tr>
        <td>決勝</td>
        <td>20 x 20</td>
        <td>8</td>
        <td>official/F-1.json</td>
        <td>kishida/Final1.json</td>
        <td></td>
    </tr>
</table>

### 必要盤面

**旧案**  
ミニプロコン当日はサイズを合わせて良い感じにして使う

<table>
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
<td>2</td>
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
<td>14 x 14</td>
<td>5</td>
<td>2</td>
<td></td>
</tr>
<tr>
<td>3位決定戦</td>
<td>18 x 18</td>
<td>6</td>
<td>2</td>
<td>マイナスを密集させる、など難しい盤面</td>
</tr>
<tr>
<td>決勝</td>
<td>20 x 20</td>
<td>8</td>
<td>2</td>
<td>特徴的で盛り上がりそうな盤面</td>
</tr>
</table>

