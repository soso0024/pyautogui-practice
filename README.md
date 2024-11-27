# PyAutoGUI Practice - YouTube 自動操作

## 概要

このプロジェクトは、PyAutoGUI を使用して YouTube での操作を自動化する Python スクリプトです。
今回は、指定した勉強用 BGM プレイリストへの自動アクセスを実現します。

https://github.com/user-attachments/assets/4fa62bba-157d-4549-af1d-fed61a1a01ea

## 機能

- ブラウザで YouTube を自動で開く
- プレイリストページへの自動移動
- 特定の勉強用 BGM プレイリストの自動選択

## 必要条件

- Python 3.x
- PyAutoGUI

## インストール方法

```bash
pip install pyautogui
```

## 使用方法

1. スクリプトを実行する

```bash
python youtube_automation.py
```

2. スクリプトが自動的に以下の操作を行います：
   - ブラウザのアドレスバーにフォーカスを移動
   - YouTube.com を開く
   - プレイリストページに移動
   - 指定した BGM プレイリストを選択

## 重要な注意事項

1. **座標の調整**

   - スクリプト内の座標値（x, y）は、あなたの画面解像度とブラウザウィンドウのサイズに応じて調整が必要です
   - 現在の座標値：
     - アドレスバー: (400, 50)
     - プレイリストボタン: (150, 390)
     - BGM プレイリスト: (450, 590)

2. **待機時間**
   - ネットワーク速度に応じて、`sleep()`の値を調整してください
   - 現在の待機時間：
     - ページ読み込み: 5 秒
     - プレイリスト読み込み: 2 秒

## カスタマイズ方法

1. 座標の確認方法：

```python
import pyautogui
print(pyautogui.position())  # マウスカーソルの現在位置を表示
```

2. 待機時間の調整：

```python
sleep(秒数)  # 必要に応じて秒数を変更
```
