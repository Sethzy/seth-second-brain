---
type: raw_capture
source_type: pasted
title: "Sunder sync: keywords.md"
url: "file:///Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-instagram-scraper/references/keywords.md"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-instagram-scraper/references/keywords.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: ".claude/skills/sales-instagram-scraper/references/keywords.md"
sha256: "c5a5db122eeb87d6098514c2f5229b53e1dc3fec800012523e7d117b2685f57e"
duplicate_of: ""
---

# Sunder sync: keywords.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-instagram-scraper/references/keywords.md`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/.claude/skills/sales-instagram-scraper/references/keywords.md

Duplicate of existing source-map entry: `none`

## Capture Text

# Default Keyword Lists

## Base Keywords (20)

Role-type keywords that identify decision makers and high-value professionals:

founder, CEO, co-founder, owner, author, coach, consultant, speaker, creator, director, entrepreneur, artist, designer, photographer, therapist, realtor, broker, instructor, trainer, advisor

## Niche Keywords (200)

Organized by vertical. Edit `generate_searches.py` DEFAULT_NICHE_KEYWORDS or pass `--config` JSON to customize.

### Business & Finance (15)
Finance, Fintech, Venture Capital, Private Equity, Real Estate, Investing, Crypto, Banking, Insurance, Wealth Management, Accounting, Tax, Mortgage, Commercial Real Estate, PropTech

### Health & Wellness (20)
MedSpa, Wellness, Fitness, Yoga, Nutrition, Mental Health, Dermatology, Dental, Chiropractic, Physical Therapy, Skincare, Plastic Surgery, Functional Medicine, Holistic Health, Pilates, CrossFit, Personal Training, Health Coach, Dietitian, Spa

### Tech & SaaS (18)
SaaS, AI, Machine Learning, Startup, Tech, Software, Cloud, Cybersecurity, Data, DevOps, Mobile App, Web3, Blockchain, IoT, Robotics, AR VR, Automation, API

### Creative & Media (15)
Photography, Videography, Podcast, Content Creator, Influencer, Brand Strategy, Graphic Design, Interior Design, Architecture, Fashion, Jewelry, Art, Music, Film, Animation

### Professional Services (15)
Law, Attorney, Legal, HR, Recruiting, Staffing, Management Consulting, Strategy, Marketing Agency, PR, Advertising, SEO, Social Media, Branding, Copywriting

### E-commerce & Retail (15)
E-commerce, DTC, Retail, Wholesale, Dropshipping, Amazon FBA, Shopify, CPG, Food & Beverage, Wine, Coffee, Restaurant, Catering, Bakery, Brewery

### Education & Training (10)
Education, Online Course, Coaching, Mentoring, Tutoring, EdTech, Leadership, Executive Coach, Life Coach, Business Coach

### Construction & Trades (10)
Construction, Contractor, HVAC, Plumbing, Electrical, Roofing, Landscaping, Home Builder, Renovation, Solar

### Automotive & Transportation (10)
Automotive, Car Dealer, Auto Repair, Fleet, Logistics, Trucking, Shipping, Supply Chain, EV, Transportation

### Hospitality & Travel (10)
Hotel, Hospitality, Travel, Tourism, Vacation Rental, Airbnb, Event Planning, Wedding, Catering, Resort

### Nonprofit & Impact (8)
Nonprofit, Philanthropy, Social Impact, Sustainability, Clean Energy, Environmental, Community, Advocacy

### Other High-Value (24)
Pet, Veterinary, Agriculture, Cannabis, Hemp, Manufacturing, Aerospace, Defense, Biotech, Pharma, Medical Device, Telehealth, Senior Care, Childcare, Insurance Agent, Financial Advisor, Wealth, Family Office, Private Banking, Angel Investor, Incubator, Accelerator

## Customization

Create a JSON config file and pass via `--config`:

```json
{
  "base_keywords": ["founder", "CEO", "owner"],
  "locations": ["Miami", "Austin", "Nashville"],
  "niche_keywords": ["MedSpa", "Wellness", "Skincare"]
}
```

This overrides all defaults, producing only 3 x 3 x 3 = 27 queries.
