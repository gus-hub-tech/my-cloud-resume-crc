# My Cloud Resume CRC

A **serverless cloud resume website** built following the [Cloud Resume Challenge](https://cloudresumechallenge.dev/). This project demonstrates modern cloud architecture using AWS services to create a scalable, cost-effective personal resume site with a visitor counter.

## 🏗️ Architecture

**Serverless Architecture Components:**
- **Frontend**: Static HTML/CSS/JS hosted on AWS S3 + CloudFront
- **Backend**: AWS Lambda function (Python) for visitor counter API
- **Database**: DynamoDB for visitor count storage
- **API**: API Gateway to expose Lambda endpoints
- **DNS**: Route 53 for custom domain (optional)
- **Security**: IAM roles and policies for secure access

## 🚀 Features

- **Fully Serverless**: No servers to manage, pay only for usage
- **Responsive Design**: Modern CSS with gradient backgrounds and animations
- **Visitor Counter**: Real-time visitor tracking using Lambda + DynamoDB
- **Professional Layout**: Clean resume format with skills matrix
- **Cloud-Native**: Built for AWS deployment from day one
- **Cost Effective**: Minimal AWS costs (likely under $1/month)

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Python 3.9+ (AWS Lambda)
- **Database**: AWS DynamoDB (NoSQL)
- **Hosting**: AWS S3 + CloudFront CDN
- **API**: AWS API Gateway (REST)
- **Infrastructure**: AWS IAM, Route 53

## 📁 Project Structure

```
my-cloud-resume-crc/
├── README.md                           # Project documentation
├── index.html                          # Main resume HTML page
├── style.css                           # Styling and responsive design
└── components/
    ├── dynamodb.json                   # DynamoDB table configuration
    ├── lambda_fucntion.py             # Python Lambda function for visitor counter
    └── visitor-counter.js             # Frontend JS for API calls
```

## 🚀 Deployment Guide

### Prerequisites
- AWS Account with appropriate permissions
- AWS CLI configured
- Basic knowledge of AWS services

### Step 1: Static Website (S3 + CloudFront)
1. Create S3 bucket for static hosting
2. Upload HTML, CSS, JS files
3. Configure bucket for static website hosting
4. Set up CloudFront distribution for CDN
5. Configure custom domain (optional)

### Step 2: Serverless Backend
1. **DynamoDB**: Create table using `components/dynamodb.json`
2. **Lambda**: Deploy `components/lambda_fucntion.py`
3. **API Gateway**: Create REST API endpoint
4. **IAM**: Configure roles and policies
5. **CORS**: Enable cross-origin requests

### Step 3: Frontend Integration
- Update `components/visitor-counter.js` with your API Gateway URL
- Test visitor counter functionality

## 🔧 Local Development

**Note**: This is a serverless application designed for cloud deployment. Local testing requires:

```bash
# Clone repository
git clone https://github.com/gus-hub-tech/my-cloud-resume-crc.git
cd my-cloud-resume-crc

# Start local server (required for CORS)
python3 -m http.server 8080

# Visit: http://localhost:8080
```

**Important**: Visitor counter won't work locally without AWS backend deployment.

## 🌐 Live Demo

**Production URL**: [main.d28epes9lsan4o.amplifyapp.com](https://main.d28epes9lsan4o.amplifyapp.com/)

## 💰 Cost Estimation

**Monthly AWS Costs** (estimated):
- S3 Storage: ~$0.02
- CloudFront: ~$0.10
- Lambda: ~$0.00 (free tier)
- DynamoDB: ~$0.00 (free tier)
- API Gateway: ~$0.00 (free tier)
- **Total**: < $1.00/month

## 🔒 Security Features

- IAM least-privilege access
- HTTPS enforced via CloudFront
- CORS properly configured
- No hardcoded credentials
- DynamoDB encryption at rest

## 🤝 Contributing

Contributions welcome! Please open issues or pull requests for:
- Bug fixes
- Feature enhancements
- Documentation improvements
- Architecture optimizations

---

**Built for the Cloud Resume Challenge**  
*Demonstrating serverless architecture and AWS cloud skills*