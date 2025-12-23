# 🔄 Zendrix Softwares - Git Workflow Architecture

[![Git](https://img.shields.io/badge/Git-Workflow-red?logo=git)](https://github.com)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com)
[![DevOps](https://img.shields.io/badge/DevOps-Best%20Practices-green)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Intellipaat](https://img.shields.io/badge/Course-DevOps%20Certification-orange)](https://www.intellipaat.com)

> **Professional Git Flow implementation for managing monthly product releases on the 25th of every month**

---

## 📋 Project Overview

**Git Flow implementation** for Zendrix Softwares to manage **monthly product releases on the 25th** of every month. This repository demonstrates a professional branching strategy for scheduled release cycles.

## 🎯 Business Requirement

- **Monthly releases** on the 25th of every month
- **Structured workflow** for feature development
- **Quick hotfix** capability for production issues
- **Maintainable** and **scalable** release process

## 🏗️ Git Workflow Architecture

<img width="1215" height="1041" alt="diagram-export-12-22-2025-6_50_41-PM" src="https://github.com/user-attachments/assets/536f4376-98b6-47e9-b38d-61075f34798d" />

## 📅 Release Schedule

| Release | Date | Version | Status |
|---------|------|---------|--------|
| January | 25th | v1.0.0 | ✅ Released |
| February | 25th | v1.1.0 | ✅ Released |
| March | 25th | v1.2.0 | 🔄 In Progress |

## 🔧 Branch Structure

| Branch Type | Purpose | Naming Convention |
|-------------|---------|-------------------|
| `main` | Production code | `main` |
| `develop` | Development integration | `develop` |
| `feature/*` | New features | `feature/feature-name` |
| `release/*` | Release preparation | `release/vX.X-mmm-dd` |
| `hotfix/*` | Emergency fixes | `hotfix/bug-description` |

## 🚀 Monthly Release Process

### Days 1-20: Feature Development
```bash
git checkout -b feature/new-feature develop
# ... develop feature ...
git checkout develop
git merge feature/new-feature
```

### Day 20: Create Release Branch
```bash
git checkout -b release/v1.0-jan-25 develop
# ... QA testing ...
```

### Day 25: Deploy to Production
```bash
git checkout main
git merge release/v1.0-jan-25
git tag -a v1.0.0 -m "January 25 release"
git push origin main --tags
```

## 🔥 Hotfix Process
```bash
# Create hotfix from main
git checkout -b hotfix/critical-bug main

# Fix and merge
git checkout main
git merge hotfix/critical-bug
git tag -a v1.0.1 -m "Critical hotfix"

# Merge back to develop
git checkout develop
git merge hotfix/critical-bug
```

## 📦 Project Structure
```
zendrix-product-release/
├── src/
│   ├── app.py              # Main application
│   ├── auth.py             # Authentication
│   ├── payment.py          # Payment gateway
│   ├── notifications.py    # Notifications
│   └── analytics.py        # Analytics
├── tests/
│   └── test_app.py        # Unit tests
├── docs/
│   └── architecture.md    # Documentation
├── VERSION.txt            # Current version
└── README.md             # This file
```

## 🎓 Learning Context

**Course:** DevOps Certification Training  
**Institution:** Intellipaat  
**Module:** Git Workflow & Version Control  
**Case Study:** Monthly Release Management

## 📊 Key Features Implemented

✅ User Authentication System  
✅ Payment Gateway Integration  
✅ Notification System  
✅ Analytics Dashboard  
✅ Automated Release Process  
✅ Hotfix Management

## 📞 Contact

**Himanshu Nitin Nehete**  
📧 Email: himanshunehete2025@gmail.com  
🔗 LinkedIn: [My Profile](https://www.linkedin.com/in/himanshu-nehete/)

---

⭐ **Star this repository** if it helped you understand Git workflow architecture!

**Keywords**: Git, Git Flow, DevOps, Release Management, Version Control, Branching Strategy
