# aws_imageresize
AWS S3+Lambdaを利用したイメージのリサイズを実行するスクリプト

# 事前準備

python3のインストール

````
$ sudo yum install python3
````

# lambdaにアップするzipファイルの作成

````
$ ./create.sh
````

# AWSにアップロード

* awsコマンドを事前に設定しておき、以下のコマンドを実行

````
aws lambda update-function-code --function-name [your lambda function name] --zip-file fileb://function.zip
````

# 追伸

s3のプロパティからイベントのPUTにlambdaを割り当てる
lambda関数にs3のアクセス権をもったロールを割り当てる
s3にuploadとsmallのディレクトリを作成
uploadにサイズの大きいJpegファイルをアップロードするとsmallに小さなサイズの画像ができます。
