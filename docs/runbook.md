---
layout: default
title: Runbook
nav_order: 17
---

# Site Maintenance Runbook

Operational procedures for maintaining the course website.

## Quick Reference

| Task | Command/Action |
|:-----|:---------------|
| Build site locally | `bundle exec jekyll serve` |
| Check build status | [GitHub Actions](https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/actions) |
| View deployment | [GitHub Pages Settings](https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/settings/pages) |

## Local Development

### Initial Setup

```bash
# Clone repository
git clone https://github.com/Digital-AI-Finance/agentic-artificial-intelligence.git
cd agentic-artificial-intelligence/docs

# Install Ruby dependencies
bundle install

# Start local server
bundle exec jekyll serve

# Site available at http://localhost:4000/agentic-artificial-intelligence/
```

### Common Issues

**Bundle install fails**
```bash
# Update bundler
gem install bundler
bundle update --bundler
bundle install
```

**Gems missing on Windows**
```bash
# Add required tools
ridk install 3
bundle install
```

**Port already in use**
```bash
bundle exec jekyll serve --port 4001
```

## Deployment

### Automatic Deployment

The site deploys automatically when changes are pushed to `main`:

1. Push triggers GitHub Actions workflow
2. Jekyll builds the site
3. GitHub Pages deploys the build
4. Site updates within 2-5 minutes

### Check Deployment Status

1. Go to [Actions tab](https://github.com/Digital-AI-Finance/agentic-artificial-intelligence/actions)
2. Find the latest "pages build and deployment" workflow
3. Check for success/failure

### Manual Rebuild

If needed, trigger a rebuild:

1. Go to Actions tab
2. Select "pages build and deployment"
3. Click "Run workflow"

## Content Updates

### Adding a New Week

1. **Add week data** to `docs/_data/weeks.yml`:
```yaml
- number: X
  title: "Week Title"
  description: "Description"
  folder: "LXX_Topic_Name"
  status: "draft"
  topics:
    - Topic 1
    - Topic 2
  learning_objectives:
    - Objective 1
  notebooks: []
  papers: []
```

2. **Create week page** at `docs/weeks/week-X.md`:
```markdown
---
layout: week
week_number: X
title: "Week X: Title"
---

Additional content here.
```

3. **Push changes** and verify deployment

### Adding Glossary Terms

Edit `docs/_data/glossary.yml`:

```yaml
- term: "New Term"
  definition: "Clear definition."
  related: ["Related Term"]
  week: X
```

### Updating Papers

Edit `docs/papers.md` following the existing format.

## Troubleshooting

### Build Failures

**Check the error in Actions**:
1. Go to failed workflow run
2. Expand the failing step
3. Look for error message

**Common fixes**:
- Liquid syntax error: Check for unclosed tags
- YAML error: Validate YAML syntax
- Missing file: Check file paths in includes

### Page Not Found (404)

1. Verify file exists in correct location
2. Check `nav_order` in front matter
3. Ensure `layout: default` is set
4. Clear browser cache

### Styles Not Updating

1. Clear browser cache (Ctrl+Shift+R)
2. Check SCSS syntax in `_sass/color_schemes/custom.scss`
3. Rebuild locally to see errors

### Search Not Working

1. Search is client-side (Lunr.js)
2. Check JavaScript console for errors
3. Verify search is enabled in `_config.yml`

## Backups

### What to Back Up

- `docs/` folder (all content)
- `_config.yml` (site configuration)
- `_data/` folder (structured data)

### Backup Procedure

The repository itself serves as backup. For additional safety:

```bash
# Create local archive
git archive --format=zip HEAD docs/ > course-site-backup.zip
```

## Monitoring

### Site Health Checks

- **Uptime**: GitHub Pages has 99.9% uptime
- **Build status**: Check Actions tab for failures
- **Broken links**: Run `bundle exec htmlproofer ./_site` locally

### Analytics (if enabled)

- Check Plausible dashboard for traffic
- Review popular pages and notebooks
- Monitor Colab link clicks

## Emergency Procedures

### Site Down

1. Check [GitHub Status](https://www.githubstatus.com/)
2. If GitHub Pages issue, wait for resolution
3. If build failure, revert to last working commit:
```bash
git revert HEAD
git push
```

### Accidental Deletion

1. Files are in git history
2. Restore with:
```bash
git checkout HEAD~1 -- path/to/file
git commit -m "Restore accidentally deleted file"
git push
```

### Security Issue

1. Remove sensitive content immediately
2. Force push if needed to remove from history:
```bash
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/file" \
  --prune-empty --tag-name-filter cat -- --all
git push origin --force --all
```

3. Rotate any exposed credentials
4. Notify affected parties

## Scheduled Maintenance

### Weekly

- [ ] Check for build failures
- [ ] Review open issues/discussions
- [ ] Verify Colab links work

### Monthly

- [ ] Update dependencies (`bundle update`)
- [ ] Check for broken external links
- [ ] Review analytics for issues

### Semester Start

- [ ] Update semester in `_config.yml`
- [ ] Reset week statuses to "draft"
- [ ] Archive previous semester projects
- [ ] Test all notebooks with current API versions

### Semester End

- [ ] Mark all weeks as "complete"
- [ ] Archive student projects
- [ ] Update paper list with new publications
- [ ] Create semester summary

---

*Last updated: December 2024*
