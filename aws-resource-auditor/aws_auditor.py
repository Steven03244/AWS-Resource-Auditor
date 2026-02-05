import boto3


def audit_ec2_tags():

    ec2 = boto3.client('ec2', region_name='us-east-1')

    print("🔍 Starting AWS Resource Audit...")

    # 1. gets all instances
    response = ec2.describe_instances()

    instance_count = 0
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_count += 1
            instance_id = instance['InstanceId']
            tags = instance.get('Tags', [])

            # 2. checks for the 'Project' tag
            has_project_tag = any(t['Key'] == 'Project' for t in tags)

            if not has_project_tag:
                print(f"⚠️ Alert: Instance {instance_id} is missing a 'Project' tag!")

                # 3. applies a fix-it tag
                ec2.create_tags(
                    Resources=[instance_id],
                    Tags=[{'Key': 'Project', 'Value': 'Unknown-Audit-Required'}]
                )
                print(f"✅ Fixed: Added 'Unknown-Audit-Required' tag to {instance_id}")
            else:
                print(f"👍 Instance {instance_id} is correctly tagged.")

    if instance_count == 0:
        print("Empty Account: No instances found to audit. Create one in the console to test!")


if __name__ == "__main__":
    audit_ec2_tags()