#!/bin/bash

# Lambdaにアップロード用 ZIPファイルの作成

# =================================================================
#    設定情報
# =================================================================

TmpDir=tmp
SrcDir=src
OutFile=function.zip
RequirementFile=requirements.txt

# =================================================================
#    メイン処理 
# =================================================================

# ワークディレクトリの初期化
if [ -d ${TmpDir} ] 
then
  rm -rf ${TmpDir} 
fi
# ワークディレクトリの作成
mkdir ${TmpDir}
cp -r ${SrcDir}/* ${TmpDir}/ 

# pip3からライブラリのインストール
pip3 install -r ${RequirementFile} -t ${TmpDir}

cd ${TmpDir}
zip -r9 ../${OutFile} ./
cd ..
