from __future__ import print_function
import time
import boto3
import json
transcribe = boto3.client('transcribe')
job_name = "Jstechno"
job_uri = "s3://jstech1/test.mp4"
transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': job_uri},
    MediaFormat='mp4',
    LanguageCode='en-US'
)
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
        print("Not ready yet...")
        time.sleep(5)
        print(status)
        file = open('text.txt','a')
        file.write(TranscriptFileUri)
        file.close()
        
       