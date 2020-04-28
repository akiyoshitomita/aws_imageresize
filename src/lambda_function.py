import json
import boto3
import urllib.parse
import os.path
from PIL import Image

def lambda_handler(event, context):
    
    # S3 へアップロード
    bucket_name = 'atomita-test'
    s3 = boto3.resource('s3')
    s3_cli = boto3.client('s3')
    print(event)
    
    try:
        # s3に接続
        print('Getting bucket name and uploaded file path ...')
        input_bucket = event['Records'][0]['s3']['bucket']['name']
        input_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'],encoding='utf-8')
        
        #                                        
        print('Getting file name and extension...')
        root, ext = os.path.splitext(input_key.replace("upload/",""))
        
        uploadFileName = 'small/' + root + ext
        filepath = '/tmp/' + root + ext
        filepath2 = '/tmp/' + root + '_2' + ext

        metafile = '/tmp/' + root + 'json'
        
        # S3からファイルを/tmpにダウンロード
        print('Getting bucket object...')
        bucket = s3.Bucket(input_bucket)
        print('Downloading s3 file')
        bucket.download_file(input_key, filepath)
        
        # ファイルサイズ変更
        print('open image')
        img = Image.open(filepath)
        print('resize image')

        img_resize = img.resize((100,100))
        print('filepath2')
        img_resize.save(filepath2)
        # S3へファイルをアップロード
        #f = open(metafile,'w')
        #f.write(json.dumps(event))
        #f.close()
        print('Uploaded file')
        print(filepath2)
        print(uploadFileName)
        bucket.upload_file(filepath2, uploadFileName)
        

    except Exception as e:
        print (e)
        print ('Opps, Error happened')
        raise e
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'event': event
    }

