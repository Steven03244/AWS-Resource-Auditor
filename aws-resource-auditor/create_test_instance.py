import boto3


def launch_test_instance():
    ec2 = boto3.client('ec2', region_name='us-east-1')

    print("🚀 Launching a test EC2 instance (Free Tier)...")

    # We use a 'Magic' ID that always finds the latest 2026 Amazon Linux image
    latest_ami = 'resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64'

    try:
        instance = ec2.run_instances(
            ImageId=latest_ami,
            MinCount=1,
            MaxCount=1,
            InstanceType='t3.micro',  # Free Tier eligible
        )

        instance_id = instance['Instances'][0]['InstanceId']
        print(f"✅ Success! Created Instance: {instance_id}")
        print("💡 Note: This instance has NO tags. It is a perfect target for your Auditor.")

    except Exception as e:
        print(f"❌ Error launching instance: {e}")


if __name__ == "__main__":
    launch_test_instance()