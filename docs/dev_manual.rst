開発マニュアル
==============

プロジェクト構成
----------------

* `docs/` Sphinxドキュメント
* `gcpug_shonan_vol3_example/` Djangoプロジェクト
* `LICENSE` ライセンス情報
* `README.md` README
* `wercker.yml` `Wercker <http://wercker.com/>`_ 用設定ファイル

開発に必要な環境
----------------

* Python 3.5.x

Sphinxでドキュメントを生成する場合は `blockdiagの依存パッケージ <http://blockdiag.com/ja/blockdiag/introduction.html#id2>`_ もインストールすること。

インストール
------------

`git clone` の後、以下の手順でPythonパッケージをインストールする::

    cd /path/to/gcpug_shonan_vol3_example/gcpug_shonan_vol3_example/
    pip install -r requirements/local.txt
    python manage.py migrate
    python manage.py runserver

Sphinxでドキュメント生成する場合は以下も実行する::

    pip install -r requirements/docs.txt
