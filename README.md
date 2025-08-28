# TalentVibe - AI-Powered Resume Analysis Platform

A comprehensive resume analysis platform that uses AI to evaluate candidates against job descriptions, with smart auto-scaling and CI/CD pipeline.

## 🚀 Features

- **AI-Powered Analysis**: GPT-4 integration for intelligent resume evaluation
- **Multi-Format Support**: PDF, DOCX, and DOC file processing
- **Smart Auto-Scaling**: Automatic start/stop based on usage patterns
- **CI/CD Pipeline**: Automated testing and deployment
- **Interview Management**: Schedule and track candidate interviews
- **Real-time Processing**: Background processing with progress tracking

## 🏗️ Architecture

- **Frontend**: React.js with modern UI/UX
- **Backend**: Flask (Python) with SQLAlchemy ORM
- **Database**: SQLite (production-ready for small-medium scale)
- **Deployment**: AWS Elastic Beanstalk
- **Auto-Scaling**: Custom Lambda functions with CloudWatch monitoring
- **CI/CD**: GitHub Actions with automated testing and deployment

## 📋 Prerequisites

- Python 3.11+
- Node.js 18+
- AWS Account with Elastic Beanstalk access
- GitHub Account

## 🛠️ Local Development Setup

### 1. Clone the Repository
```bash
git clone <your-github-repo-url>
cd talentvibe-cicd
```

### 2. Backend Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Run the application locally
python application.py
```

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

### 4. Build Frontend for Production
```bash
# From the frontend directory
npm run build

# Copy build to root directory
cp -r build ../frontend_build
```

## 🚀 CI/CD Pipeline

### Automated Workflow

The project uses GitHub Actions for continuous integration and deployment:

1. **Code Push**: Every push to main/master branch triggers the pipeline
2. **Testing**: Automated tests run to ensure code quality
3. **Frontend Build**: React app is built and optimized
4. **Deployment**: Application is automatically deployed to AWS Elastic Beanstalk
5. **Health Check**: Automated verification that the deployment was successful

### Pipeline Stages

```
Code Push → Test → Build Frontend → Deploy to EB → Health Check → Success
```

### Manual Deployment

You can also trigger deployments manually:
1. Go to GitHub repository
2. Navigate to Actions tab
3. Select "Deploy TalentVibe to AWS Elastic Beanstalk"
4. Click "Run workflow"

## 🔧 Configuration

### Environment Variables

Set these in GitHub repository secrets:

- `AWS_ACCESS_KEY_ID`: AWS access key for deployment
- `AWS_SECRET_ACCESS_KEY`: AWS secret key for deployment

### AWS Configuration

- **Region**: us-east-2
- **Application**: TalentVibe-deployment
- **Environment**: TalentVibe-deployment-env

## 📊 Auto-Scaling Features

### Smart Activity Detection
- Monitors real user activity via CloudWatch metrics
- Automatically starts environment when accessed
- Stops after 30 minutes of inactivity
- Business hours awareness (9 AM - 6 PM UTC)

### Cost Optimization
- **Running Cost**: ~$50-80/month
- **Stopped Cost**: ~$1-2/month
- **Savings**: 85-95% when not in use

## 🧪 Testing

### Run Tests Locally
```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=./ --cov-report=html

# Run specific test file
python -m pytest test_application.py
```

### Test Coverage
The CI/CD pipeline includes:
- Unit tests
- Integration tests
- Code linting (flake8)
- Security scanning

## 📁 Project Structure

```
talentvibe-cicd/
├── .github/workflows/     # CI/CD configuration
├── frontend/              # React application
├── backend/               # Python backend
├── .ebextensions/         # Elastic Beanstalk config
├── .platform/             # Platform hooks
├── application.py         # Main Flask application
├── requirements.txt       # Python dependencies
├── test_application.py    # Test suite
└── README.md             # This file
```

## 🔄 Development Workflow

### Making Changes
1. **Edit in Cursor**: Make your code changes
2. **Test Locally**: Run tests to ensure everything works
3. **Commit Changes**: `git add . && git commit -m "Description"`
4. **Push to GitHub**: `git push origin main`
5. **Automatic Deployment**: CI/CD pipeline handles the rest

### Branch Strategy
- `main`: Production-ready code
- `develop`: Development branch (optional)
- Feature branches: For new features

## 🚨 Troubleshooting

### Common Issues

1. **Deployment Fails**
   - Check GitHub Actions logs
   - Verify AWS credentials
   - Ensure all required files are present

2. **Tests Fail**
   - Run tests locally first
   - Check for missing dependencies
   - Verify Python/Node.js versions

3. **Auto-Scaling Issues**
   - Check CloudWatch logs
   - Verify Lambda function permissions
   - Monitor SNS notifications

### Getting Help

1. Check the GitHub Actions logs for detailed error messages
2. Review the AWS CloudWatch logs for application issues
3. Check the auto-scaling Lambda function logs

## 📈 Monitoring

### Health Checks
- Application health: `/api/health`
- Auto-scaling status: CloudWatch metrics
- Deployment status: GitHub Actions

### Logs
- Application logs: AWS CloudWatch
- CI/CD logs: GitHub Actions
- Auto-scaling logs: Lambda function logs

## 🔐 Security

- AWS credentials are stored as GitHub secrets
- Environment variables are properly configured
- No sensitive data in code repository
- Regular security updates via dependency management

## 📝 License

This project is proprietary software. All rights reserved.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

---

**TalentVibe** - Making recruitment smarter with AI-powered analysis and intelligent infrastructure management.
# CI/CD Test - Wed Aug 27 09:30:44 EDT 2025
