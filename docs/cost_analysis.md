# AWS Cost Analysis

The following is an estimated annual cost breakdown for the AWS services used in this project. Prices are based on AWS pricing as of 2023 in the US East (N. Virginia) region.

## EC2 Instance

- **Instance Type**: t2.micro (Free tier eligible for 12 months)
- **Operating System**: Amazon Linux 2
- **Usage**: 24/7 (8,760 hours per year)
- **On-Demand Pricing**: $0.0116 per hour
- **Annual Cost**: $0.0116 × 8,760 = **$101.62 per year**
- **Free Tier**: 750 hours per month for 12 months (if eligible)
- **Annual Cost with Free Tier (first year)**: $0 (assuming usage stays within free tier limits)

## S3 Bucket (Static Website)

- **Storage**: Assuming 1 GB of storage
- **Standard Storage**: $0.023 per GB per month
- **Annual Storage Cost**: $0.023 × 1 GB × 12 months = **$0.276 per year**
- **Data Transfer**: Assuming 10 GB of data transfer out per month
- **Data Transfer Cost**: $0.09 per GB (first 10 TB) × 10 GB × 12 months = **$10.80 per year**
- **PUT/COPY/POST/LIST Requests**: Assuming 10,000 requests per month
- **Request Cost**: $0.005 per 1,000 requests × 10 × 12 months = **$0.60 per year**
- **GET Requests**: Assuming 100,000 requests per month
- **GET Cost**: $0.0004 per 1,000 requests × 100 × 12 months = **$4.80 per year**
- **Free Tier**: 5 GB storage, 20,000 GET requests, 2,000 PUT requests per month for 12 months (if eligible)
- **Annual S3 Cost with Free Tier (first year)**: Approximately **$0** (assuming usage stays within free tier limits)

## Lambda Function

- **Invocations**: Assuming 100,000 invocations per month
- **Compute Time**: Assuming 1 second average duration with 128 MB memory
- **Pricing**: $0.20 per 1 million requests, $0.0000166667 per GB-second
- **Annual Invocation Cost**: $0.20 × 0.1 × 12 = **$0.24 per year**
- **Annual Compute Cost**: $0.0000166667 × 0.128 × 1 second × 100,000 × 12 = **$2.56 per year**
- **Free Tier**: 1 million invocations and 400,000 GB-seconds per month (perpetual)
- **Annual Lambda Cost with Free Tier**: **$0** (assuming usage stays within free tier limits)

## CloudWatch Logs

- **Data Ingestion**: Assuming 5 GB per month
- **Data Storage**: Assuming 5 GB per month
- **Pricing**: $0.50 per GB ingested, $0.03 per GB stored
- **Annual Ingestion Cost**: $0.50 × 5 GB × 12 months = **$30.00 per year**
- **Annual Storage Cost**: $0.03 × 5 GB × 12 months = **$1.80 per year**
- **Free Tier**: 5 GB of logs data ingestion, 5 GB of logs data storage (perpetual)
- **Annual CloudWatch Cost with Free Tier**: **$0** (assuming usage stays within free tier limits)

## Security Group & IAM

- These services are provided at no additional cost.

## Total Estimated Annual Cost

- **Without Free Tier**: $101.62 (EC2) + $16.46 (S3) + $2.80 (Lambda) + $31.80 (CloudWatch) = **$152.68 per year**
- **With Free Tier (first year)**: **$0** (assuming all usage stays within free tier limits)
- **With Free Tier (after first year)**: $101.62 (EC2) + $16.46 (S3) + $0 (Lambda) + $0 (CloudWatch) = **$118.08 per year**

## Cost Optimization Recommendations

1. **EC2 Instance**:

   - Consider using Spot Instances for non-critical workloads (up to 90% savings)
   - Use Auto Scaling to adjust capacity based on demand
   - Implement instance scheduling to turn off during non-business hours

2. **S3 Storage**:

   - Implement lifecycle policies to archive or delete unused objects
   - Use S3 Intelligent-Tiering for infrequently accessed objects

3. **Lambda**:

   - Optimize Lambda function code to reduce execution time
   - Appropriately size Lambda memory to match workload needs

4. **CloudWatch Logs**:
   - Implement log filtering to reduce the amount of data stored
   - Set appropriate retention periods for logs
