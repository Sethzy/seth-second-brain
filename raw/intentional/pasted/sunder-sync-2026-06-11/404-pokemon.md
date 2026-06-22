---
type: raw_capture
source_type: pasted
title: "Sunder sync: pokemon.md"
url: "https://raw.githubusercontent.com/bigfoott/ScrapedDuck/data/events.json"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/02_Areas/Sales/Scraped Data/FoodAgri/pokemon.md"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "02_Areas/Sales/Scraped Data/FoodAgri/pokemon.md"
sha256: "cd59ba307760949fcd520aeeb925842ce5f7edfd5c319e5b7de58e330005593a"
duplicate_of: ""
---

# Sunder sync: pokemon.md

Source file: `/Users/sethlim/Documents/Sunder Workspace/02_Areas/Sales/Scraped Data/FoodAgri/pokemon.md`

Primary URL: https://raw.githubusercontent.com/bigfoott/ScrapedDuck/data/events.json

Duplicate of existing source-map entry: `none`

## Capture Text

Perfect! I've updated the plan to use ScrapedDuck instead of building our own scraper. This is much better:

Key improvements:

- ✅ No Playwright/browser automation needed (lighter, simpler)
- ✅ Just fetch JSON from ScrapedDuck's GitHub data branch
- ✅ ScrapedDuck updates nightly automatically (maintained by community)
- ✅ Same data source used by GO Calendar and other community apps
- ✅ Much less code to maintain  


Updated flow:

1. Fetch events JSON from https://raw.githubusercontent.com/bigfoott/ScrapedDuck/data/events.json
2. Transform ScrapedDuck format → our calendar format
3. Filter out GO Pass/Battle League
4. Save to static JSON files
5. Frontend calendar loads and displays events
6. Monthly cron refreshes data + redeploys to Surge  


This is way more maintainable than scraping HTML. Ready to proceed?

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Ready to code?

Here is Claude's plan:  
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
Pokemon Go Monthly Event Calendar

Overview

Build a standalone Pokemon Go event calendar that:

- Fetches event data from ScrapedDuck (community-maintained JSON feed)
- Displays monthly calendar view (similar to LeekDuck)
- Filters out "GO Pass" and "GO Battle League" events
- Provides custom detail pages for each event
- Auto-updates via monthly cron job
- Deploys to Surge.sh  


Architecture

Tech Stack

- Frontend: Vanilla HTML/CSS/JavaScript (static site)
- Calendar Library: FullCalendar.js (handles monthly view, events, clickable days)
- Data Source: ScrapedDuck GitHub repo (https://github.com/bigfoott/ScrapedDuck)
- Data Fetching: Simple Node.js script (fetch JSON from GitHub)
- Data Storage: JSON files (data/events-YYYY-MM.json)
- Automation: Node-cron for monthly data fetch
- Deployment: Surge.sh CLI  


Project Structure

pokemon-go-calendar/  
 ├── public/  
 │ ├── index.html # Monthly calendar view  
 │ ├── event.html # Event detail page template  
 │ ├── css/  
 │ │ ├── main.css # Custom styles  
 │ │ └── calendar.css # Calendar overrides  
 │ ├── js/  
 │ │ ├── calendar.js # Initialize FullCalendar, load events  
 │ │ ├── events.js # Event filtering, rendering logic  
 │ │ └── detail.js # Detail page population  
 │ └── data/  
 │ └── events-2026-02.json # Monthly event data  
 ├── scripts/  
 │ ├── fetch-events.js # Fetch from ScrapedDuck GitHub  
 │ ├── transform.js # Transform to our JSON format  
 │ └── deploy.sh # Build & deploy to Surge  
 ├── cron-job.js # Monthly automation runner  
 ├── package.json  
 └── README.md

Implementation Plan

Phase 1: Data Fetching Pipeline

Goal: Fetch event data from ScrapedDuck and transform to our JSON format

Why ScrapedDuck:

- Community-maintained repo that already scrapes LeekDuck
- Provides structured JSON (no HTML parsing needed)
- Used by GO Calendar, PoGOEvents, and other community apps
- Updates nightly automatically
- Much simpler than maintaining our own scraper  


Files to create:

- scripts/fetch-events.js - Fetch JSON from ScrapedDuck GitHub
- scripts/transform.js - Transform ScrapedDuck JSON → our format  


Fetch logic:

1.  Fetch events JSON from ScrapedDuck's data branch:  
    https://raw.githubusercontent.com/bigfoott/ScrapedDuck/data/events.json
2.  Parse JSON response
3.  Filter events by date range (current + next month)
4.  Filter OUT: "GO Pass", "GO Battle League" event types
5.  Transform to our calendar format
6.  Save to public/data/events-YYYY-MM.json  


ScrapedDuck JSON structure (example):  
 {  
 "events": [  
 {  
 "name": "Community Day: Bulbasaur",  
 "eventType": "community-day",  
 "start": "2026-02-15 11:00",  
 "end": "2026-02-15 17:00",  
 "image": "https://leekduck.com/assets/img/events/...",  
 "features": ["3x Catch XP", "Shiny available"],  
 "spawns": ["Bulbasaur"]  
 }  
 ]  
 }

Our transformed format:  
 {  
 "month": "2026-02",  
 "lastUpdated": "2026-02-04T12:00:00Z",  
 "source": "ScrapedDuck",  
 "events": [  
 {  
 "id": "community-day-bulbasaur-2026-02",  
 "name": "Community Day: Bulbasaur",  
 "startDate": "2026-02-15T11:00:00",  
 "endDate": "2026-02-15T17:00:00",  
 "type": "Community Day",  
 "pokemon": ["Bulbasaur"],  
 "bonuses": ["3x Catch XP", "Shiny available"],  
 "imageUrl": "https://leekduck.com/assets/img/events/..."  
 }  
 ]  
 }

Dependencies: node-fetch (or native fetch in Node 18+), date-fns

---

Phase 2: Frontend Calendar View

Goal: Display monthly calendar with events, clickable days

Files to create:

- public/index.html - Main calendar page
- public/css/main.css - Styling to match LeekDuck aesthetic
- public/js/calendar.js - Initialize FullCalendar  


Calendar implementation:

1.  Include FullCalendar CDN (or install via npm + bundle)
2.  Load data/events-YYYY-MM.json on page load
3.  Map events to FullCalendar format:  
    {  
     title: event.name,  
     start: event.startDate,  
     end: event.endDate,  
     url: `/event.html?id=${event.id}`,  
     backgroundColor: getEventColor(event.type)  
    }
4.  Render month view by default
5.  Hide GO Pass / GO Battle League (already filtered in scraper)  


Visual design:

- 7-column grid (Mon-Sun)
- Event cards show Pokemon sprite + event name
- Color-coded by event type (Research = blue, Raid = red, Community Day = green)
- Compact view (multiple events per day)  


FullCalendar config:  
 new FullCalendar.Calendar(calendarEl, {  
 initialView: 'dayGridMonth',  
 events: events,  
 eventClick: function(info) {  
 window.location.href = info.event.url;  
 }  
 });

Alternative (if FullCalendar is too heavy):

- Build custom grid with CSS Grid (7 columns)
- Use date-fns to calculate days in month
- Manually populate event badges per day  


---

Phase 3: Event Detail Pages

Goal: Show full event info when clicking a day/event

Files to create:

- public/event.html - Detail page template
- public/js/detail.js - Populate event data from URL param  


Detail page content:

- Event name & dates (formatted: "Feb 15, 2026, 11:00 AM - 5:00 PM")
- Pokemon featured (images from PokéAPI or local assets)
- Bonuses list (bullets)
- Event description (if available from LeekDuck)
- Back button to calendar  


Implementation:

1.  Parse ?id=event-id from URL
2.  Load data/events-YYYY-MM.json
3.  Find matching event by ID
4.  Populate DOM:
<div class="event-detail">                                                                                                       
  <h1>{{ event.name }}</h1>                                                                                                      
  <div class="dates">{{ formattedDates }}</div>                                                                                  
  <div class="pokemon">                                                                                                          
    <img src="pokemon-sprite-url" />                                                                                             
  </div>                                                                                                                         
  <ul class="bonuses">                                                                                                           
    <li>{{ bonus }}</li>                                                                                                         
  </ul>                                                                                                                          
</div>                                                                                                                           


Pokemon images: Use PokéAPI sprites (https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png)

---

Phase 4: Monthly Automation

Goal: Auto-scrape and deploy on 1st of each month

Files to create:

- cron-job.js - Orchestrates scraping + deployment
- scripts/deploy.sh - Surge deployment script  


Cron job logic:  
 const cron = require('node-cron');

// Run on 1st of every month at 2:00 AM  
 cron.schedule('0 2 1 \* \*', async () => {  
 console.log('Starting monthly update...');

// 1. Fetch events from ScrapedDuck  
 await fetchEvents();

// 2. Transform and filter data  
 await transformEvents();

// 3. Deploy to Surge  
 await deployToSurge();

console.log('Monthly update complete!');  
 });

Deploy script (scripts/deploy.sh):  
 #!/bin/bash  
 cd public  
 surge --domain pokemon-go-calendar.surge.sh

Surge credentials: Store in .env file (not committed):  
 SURGE_LOGIN=neosuperslug@gmail.com  
 SURGE_TOKEN=G8tH@wke1

Run cron locally: Use node cron-job.js (must keep process running)

Alternative (GitHub Actions):

- Schedule workflow to run monthly
- Scrape → commit JSON → deploy to Surge
- No local machine needed  


---

Phase 5: Deployment & Testing

Initial deployment:

1.  Install Surge CLI: npm install -g surge
2.  Login: surge login (use credentials above)
3.  Deploy: cd public && surge
4.  Choose domain: pokemon-go-calendar.surge.sh (or custom)  


Testing checklist:

- Fetch successfully retrieves events from ScrapedDuck
- JSON transformation correctly maps ScrapedDuck → our format
- GO Pass / GO Battle League events are filtered out
- Calendar displays all events for current month
- Clicking event navigates to detail page
- Detail page shows all bonuses and Pokemon
- Responsive on mobile (calendar adapts to small screens)
- Cron job runs successfully on 1st of month
- Surge deployment updates live site  


---

Critical Files

Files to create (in order):

1.  package.json - Dependencies (node-fetch, node-cron, date-fns)
2.  scripts/fetch-events.js - Fetch from ScrapedDuck GitHub
3.  scripts/transform.js - Transform to our JSON format
4.  public/data/events-2026-02.json - Sample data (for testing frontend)
5.  public/index.html - Calendar page
6.  public/js/calendar.js - FullCalendar initialization
7.  public/event.html - Detail page template
8.  public/js/detail.js - Detail page logic
9.  cron-job.js - Monthly automation
10. scripts/deploy.sh - Surge deployment
11. .env - Surge credentials (gitignored)
12. README.md - Setup instructions  


Files to ignore (.gitignore):

node_modules/  
 .env  
 .DS_Store

---

Dependencies

{  
 "dependencies": {  
 "date-fns": "^3.0.0",  
 "node-cron": "^3.0.0",  
 "dotenv": "^16.0.0"  
 }  
 }

Note: If using Node 18+, native fetch is available. For older Node versions, add node-fetch.

Frontend (CDN links in HTML):

- FullCalendar: https://cdn.jsdelivr.net/npm/fullcalendar@6.1.0/index.global.min.js
- (Or use npm + bundle with Vite if preferred)  


---

Verification Steps

After implementation, verify end-to-end:

1.  Manual fetch test:  
    node scripts/fetch-events.js

# Check public/data/events-2026-02.json exists and looks correct

2.  Local frontend test:  
    cd public  
    python3 -m http.server 8000

# Visit http://localhost:8000

# Verify calendar renders, events show up, detail pages work

3.  Cron test (run immediately instead of waiting for schedule):  
    node cron-job.js --run-now

# Verify fetch runs, JSON updates, deployment succeeds

4.  Surge deployment test:  
    cd public  
    surge

# Visit generated URL, verify live site matches local

5.  Filter verification:

- Check that no "GO Pass" or "GO Battle League" events appear
- Manually compare with LeekDuck to ensure we're not missing events  


---

Future Enhancements (Optional)

- Add timezone selector (events vary by region)
- Month navigation (prev/next month buttons)
- Event search/filter by type
- Desktop notifications for upcoming events
- Shiny checklist integration
- Dark mode toggle
- Multiple language support (LeekDuck has translations)
