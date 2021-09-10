# 8.4.1 SQL
# SQL文は大きく分けて2つのカテゴリがある
# DDL（データ定義言語 Data Definition Language）
#   テーブルやデータベースの作成、削除、制約、許可などの処理
# DML（データ操作言語 Data Manipulation Language）
# データの挿入、選択。更新。削除などの処理

# DDL
CREATE DATABASE dbname
USE dbname
DROP DATABASE dbname
CREATE TABLE tbname (coldefs)
DROP TABLE tbname
TRUNCATE TABLE tbname

# DML
# CRUD
# C(Create)
#   INSERT文を使った作成
INSERT INTO tbname VALUES()
# R(Read)
#   SELECT文を使った読み出し
SELECT * FROM tbname
SELECT cols FROM tbname
SELECT cols FROM tbname WHERE condition
# U(Update)
#   UPDATE文を使った更新
UPDATE tbname SET col = value WHERE condition
# D(Delete)
#   DELETE文を使った削除
DELETE FROM tbname WHERE condition
