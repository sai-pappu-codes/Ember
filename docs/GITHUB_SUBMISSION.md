# GitHub Submission Checklist (Cafe Fausse)

## Create Private Repository
1. Create a new private repo on GitHub (suggested name: cafe-fausse)
2. Initialize without any files (we already have a local repo)

## Add Remote & Push
```bash
cd /Users/mihai/cafe-fausse
# Option A: HTTPS (prompts for token on first push)
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/<your-username>/cafe-fausse.git
git push -u origin main
```

## Add Collaborator (quantic-grader)
1. GitHub → Repo → Settings → Collaborators → Add people
2. Add username: `quantic-grader`

## Required Documents
- README.md: already includes local run instructions
- AI_TOOLS_USAGE.md: summary of AI assistance
- docs/PGADMIN_SETUP.md: pgAdmin step-by-step
- docs/LOCAL_SETUP.md: quick local start and verify steps

## Optional CLI Alternative
Install GitHub CLI (gh) and run:
```bash
brew install gh
gh auth login
cd /Users/mihai/cafe-fausse
gh repo create <your-username>/cafe-fausse --private --source=. --remote=origin --push
# Add collaborator
gh api -X PUT \
  repos/<your-username>/cafe-fausse/collaborators/quantic-grader \
  -f permission=push
```

## Deliverable
- Provide the private repo URL in your submission document
- Ensure the grader account has access before submitting
