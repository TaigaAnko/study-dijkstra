# 環境構築とテスト実行ガイド

## 1. **`requirements.txt` によるパッケージのインストール**

`requirements.txt` ファイルに必要なパッケージとそのバージョンを記載します。以下は例です：

```plaintext
pytest==7.4.2
numpy==1.24.4
```

パッケージのインストール方法は以下の通りです：

### **手順**
1. 必要なモジュールをリストアップした `requirements.txt` をプロジェクトルートに配置。
2. 次のコマンドでパッケージをインストール：

```bash
pip install -r requirements.txt
```

---

## 2. **`venv` による仮想環境のセットアップ**

仮想環境を使うことで、グローバル環境を汚さずにプロジェクトごとに依存関係を管理できます。

### **Windows の場合**

1. 仮想環境を作成：
   ```bash
   python -m venv venv
   ```

2. 仮想環境を有効化：
   ```bash
   venv\Scripts\activate
   ```

3. 仮想環境を無効化：
   ```bash
   deactivate
   ```

---

### **Mac/Linux の場合**

1. 仮想環境を作成：
   ```bash
   python3 -m venv venv
   ```

2. 仮想環境を有効化：
   ```bash
   source venv/bin/activate
   ```

3. 仮想環境を無効化：
   ```bash
   deactivate
   ```

---

## 3. **`pytest` の利用方法**

### **テストコードの例**

以下のようなテストコードが `test/app/demo.py` にあると仮定します：

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

### **`pytest` コマンドの実行方法**

1. 仮想環境を有効化（手順は上記参照）。
2. プロジェクトルートで次のコマンドを実行：

```bash
pytest test/app/demo.py
```

### **結果の確認**

- 成功したテストは緑色の `.` として表示。
- 失敗したテストは赤色で詳細なエラーメッセージが表示されます。

---

## まとめ

1. 仮想環境をセットアップし、必要な依存関係をインストール。
2. テストコードを記述し、`pytest` を使って実行。
3. 仮想環境を活用することで、プロジェクト環境を簡単に管理できます。

必要に応じて、追加のスクリプトやコマンドを `Makefile` や `shell` スクリプトで管理すると便利です。
