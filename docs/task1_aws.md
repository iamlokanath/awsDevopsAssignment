# Task 1: AWS

## 1. S3 Bucket Creation and Configuration

### Steps to create an S3 bucket for static website hosting:

1. **Login to AWS Console**:

   - Navigate to https://aws.amazon.com/console/
   - Log in with your AWS account credentials

2. **Navigate to S3 Service**:

   - From the AWS Management Console, search for "S3" or find it under Services

3. **Create a New Bucket**:

   - Click "Create bucket"
   - Enter a unique bucket name: `devops-assignment-lokanath` (replace with your unique name)
   - Select a Region (e.g., us-east-1)
   - Uncheck "Block all public access"
   - Acknowledge that making the bucket public might result in public data access
   - Keep other settings as default
   - Click "Create bucket"

4. **Configure for Static Website Hosting**:

   - Open the newly created bucket
   - Navigate to the "Properties" tab
   - Scroll to find "Static website hosting"
   - Click "Edit"
   - Select "Enable"
   - Set "Index document" to "index.html"
   - Set "Error document" to "error.html" (optional)
   - Save changes

5. **Set Bucket Policy for Public Access**:

   - Go to the "Permissions" tab
   - Click on "Bucket Policy"
   - Add the following policy (replace `BUCKET_NAME` with your actual bucket name, i.e: `devops-assignment-lokanath` for my bucket):

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "PublicReadGetObject",
         "Effect": "Allow",
         "Principal": "*",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::BUCKET_NAME/*"
       }
     ]
   }
   ```

   - Click "Save changes"

6. **Upload Test Files**:

   - Go to the "Objects" tab
   - Click "Upload"
   - Upload a simple index.html file for testing
   - Click "Upload"

7. **Verify Website Configuration**:
   - Go back to "Properties" tab
   - Scroll to "Static website hosting"
   - Note down the "Bucket website endpoint" URL (for me it is: `http://devops-assignment-lokanath.s3-website-us-east-1.amazonaws.com/`)
   - Open this URL in a browser to verify the static website is working

### ✅ Status: Completed

The S3 bucket has been successfully set up and configured for static website hosting. The website is now accessible at:

**S3 Endpoint URL**: [http://devops-assignment-lokanath.s3-website-us-east-1.amazonaws.com/](http://devops-assignment-lokanath.s3-website-us-east-1.amazonaws.com/)

## 2. EC2 Instance Setup

### Steps to set up an EC2 instance with a web server:

1. **Navigate to EC2 Service**:

   - From the AWS Management Console, search for "EC2" or find it under Services
   - Click on "Launch Instance"

2. **Configure the EC2 Instance**:

   - Name your instance (e.g., "devOpsServer")
   - Select "Amazon Linux 2 AMI" as the Amazon Machine Image (AMI)
   - Choose "t2.micro" as the instance type (free tier eligible)
   - Create a new key pair or select an existing one (required for SSH)(i have created a key pair, i.e: devOpsPair)
   - Download the key pair file (.pem) if creating a new one

3. **Configure Security Group**:

   - Create a new security group
   - Add a rule to allow SSH traffic (port 22) from your IP
   - Add a rule to allow HTTP traffic (port 80) from your IP
   - Name it "WebServerSG"
   - Click "Launch Instance"

4. **SSH into the Instance**:

   - Wait for the instance to be in "running" state
   - Note the public IP address or DNS
   - Open a terminal on your local machine
   - Use SSH to connect (replace with your details):

   ```
   ssh -i "devOpsPair.pem" ec2-user@ec2-52-202-214-202.compute-1.amazonaws.com
   ```

5. **Install Web Server (Apache)**:

   - Update the system packages:

   ```bash
   sudo yum update -y
   ```

   - Install Apache web server:

   ```bash
   sudo yum install httpd -y
   ```

   - Start and enable the Apache service:

   ```bash
   sudo systemctl start httpd
   sudo systemctl enable httpd
   ```

6. **Create a Simple HTML Page**:

   - Navigate to the web server's document root:

   ```bash
   cd /var/www/html
   ```

   - Create an index.html file:

   ```bash
   sudo bash -c 'cat > index.html << EOF
   <!DOCTYPE html>
   <html>
   <head>
       <title>My EC2 Web Server</title>
       <style>
           body {
               font-family: Arial, sans-serif;
               margin: 40px;
               text-align: center;
           }
           h1 {
               color: #333;
           }
       </style>
   </head>
   <body>
       <h1>Hello from EC2!</h1>
       <p>This is a simple web page hosted on Amazon EC2 using Apache.</p>
       <p>Instance time: <span id="time"></span></p>
       <script>
           document.getElementById("time").textContent = new Date().toLocaleString();
       </script>
   </body>
   </html>
   EOF'
   ```

7. **Verify Web Server**:
   - Open a web browser and enter your EC2 instance's public IP address
   - You should see the webpage you created

Public IP address: `52.202.214.202` (The EC2 instance will only be accessible when it is running)

### ✅ Status: Completed

The EC2 instance has been successfully set up with Apache web server running a simple HTML page. The web page is accessible at:

**EC2 Public URL**: [http://52.202.214.202/](http://52.202.214.202/) (Note: This link will only work when the EC2 instance is running)

## 3. Security Group Configuration

### Steps to configure security group for your EC2 instance:

1. **Navigate to EC2 Security Groups**:

   - In the EC2 console, click on "Security Groups" under "Network & Security" in the left sidebar
   - Select the security group associated with your EC2 instance ("WebServerSG")

2. **Edit Inbound Rules**:

   - Click on the "Inbound rules" tab
   - Click "Edit inbound rules"

3. **Configure HTTP Access**:

   - If not already present, add a new rule:
     - Type: HTTP
     - Protocol: TCP
     - Port range: 80
     - Source: Custom, and enter your public IP address followed by /32 (e.g., 203.0.113.1/32)
     - Description: "HTTP access from my IP"

4. **Configure SSH Access**:

   - Edit the existing SSH rule (or add if not present):
     - Type: SSH
     - Protocol: TCP
     - Port range: 22
     - Source: Custom, and enter your public IP address followed by /32 (e.g., 203.0.113.1/32)
     - Description: "SSH access from my IP"

5. **Save Rules**:
   - Click "Save rules"

### ✅ Status: Completed

Security groups have been properly configured to allow HTTP access from specific IP addresses for improved security.

## 4. AWS Lambda Function

Creating a Lambda function to log S3 bucket events:

1. **Navigate to Lambda Service**:

   - From the AWS Management Console, search for "Lambda" or find it under Services
   - Click "Create function"

2. **Configure Lambda Function**:

   - Choose "Author from scratch"
   - Function name: "S3EventLogger"
   - Runtime: Python 3.9
   - Architecture: x86_64
   - Execution role: Create a new role with basic Lambda permissions
   - Click "Create function"

3. **Configure S3 Trigger**:

   - In the Function overview, click "Add trigger"
   - Select "S3" as the trigger
   - Select your S3 bucket
   - Event type: "All object create events"
   - Acknowledge the recursive invocation warning if needed
   - Click "Add"

4. **Add Lambda Code**:

   - Replace the default code in the code editor with the following:

   ```python
   import json
   import logging

   # Configure logging
   logger = logging.getLogger()
   logger.setLevel(logging.INFO)

   def lambda_handler(event, context):
       # Log the full event
       logger.info('Received S3 event: ' + json.dumps(event))

       # Extract and log key details
       for record in event.get('Records', []):
           bucket = record.get('s3', {}).get('bucket', {}).get('name', 'unknown')
           key = record.get('s3', {}).get('object', {}).get('key', 'unknown')
           event_name = record.get('eventName', 'unknown')

           logger.info(f'Event: {event_name}, Bucket: {bucket}, Key: {key}')

       return {
           'statusCode': 200,
           'body': json.dumps('Event processed successfully!')
       }
   ```

   - Click "Deploy"

5. **Test the Function**:
   - Upload a new object to your S3 bucket
   - Navigate to CloudWatch Logs in the AWS Console
   - Find the log group for your Lambda function (/aws/lambda/S3EventLogger)
   - Verify that the event details are being logged

### ✅ Status: Completed

AWS Lambda function has been successfully created and configured to log S3 bucket events to CloudWatch.
