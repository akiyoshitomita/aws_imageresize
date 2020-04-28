#!/bin/bash

# Lambdaにアップロード用 ZIPファイルの作成

# =================================================================
#    設定情報
# =================================================================

TmpDir=tmp
SrcDir=src
PipLibFile=piplib.zip
OutFile=function.zip
RequirementFile=requirements.txt

# =================================================================
#    メイン処理 
# =================================================================

# pip3のライブラリファイルを作成
#  * 存在する場合は再作成しない
if [ ! -f ${PipLibFile} ] 
then
  # ワークディレクトリの初期化
  if [ -d ${TmpDir} ] 
    then
    rm -rf ${TmpDir} 
  fi
  mkdir ${TmpDir}

  pip3 install -r ${RequirementFile} -t ${TmpDir}
  cd ${TmpDir}
  zip -r9 ../${PipLibFile} ./
  cd .. 
fi

cp -f ${PipLibFile} ${OutFile}
cd ${SrcDir}
  zip -g -r ../${OutFile} ./
cd ..
