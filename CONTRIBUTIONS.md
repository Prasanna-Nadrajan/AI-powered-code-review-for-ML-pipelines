# Contributing to ML Code Reviewer 🤝

Thank you for your interest in contributing to the ML Code Reviewer! We welcome contributions from developers of all skill levels. This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Types of Contributions](#types-of-contributions)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Submitting Changes](#submitting-changes)
- [Review Process](#review-process)
- [Community](#community)

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct:

- **Be respectful**: Treat everyone with respect, regardless of their experience level, personal background, or opinions
- **Be inclusive**: Welcome newcomers and help them get started
- **Be constructive**: Provide helpful feedback and suggestions
- **Be patient**: Remember that everyone is learning and growing
- **Focus on the code**: Keep discussions technical and objective

## Getting Started

### Prerequisites

Before contributing, ensure you have:

- **Node.js** (v16 or higher)
- **Python** (v3.8 or higher)
- **Git** for version control
- A **GitHub account**
- Basic knowledge of:
  - JavaScript/TypeScript
  - React
  - Python
  - Machine Learning concepts

### Find an Issue

1. **Browse open issues** on GitHub
2. **Look for labels**:
   - `good first issue` - Perfect for newcomers
   - `help wanted` - We need community help
   - `bug` - Something that needs fixing
   - `enhancement` - New features or improvements
   - `documentation` - Documentation improvements

3. **Comment on the issue** to let others know you're working on it

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/Prasanna-Nadrajan/AI-powered-code-review-for-ML-pipelines.git
cd AI_powered_code_review_for_ML_pipelines
```

### 2. Set Up Development Environment

```bash
# Install frontend dependencies
cd client
npm install

# Install backend dependencies
cd ../server
npm install

# Set up Python environment (recommended: virtual environment)
cd ../
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
cd ml_analyzer
pip install -r requirements.txt
```

### 3. Create a Development Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number-description
```

### 4. Start Development Servers

```bash
# Terminal 1: Backend
cd server
npm run dev

# Terminal 2: Frontend
cd client
npm run dev
```

## Contributing Guidelines

### Issue Reporting

When reporting bugs or requesting features:

1. **Search existing issues** first to avoid duplicates
2. **Use clear, descriptive titles**
3. **Provide detailed descriptions** including:
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Environment details (OS, browser, versions)
   - Screenshots or code samples if relevant

### Feature Requests

For new features:

1. **Explain the use case** and why it's valuable
2. **Describe the proposed solution**
3. **Consider alternatives** you've thought about
4. **Be open to discussion** about implementation approaches

## Types of Contributions

### 🐛 Bug Fixes

- Fix existing functionality that isn't working correctly
- Improve error handling and edge cases
- Performance optimizations

### ✨ New Features

- **Frontend Features**:
  - UI/UX improvements
  - New dashboard components
  - Enhanced file upload functionality
  - Better error messaging

- **Backend Features**:
  - New API endpoints
  - Enhanced file processing
  - Better error handling
  - Performance improvements

- **ML Analysis Features**:
  - New analysis rules
  - Support for additional ML libraries
  - Improved pattern detection
  - Enhanced reporting

### 📚 Documentation

- README improvements
- Code comments and docstrings
- API documentation
- Tutorial creation
- Examples and guides

### 🧪 Testing

- Unit tests for components
- Integration tests
- End-to-end testing
- Performance testing
- Test data creation

## Development Workflow

### 1. Planning

- **Discuss major changes** in issues before starting
- **Break down large features** into smaller, manageable pieces
- **Consider backward compatibility**

### 2. Implementation

- **Write clean, readable code**
- **Follow existing patterns** and conventions
- **Add appropriate comments** for complex logic
- **Handle errors gracefully**

### 3. Testing

- **Test your changes thoroughly**
- **Add tests for new functionality**
- **Ensure existing tests still pass**
- **Test across different browsers/environments**

## Coding Standards

### Frontend (React/TypeScript)

```typescript
// Use descriptive component names
interface FileUploadProps {
  onAnalysisStart: () => void;
  onAnalysisComplete: (result: Analysis) => void;
  isLoading: boolean;
}

// Use proper TypeScript types
const FileUpload: React.FC<FileUploadProps> = ({ 
  onAnalysisStart, 
  onAnalysisComplete, 
  isLoading 
}) => {
  // Component logic here
};

// Use meaningful variable names
const [uploadProgress, setUploadProgress] = useState(0);
const [analysisResults, setAnalysisResults] = useState<Analysis[]>([]);
```

### Backend (Node.js/TypeScript)

```typescript
// Use proper error handling
router.post('/analysis', upload.single('file'), async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: 'No file uploaded' });
    }
    
    // Process file
    const results = await analyzeFile(req.file.path);
    res.json(results);
  } catch (error) {
    console.error('Analysis failed:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});
```

### Python (ML Analyzer)

```python
class MLCodeReviewer:
    """
    Analyzes Python ML code for best practices and potential issues.
    
    This class provides comprehensive analysis of machine learning code,
    detecting common pitfalls and suggesting improvements.
    """
    
    def analyze_code(self, code: str) -> List[Dict[str, Any]]:
        """
        Performs comprehensive analysis of the given code.
        
        Args:
            code (str): The Python code to analyze
            
        Returns:
            List[Dict[str, Any]]: List of detected issues
        """
        # Implementation here
        pass
```

### General Guidelines

- **Use consistent indentation** (2 spaces for JS/TS, 4 for Python)
- **Follow naming conventions**:
  - camelCase for JavaScript/TypeScript
  - snake_case for Python
  - PascalCase for React components
- **Keep functions small and focused**
- **Write self-documenting code**
- **Use meaningful commit messages**

## Testing Guidelines

### Frontend Testing

```typescript
// Component tests
import { render, screen, fireEvent } from '@testing-library/react';
import FileUpload from './FileUpload';

describe('FileUpload', () => {
  it('should display upload area', () => {
    render(<FileUpload onAnalysisStart={() => {}} onAnalysisComplete={() => {}} isLoading={false} />);
    expect(screen.getByText(/drag & drop/i)).toBeInTheDocument();
  });
});
```

### Backend Testing

```typescript
// API endpoint tests
import request from 'supertest';
import app from '../src/index';

describe('POST /api/analysis', () => {
  it('should analyze uploaded file', async () => {
    const response = await request(app)
      .post('/api/analysis')
      .attach('file', 'test-files/sample.py')
      .expect(200);
      
    expect(response.body).toHaveProperty('overallScore');
  });
});
```

### Python Testing

```python
import unittest
from analyzer import MLCodeReviewer

class TestMLCodeReviewer(unittest.TestCase):
    def setUp(self):
        self.reviewer = MLCodeReviewer()
    
    def test_detects_scaling_issues(self):
        code = """
        from sklearn.linear_model import LogisticRegression
        model = LogisticRegression()
        """
        issues = self.reviewer.analyze_code(code)
        self.assertTrue(any('scaling' in issue['category'] for issue in issues))
```

## Submitting Changes

### 1. Commit Messages

Use clear, descriptive commit messages:

```bash
# Good examples:
git commit -m "feat: add support for TensorFlow analysis rules"
git commit -m "fix: resolve file upload progress bar issue"
git commit -m "docs: update API documentation with new endpoints"
git commit -m "test: add unit tests for ML analyzer"

# Use conventional commit format:
# type(scope): description
#
# Types: feat, fix, docs, style, refactor, test, chore
```

### 2. Pull Request Process

1. **Update your branch** with the latest main:
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Push your changes**:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request** on GitHub with:
   - **Clear title** describing the change
   - **Detailed description** explaining what and why
   - **Link to related issues**
   - **Screenshots** for UI changes
   - **Testing instructions**

### 3. Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring
- [ ] Performance improvement

## Testing
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] Manual testing completed

## Screenshots (if applicable)
Add screenshots for UI changes

## Related Issues
Closes #123
```

## Review Process

### What to Expect

1. **Automated checks** will run (linting, tests)
2. **Code review** by maintainers
3. **Feedback and suggestions** for improvements
4. **Approval and merge** once ready

### Review Criteria

- **Code quality** and adherence to standards
- **Functionality** works as expected
- **Tests** are adequate and passing
- **Documentation** is updated if needed
- **Performance** impact is acceptable
- **Security** considerations are addressed

## Community

### Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **Discussions**: For questions and general discussion
- **Email**: For private concerns or security issues

### Recognition

Contributors will be:
- **Listed in README** acknowledgments
- **Tagged in releases** for their contributions
- **Invited to join** the maintainers team (for regular contributors)

## Development Tips

### Debugging

```bash
# Backend debugging
cd server
npm run dev  # Watch mode with auto-restart

# Frontend debugging
cd client
npm run dev  # Hot reload development server

# Python debugging
cd ml_analyzer
python -m pdb main.py test_file.py
```

### Useful Commands

```bash
# Lint code
npm run lint

# Format code
npm run format

# Run tests
npm test

# Build for production
npm run build
```

### Common Issues

1. **Port conflicts**: Ensure ports 5001 and 5173 are available
2. **Python path issues**: Use absolute imports in Python modules
3. **CORS errors**: Check frontend/backend URL configuration
4. **File upload limits**: Adjust multer configuration if needed

---

## Thank You! 🎉

Every contribution, no matter how small, helps make ML Code Reviewer better for everyone. We appreciate your time and effort in improving this tool for the ML community!

**Happy coding!** 🚀