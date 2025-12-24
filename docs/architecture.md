# Zendrix Softwares - Git Workflow Architecture

## System Overview

**Purpose:** Structured Git workflow for managing monthly product releases on the 25th of every month.

**Key Goals:**
- Monthly scheduled releases (25th of each month)
- Parallel feature development
- Production stability
- Rapid hotfix deployment

---

## Architecture Diagram

```
main (production)
  ↑
  ├── release/v1.0-jan-25  (QA & deployment)
  ├── hotfix/critical-bug   (emergency fixes)
  ↑
develop (integration)
  ↑
  ├── feature/user-auth
  ├── feature/payment-gateway
  ├── feature/notifications
  └── feature/analytics
```

---

## Branch Structure

### 1. Main Branch
- **Purpose:** Production code only
- **Merges From:** release/*, hotfix/*
- **Rules:** 
  - Never commit directly
  - Always tagged with versions (v1.0.0)
  - Deploy after merge

### 2. Develop Branch
- **Purpose:** Integration of all features
- **Merges From:** feature/*, hotfix/*
- **Merges To:** release/*
- **Rules:**
  - All features merge here first
  - Deploy to staging environment

### 3. Feature Branches
- **Naming:** `feature/<feature-name>`
- **Lifespan:** Temporary
- **Process:**
  - Create from develop
  - Develop feature
  - Merge back to develop
  - Delete after merge

**Examples:**
- `feature/user-authentication`
- `feature/payment-gateway`
- `feature/notification-system`

### 4. Release Branches
- **Naming:** `release/v<version>-<month>-<day>`
- **Lifespan:** 5 days (Day 20-25)
- **Process:**
  - Create from develop on Day 20
  - QA testing only (no new features)
  - Merge to main on Day 25
  - Merge back to develop
  - Delete after merge

**Examples:**
- `release/v1.0-jan-25`
- `release/v1.1-feb-25`

### 5. Hotfix Branches
- **Naming:** `hotfix/<bug-description>`
- **Lifespan:** Hours to 1 day
- **Process:**
  - Create from main
  - Fix critical bug
  - Merge to main AND develop
  - Tag with patch version (v1.0.1)
  - Delete after merge

**Examples:**
- `hotfix/critical-auth-bug`
- `hotfix/payment-failure`

---

## Monthly Release Timeline

| Days | Phase | Activity |
|------|-------|----------|
| 1-19 | Development | Create and complete features in parallel |
| 20 | Release Prep | Create release branch from develop |
| 21-24 | QA Testing | Bug fixes only, comprehensive testing |
| 25 | Deployment | Merge to main, tag, deploy to production |
| 26-28 | Monitoring | Post-release observation and planning |

---

## Workflow Processes

### Feature Development
```bash
git checkout develop
git pull origin develop
git checkout -b feature/new-feature
# ... develop feature ...
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
# ... create PR to develop ...
git checkout develop
git merge feature/new-feature
git branch -d feature/new-feature
```

### Release Process (Day 20-25)
```bash
# Day 20: Create release branch
git checkout develop
git checkout -b release/v1.0-jan-25

# Day 21-24: QA fixes only
git commit -m "Fix bug found in QA"

# Day 25: Deploy
git checkout main
git merge release/v1.0-jan-25
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin main --tags

# Merge back to develop
git checkout develop
git merge release/v1.0-jan-25
git branch -d release/v1.0-jan-25
```

### Hotfix Process
```bash
# Create hotfix from production
git checkout main
git checkout -b hotfix/critical-bug

# Fix and test
git commit -m "Fix critical bug"

# Deploy to production
git checkout main
git merge hotfix/critical-bug
git tag -a v1.0.1 -m "Hotfix v1.0.1"
git push origin main --tags

# Sync with develop
git checkout develop
git merge hotfix/critical-bug
git branch -d hotfix/critical-bug
```

---

## Version Numbering

**Format:** `vMAJOR.MINOR.PATCH`

- **MAJOR:** Breaking changes (v2.0.0)
- **MINOR:** New features, monthly releases (v1.1.0, v1.2.0)
- **PATCH:** Bug fixes, hotfixes (v1.0.1, v1.0.2)

**Examples:**
- `v1.0.0` - January 25 release (initial)
- `v1.0.1` - Emergency hotfix
- `v1.1.0` - February 25 release
- `v1.2.0` - March 25 release

---

## Technical Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Version Control** | Git | Source code management |
| **Repository Hosting** | GitHub | Remote repository and collaboration |
| **Backend** | Python Flask | Application server |
| **Database** | PostgreSQL | Data persistence |
| **Deployment** | AWS EC2 | Production hosting |
| **CI/CD** | GitHub Actions | Automated testing and deployment |

---

## Branch Protection Rules

### Main Branch
- ✅ Require pull request reviews (2 approvers)
- ✅ Require status checks to pass
- ✅ Require branches to be up to date
- ✅ No direct commits
- ✅ No force pushes

### Develop Branch
- ✅ Require pull request reviews (1 approver)
- ✅ Require status checks to pass
- ⚠️ Allow direct commits (for urgent fixes)

---

## Best Practices

### Commit Messages
```bash
# Good
git commit -m "Add user authentication module"
git commit -m "Fix login validation bug"

# Bad
git commit -m "changes"
git commit -m "fixed stuff"
```

### Branch Naming
```bash
# Good
feature/user-authentication
hotfix/critical-payment-bug
release/v1.0-jan-25

# Bad
fix-stuff
new-branch
test123
```

### Merge Strategy
- Use **merge commits** for feature → develop (preserve history)
- Use **squash merge** for cleanup (optional)
- Never rebase public branches

---

## Emergency Procedures

### Production Down
1. Create hotfix branch from main immediately
2. Fix issue with minimal changes
3. Test in staging if time permits
4. Merge to main and deploy
5. Merge to develop to sync

### Release Day Issues
1. If critical bug found: Delay release, fix in release branch
2. If minor bug: Document as known issue, fix in next cycle
3. If deployment fails: Rollback using previous tag

### Rollback Procedure
```bash
# Identify last stable version
git tag

# Checkout previous version
git checkout v1.0.0

# Deploy to production
# or
# Revert merge commit
git revert -m 1 <merge-commit-hash>
```

---

## Key Metrics

**Success Indicators:**
- ✅ On-time releases (25th of every month)
- ✅ Zero production incidents during deployment
- ✅ Hotfix deployment < 2 hours
- ✅ Feature development time < 15 days
- ✅ QA cycle completion in 5 days

---

## Contact & Support

**Project Owner:** Himanshu Nitin Nehete  
**Email:** himanshunehete2025@gmail.com   

**For Questions:**
- Architecture decisions: Contact DevOps team
- Feature planning: Contact Product team
- Technical issues: Create GitHub issue

---

**Last Updated:** December 2025 
**Version:** 1.0  
**Status:** Active
