# ☁️ AWS Resource Auditor & Cost Optimizer

An automated infrastructure auditing tool built with Python and Boto3. This project identifies "zombie" resources—unused or unattached AWS assets that incur unnecessary costs—providing IT teams with actionable data for cloud cost optimization.

##  The Problem
In cloud environments, it is common for developers to leave EBS volumes unattached, forget to release Elastic IPs, or leave old snapshots active long after they are needed. These "zombie" resources can account for 10-30% of a company's cloud waste.

##  Key Features
* **EBS Volume Audit:** Scans for "Available" (unattached) EBS volumes.
* **Stale Snapshot Detection:** Identifies snapshots that are no longer associated with active volumes.
* **Elastic IP (EIP) Tracking:** Reports unassociated EIPs to prevent idle-address charges.
* **Cost Efficiency:** Provides a consolidated view of potential savings in the terminal.

## Tech Stack
* **Language:** Python 3.x
* **AWS SDK:** Boto3
* **Authentication:** AWS CLI / IAM Roles

## How It Works
The script utilizes the `boto3` library to query the AWS EC2 and EBS APIs. It iterates through the specified region, filters for resources with a status of 'available' or 'unassociated', and prints a detailed report of the Resource ID and its current state.

## Prerequisites
* **AWS CLI** configured with `aws configure`.
* **IAM Permissions:** Access to `ec2:DescribeVolumes`, `ec2:DescribeSnapshots`, and `ec2:DescribeAddresses`.

