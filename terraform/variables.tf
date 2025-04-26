variable "aws_region" {
  description = "AWS region for all resources"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Name of the project for resource naming"
  type        = string
  default     = "aws-devops-assignment"
}

variable "ec2_instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "ec2_key_name" {
  description = "Name of the EC2 key pair to use"
  type        = string
  default     = null
}

variable "allowed_ip" {
  description = "IP address allowed to connect to the EC2 instance"
  type        = string
  default     = "0.0.0.0/0"  # Replace with your actual IP
}

variable "s3_bucket_name" {
  description = "Name of the S3 bucket for static website hosting"
  type        = string
  default     = null  # Will be auto-generated if not provided
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
  default     = "s3-event-logger"
}

variable "tags" {
  description = "Tags to be applied to all resources"
  type        = map(string)
  default = {
    Environment = "Dev"
    Project     = "AWS DevOps Assignment"
  }
} 