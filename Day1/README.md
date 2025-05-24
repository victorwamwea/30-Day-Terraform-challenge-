# Day 1 - S3 Bucket with Best Practices

## Overview
This Terraform configuration creates an S3 bucket following AWS best practices and security guidelines.

## Features
- Versioning enabled
- Proper resource tagging
- Input validation
- No public access
- Uses variables for configuration

## Prerequisites
- AWS CLI configured
- Terraform >= 1.0.0
- AWS credentials with appropriate permissions

## Usage

1. Initialize Terraform:
```bash
terraform init
```

2. Review the plan:
```bash
terraform plan -var="bucket_name=your-unique-bucket-name"
```

3. Apply the configuration:
```bash
terraform apply -var="bucket_name=your-unique-bucket-name"
```

## Variables

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| aws_region | AWS region to deploy resources | string | us-east-1 | no |
| bucket_name | Name of the S3 bucket to create | string | n/a | yes |
| environment | Environment name (dev, staging, prod) | string | dev | no |

## Outputs

| Name | Description |
|------|-------------|
| bucket_name | Name of the created bucket |
| bucket_arn | ARN of the created bucket |
| bucket_region | Region where the bucket was created |
| versioning_status | Versioning status of the bucket |

## Security Considerations
- No public access allowed
- Versioning enabled for data protection
- Resource tagging for better management
- Input validation for bucket naming conventions

## Testing
- Validated with `terraform fmt`
- Validated with `terraform validate`
- Tested resource creation and destruction
- Verified tag application

## Author
test-user

## License
MIT
