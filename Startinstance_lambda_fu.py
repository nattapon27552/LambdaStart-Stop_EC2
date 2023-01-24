import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    instance_id = event.get('instance_id', 'i-00000000000000000') # Default value for instance_id
    region = event.get('region', 'ap-southeast-1') # Default value for region ap-southeast-1
    # Starting the instance
    ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
    print(f'Instance with ID {instance_id} has been started.')
