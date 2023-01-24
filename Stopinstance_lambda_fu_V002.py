import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=event.get('region', 'ap-southeast-1')) # set region 
    instance_id = event.get('instance_id', 'i-00000000000000000') # get instance_id from event
    if not instance_id:
        raise ValueError("instance_id is missing in event")
    try:
        ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
        print(f'Instance with ID {instance_id} has been stopped.')
    except botocore.exceptions.ClientError as e:
        raise ValueError("Failed to stop instance: %s" % e)
