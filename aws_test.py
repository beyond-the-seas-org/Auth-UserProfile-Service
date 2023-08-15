import boto3

s3 = boto3.resource('s3')

# for bucket in s3.buckets.all():
#     print(bucket.name)

# Upload a new file
data = open('Profile.jpg', 'rb')
s3.Bucket('beyond-the-seas-storage').put_object(Key='Profile Photo', Body=data)
