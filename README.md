# AWS DevOps Assignment

This repository contains solutions for the AWS DevOps assignment including infrastructure as code, scripting, and CI/CD pipeline.

## Project Structure

- `/terraform` - Contains Terraform configuration files for infrastructure provisioning
- `/scripts` - Contains Python scripts for AWS SDK interaction and data analysis
- `/lambda` - Contains AWS Lambda functions and tests
- `/docs` - Contains detailed documentation for each task
- `.github/workflows` - Contains CI/CD pipeline configuration

## Task 1: AWS

Detailed documentation for AWS resources setup is available in [docs/task1_aws.md](docs/task1_aws.md).

1. **S3 Bucket**

   - Creation and configuration for static website hosting
   - Public access configuration
   - **S3 Endpoint URL**: [http://devops-assignment-lokanath.s3-website-us-east-1.amazonaws.com/](http://devops-assignment-lokanath.s3-website-us-east-1.amazonaws.com/)
   - Screenshot:
     ![S3 Bucket Configuration](screenshots/s3-bucket-config.png)

2. **EC2 Instance**

   - Setup with Amazon Linux
   - Apache web server installation
   - Simple HTML page hosting
   - **EC2 Public URL**: [http://52.202.214.202/](http://52.202.214.202/) (Note: This link will only work when the EC2 instance is running)
   - Screenshot:
     ![EC2 Web Server](screenshots/ec2-webserver.png)

3. **Security Group Configuration**

   - HTTP traffic allowance
   - IP restriction for security
   - Screenshot:
     ![Security Group Configuration](screenshots/security-group-config.png)

4. **AWS Lambda**
   - S3 event-triggered function
   - CloudWatch logging integration
   - Screenshot:
     ![Lambda Function Configuration](screenshots/lambda-function.png)

## Task 2: Scripting

Python scripts that utilize AWS SDK (boto3) to:

1. **list_s3_buckets.py**

   - Lists all S3 buckets in your AWS account
   - Displays object count in a specified bucket
   - Usage: `python scripts/list_s3_buckets.py --bucket <bucket-name>`

2. **csv_analyzer.py**

   - Analyzes a CSV file (name, age, grade)
   - Prints students with grades above a threshold
   - Usage: `python scripts/csv_analyzer.py scripts/sample_students.csv --threshold 80`

3. **SDK Documentation References**
   - See [docs/sdk_documentation.md](docs/sdk_documentation.md) for links to the AWS SDK documentation

## Task 3: CI/CD

GitHub Actions workflow configured to:

1. Run tests on Python scripts
2. Validate Terraform configurations
3. Build and package Lambda functions
4. Deploy to AWS (when configured)

## Task 4: Infrastructure as Code

Terraform scripts for automating AWS infrastructure:

1. **AWS Resources**

   - EC2 instance with security group
   - S3 bucket for static website
   - Lambda function with CloudWatch integration
   - IAM roles and policies

2. **Usage**
   ```bash
   cd terraform
   terraform init
   terraform plan
   terraform apply
   ```

## Cost Analysis

The [cost analysis document](docs/cost_analysis.md) provides a detailed breakdown of the annual AWS cost for this setup, including:

- EC2 Instance costs
- S3 storage and request costs
- Lambda function costs
- CloudWatch logs costs

## Setup Instructions

1. **Prerequisites**

   - AWS CLI configured with appropriate credentials
   - Python 3.9 or higher
   - Terraform 1.0.0 or higher

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS Credentials**

   ```bash
   aws configure
   ```

4. **Deploy Infrastructure with Terraform**

   ```bash
   cd terraform
   terraform init
   terraform apply
   ```

5. **Run Python Scripts**
   ```bash
   python scripts/list_s3_buckets.py --bucket <your-bucket-name>
   python scripts/csv_analyzer.py scripts/sample_students.csv --threshold 75
   ```

## Testing

1. **Run Python Tests**

   ```bash
   pytest scripts/test_csv_analyzer.py
   pytest lambda/test_s3_event_logger.py
   ```

2. **Validate Terraform**
   ```bash
   cd terraform
   terraform validate
   ```
