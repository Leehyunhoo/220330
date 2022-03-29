from google.cloud import storage

def upload_to_bucket(blob_name, path_to_file, bucket_name):
    """ Upload data to a bucket(아까 만들었던 저장소)"""

    # Explicitly use service account credentials by specifying the private key
    # file.

    storage_client = storage.Client.from_service_account_json(
        'melodic-subject-345211-d2ac075627d0.json')
    #print(buckets = list(storage_client.list_buckets())

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)
    
    #접근권한 public 으로 설정
    blob.make_public()
    
    #파일 url 만들어주기
    url = blob.public_url
    #returns a public url
    return url
#parameter순서대로 공유된 파일이름, 로컬저장된파일 경로, 저장소 이름 
# url =upload_to_bucket("4.PNG","4.PNG","example_220325")
# print(url)