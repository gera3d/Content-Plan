# Content Strategy Dashboard - AI Coding Guidelines

## Project Overview
**Purpose:** Interactive content strategy command center for Gera Yeremin's custom software development business  
**Tech Stack:** Python 3.x, Streamlit, pandas, plotly, pytrends  
**Main Application:** `dashboard.py` (3398 lines) - multi-tab Streamlit dashboard  
**Primary User:** Gera Yeremin (gera3d@gmail.com) - Digital Marketing & Software Architecture specialist at 57 Seconds

## Most important:
**Assistant to copilot:** OK I just loaded chatgpt codex cli into the terminal He is going to act as your Assistant. He will take the role of Master on a topic but still your assistant. If he is not running make sure you start him first.

## Architecture Patterns

### Streamlit Dashboard Structure
- **9-Tab Layout:** Strategy Overview, Interactive Tools, Content Calendar, Content Opportunities, Strategy, Content Review, Voice Guide, Tools, Distribution Channels
- **Session State:** Use `st.session_state.researcher` for KeywordResearcher instance (initialized once)
- **Page Config:** Wide layout, collapsed sidebar, custom title/icon, minimal CSS (hide MainMenu/footer)
- **Component Style:** Native Streamlit components preferred over custom HTML/CSS

### Data Integration
- **Keyword Research:** `KeywordResearcher` class from `keyword_research.py` using Google Trends API (pytrends)
- **Platform Tracking:** JSON file at `platform_accounts.json` with 11 distribution channels (Medium, LinkedIn, YouTube, etc.)
- **Results Storage:** Save keyword analysis to `keyword_results.json` with timestamps

### File Naming Conventions
- **Backup files:** `*_backup.py`, `*_old.py`, `*_v2.html` (keep for version history)
- **Interactive tools:** `*-calculator.html`, `*-tracker.html`, `*-graphics.html`
- **Documentation:** `*-guide.md`, `*_README.md`, `brand-profile.md`, `writing-voice-guide.md`

## Development Workflows

### Running the Dashboard
```bash
# Activate virtual environment first
source .venv/bin/activate

# Run dashboard (opens at http://localhost:8501)
streamlit run dashboard.py

# Test Streamlit installation
streamlit hello
```

### Keyword Research Workflow
```python
# Import and initialize
from keyword_research import KeywordResearcher
researcher = KeywordResearcher()

# Analyze keywords (max 5 at a time for Google Trends)
keywords = ['custom software development', 'business applications']
results = researcher.analyze_keywords(keywords, timeframe='today 12-m')

# Save results with timestamp
researcher.save_results(results, 'keyword_results.json')
```

### Platform Account Management
- **JSON Schema:** Each platform has: `email`, `status`, `profile_url`, `setup_date`, `notes`, `action_needed`
- **Status Values:** `needs_verification`, `active`, `setup_required`
- **Dashboard Integration:** Tab 9 reads `platform_accounts.json` and displays status with color coding

## Code Style & Conventions

### Python Patterns
- **Imports:** Group by standard library, third-party, local modules
- **Docstrings:** Use triple-quoted strings for module/function documentation
- **Error Handling:** Graceful handling for missing files/API failures
- **Data Frames:** pandas for tabular data, plotly for visualizations

### Streamlit Best Practices
- **Layout:** Use `st.columns()` for side-by-side content
- **Metrics:** `st.metric()` for KPIs with delta indicators
- **Charts:** `st.plotly_chart()` for interactive graphs (scatter plots, line charts)
- **User Feedback:** `st.info()`, `st.success()`, `st.warning()` for contextual messages
- **Data Display:** `st.dataframe()` with `column_config` for custom formatting

### Interactive HTML Tools
- **Self-contained:** All CSS/JS inline, no external dependencies
- **localStorage:** Auto-save user input for persistence
- **Export:** JSON download functionality for data portability
- **Mobile-friendly:** Responsive design, touch-optimized

## Brand Voice Guidelines

### Gera Yeremin's Writing Style
- **Tone:** Direct, conversational, no BS - "professional without being corporate"
- **Openings:** Skip formalities, lead with the main point
  - ✅ "Your team is drowning in spreadsheets."
  - ❌ "In today's rapidly evolving business landscape..."
- **Structure:** Short paragraphs, bullet points, scannable content
- **Language:** Simple words, active voice, conversational rhythm

### Content Focus Areas
1. **Custom Software Development:** Review management, CRM, workflow automation, BI tools
2. **Target Keywords:** custom software development, custom business software, bespoke software (6 primary + 5 niche)
3. **Distribution Channels:** 11 platforms (Medium DA:95, LinkedIn DA:99, Dev.to DA:85, etc.)
4. **Positioning:** "Local + Strategic + Marketing-savvy developer who understands business ROI"

## Common Tasks & Commands

### Adding New Platforms
1. Update `platform_accounts.json` with new entry
2. Add display logic in `dashboard.py` Tab 9
3. Update setup guides: `setup_accounts_guide.md`, `account_setup_tracker.html`

### Creating Interactive Tools
1. Follow `roi-calculator.html` or `account_setup_tracker.html` as templates
2. Include: inline CSS, localStorage persistence, JSON export, responsive design
3. Add link in dashboard Tab 2 "Interactive Tools"

### Keyword Analysis Updates
1. Modify keyword lists in `analyze_content_keywords.py` or `dashboard.py`
2. Run analysis: `researcher.analyze_keywords(keywords)`
3. Update dashboard charts/tables with new data

### Environment Setup
```bash
# Create virtual environment
python3 -m venv .venv

# Install dependencies
pip install streamlit pandas plotly pytrends

# Verify installation
streamlit --version
```

## File Organization
- **Main App:** `dashboard.py` (single source of truth)
- **Keyword Tools:** `keyword_research.py`, `analyze_content_keywords.py`
- **Data Files:** `*.json` (platform_accounts, keyword_results, schema-markup, research)
- **Guides:** `*.md` (brand-profile, writing-voice-guide, setup guides)
- **Interactive Tools:** `*.html` (ROI calculator, account tracker, quote graphics)
- **Backups:** Keep old versions (dashboard_old.py, roi-calculator-backup.html)

## Testing & Validation
- **Manual Testing:** Run `streamlit run dashboard.py` after changes
- **Data Validation:** Check JSON files are valid before dashboard reads them
- **Browser Testing:** Test HTML tools in Chrome/Safari for localStorage support
- **Keyword API:** pytrends may rate-limit - add delays between requests if needed

## Troubleshooting
- **Streamlit Issues:** Check `.venv` is activated, reinstall with `pip install --upgrade streamlit`
- **Google Trends API:** pytrends may block rapid requests - add `time.sleep(2)` between calls
- **Missing Data:** Verify JSON files exist and have valid schema
- **Chart Rendering:** Ensure plotly installed: `pip install plotly`

## Quick Reference
- **Dashboard Tabs:** 1=Strategy, 2=Tools, 3=Calendar, 4=Opportunities, 5=Strategy, 6=Review, 7=Voice, 8=Tools, 9=Distribution
- **Primary Email:** gera3d@gmail.com (all platforms)
- **Target Audience:** SMB owners needing custom software (review systems, CRM, automation)
- **Content Calendar:** 12 weeks, focus on custom business software keywords
- **SEO Strategy:** Low-competition keywords with rising queries (custom business software, review management)
