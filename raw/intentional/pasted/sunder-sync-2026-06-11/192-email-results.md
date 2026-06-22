---
type: raw_capture
source_type: pasted
title: "Sunder sync: email-results.json"
url: "file:///Users/sethlim/Documents/Sunder Workspace/02_Areas/Sales/Scraped Data/DistributorPricing/email-results.json"
collected_at: 2026-06-11T03:10:00+08:00
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
source_file: "/Users/sethlim/Documents/Sunder Workspace/02_Areas/Sales/Scraped Data/DistributorPricing/email-results.json"
source_root: "/Users/sethlim/Documents/Sunder Workspace"
source_relpath: "02_Areas/Sales/Scraped Data/DistributorPricing/email-results.json"
sha256: "35df11f855394509c871fb3187a637a9a4ec70d65a466ac2e7e2d10e85aed40e"
duplicate_of: ""
---

# Sunder sync: email-results.json

Source file: `/Users/sethlim/Documents/Sunder Workspace/02_Areas/Sales/Scraped Data/DistributorPricing/email-results.json`

Primary URL: file:///Users/sethlim/Documents/Sunder Workspace/02_Areas/Sales/Scraped Data/DistributorPricing/email-results.json

Duplicate of existing source-map entry: `none`

## Capture Text

```json
{
  "stage": "stage6_parallel",
  "processed": 224,
  "workers": 4,
  "elapsed_seconds": 896.7,
  "stats": {
    "success": 224,
    "errors": 0,
    "with_email": 63,
    "with_linkedin": 192,
    "with_both": 31,
    "emails_generated": 224,
    "linkedin_generated": 189,
    "voice_generated": 189
  },
  "results": [
    {
      "company_name": "TechCom Technology",
      "contact_name": "Mark Khoo",
      "contact_email": "*********@techcom.com.sg",
      "email_1": {
        "subject": "quick question on electronics distribution",
        "body": "Hi Mark,\n\n We're building an AI assistant that's always one step ahead for SG electronics distribution. It proactively checks in - running daily reconciliation of supplier invoices against purchase orders, tracking missing price updates and sending follow-ups to suppliers, or giving you morning updates on critical material price changes - all without you having to ask. \n\nYou just WhatsApp or email it instructions and it does your back office work around the clock. \n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what electronics distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference. \n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Woodlands Terrace if that's easier! \n\nBest,\nSeth \n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for TechCom Technology.",
        "ps_used": "Before our call, I can train our AI on your {their_doc_type} so you can see exactly what we'd catch for {company}."
      },
      "email_2": {
        "subject": "Mark <> Seth",
        "body": "Hi Mark,\n\n I did some digging into TechCom Technology and had a few ideas on where we could save time: - Extract 99% accurate pricing from your component price lists in seconds. - Get audit-ready reconciliation of supplier invoices against purchase orders. - Automatically update your ERP with current prices, catching what humans miss. Have you solved for keeping supplier pricing current across your catalog or is your team still doing it manually? If we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting? \n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing from your component price lists in seconds.",
          "Get audit-ready reconciliation of supplier invoices against purchase orders.",
          "Automatically update your ERP with current prices, catching what humans miss."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on electronics distribution",
        "body": "Hi Mark,\n\n My co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes. Given your experience in electronics distribution, I was hoping to get your opinion. \n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs. \n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference. \n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call. \n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean, ready to import data into Excel, would that be useful? \n\nWould you be open to a quick chat to point us in the right direction? \n\nBest,\nSeth \n\nP.S. Happy to drop by your office at Woodlands Terrace if that's easier!",
        "hook_used": "Fallback: Given your experience in {industry_short}, I was hoping to get your opinion.",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean, ready to import data into Excel, would that be useful?",
        "value_line_source": "document_pain_analysis + company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading TechCom Technology, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite (derived)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Mark,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like TechCom Technology. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Woodlands Terrace as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Woodlands Terrace",
        "generated": true
      }
    },
    {
      "company_name": "Air Liquide Singapore",
      "contact_name": "Tina",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "N/A",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "N/A",
        "generated": false
      }
    },
    {
      "company_name": "Mlion Corporation",
      "contact_name": "Eric Leong",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Mlion Corporation, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Eric,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Mlion Corporation. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at WCEGA Tower as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "WCEGA Tower",
        "generated": true
      }
    },
    {
      "company_name": "SP Muthiah & Sons",
      "contact_name": "Muthu Selvarathenam",
      "contact_email": "muthu@sp-muthiah.om.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Muthu,\n\nWe're building an AI assistant that's always one step ahead for SG food & beverage distributors.\n\nIt proactively checks in - reconciling purchase orders with supplier invoices, tracking missing supplier price lists and sending follow-ups, or giving you morning updates on product catalog discrepancies - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Eunos Technolink if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for SP Muthiah & Sons.",
        "ps_used": "Before call, train AI on supplier price lists"
      },
      "email_2": {
        "subject": "Muthu <> Seth",
        "body": "Hi Muthu,\n\nI did some digging into SP Muthiah & Sons and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from SP Muthiah's diverse supplier price lists.\n- Get audit-ready reconciliation of purchase orders against supplier invoices.\n- Flag critical price changes from suppliers that humans miss.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from SP Muthiah's diverse supplier price lists.",
          "Get audit-ready reconciliation of purchase orders against supplier invoices.",
          "Flag critical price changes from suppliers that humans miss."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Muthu,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your 19+ years in the industry, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate price data in Excel ready to update your systems, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Eunos Technolink if that's easier!",
        "hook_used": "10+ years",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate price data in Excel ready to update your systems",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 19+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Muthu,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like SP Muthiah & Sons.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Eunos Technolink as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Eunos Technolink",
        "generated": true
      }
    },
    {
      "company_name": "MEASUREMENT & METROLOGY (S) PTE LTD",
      "contact_name": "Henry Lim",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Measurement & Metrology, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Henry,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Measurement & Metrology. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Sing Industrial Complex as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Sing Industrial Complex",
        "generated": true
      }
    },
    {
      "company_name": "Measurite",
      "contact_name": "Scott Lee",
      "contact_email": "scott@measurite.com.sg",
      "email_1": {
        "subject": "quick question on industrial distribution",
        "body": "Hi Scott,\n\nWe're building an AI assistant that's always one step ahead for SG industrial distributors.\n\nIt proactively checks in - running daily reconciliation of supplier price lists against current stock, tracking outdated product datasheets and sending update reminders, or giving you morning updates on new supplier price changes - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what industrial distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Techniques Centre if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Measurite.",
        "ps_used": "Custom \n\nP.S. based on supplier price lists from document_pain_analysis and company_profile."
      },
      "email_2": {
        "subject": "Scott <> Seth",
        "body": "Hi Scott,\n\nI did some digging into Measurite and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from supplier price lists for quick updates.\n- Flag discrepancies that humans miss on product datasheets and specifications.\n- Get complete, ready to review quotes with current pricing for Measurite customers.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from supplier price lists for quick updates.",
          "Flag discrepancies that humans miss on product datasheets and specifications.",
          "Get complete, ready to review quotes with current pricing for Measurite customers."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on industrial distribution",
        "body": "Hi Scott,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate pricing data in Excel, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Techniques Centre if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate pricing data in Excel, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Measurite, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Scott,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Measurite.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Techniques Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Techniques Centre",
        "generated": true
      }
    },
    {
      "company_name": "Inout Enterprise",
      "contact_name": "Matthew Ang Hwee Tong",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "N/A",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "N/A",
        "generated": false
      }
    },
    {
      "company_name": "Techfield Supply",
      "contact_name": "Richard Boon",
      "contact_email": "richard@techfield.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Richard,\n\nWe're building an AI assistant that's always one step ahead for SG industrial distributors.It proactively checks in - running daily reconciliation of UHP product invoices vs. POs, tracking outstanding supplier price lists and sending follow-ups, or giving you morning updates on PFA manifold BOMs awaiting approval - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Kaki Bukit Road 1 if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Techfield Supply.",
        "ps_used": "default document demo"
      },
      "email_2": {
        "subject": "Richard <> Seth",
        "body": "Hi Richard,\n\nI did some digging into Techfield Supply and had a few ideas on where we could save time:- Extract 99% accurate data from diverse supplier price lists for Techfield Supply.- Get audit-ready reconciliation of PFA manifold BOMs against engineering specs.- Flag discrepancies in UHP product catalogs that humans miss.Have you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?If we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from diverse supplier price lists for Techfield Supply.",
          "Get audit-ready reconciliation of PFA manifold BOMs against engineering specs.",
          "Flag discrepancies in UHP product catalogs that humans miss."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Richard,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.Given your experience leading Techfield Supply, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean, ready-to-import pricing data in Excel, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Kaki Bukit Road 1 if that's easier!",
        "hook_used": "C-suite",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean, ready-to-import pricing data in Excel",
        "value_line_source": "document_pain_analysis"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Techfield Supply, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Richard,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Techfield Supply.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Kaki Bukit Road 1 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Kaki Bukit Road 1",
        "generated": true
      }
    },
    {
      "company_name": "Hermes-Epitek Corporation",
      "contact_name": "Elvin Chu",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed Hermes-Epitek Corporation's wafer testing subsidiary HTSI is set to list on the OTC market - figured you'd have perspective on how operations are scaling. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "News",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Elvin,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Hermes-Epitek Corporation. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Hermes-Epitek Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Hermes-Epitek Centre",
        "generated": true
      }
    },
    {
      "company_name": "Techcom Technology",
      "contact_name": "Sam Lim",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 24+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Sam,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Techcom Technology. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Woodlands Terrace as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Woodlands Terrace",
        "generated": true
      }
    },
    {
      "company_name": "FAR EAST GROUP LIMITED",
      "contact_name": "Francis Lai",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Far East Group, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Francis,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Far East Group. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Ubi Avenue 3 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Ubi Avenue 3",
        "generated": true
      }
    },
    {
      "company_name": "Macnica Cytech",
      "contact_name": "Effendy Tukimin",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Macnica Cytech, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Effendy,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Macnica Cytech. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Home-Fix Building as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Home-Fix Building",
        "generated": true
      }
    },
    {
      "company_name": "YHI CORPORATION (SINGAPORE) PTE LTD",
      "contact_name": "Richard Tay",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading YHI Corporation, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Richard,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like YHI Corporation. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Pandan Road as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Pandan Road",
        "generated": true
      }
    },
    {
      "company_name": "ICHI SEIKI PTE LTD",
      "contact_name": "Jane Low",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Ichi Seiki, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Jane,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Ichi Seiki.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Kaki Bukit as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Kaki Bukit",
        "generated": true
      }
    },
    {
      "company_name": "Hafary Pte Ltd",
      "contact_name": "Mandy Lee",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Hafary, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Mandy,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Hafary. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Eunos Avenue 3 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Eunos Avenue 3",
        "generated": true
      }
    },
    {
      "company_name": "A.C.T Hardware",
      "contact_name": "Conan Teh",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed A.C.T Hardware kicked off with Makita and announced plans to bring in more brands in 2026 - figured you'd have perspective on how operations are scaling. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "News",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Conan,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like A.C.T Hardware. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Nordcom Two as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Nordcom Two",
        "generated": true
      }
    },
    {
      "company_name": "Hoffmann Quality Tools Asia Pacific",
      "contact_name": "Direkrid Manasnayakorn",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Hoffmann Quality Tools Asia Pacific, I was hoping to get your opinion. We're building an AI assistant that does back office work around the clock. Sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Direkrid,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Hoffmann Quality Tools Asia Pacific.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at German Centre Singapore as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "German Centre Singapore",
        "generated": true
      }
    },
    {
      "company_name": "FA Systems Automation",
      "contact_name": "Chunheong Tan",
      "contact_email": "ch*******@fasystems.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Chunheong,\n\nWe're building an AI assistant that's always one step ahead for SG distributors.\n\nIt proactively checks in - running daily reconciliation of supplier price lists against internal cost models, tracking pending engineering change notices and sending follow-ups, or giving you morning updates on high-precision component lead times - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Changi South if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for FA Systems Automation.",
        "ps_used": "Before the call, I can train our AI on your {their_doc_type} so you can see exactly what we'd catch for {company}. (supplier price lists from research as doc type.)"
      },
      "email_2": {
        "subject": "Chunheong <> Seth",
        "body": "Hi Chunheong,\n\nI did some digging into FA Systems Automation and had a few ideas on where we could save time:\n\n- Extract 99% accurate pricing from varied supplier lists into your ERP.\n- Flag critical discrepancies that humans miss in BOMs and ECNs.\n- Generate complete, ready-to-review reconciliation reports for project invoices.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing from varied supplier lists into your ERP.",
          "Flag critical discrepancies that humans miss in BOMs and ECNs.",
          "Generate complete, ready-to-review reconciliation reports for project invoices."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Chunheong,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists, technical specs, and lead-time information and get back 99% accurate pricing data in Excel, ready for your ERP, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Changi South if that's easier!",
        "hook_used": "Fallback (none)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists, technical specs, and lead-time information and get back 99% accurate pricing data in Excel, ready for your ERP, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "YAMAZEN (S) PTE LTD",
      "contact_name": "Takuro Matsui",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Yamazen Singapore, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Takuro,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Yamazen. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Henderson Road as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Henderson Road",
        "generated": true
      }
    },
    {
      "company_name": "ERIKS",
      "contact_name": "Chloe Ong",
      "contact_email": "*****@eriks.com.sg",
      "email_1": {
        "subject": "quick question on industrial distribution",
        "body": "Hi Chloe,\n\nOur co-founder and I are building an AI assistant that's always one step ahead for SG industrial distributors.It proactively checks in - running daily reconciliations of supplier invoices against purchase orders, tracking overdue supplier price list updates and sending follow-ups, or giving you morning updates on product catalogs awaiting approval - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what industrial distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tuas Loop if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for ERIKS.",
        "ps_used": "Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for ERIKS."
      },
      "email_2": {
        "subject": "Chloe <> Seth",
        "body": "Hi Chloe,\n\nI did some digging into ERIKS and had a few ideas on where we could save time:- Extract 99% accurate data from diverse supplier price lists.- Flag price discrepancies in purchase orders to prevent margin erosion.- Get audit-ready reconciliation of supplier invoices and payments.Have you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?If we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from diverse supplier price lists.",
          "Flag price discrepancies in purchase orders to prevent margin erosion.",
          "Get audit-ready reconciliation of supplier invoices and payments."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on industrial distribution",
        "body": "Hi Chloe,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.Given your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate data ready to update your systems, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Tuas Loop if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate data ready to update your systems, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at ERIKS, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Chloe,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like ERIKS.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Tuas Loop as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tuas Loop",
        "generated": true
      }
    },
    {
      "company_name": "Le Champ",
      "contact_name": "Angelina Peh",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Le Champ, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Angelina,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Le Champ.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Jalan Mesin as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Jalan Mesin",
        "generated": true
      }
    },
    {
      "company_name": "Excel Hardware Pte Ltd",
      "contact_name": "Kaden Choa",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed Excel Hardware published a video about the Excel Brand Experience Center - figured you'd have perspective on how operations are scaling. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "News",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Kaden,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Excel Hardware.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at North Link Building as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "North Link Building",
        "generated": true
      }
    },
    {
      "company_name": "Avani Resources",
      "contact_name": "Rajesh Johar",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 14+ years in the distribution industry, I was hoping to get your opinion. I'm also sending a voice note about our idea for a WhatsApp AI assistant that does back office work around the clock!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Rajesh,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Avani Resources.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Cecil Street as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Cecil Street",
        "generated": true
      }
    },
    {
      "company_name": "Swee Choon Co",
      "contact_name": "Wee Meng",
      "contact_email": "main@sweechoon.com.sg",
      "email_1": {
        "subject": "quick question on F&B distribution",
        "body": "Hi Wee Meng,\n\nWe're building an AI assistant that's always one step ahead for SG F&B distributors.\n\nIt proactively checks in - running daily reconciliation of supplier invoices against purchase orders, tracking pending ingredient deliveries and sending follow-ups, or giving you morning updates on stock levels for popular dim sum items - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what F&B distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Jalan Bukit Merah if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your a sample invoice so you can see exactly what we'd catch for Swee Choon Co.",
        "ps_used": "default"
      },
      "email_2": {
        "subject": "Wee Meng <> Seth",
        "body": "Hi Wee Meng,\n\nI did some digging into Swee Choon Co and had a few ideas on where we could save time:\n\n- Extract 99% accurate pricing from diverse ingredient supplier lists for Swee Choon Co.\n- Flag discrepancies in new supplier invoices that humans might miss.\n- Generate complete, ready-to-review cost reports for popular dim sum menu items.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing from diverse ingredient supplier lists for Swee Choon Co.",
          "Flag discrepancies in new supplier invoices that humans might miss.",
          "Generate complete, ready-to-review cost reports for popular dim sum menu items."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on F&B distribution",
        "body": "Hi Wee Meng,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in F&B distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your documents and get back organized, audit-ready Excel reports showing your current ingredient costs, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Jalan Bukit Merah if that's easier!",
        "hook_used": "Fallback (none)",
        "value_line": "If you could just email or WhatsApp an AI assistant your documents and get back organized, audit-ready Excel reports showing your current ingredient costs, would that be useful?",
        "value_line_source": "company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Swee Choon Co, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Wee Meng,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Swee Choon Co. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Jalan Bukit Merah as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Jalan Bukit Merah",
        "generated": true
      }
    },
    {
      "company_name": "Exim & Mfr Enterprise",
      "contact_name": "Felix Lian",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 26+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Felix,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Exim & Mfr Enterprise. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Techpoint as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Techpoint",
        "generated": true
      }
    },
    {
      "company_name": "Tachibana Sales",
      "contact_name": "Minkim Wang",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Tachibana Sales, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Minkim,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Tachibana Sales.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office near International Plaza as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "International Plaza",
        "generated": true
      }
    },
    {
      "company_name": "Noah Agencies 'N' Marine Services",
      "contact_name": "Eugene Wee",
      "contact_email": "eugene.wee@noah.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Eugene,\n\nWe're building an AI assistant that's always one step ahead for SG industrial distributors.\n\nIt proactively checks in - running daily reconciliation of supplier price lists against internal catalog, tracking missing compliance certificates and sending follow-ups, or giving you morning updates on quotes awaiting pricing approval - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tuas Avenue 4 if that's easier!\n\nBest,\nSeth",
        "ps_used": "P.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Noah Agencies 'N' Marine Services."
      },
      "email_2": {
        "subject": "Eugene <> Seth",
        "body": "Hi Eugene,\n\nI did some digging into Noah Agencies 'N' Marine Services and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from complex supplier price lists in seconds.\n- Get audit-ready reconciliation of supplier price changes into your ERP system.\n- Generate complete, ready-to-review quote sheets with current pricing for Noah Agencies 'N' Marine Services.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from complex supplier price lists in seconds.",
          "Get audit-ready reconciliation of supplier price changes into your ERP system.",
          "Generate complete, ready-to-review quote sheets with current pricing for Noah Agencies 'N' Marine Services."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Eugene,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your 32+ years in the industry, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back audit-ready reconciliation in Excel, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Tuas Avenue 4 if that's easier!",
        "hook_used": "10+ years",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back audit-ready reconciliation in Excel, would that be useful?",
        "value_line_source": "document_pain_analysis"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 32+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Eugene,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Noah Agencies 'N' Marine Services.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Tuas Avenue 4 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tuas Avenue 4",
        "generated": true
      }
    },
    {
      "company_name": "SinMetal International",
      "contact_name": "Emma Li",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading SinMetal International, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Emma,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like SinMetal International. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Tuas Avenue 8 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tuas Avenue 8",
        "generated": true
      }
    },
    {
      "company_name": "Pacific-Tec Scientific",
      "contact_name": "Sophie Bochot",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Pacific-Tec Scientific, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Sophie,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Pacific-Tec Scientific.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Ubi Ave 3 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Ubi Ave 3",
        "generated": true
      }
    },
    {
      "company_name": "Central-Midori International",
      "contact_name": "Stephen Quek",
      "contact_email": "stephenquek@central-midori.com.sg",
      "email_1": {
        "subject": "quick question on electronics distribution",
        "body": "Hi Stephen,\n\nWe're building an AI assistant that's always one step ahead for SG electronics distributors.\n\nIt proactively checks in - running daily reconciliation of supplier quotes against purchase orders, tracking missing Certificates of Conformity and sending automated follow-ups, or giving you morning updates on BOM revision changes - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what electronics distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tukang Innovation Grove if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier quotes and purchase orders so you can see exactly what we'd catch for Central-Midori International.",
        "ps_used": "Before our call, I can train our AI on your supplier quotes and purchase orders so you can see exactly what we'd catch for Central-Midori International."
      },
      "email_2": {
        "subject": "Stephen <> Seth",
        "body": "Hi Stephen,\n\nI did some digging into Central-Midori International and had a few ideas on where we could save time:\n\n- Extract 99% accurate component price data from supplier lists.\n- Auto-update ERP with audit-ready BOM and part revision changes.\n- Flag pricing discrepancies to ensure accurate client quotes for Central-Midori.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate component price data from supplier lists.",
          "Auto-update ERP with audit-ready BOM and part revision changes.",
          "Flag pricing discrepancies to ensure accurate client quotes for Central-Midori."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Stephen,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your BOMs and supplier data and get back 99% accurate, clean data in Excel, ready to import into your ERP, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Tukang Innovation Grove if that's easier!",
        "hook_used": "Fallback",
        "value_line": "If you could just email or WhatsApp an AI assistant your BOMs and supplier data and get back 99% accurate, clean data in Excel, ready to import into your ERP, would that be useful?",
        "value_line_source": "document_pain_analysis"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "D SQUARED TECHNOLOGY PTE LTD",
      "contact_name": "Kelvin Tay",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 27+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Kelvin,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like D Squared Technology.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Geylang as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Geylang",
        "generated": true
      }
    },
    {
      "company_name": "Direct Wholesale",
      "contact_name": "Deepak R B",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Direct Wholesale, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Deepak,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Direct Wholesale.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "",
        "generated": true
      }
    },
    {
      "company_name": "FC MEASUREMENT & CONTROLS PTE LTD",
      "contact_name": "Steven Yip",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed Furness Controls released the FCS 600 PAPR Duration Tester - figured you'd have perspective on how operations are scaling. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "News",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Steven,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like FC Measurement & Controls. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at IBiz Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "IBiz Centre",
        "generated": true
      }
    },
    {
      "company_name": "JJ-LAPP",
      "contact_name": "Hanis Koh",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading JJ-LAPP, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Hanis,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like JJ-LAPP. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Corporation Place as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Corporation Place",
        "generated": true
      }
    },
    {
      "company_name": "J.P. Electronics",
      "contact_name": "Utkarsh Savla",
      "contact_email": "utkarsh@jpegroup.com",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Utkarsh,\n\nWe're building an AI assistant that's always one step ahead for SG electronics distribution companies.\n\nIt proactively checks in - running daily reconciliation of supplier price lists against purchase orders, tracking overdue payment confirmations and sending follow-ups, or giving you morning updates on incoming product catalogs - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tai Seng Avenue if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for J.P. Electronics.",
        "ps_used": "Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for J.P. Electronics."
      },
      "email_2": {
        "subject": "Utkarsh <> Seth",
        "body": "Hi Utkarsh,\n\nI did some digging into J.P. Electronics and had a few ideas on where we could save time:\n\n- Extract 99% accurate component pricing from diverse supplier formats for J.P. Electronics.\n- Flag critical price changes and exceptions across your 50+ supplier catalogs.\n- Generate complete, ready-to-review quote sheets with current pricing in seconds.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate component pricing from diverse supplier formats for J.P. Electronics.",
          "Flag critical price changes and exceptions across your 50+ supplier catalogs.",
          "Generate complete, ready-to-review quote sheets with current pricing in seconds."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Utkarsh,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate pricing data in Excel ready for your ERP, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Tai Seng Avenue if that's easier!",
        "hook_used": "Fallback (none)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate pricing data in Excel ready for your ERP, would that be useful?",
        "value_line_source": "document_pain_analysis"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "App Systems Services",
      "contact_name": "C. P. Lee",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading App Systems Services, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi C. P.,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like App Systems Services. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Toh Guan Road East as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Toh Guan Road East",
        "generated": true
      }
    },
    {
      "company_name": "IGUS Singapore Pte Ltd",
      "contact_name": "Lena Tan",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Igus Singapore, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Lena,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Igus Singapore. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Axxel Innovation Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Axxel Innovation Centre",
        "generated": true
      }
    },
    {
      "company_name": "Hirata FA Engineering",
      "contact_name": "Beng Thiam",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Hirata FA Engineering, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Beng Thiam,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Hirata FA Engineering.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Interlocal Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Interlocal Centre",
        "generated": true
      }
    },
    {
      "company_name": "Best Chemical Co",
      "contact_name": "Johnny Wong",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Best Chemical Co, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Johnny,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Best Chemical Co.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Senoko Road as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Senoko Road",
        "generated": true
      }
    },
    {
      "company_name": "Quantel",
      "contact_name": "Johnson Hsu",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed you spent time in SF - I was working there last year. Given your experience in distribution, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "SF",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Johnson,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Quantel.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Kallang Avenue as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Kallang Avenue",
        "generated": true
      }
    },
    {
      "company_name": "Hermes-Epitek Corporation",
      "contact_name": "Tommy Lin",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Hermes-Epitek Corporation, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Tommy,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Hermes-Epitek Corporation.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Hermes-Epitek Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Hermes-Epitek Centre",
        "generated": true
      }
    },
    {
      "company_name": "Bizit Systems and Solutions",
      "contact_name": "KS Chan",
      "contact_email": "sales@bizits.com",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi KS,\n\nWe're building an AI assistant that's always one step ahead for SG Industrial/MRO distributors.\n\nIt proactively checks in - running daily status reports on open UR project quotes, tracking pending client inquiries and sending follow-ups, or giving you morning updates on new service agreements awaiting approval - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at CT Hub if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your project briefs or quotes so you can see exactly what we'd catch for Bizit Systems and Solutions.",
        "ps_used": "Customized document-specific demo \n\nP.S."
      },
      "email_2": {
        "subject": "KS <> Seth",
        "body": "Hi KS,\n\nI did some digging into Bizit Systems and Solutions and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from client project briefs for faster scoping.\n- Flag discrepancies in UR automation project quotes to prevent errors.\n- Get complete installation and training reports ready for cross-border teams.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from client project briefs for faster scoping.",
          "Flag discrepancies in UR automation project quotes to prevent errors.",
          "Get complete installation and training reports ready for cross-border teams."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi KS,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your quotes for UR automation projects and get back audit-ready reconciliations against project requirements, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at CT Hub if that's easier!",
        "hook_used": "Fallback (no specific signals)",
        "value_line": "If you could just email or WhatsApp an AI assistant your quotes for UR automation projects and get back audit-ready reconciliations against project requirements, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "Maiolika SG",
      "contact_name": "Sofia Fricano",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Maiolika SG, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Sofia,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Maiolika SG.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "",
        "generated": true
      }
    },
    {
      "company_name": "Optical Gaging",
      "contact_name": "Kelly Ho",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Optical Gaging, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Kelly,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Optical Gaging. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Tannery Road as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tannery Road",
        "generated": true
      }
    },
    {
      "company_name": "Sonepar Singapore",
      "contact_name": "Hun Leng Loo",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Sonepar Singapore, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Hun Leng,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Sonepar Singapore. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Eunos Ave 3 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Eunos Ave 3",
        "generated": true
      }
    },
    {
      "company_name": "HAKUTO SINGAPORE PTE LTD",
      "contact_name": "David Goh",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Hakuto Singapore, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi David,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Hakuto Singapore.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Kallang Avenue as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Kallang Avenue",
        "generated": true
      }
    },
    {
      "company_name": "Cadtronics Singapore",
      "contact_name": "Shirley Ng",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Cadtronics Singapore, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Shirley,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Cadtronics Singapore. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Enterprise Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Enterprise Centre",
        "generated": true
      }
    },
    {
      "company_name": "Nam Leong Co. Pte Ltd",
      "contact_name": "Mark Poh Seng Kui",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Nam Leong Co., I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Mark,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Nam Leong Co. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Jalan Besar as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Jalan Besar",
        "generated": true
      }
    },
    {
      "company_name": "Ghee Hoe Hardware & Engineering Co",
      "contact_name": "B Boon Tan",
      "contact_email": "ghengrg@singnet.com.sg",
      "email_1": {
        "subject": "quick question on building materials distribution",
        "body": "Hi B Boon,\n\n \u041c\u044b \u0441\u0442\u0440\u043e\u0438\u043c \u0418\u0418-\u043f\u043e\u043c\u043e\u0449\u043d\u0438\u043a\u0430, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0432\u0441\u0435\u0433\u0434\u0430 \u043d\u0430 \u0448\u0430\u0433 \u0432\u043f\u0435\u0440\u0435\u0434\u0438 \u0434\u043b\u044f \u0441\u0438\u043d\u0433\u0430\u043f\u0443\u0440\u0441\u043a\u0438\u0445 \u0434\u0438\u0441\u0442\u0440\u0438\u0431\u044c\u044e\u0442\u043e\u0440\u043e\u0432 \u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432.  \u041e\u043d \u0430\u043a\u0442\u0438\u0432\u043d\u043e \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0435\u0442 - \u0435\u0436\u0435\u0434\u043d\u0435\u0432\u043d\u043e \u0441\u0432\u0435\u0440\u044f\u0435\u0442 \u0441\u043f\u0438\u0441\u043a\u0438 \u0446\u0435\u043d \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432 \u0441 \u0442\u0435\u043a\u0443\u0449\u0438\u043c\u0438 \u0437\u0430\u043f\u0430\u0441\u0430\u043c\u0438 \u0434\u043b\u044f \u0432\u044b\u044f\u0432\u043b\u0435\u043d\u0438\u044f \u0440\u0438\u0441\u043a\u043e\u0432 \u043c\u0430\u0440\u0436\u0438, \u043e\u0442\u0441\u043b\u0435\u0436\u0438\u0432\u0430\u0435\u0442 \u043f\u0440\u043e\u0441\u0440\u043e\u0447\u0435\u043d\u043d\u044b\u0435 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0446\u0435\u043d \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432 \u0438 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u044f\u0435\u0442 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u044f, \u0438\u043b\u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0438\u0440\u0443\u0435\u0442 \u0432\u0430\u0441 \u043f\u043e \u0443\u0442\u0440\u0430\u043c \u043e \u0432\u0445\u043e\u0434\u044f\u0449\u0438\u0445 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f\u0445 \u0432 \u043f\u0440\u0430\u0439\u0441-\u043b\u0438\u0441\u0442\u0430\u0445 \u0438 \u043e\u0436\u0438\u0434\u0430\u044e\u0449\u0438\u0445 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f\u0445 \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u043e\u0432 - \u0438 \u0432\u0441\u0435 \u044d\u0442\u043e \u0431\u0435\u0437 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e\u0441\u0442\u0438 \u0441\u043f\u0440\u0430\u0448\u0438\u0432\u0430\u0442\u044c. \u0412\u044b \u043f\u0440\u043e\u0441\u0442\u043e \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u044f\u0435\u0442\u0435 \u0435\u043c\u0443 \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0438 \u043f\u043e WhatsApp \u0438\u043b\u0438 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u043f\u043e\u0447\u0442\u0435, \u0438 \u043e\u043d \u043a\u0440\u0443\u0433\u043b\u043e\u0441\u0443\u0442\u043e\u0447\u043d\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u044f\u0435\u0442 \u0432\u0430\u0448\u0443 \u0431\u044d\u043a-\u043e\u0444\u0438\u0441\u043d\u0443\u044e \u0440\u0430\u0431\u043e\u0442\u0443.  \u041c\u044b - \u0433\u0440\u0443\u043f\u043f\u0430 \u0438\u0437 \u041a\u0435\u043c\u0431\u0440\u0438\u0434\u0436\u0430 \u0441 \u0440\u0430\u0431\u043e\u0447\u0438\u043c \u043f\u0440\u043e\u0442\u043e\u0442\u0438\u043f\u043e\u043c \u0434\u043b\u044f \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0438\u0438, \u043d\u043e \u044d\u0442\u043e \u043d\u0435 \u0437\u0432\u043e\u043d\u043e\u043a \u043f\u043e \u043f\u0440\u043e\u0434\u0430\u0436\u0430\u043c. \u041c\u044b \u043f\u044b\u0442\u0430\u0435\u043c\u0441\u044f \u0443\u0437\u043d\u0430\u0442\u044c, \u0447\u0442\u043e \u043a\u043e\u043c\u0430\u043d\u0434\u044b \u0432 \u0441\u0444\u0435\u0440\u0435 \u0434\u0438\u0441\u0442\u0440\u0438\u0431\u0443\u0446\u0438\u0438 \u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u043e\u0432 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043d\u0430\u0445\u043e\u0434\u044f\u0442 \u043f\u043e\u043b\u0435\u0437\u043d\u044b\u043c, \u043a\u0430\u043a\u0438\u0435 \u0431\u043e\u043b\u0435\u0432\u044b\u0435 \u0442\u043e\u0447\u043a\u0438 \u043f\u043e\u0441\u0442\u043e\u044f\u043d\u043d\u043e \u0432\u043e\u0437\u043d\u0438\u043a\u0430\u044e\u0442, \u0438 \u043a\u0430\u043a \u0432\u044b \u043c\u044b\u0441\u043b\u0438\u0442\u0435 \u043e \u0431\u0443\u0434\u0443\u0449\u0435\u043c \u0441\u0432\u043e\u0435\u0433\u043e \u0431\u0438\u0437\u043d\u0435\u0441\u0430. 30 \u043c\u0438\u043d\u0443\u0442 \u0432\u0430\u0448\u0435\u0433\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0438\u043c\u0435\u043b\u0438 \u0431\u044b \u043e\u0433\u0440\u043e\u043c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435.  \u042f \u0437\u043d\u0430\u044e, \u0447\u0442\u043e \u0432\u044b \u0437\u0430\u043d\u044f\u0442\u044b, \u043f\u043e\u044d\u0442\u043e\u043c\u0443 \u0434\u0430\u0439\u0442\u0435 \u043c\u043d\u0435 \u0437\u043d\u0430\u0442\u044c, \u043a\u0430\u043a\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u043b\u0443\u0447\u0448\u0435 \u0434\u043b\u044f \u0437\u0432\u043e\u043d\u043a\u0430, \u0438\u043b\u0438 \u044f \u043c\u043e\u0433\u0443 \u0437\u0430\u0439\u0442\u0438 \u0432 \u0432\u0430\u0448 \u043e\u0444\u0438\u0441 \u0432 \u0411\u0435\u043d\u0434\u0435\u043c\u0435\u0440 \u0412\u0438\u043b\u043b\u0435, \u0435\u0441\u043b\u0438 \u0442\u0430\u043a \u0431\u0443\u0434\u0435\u0442 \u043f\u0440\u043e\u0449\u0435!  \n\nBest,\nSeth  \n\nP.S. \u0415\u0441\u043b\u0438 \u0432\u044b \u0436\u043e\u043d\u0433\u043b\u0438\u0440\u0443\u0435\u0442\u0435 \u043f\u0440\u0430\u0439\u0441-\u043b\u0438\u0441\u0442\u0430\u043c\u0438 \u043e\u0442 \u0431\u043e\u043b\u0435\u0435 \u0447\u0435\u043c 50 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432, \u044f \u043c\u043e\u0433\u0443 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0432\u0430\u043c, \u043a\u0430\u043a \u043e\u0434\u0438\u043d \u0434\u0438\u0441\u0442\u0440\u0438\u0431\u044c\u044e\u0442\u043e\u0440 \u043a\u043e\u043d\u0441\u043e\u043b\u0438\u0434\u0438\u0440\u043e\u0432\u0430\u043b \u0432\u0441\u0435 \u0432 \u0435\u0434\u0438\u043d\u044b\u0439 \u0440\u0430\u0431\u043e\u0447\u0438\u0439 \u043f\u0440\u043e\u0446\u0435\u0441\u0441 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f.",
        "ps_used": "multiple_suppliers"
      },
      "email_2": {
        "subject": "B Boon <> Seth",
        "body": "Hi B Boon,\n\n \u042f \u043d\u0435\u043c\u043d\u043e\u0433\u043e \u043f\u043e\u043a\u043e\u043f\u0430\u043b\u0441\u044f \u0432 Ghee Hoe Hardware & Engineering Co \u0438 \u0443 \u043c\u0435\u043d\u044f \u0431\u044b\u043b\u043e \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0438\u0434\u0435\u0439, \u0433\u0434\u0435 \u043c\u044b \u043c\u043e\u0433\u043b\u0438 \u0431\u044b \u0441\u044d\u043a\u043e\u043d\u043e\u043c\u0438\u0442\u044c \u0432\u0440\u0435\u043c\u044f:  - \u0418\u0437\u0432\u043b\u0435\u043a\u0430\u0439\u0442\u0435 \u043d\u0430 99% \u0442\u043e\u0447\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u0440\u0430\u0437\u043d\u043e\u043e\u0431\u0440\u0430\u0437\u043d\u044b\u0445 \u043f\u0440\u0430\u0439\u0441-\u043b\u0438\u0441\u0442\u043e\u0432 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432 \u0430\u043f\u043f\u0430\u0440\u0430\u0442\u043d\u044b\u0445 \u0441\u0440\u0435\u0434\u0441\u0442\u0432. - \u041f\u043e\u043b\u0443\u0447\u0438\u0442\u0435 \u0433\u043e\u0442\u043e\u0432\u043e\u0435 \u043a \u0430\u0443\u0434\u0438\u0442\u0443 \u0441\u0432\u0435\u0440\u043a\u0443 \u0446\u0435\u043d \u043d\u0430 \u043d\u043e\u0432\u044b\u0435 \u0441\u0442\u0430\u043b\u044c\u043d\u044b\u0435 \u0431\u043e\u043b\u0442\u044b \u0441 \u0432\u0430\u0448\u0435\u0439 ERP. - \u041e\u0442\u043c\u0435\u0447\u0430\u0439\u0442\u0435 \u043a\u0440\u0438\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0446\u0435\u043d \u043d\u0430 \u043f\u0438\u043b\u043e\u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043b\u044e\u0434\u0438 \u043c\u043e\u0433\u0443\u0442 \u043f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c.  \u0412\u044b \u0440\u0435\u0448\u0438\u043b\u0438 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0443 \u0441 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435\u043c \u0430\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0446\u0435\u043d \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432 \u0432 \u0432\u0430\u0448\u0435\u043c \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0435 \u0438\u043b\u0438 \u0432\u0430\u0448\u0430 \u043a\u043e\u043c\u0430\u043d\u0434\u0430 \u0432\u0441\u0435 \u0435\u0449\u0435 \u0434\u0435\u043b\u0430\u0435\u0442 \u044d\u0442\u043e \u0432\u0440\u0443\u0447\u043d\u0443\u044e?  \u0415\u0441\u043b\u0438 \u0431\u044b \u043c\u044b \u043c\u043e\u0433\u043b\u0438 \u043f\u043e\u043c\u043e\u0447\u044c \u0432\u0430\u043c \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0442\u043e \u0436\u0435 \u0441\u0430\u043c\u043e\u0435 \u0438 \u0441\u044d\u043a\u043e\u043d\u043e\u043c\u0438\u0442\u044c \u0431\u043e\u043b\u0435\u0435 10 \u0447\u0430\u0441\u043e\u0432 \u0432 \u043d\u0435\u0434\u0435\u043b\u044e, \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0447\u0435\u0440\u0435\u0437 WhatsApp, \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0443\u044e \u043f\u043e\u0447\u0442\u0443 \u0438\u043b\u0438 \u043b\u044e\u0431\u043e\u0435 \u0434\u0440\u0443\u0433\u043e\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0447\u0430\u0442\u0430, \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0432\u044b \u0443\u0436\u0435 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0435, \u0431\u044b\u043b\u043e \u0431\u044b \u044d\u0442\u043e \u0438\u043d\u0442\u0435\u0440\u0435\u0441\u043d\u043e?  \n\nBest,\nSeth",
        "ideas_used": [
          "\u0418\u0437\u0432\u043b\u0435\u043a\u0430\u0439\u0442\u0435 \u043d\u0430 99% \u0442\u043e\u0447\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u0440\u0430\u0437\u043d\u043e\u043e\u0431\u0440\u0430\u0437\u043d\u044b\u0445 \u043f\u0440\u0430\u0439\u0441-\u043b\u0438\u0441\u0442\u043e\u0432 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432 \u0430\u043f\u043f\u0430\u0440\u0430\u0442\u043d\u044b\u0445 \u0441\u0440\u0435\u0434\u0441\u0442\u0432.",
          "\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u0435 \u0433\u043e\u0442\u043e\u0432\u0443\u044e \u043a \u0430\u0443\u0434\u0438\u0442\u0443 \u0441\u0432\u0435\u0440\u043a\u0443 \u0446\u0435\u043d \u043d\u0430 \u043d\u043e\u0432\u044b\u0435 \u0441\u0442\u0430\u043b\u044c\u043d\u044b\u0435 \u0431\u043e\u043b\u0442\u044b \u0441 \u0432\u0430\u0448\u0435\u0439 ERP.",
          "\u041e\u0442\u043c\u0435\u0447\u0430\u0439\u0442\u0435 \u043a\u0440\u0438\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0446\u0435\u043d \u043d\u0430 \u043f\u0438\u043b\u043e\u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043b\u044e\u0434\u0438 \u043c\u043e\u0433\u0443\u0442 \u043f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on building materials distribution",
        "body": "Hi B Boon,\n\n \u041c\u043e\u0439 \u0441\u043e\u0443\u0447\u0440\u0435\u0434\u0438\u0442\u0435\u043b\u044c \u0438 \u044f \u0441\u0442\u0440\u043e\u0438\u043c \u0441\u0442\u0430\u0440\u0442\u0430\u043f \u0432 \u0421\u0438\u043d\u0433\u0430\u043f\u0443\u0440\u0435 \u0434\u043b\u044f \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0438 \u043c\u0435\u0441\u0442\u043d\u044b\u0445 \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u0439, \u0438 \u043c\u044b \u0445\u043e\u0442\u0435\u043b\u0438 \u0441\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f \u0441 \u0432\u0430\u043c\u0438, \u043f\u043e\u0442\u043e\u043c\u0443 \u0447\u0442\u043e \u0432\u0430\u0448 \u043e\u043f\u044b\u0442 \u043c\u043e\u0436\u0435\u0442 \u0438\u0437\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u0430\u0441 \u043e\u0442 \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u0430 \u043e\u0448\u0438\u0431\u043e\u043a.  \u0423\u0447\u0438\u0442\u044b\u0432\u0430\u044f \u0432\u0430\u0448 \u043e\u043f\u044b\u0442 \u0432 \u0434\u0438\u0441\u0442\u0440\u0438\u0431\u0443\u0446\u0438\u0438, \u044f \u043d\u0430\u0434\u0435\u044f\u043b\u0441\u044f \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0432\u0430\u0448\u0435 \u043c\u043d\u0435\u043d\u0438\u0435.  \u0414\u043b\u044f \u0441\u043f\u0440\u0430\u0432\u043a\u0438, \u043d\u0430 \u043f\u0440\u043e\u0448\u043b\u043e\u0439 \u043d\u0435\u0434\u0435\u043b\u0435 \u043c\u044b \u043e\u0431\u0449\u0430\u043b\u0438\u0441\u044c \u0441\u043e \u0441\u0442\u0430\u0440\u0448\u0438\u043c\u0438 \u0433\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u043c\u0438 \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f\u043c\u0438 \u0432 Smart Nation - \u043e\u043d\u0438 \u043f\u043e\u0434\u0435\u043b\u0438\u043b\u0438\u0441\u044c, \u0447\u0442\u043e \u043c\u0430\u043b\u044b\u0435 \u0438 \u0441\u0440\u0435\u0434\u043d\u0438\u0435 \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u044f \u0432 \u043d\u0435\u0434\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u0435\u043c\u044b\u0445 \u0440\u0430\u0439\u043e\u043d\u0430\u0445 \u043f\u043e\u043b\u0443\u0447\u0430\u0442 \u043d\u0430\u0438\u0431\u043e\u043b\u044c\u0448\u0443\u044e \u0432\u044b\u0433\u043e\u0434\u0443 \u043e\u0442 \u0418\u0418 \u043f\u043e \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044e \u0441 \u043c\u043d\u043e\u0433\u043e\u043d\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u043c\u0438 \u043a\u043e\u0440\u043f\u043e\u0440\u0430\u0446\u0438\u044f\u043c\u0438.  \u0421\u0435\u0439\u0447\u0430\u0441 \u043c\u044b \u043f\u044b\u0442\u0430\u0435\u043c\u0441\u044f \u0432\u044b\u044f\u0441\u043d\u0438\u0442\u044c, \u043a\u0430\u043a\u0438\u0435 \u0441\u0430\u043c\u044b\u0435 \u0431\u043e\u043b\u044c\u0448\u0438\u0435 \u0431\u043e\u043b\u0435\u0432\u044b\u0435 \u0442\u043e\u0447\u043a\u0438 \u0438\u0441\u043f\u044b\u0442\u044b\u0432\u0430\u044e\u0442 \u0434\u0438\u0441\u0442\u0440\u0438\u0431\u044c\u044e\u0442\u043e\u0440\u044b, \u0438 30 \u043c\u0438\u043d\u0443\u0442 \u0432\u0430\u0448\u0435\u0433\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438 \u0438\u043c\u0435\u043b\u0438 \u0431\u044b \u043e\u0433\u0440\u043e\u043c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435.  \u041c\u044b - \u0433\u0440\u0443\u043f\u043f\u0430 \u0438\u0437 \u041a\u0435\u043c\u0431\u0440\u0438\u0434\u0436\u0430, \u0431\u0430\u0437\u0438\u0440\u0443\u044e\u0449\u0430\u044f\u0441\u044f \u0432 \u0421\u0438\u043d\u0433\u0430\u043f\u0443\u0440\u0435, \u0438 \u0443 \u043d\u0430\u0441 \u0435\u0441\u0442\u044c \u043f\u0440\u043e\u0442\u043e\u0442\u0438\u043f, \u043d\u043e \u044d\u0442\u043e \u043d\u0438 \u0432 \u043a\u043e\u0435\u043c \u0441\u043b\u0443\u0447\u0430\u0435 \u043d\u0435 \u043f\u0440\u043e\u0434\u0430\u0436\u043d\u044b\u0439 \u0437\u0432\u043e\u043d\u043e\u043a.  \u0415\u0441\u043b\u0438 \u0431\u044b \u0432\u044b \u043c\u043e\u0433\u043b\u0438 \u043f\u0440\u043e\u0441\u0442\u043e \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0418\u0418-\u043f\u043e\u043c\u043e\u0449\u043d\u0438\u043a\u0443 \u0441\u0432\u043e\u0438 \u043f\u0440\u0430\u0439\u0441-\u043b\u0438\u0441\u0442\u044b \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432 \u043f\u043e \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u043f\u043e\u0447\u0442\u0435 \u0438\u043b\u0438 WhatsApp \u0438 \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u043d\u0430 99% \u0442\u043e\u0447\u043d\u043e\u0435 \u0438\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u0435 \u0432\u0441\u0435\u0445 \u043f\u0440\u0430\u0439\u0441-\u043b\u0438\u0441\u0442\u043e\u0432 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432 \u0432 Excel, \u0433\u043e\u0442\u043e\u0432\u043e\u0435 \u0434\u043b\u044f \u0432\u0430\u0448\u0435\u0439 ERP, \u0431\u044b\u043b\u043e \u0431\u044b \u044d\u0442\u043e \u043f\u043e\u043b\u0435\u0437\u043d\u043e?  \u0412\u044b \u0431\u044b\u043b\u0438 \u0431\u044b \u043e\u0442\u043a\u0440\u044b\u0442\u044b \u0434\u043b\u044f \u0431\u044b\u0441\u0442\u0440\u043e\u0439 \u0431\u0435\u0441\u0435\u0434\u044b, \u0447\u0442\u043e\u0431\u044b \u0443\u043a\u0430\u0437\u0430\u0442\u044c \u043d\u0430\u043c \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e\u0435 \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435?  \n\nBest,\nSeth  \n\nP.S. \u0411\u0443\u0434\u0443 \u0440\u0430\u0434 \u0437\u0430\u0439\u0442\u0438 \u0432 \u0432\u0430\u0448 \u043e\u0444\u0438\u0441 \u0432 \u0411\u0435\u043d\u0434\u0435\u043c\u0435\u0440 \u0412\u0438\u043b\u043b\u0435, \u0435\u0441\u043b\u0438 \u0442\u0430\u043a \u0431\u0443\u0434\u0435\u0442 \u043f\u0440\u043e\u0449\u0435!",
        "hook_used": "Fallback (no signals)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back a 99% accurate extraction of all supplier price lists into Excel, ready for your ERP, would that be useful?",
        "value_line_source": "document_pain_analysis"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "Central Midori",
      "contact_name": "Kin Lim",
      "contact_email": "hengkinlim@central-midori.com.sg",
      "email_1": {
        "subject": "quick question on Electronics Distribution",
        "body": "Hi Kin Lim,\n\nWe're building an AI assistant that's always one step ahead for SG electronics distributors.\n\nIt proactively checks in - running daily reconciliation of supplier price lists against internal part numbers, tracking missing conformity certificates and sending follow-ups, or giving you morning updates on pending BOM revisions - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what Electronics Distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at JTC Medtech Hub if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier quotes so you can see exactly what we'd catch for Central Midori.",
        "ps_used": "Before our call, I can train our AI on your supplier quotes so you can see exactly what we'd catch for Central Midori."
      },
      "email_2": {
        "subject": "Kin Lim <> Seth",
        "body": "Hi Kin Lim,\n\nI did some digging into Central Midori and had a few ideas on where we could save time:\n\n- Extract 99% accurate pricing data from any supplier format for Central Midori.\n- Get audit-ready reconciliation of supplier price lists against your ERP system.\n- Flag discrepancies that humans miss in engineering change notices (ECNs).\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing data from any supplier format for Central Midori.",
          "Get audit-ready reconciliation of supplier price lists against your ERP system.",
          "Flag discrepancies that humans miss in engineering change notices (ECNs)."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on Electronics Distribution",
        "body": "Hi Kin Lim,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back clean, ready to import data in Excel, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at JTC Medtech Hub if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back clean, ready to import data in Excel, would that be useful?",
        "value_line_source": "document_pain_analysis"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Central Midori, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Kin Lim,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Central Midori.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at JTC Medtech Hub as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "JTC Medtech Hub",
        "generated": true
      }
    },
    {
      "company_name": "Silversky - Delivering WOW!",
      "contact_name": "Esmond Low",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 20+ years in the distribution industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Esmond,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Silversky.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Hola Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Hola Centre",
        "generated": true
      }
    },
    {
      "company_name": "Tachibana Sales",
      "contact_name": "Nishiyama",
      "contact_email": "******@tachibana.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Nishiyama,\n\nWe're building an AI assistant that's always one step ahead for SG electronics distributors.\n\nIt proactively checks in - running daily reconciliations of supplier price lists against internal pricing masters, tracking missing price updates and sending reminders to suppliers, or giving you morning updates on supplier price changes - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at International Plaza if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Tachibana Sales.",
        "ps_used": "Email 1 template \n\nP.S. formula"
      },
      "email_2": {
        "subject": "Nishiyama <> Seth",
        "body": "Hi Nishiyama,\n\nI did some digging into Tachibana Sales and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from diverse supplier price lists for Tachibana Sales.\n- Get audit-ready updates of component price lists automatically into your ERP.\n- Flag critical price changes that impact margins across your large catalog.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from diverse supplier price lists for Tachibana Sales.",
          "Get audit-ready updates of component price lists automatically into your ERP.",
          "Flag critical price changes that impact margins across your large catalog."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Nishiyama,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back 99% accurate, clean data in Excel, ready to import, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at International Plaza if that's easier!",
        "hook_used": "Fallback (none)",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back 99% accurate, clean data in Excel, ready to import",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "LFC",
      "contact_name": "Temmy Kwa",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 17+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years experience",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Temmy,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like LFC.\nThis isn't a sales call - just looking for your perspective.\nHappy to buy you lunch near your office at Zervex as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Zervex",
        "generated": true
      }
    },
    {
      "company_name": "Dashmesh Singapore",
      "contact_name": "Arthur Tan",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed Dashmesh Singapore announced a strategic partnership with Alibaba.com on August 12, 2025 - figured you'd have perspective on how operations are scaling. We help food & beverage distribution companies save 10+ hours each week on admin. No need to hop on a call, could I send a video of how it works?",
        "hook_used": "News",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Arthur,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Dashmesh Singapore.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Changi Logistics Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Changi Logistics Centre",
        "generated": true
      }
    },
    {
      "company_name": "D SQUARED TECHNOLOGY PTE LTD",
      "contact_name": "Tony Tan",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 35+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Tony,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like D Squared Technology.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Lorong 17 Geylang as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Lorong 17 Geylang",
        "generated": true
      }
    },
    {
      "company_name": "FA Systems Automation",
      "contact_name": "Lua Kim Teng",
      "contact_email": "lu*******@fasystems.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Kim Teng,\n\nWe're building an AI assistant that's always one step ahead for SG industrial distributors.It proactively checks in - running daily reconciliation of supplier price lists, tracking missing change notices (ECNs) and sending follow-ups, or giving you morning updates on quotes awaiting approval - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Changi South if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for FA Systems Automation.",
        "ps_used": "P.S. Before our call, I can train our AI on your [their_doc_type] so you can see exactly what we'd catch for [company]. (using supplier price lists and FA Systems Automation as inputs). Default \n\nP.S. due to fixed template structure for Email 1, not from \n\nP.S. Options in Industry Context section for Email 2."
      },
      "email_2": {
        "subject": "Kim Teng <> Seth",
        "body": "Hi Kim Teng,\n\nJust wanted to check in again in case this missed your inbox.We're building an AI assistant that's always one step ahead. It proactively checks in - running daily reconciliation of supplier price lists, tracking missing change notices (ECNs) and sending follow-ups, or giving you morning updates on quotes awaiting approval - all without you having to ask.\n\nCurious whether teams in distribution would actually use this from WhatsApp or email - would love your perspective if you have 15 mins.\n\nBest,\nSeth\n\nP.S. Happy to show you a 2-minute demo of how supplier price extraction actually works - no commitment, just context.",
        "ideas_used": [
          "Extract 99% accurate pricing from varied supplier lists to auto-update ERP.",
          "Flag discrepancies that humans miss in your supplier price changes, preventing margin erosion.",
          "Generate complete, ready-to-review quote sheets with current component pricing."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Kim Teng,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.Given your 20+ years in the industry, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and BOMs and get back 99% accurate data in Excel ready for your ERP system, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Changi South if that's easier!",
        "hook_used": "10+ years experience",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and BOMs and get back 99% accurate data in Excel ready for your ERP system, would that be useful?",
        "value_line_source": "document_pain_analysis and company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "VRV Global",
      "contact_name": "Rakesh Bangera",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading VRV Global, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Rakesh,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like VRV Global.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Cecil Court as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Cecil Court",
        "generated": true
      }
    },
    {
      "company_name": "XYRIX ELECTRONICS PTE LTD",
      "contact_name": "Kelvin Pang",
      "contact_email": "kelvin@xyrix.com.sg",
      "email_1": {
        "subject": "quick question on electronics distribution",
        "body": "Hi Kelvin,\n\nWe're building an AI assistant that's always one step ahead for SG electronics distributors.\n\nIt proactively checks in - running daily margin reconciliations, tracking missing price list updates and sending automated follow-ups, or giving you morning updates on new supplier catalogs - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what electronics distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Shun Li Industrial Park if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Xyrix Electronics.",
        "ps_used": "supplier price lists"
      },
      "email_2": {
        "subject": "Kelvin <> Seth",
        "body": "Hi Kelvin,\n\nI did some digging into Xyrix Electronics and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from diverse supplier price lists for faster updates.\n- Flag critical price changes and automatically update your procurement system.\n- Generate complete margin reconciliation reports to protect profitability at Xyrix Electronics.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from diverse supplier price lists for faster updates.",
          "Flag critical price changes and automatically update your procurement system.",
          "Generate complete margin reconciliation reports to protect profitability at Xyrix Electronics."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Kelvin,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back 99% accurate structured data in Excel, ready to import, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Shun Li Industrial Park if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back 99% accurate structured data in Excel, ready to import",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "VRV Global",
      "contact_name": "Zac Ng",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed you recently took over as Director in November - figured you'd have perspective on what's working and what's not. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "New role",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Zac,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like VRV Global.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Cecil Court as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Cecil Court",
        "generated": true
      }
    },
    {
      "company_name": "Measurite",
      "contact_name": "Peter Hoh",
      "contact_email": "peter@measurite.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Peter,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your quotations and invoices and get back audit-ready reconciliations in Excel, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Techniques Centre if that's easier!",
        "ps_used": "location from research (Techniques Centre)"
      },
      "email_2": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Peter,\n\nJust wanted to check in again in case this missed your inbox.\n\nWe're building an AI assistant that's always one step ahead. It proactively checks in - giving you morning updates on new product specifications, tracking supplier price list changes, or running weekly audits on invoice discrepancies without you having to ask.\n\nCurious whether teams in distribution would actually use this from WhatsApp or email - would love your perspective if you have 15 mins.\n\nBest,\nSeth\n\nP.S. Before the call, I can train our AI on your product datasheets so you can see exactly what we'd catch for Measurite.",
        "ideas_used": [
          "Extract 99% accurate pricing from supplier lists to update Measurite's catalog.",
          "Get audit-ready reconciliation of purchase orders against supplier invoices.",
          "Flag critical changes in product datasheets and technical specifications."
        ]
      },
      "email_3": {
        "subject": "Peter <> Seth",
        "body": "Hi Peter,\n\nI did some digging into Measurite and had a few ideas on where we could save time:\n\n- Extract 99% accurate pricing from supplier lists to update Measurite's catalog.\n- Get audit-ready reconciliation of purchase orders against supplier invoices.\n- Flag critical changes in product datasheets and technical specifications.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "hook_used": "10+ years experience",
        "value_line": "If you could just email or WhatsApp an AI assistant your quotations and invoices and get back audit-ready reconciliations in Excel, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "Multi Ways Equipment Pte Ltd",
      "contact_name": "James Lim",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Multi Ways Equipment, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi James,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Multi Ways Equipment.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Gul Circle as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Gul Circle",
        "generated": true
      }
    },
    {
      "company_name": "Redtec Industries",
      "contact_name": "Dexter Ng",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Redtec Industries, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Dexter,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Redtec Industries.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Gemini @ Sims as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Gemini @ Sims",
        "generated": true
      }
    },
    {
      "company_name": "KOKI (SINGAPORE) PTE LTD",
      "contact_name": "Mitsuo Fukushima",
      "contact_email": "info@koki.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Mitsuo,\n\nWe're building an AI assistant that's always one step ahead for SG electronics distribution companies.\n\nIt proactively checks in - running daily reconciliation of supplier invoices against purchase orders, tracking pending service orders and sending follow-ups, or giving you morning updates on supplier price changes - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what electronics distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Ubi Tech Park if that's easier!\n\nBest,\nSeth\n\nP.S. If you're juggling price lists from 50+ suppliers, I can show you how one distributor consolidated everything into a single update workflow.",
        "ps_used": "multiple_suppliers"
      },
      "email_2": {
        "subject": "Mitsuo <> Seth",
        "body": "Hi Mitsuo,\n\nI did some digging into Koki Singapore and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from Koki Singapore's supplier price lists.\n- Flag critical price changes that impact Koki Singapore's margins.\n- Get complete, ready-to-review customer quotes with current pricing.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from Koki Singapore's supplier price lists.",
          "Flag critical price changes that impact Koki Singapore's margins.",
          "Get complete, ready-to-review customer quotes with current pricing."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Mitsuo,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back 99% accurate, clean, and ready-to-import pricing data in Excel, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Ubi Tech Park if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back 99% accurate, clean, and ready-to-import pricing data in Excel, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "Limwood",
      "contact_name": "Cindy Casey Henwood",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Limwood, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Cindy,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Limwood.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Joo Seng Road as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Joo Seng Road",
        "generated": true
      }
    },
    {
      "company_name": "Avani Resources Pte. Ltd.",
      "contact_name": "Partha Banerjee",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Avani Resources, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "Fallback (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Partha,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Avani Resources. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Cecil Street as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Cecil Street",
        "generated": true
      }
    },
    {
      "company_name": "Qtest Technologies",
      "contact_name": "Robert Ng",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 47+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Robert,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Qtest Technologies.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Kaki Bukit as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Kaki Bukit",
        "generated": true
      }
    },
    {
      "company_name": "Wan-Pro (Far East)",
      "contact_name": "Frankie Chan",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 52+ years in the industry, I was hoping to get your opinion. I'm sending a voice note to share more about our idea for a WhatsApp AI assistant that does back office work around the clock.",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Frankie,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Wan-Pro (Far East).\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Tai Seng Avenue as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tai Seng Avenue",
        "generated": true
      }
    },
    {
      "company_name": "Foresight Metal Engineering Pte Ltd",
      "contact_name": "K Yong Qirong New Liang",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 22+ years in the distribution industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi K Yong Qirong,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Foresight Metal Engineering. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Jalan Berseh as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Jalan Berseh",
        "generated": true
      }
    },
    {
      "company_name": "Panasonic System Solutions Asia Pacific",
      "contact_name": "Takayuki Tateishi",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Panasonic System Solutions Asia Pacific, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Takayuki,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Panasonic System Solutions Asia Pacific.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "none",
        "generated": true
      }
    },
    {
      "company_name": "Wemark Techno Engineering",
      "contact_name": "Kelvin Yee",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Wemark Techno Engineering, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Kelvin,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Wemark Techno Engineering. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Tuas Basin as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tuas Basin",
        "generated": true
      }
    },
    {
      "company_name": "Tradeasia International",
      "contact_name": "Germaine",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Tradeasia International, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Germaine,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Tradeasia International. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Cecil Street as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Cecil Street",
        "generated": true
      }
    },
    {
      "company_name": "ICHI SEIKI PTE LTD",
      "contact_name": "Philip Kia",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 38+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Philip,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Ichi Seiki.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Kaki Bukit as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Kaki Bukit",
        "generated": true
      }
    },
    {
      "company_name": "SHENG SHENG F & B INDUSTRIES PTE LTD",
      "contact_name": "Chua Kim Hock",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Sheng Sheng F & B Industries, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Kim Hock,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Sheng Sheng F & B Industries. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Tuas South as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tuas South",
        "generated": true
      }
    },
    {
      "company_name": "Kowa Asia Pacific",
      "contact_name": "Yuuki Tanizaki",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Kowa Asia Pacific, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Yuuki,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Kowa Asia Pacific. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Collyer Quay Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Collyer Quay Centre",
        "generated": true
      }
    },
    {
      "company_name": "Macnica Cytech",
      "contact_name": "YM Gui",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed Macnica Cytech signed a distribution franchise with Cypress to broaden its distribution footprint - figured you'd have perspective on how operations are scaling. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "News",
        "generated": true
      },
      "voice_note": {
        "script": "Hi YM,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Macnica Cytech.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Tai Seng Avenue as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tai Seng Avenue",
        "generated": true
      }
    },
    {
      "company_name": "APP Systems Services",
      "contact_name": "Darren Tan",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed APP Systems Services participated in SEMICON SEA 2025 - figured you'd have perspective on how operations are scaling. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "News",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Darren,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like APP Systems Services. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Toh Guan Road East as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Toh Guan Road East",
        "generated": true
      }
    },
    {
      "company_name": "RMG TECHNOLOGIES PTE LTD",
      "contact_name": "Ricardo Liew",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at RMG Technologies, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Ricardo,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like RMG Technologies. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Prestige Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Prestige Centre",
        "generated": true
      }
    },
    {
      "company_name": "Megachem",
      "contact_name": "Chan Kam Loon",
      "contact_email": "klchan@sg.megachem.com",
      "email_1": {
        "subject": "quick question on chemical distribution",
        "body": "Hi Kam Loon,\n\nWe're building an AI assistant that's always one step ahead for SG chemical distributors.\n\nIt proactively checks in - running daily reconciliations of incoming supplier price lists against current stock, tracking pending price updates and sending follow-ups to suppliers, or giving you morning updates on new regulatory documents or price changes - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what chemical distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tuas Link 1 if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Megachem.",
        "ps_used": "Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Megachem."
      },
      "email_2": {
        "subject": "Kam Loon <> Seth",
        "body": "Hi Kam Loon,\n\nI did some digging into Megachem and had a few ideas on where we could save time:\n\n- Extract 99% accurate pricing from Megachem's diverse supplier lists.\n- Auto-update your systems with clean, ready-to-import pricing data.\n- Flag critical price changes and exceptions that humans miss.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing from Megachem's diverse supplier lists.",
          "Auto-update your systems with clean, ready-to-import pricing data.",
          "Flag critical price changes and exceptions that humans miss."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on chemical distribution",
        "body": "Hi Kam Loon,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate pricing data in Excel, clean and ready to import into your ERP, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Tuas Link 1 if that's easier!",
        "hook_used": "Fallback",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate pricing data in Excel, clean and ready to import into your ERP",
        "value_line_source": "Inferred from Chemicals Distributor industry context and general distribution pain points"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "Lionapex Equipment",
      "contact_name": "Lewis Ng",
      "contact_email": "lionapex@pacific.net.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Lewis,\n\nWe're building an AI assistant that's always one step ahead for SG industrial distribution companies.\n\nIt proactively checks in - running daily reconciliation of supplier price lists against your catalog, tracking missing price updates and sending automated follow-ups to suppliers, or giving you morning updates on supplier price changes impacting your margins - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Woodlands Industrial Park E1 if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Lionapex Equipment.",
        "ps_used": "Before our call, I can train our AI on your [their_doc_type] so you can see exactly what we'd catch for [company]."
      },
      "email_2": {
        "subject": "Lewis <> Seth",
        "body": "Hi Lewis,\n\nI did some digging into Lionapex Equipment and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from Lionapex's diverse supplier price lists.\n- Get audit-ready reconciliation of new supplier updates against your existing catalog.\n- Flag margin-eroding price discrepancies that humans miss across your product lines.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from Lionapex's diverse supplier price lists.",
          "Get audit-ready reconciliation of new supplier updates against your existing catalog.",
          "Flag margin-eroding price discrepancies that humans miss across your product lines."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Lewis,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back clean, ready to import pricing data in Excel, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Woodlands Industrial Park E1 if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and get back clean, ready to import pricing data in Excel",
        "value_line_source": "document_pain_analysis"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Lionapex Equipment, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Lewis,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Lionapex Equipment.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Woodlands Industrial Park E1 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Woodlands Industrial Park E1",
        "generated": true
      }
    },
    {
      "company_name": "GLAMCO AVIATION PTE LTD",
      "contact_name": "Justin Kho",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Congrats on the promotion to Managing Director - figured you'd have perspective on what the team needs. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "Promoted",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Justin,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Glamco Aviation.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Ruby Industrial Complex as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Ruby Industrial Complex",
        "generated": true
      }
    },
    {
      "company_name": "KONTAKT INTERNATIONAL PTE LTD",
      "contact_name": "Vinod Danani",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Kontakt International, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Vinod,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Kontakt International. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Ubi Avenue 1 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Ubi Avenue 1",
        "generated": true
      }
    },
    {
      "company_name": "Inout Enterprise",
      "contact_name": "Eric Yong",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Inout Enterprise, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Eric,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Inout Enterprise. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Harvest@Woodlands as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Harvest@Woodlands",
        "generated": true
      }
    },
    {
      "company_name": "Megachem",
      "contact_name": "Janhvi Mandhare",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 14+ years in the distribution industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Janhvi,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Megachem.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Tuas Link 1 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tuas Link 1",
        "generated": true
      }
    },
    {
      "company_name": "IGUS Singapore Pte Ltd",
      "contact_name": "Stephen Moreno",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 28+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Stephen,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like igus. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Genting Lane as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Genting Lane",
        "generated": true
      }
    },
    {
      "company_name": "LASER 21 PTE LTD",
      "contact_name": "Popoh Low",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Laser 21, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Popoh,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Laser 21.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Lam Soon Industrial Building as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Lam Soon Industrial Building",
        "generated": true
      }
    },
    {
      "company_name": "Ace Pressureweld International",
      "contact_name": "Nancy Ong",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Ace Pressureweld International, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Nancy,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Ace Pressureweld International.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Senoko Industrial Estate as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Senoko Industrial Estate",
        "generated": true
      }
    },
    {
      "company_name": "Lionapex Equipment",
      "contact_name": "Samuel Yap",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Lionapex Equipment, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Samuel,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Lionapex Equipment. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Woodlands Industrial Park E1 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Woodlands Industrial Park E1",
        "generated": true
      }
    },
    {
      "company_name": "Tong Seng Produce",
      "contact_name": "Max Ng",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Tong Seng Produce, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Max,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Tong Seng Produce.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Senoko South Road as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Senoko South Road",
        "generated": true
      }
    },
    {
      "company_name": "Yamazaki Mazak Singapore",
      "contact_name": "KS Chong",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed Yamazaki Mazak Singapore Mazak Singapore Open House 2025  -  Two Days of Innovation and Connection (Nov 7, 2025) - figured you'd have perspective on how operations are scaling. We've developed an AI assistant that handles back office work around the clock. Sending a voice note now to explain more!",
        "hook_used": "News",
        "generated": true
      },
      "voice_note": {
        "script": "Hi KS,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Yamazaki Mazak Singapore.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Joo Koon Circle as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Joo Koon Circle",
        "generated": true
      }
    },
    {
      "company_name": "VRV Global",
      "contact_name": "Yasuswini Subramanian",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at VRV Global, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Yasuswini,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like VRV Global. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Cecil Court as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Cecil Court",
        "generated": true
      }
    },
    {
      "company_name": "Welhunt",
      "contact_name": "Michael Selesnik",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Welhunt, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Michael,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Welhunt.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "none",
        "generated": true
      }
    },
    {
      "company_name": "DKSH Technology",
      "contact_name": "Hanno Elbraechter",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 38+ years in the distribution industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Hanno,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like DKSH Technology. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at New Tech Park as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "New Tech Park",
        "generated": true
      }
    },
    {
      "company_name": "SCL System Enterprise",
      "contact_name": "Eric Chew",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading SCL System Enterprise, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Eric,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like SCL System Enterprise. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Kong Beng Industrial Building as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Kong Beng Industrial Building",
        "generated": true
      }
    },
    {
      "company_name": "IDeall Solutionz",
      "contact_name": "Puja Gill Saxena",
      "contact_email": "ideallss@ideallss.com",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Puja,\n\nWe're building an AI assistant that's always one step ahead for SG distributors.It proactively checks in - running daily reconciliations of supplier price lists against your master catalog, tracking missing price updates and sending automated follow-ups, or giving you morning updates on critical price changes - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Excalibur Centre if that's easier!\n\nBest,\nSeth\n\nP.S. If you're juggling price lists from 50+ suppliers, I can show you how one distributor consolidated everything into a single update workflow.",
        "ps_used": "multiple_suppliers"
      },
      "email_2": {
        "subject": "Puja <> Seth",
        "body": "Hi Puja,\n\nI did some digging into IDeall Solutionz and had a few ideas on where we could save time:- Extract 99% accurate data from all your supplier price lists.- Auto-update IDeall Solutionz's ERP with clean, ready to import pricing.- Flag critical price changes from 50+ suppliers that humans miss.Have you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?If we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from all your supplier price lists.",
          "Auto-update IDeall Solutionz's ERP with clean, ready to import pricing.",
          "Flag critical price changes from 50+ suppliers that humans miss."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Puja,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.Given your 47+ years in the industry, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back audit-ready reconciliations in Excel showing current vs. old pricing and identified margin impacts, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Excalibur Centre if that's easier!",
        "hook_used": "10+ years",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and get back audit-ready reconciliations in Excel showing current vs. old pricing and identified margin impacts",
        "value_line_source": "document_pain_analysis"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 47+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Puja,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like IDeall Solutionz.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Excalibur Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Excalibur Centre",
        "generated": true
      }
    },
    {
      "company_name": "O S ELECTRONICS (S) PTE LTD",
      "contact_name": "Masayuki Miyahara",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed you recently took over as Director, Managing Executive Officer in June - figured you'd have perspective on what's working and what's not. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "New role",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Masayuki,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like OS Electronics.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Ingolstadt Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Ingolstadt Centre",
        "generated": true
      }
    },
    {
      "company_name": "Cairnhill Metrology",
      "contact_name": "Jeffrey Ong",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 19+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Jeffrey,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Cairnhill Metrology. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Petro Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Petro Centre",
        "generated": true
      }
    },
    {
      "company_name": "Beijer Ref Singapore",
      "contact_name": "Dennis Fong",
      "contact_email": "d****@beijerref.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Dennis,\n\nWe're building an AI assistant that's always one step ahead for SG industrial distributors.\n\nIt proactively checks in - running daily reconciliation of supplier price lists against your catalog, tracking missing lead time updates and sending follow-ups to suppliers, or giving you morning updates on new component price lists awaiting review - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tagore Lane if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Beijer Ref Singapore.",
        "ps_used": "generic training on their doc type"
      },
      "email_2": {
        "subject": "Dennis <> Seth",
        "body": "Hi Dennis,\n\nI did some digging into Beijer Ref Singapore and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from Beijer Ref's diverse component price lists.\n- Flag discrepancies in MOQ sheets to catch what humans miss before ordering.\n- Get complete, ready to review reports on lead time updates for better planning.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from Beijer Ref's diverse component price lists.",
          "Flag discrepancies in MOQ sheets to catch what humans miss before ordering.",
          "Get complete, ready to review reports on lead time updates for better planning."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Dennis,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back audit-ready reconciliation in Excel showing price differences, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Tagore Lane if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and get back audit-ready reconciliation in Excel showing price differences,",
        "value_line_source": "document_pain_analysis"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Beijer Ref Singapore, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Dennis,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Beijer Ref.\nThis isn't a sales call - just looking for your perspective.\nHappy to buy you lunch near your office at Tagore Lane as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tagore Lane",
        "generated": true
      }
    },
    {
      "company_name": "Crownfruit",
      "contact_name": "Marais Stephanus",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Crownfruit, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Marais,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Crownfruit. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Parkview Square as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Parkview Square",
        "generated": true
      }
    },
    {
      "company_name": "AT&S",
      "contact_name": "Richard",
      "contact_email": "**************@ksenergy.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Richard,\n\nWe're building an AI assistant that's always one step ahead for SG industrial distribution companies.\n\nIt proactively checks in - running daily reconciliation of supplier price lists against product catalogs, tracking missing certifications and sending follow-ups, or giving you morning updates on purchase orders awaiting approval - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Jurong Port Road if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for AT&S.",
        "ps_used": "Specific value demo from Generation Mode instructions (supplier price lists)"
      },
      "email_2": {
        "subject": "Richard <> Seth",
        "body": "Hi Richard,\n\nI did some digging into AT&S and had a few ideas on where we could save time:\n\n- Extract 99% accurate pricing data from AT&S's varied supplier price lists.\n- Flag discrepancies and auto-update your ERP with current product catalog prices.\n- Get audit-ready reports reconciling purchase orders with invoices for AT&S.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing data from AT&S's varied supplier price lists.",
          "Flag discrepancies and auto-update your ERP with current product catalog prices.",
          "Get audit-ready reports reconciling purchase orders with invoices for AT&S."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Richard,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nNoticed you're hiring for an Accounts Assistant - figured you'd have perspective on where the bottlenecks are.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate pricing data in Excel, ready to update your ERP, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Jurong Port Road if that's easier!",
        "hook_used": "Hiring (Accounts Assistant)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate pricing data in Excel, ready to update your ERP, would that be useful?",
        "value_line_source": "document_pain_analysis"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "SA Group",
      "contact_name": "Steve Jackson",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading SA Group, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Steve,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like SA Group.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Ang Mo Kio as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Ang Mo Kio",
        "generated": true
      }
    },
    {
      "company_name": "NICAD POWER PTE LTD",
      "contact_name": "Ng King",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Nicad Power, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi King,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Nicad Power. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Ubi Road 3 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Ubi Road 3",
        "generated": true
      }
    },
    {
      "company_name": "MELT-EX PTE LTD.",
      "contact_name": "Taner Kalan",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Melt-Ex, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Taner,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Melt-Ex.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Tras Street as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tras Street",
        "generated": true
      }
    },
    {
      "company_name": "LASER 21 PTE LTD",
      "contact_name": "Ching-Wat Chia",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Laser 21, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Ching-Wat,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Laser 21. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Lam Soon Industrial Building as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Lam Soon Industrial Building",
        "generated": true
      }
    },
    {
      "company_name": "JTU",
      "contact_name": "Jack Wong",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 39+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Jack,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like JTU. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Ubi Avenue 3 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Ubi Avenue 3",
        "generated": true
      }
    },
    {
      "company_name": "TDK Singapore",
      "contact_name": "Sandeep Pandya",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed TDK and Porsche Motorsport formed a technology partnership - figured you'd have perspective on how operations are scaling. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "News",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Sandeep,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like TDK Singapore. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at The Metropolis as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "The Metropolis",
        "generated": true
      }
    },
    {
      "company_name": "SA Group",
      "contact_name": "Tim Mister",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading SA Group, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Tim,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like SA Group. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Ang Mo Kio as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Ang Mo Kio",
        "generated": true
      }
    },
    {
      "company_name": "Ellipsiz Communications",
      "contact_name": "Sam Tan",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Ellipsiz Communications, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Sam,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Ellipsiz Communications.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at NorthTech Lobby as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "NorthTech Lobby",
        "generated": true
      }
    },
    {
      "company_name": "LASER 21 PTE LTD",
      "contact_name": "Ching Wat Chia",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Laser 21, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Ching Wat,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Laser 21.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Hillview Avenue as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Hillview Avenue",
        "generated": true
      }
    },
    {
      "company_name": "Spartan Bizcorp",
      "contact_name": "Nitin Khanchandani",
      "contact_email": "nitin@spartanbizcorp.com",
      "email_1": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Nitin,\n\nJust wanted to check in again in case this missed your inbox.\n\nWe're building an AI assistant that's always one step ahead. It proactively checks in - giving you morning updates on new supplier price lists, tracking inconsistencies between purchase orders and invoices, or running weekly audits on cross-border pricing compliance without you having to ask.\n\nCurious whether teams in distribution would actually use this from WhatsApp or email - would love your perspective if you have 15 mins.\n\nBest,\nSeth\n\nP.S. If you're juggling price lists from 50+ suppliers, I can show you how one distributor consolidated everything into a single update workflow.",
        "ps_used": "multiple_suppliers"
      },
      "email_2": {
        "subject": "Nitin <> Seth",
        "body": "Hi Nitin,\n\nI did some digging into Spartan Bizcorp and had a few ideas on where we could save time:\n\n- Extract 99% accurate pricing from any supplier format for Spartan Bizcorp.\n- Auto-update ERP/pricing systems and flag price changes instantly.\n- Generate complete, audit-ready quote sheets with real-time pricing for customers.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing from any supplier format for Spartan Bizcorp.",
          "Auto-update ERP/pricing systems and flag price changes instantly.",
          "Generate complete, audit-ready quote sheets with real-time pricing for customers."
        ]
      },
      "email_3": {
        "subject": "quick question on distribution",
        "body": "Hi Nitin,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate pricing data in Excel, ready for your systems, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at North Bridge Road if that's easier!",
        "hook_used": "Fallback (none)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate pricing data in Excel, ready for your systems, would that be useful?",
        "value_line_source": "document_pain_analysis"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Spartan Bizcorp, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Nitin,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Spartan Bizcorp. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at North Bridge Road as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "North Bridge Road",
        "generated": true
      }
    },
    {
      "company_name": "ZMC Technologies",
      "contact_name": "Lawrence Lee",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading ZMC Technologies, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Lawrence,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like ZMC Technologies. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Ubi Techpark as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Ubi Techpark",
        "generated": true
      }
    },
    {
      "company_name": "Delight OptoElectronics",
      "contact_name": "Prabhakar KS",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 26+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Prabhakar,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Delight OptoElectronics.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Sin Ming Lane as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Sin Ming Lane",
        "generated": true
      }
    },
    {
      "company_name": "Hafary Pte Ltd",
      "contact_name": "Lim Wah Fong",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 28+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Wah Fong,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Hafary. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Eunos as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Eunos",
        "generated": true
      }
    },
    {
      "company_name": "J.P. Electronics",
      "contact_name": "Sudha Ravindran",
      "contact_email": "sudha@jpegroup.com",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Sudha,\n\nWe're building an AI assistant that's always one step ahead for SG electronics distributors.\n\nIt proactively checks in - running daily reconciliation of supplier price lists against internal pricing, tracking missing supplier price updates and sending automated follow-ups, or giving you morning updates on critical price changes - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what electronics distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tai Seng Avenue if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for J.P. Electronics.",
        "ps_used": "Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for J.P. Electronics."
      },
      "email_2": {
        "subject": "Sudha <> Seth",
        "body": "Hi Sudha,\n\nI did some digging into J.P. Electronics and had a few ideas on where we could save time:\n\n- Extract 99% accurate pricing data from 50+ diverse supplier formats.\n- Flagging price changes that impact J.P. Electronics' margins automatically.\n- Generate complete, ready to review quote sheets with updated component prices.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "- Extract 99% accurate pricing data from 50+ diverse supplier formats.",
          "- Flagging price changes that impact J.P. Electronics' margins automatically.",
          "- Generate complete, ready to review quote sheets with updated component prices."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Sudha,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean, ready to import price updates in Excel, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Tai Seng Avenue if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean, ready to import price updates in Excel, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at J.P. Electronics, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Sudha,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like J.P. Electronics.\nThis isn't a sales call - just looking for your perspective.\nHappy to buy you lunch near your office at Tai Seng Avenue as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tai Seng Avenue",
        "generated": true
      }
    },
    {
      "company_name": "Tong Seng Produce",
      "contact_name": "Jerry Ng",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Tong Seng Produce, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Jerry,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Tong Seng Produce. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Senoko South Road as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Senoko South Road",
        "generated": true
      }
    },
    {
      "company_name": "Ingram Micro Asia",
      "contact_name": "Diego Utge",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Ingram Micro Asia, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Diego,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Ingram Micro Asia. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Kallang Bahru as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Kallang Bahru",
        "generated": true
      }
    },
    {
      "company_name": "GBS (Singapore)",
      "contact_name": "Bobby Bock",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 32+ years in the distribution industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Bobby,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like GBS (Singapore). This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Tampines North Drive 1 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tampines North Drive 1",
        "generated": true
      }
    },
    {
      "company_name": "FA Systems Automation",
      "contact_name": "Dr Chua Eng Hwa",
      "contact_email": "ch*******@fasystems.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Eng Hwa,\n\nWe're building an AI assistant that's always one step ahead for SG industrial/MRO distributors.\n\nIt proactively checks in - running daily reconciliation of purchase orders against supplier invoices, tracking outstanding engineering change notices and sending reminders, or giving you morning updates on critical component price list changes - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what industrial/MRO distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Changi South if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for FA Systems Automation.",
        "ps_used": "Document-specific value demo (supplier price lists)"
      },
      "email_2": {
        "subject": "Eng Hwa <> Seth",
        "body": "Hi Eng Hwa,\n\nI did some digging into FA Systems Automation and had a few ideas on where we could save time:\n\n- Extract 99% accurate component pricing from diverse supplier formats.\n- Get clean, ready-to-import BOM data for ERP auto-updates.\n- Flag discrepancies that humans miss in engineering change notices.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate component pricing from diverse supplier formats.",
          "Get clean, ready-to-import BOM data for ERP auto-updates.",
          "Flag discrepancies that humans miss in engineering change notices."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Eng Hwa,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and specifications and get back 99% accurate, clean data in Excel ready for your ERP system updates, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Changi South if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and specifications and get back 99% accurate, clean data in Excel ready for your ERP system updates",
        "value_line_source": "document_pain_analysis"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "SKLO",
      "contact_name": "Ming Thoo",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading SKLO, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Ming Thoo,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like SKLO.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Mandai Estate as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Mandai Estate",
        "generated": true
      }
    },
    {
      "company_name": "Megachem",
      "contact_name": "Yau Thiam Hwa",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 44+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Thiam Hwa,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Megachem.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Tuas as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tuas",
        "generated": true
      }
    },
    {
      "company_name": "IGUS Singapore Pte Ltd",
      "contact_name": "Carsten Haecker",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 26+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Carsten,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like igus.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Genting Lane as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Genting Lane",
        "generated": true
      }
    },
    {
      "company_name": "Globalink Electronics",
      "contact_name": "Audrey Chee",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Globalink Electronics, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Audrey,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Globalink Electronics.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Henderson Building as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Henderson Building",
        "generated": true
      }
    },
    {
      "company_name": "Ideal Technology",
      "contact_name": "Loh Chin Cheang",
      "contact_email": "***@idealtech.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Chin Cheang,\n\nWe're building an AI assistant that's always one step ahead for SG electronics distributors.\n\nIt proactively checks in - running daily reconciliation of supplier price lists against your current catalog, tracking missing price updates from key suppliers and sending follow-ups, or giving you morning updates on supplier price changes - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Jurong Gateway Road if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your a sample invoice so you can see exactly what we'd catch for Ideal Technology.",
        "ps_used": "Before our call, I can train our AI on your a sample invoice so you can see exactly what we'd catch for Ideal Technology."
      },
      "email_2": {
        "subject": "Chin Cheang <> Seth",
        "body": "Hi Chin Cheang,\n\nI did some digging into Ideal Technology and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from diverse supplier price lists for Ideal Technology.\n- Get audit-ready reconciliation of component pricing against sales orders.\n- Flag critical price changes that impact Ideal Technology's margins automatically.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from diverse supplier price lists for Ideal Technology.",
          "Get audit-ready reconciliation of component pricing against sales orders.",
          "Flag critical price changes that impact Ideal Technology's margins automatically."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Chin Cheang,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your documents and get back clean, ready to import pricing data in Excel, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Jurong Gateway Road if that's easier!",
        "hook_used": "Fallback",
        "value_line": "just email or WhatsApp an AI assistant your documents and get back clean, ready to import pricing data in Excel",
        "value_line_source": "document_pain_analysis (fallback) / company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Ideal Technology, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Chin Cheang,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Ideal Technology.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Jurong Gateway Road as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Jurong Gateway Road",
        "generated": true
      }
    },
    {
      "company_name": "Yamazaki Mazak Singapore",
      "contact_name": "Mr. Lee",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed Yamazaki Mazak Singapore's Open House 2025 and the launch of the QRX Series - figured you'd have perspective on how operations are scaling. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "News",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Lee,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Mazak Singapore. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Joo Koon Circle as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Joo Koon Circle",
        "generated": true
      }
    },
    {
      "company_name": "JSB Tech",
      "contact_name": "Jim Li Hui Hong",
      "contact_email": "jimhhli@jsbtech.com",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Jim,\n\nWe're building an AI assistant that's always one step ahead for SG electronics distributors.\n\nIt proactively checks in - running daily reconciliations of supplier price lists against internal catalogs, tracking overdue supplier price updates and sending follow-ups, or giving you morning updates on critical component price changes - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Pasir Panjang Road if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for JSB Tech.",
        "ps_used": "supplier price lists"
      },
      "email_2": {
        "subject": "Jim <> Seth",
        "body": "Hi Jim,\n\nI did some digging into JSB Tech and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from diverse supplier price lists.\n- Flag critical component price changes for JSB Tech instantly.\n- Auto-update your pricing systems with clean, ready-to-import data.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from diverse supplier price lists.",
          "Flag critical component price changes for JSB Tech instantly.",
          "Auto-update your pricing systems with clean, ready-to-import data."
        ]
      },
      "email_3": {
        "subject": "quick question on distribution",
        "body": "Hi Jim,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back audit-ready reconciliation of supplier price lists against internal pricing in Excel, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Pasir Panjang Road if that's easier!",
        "hook_used": "Fallback (Given your experience in {industry_short})",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back audit-ready reconciliation of supplier price lists against internal pricing in Excel",
        "value_line_source": "document_pain_analysis"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at JSB Tech, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "Fallback (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Jim,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like JSB Tech.\nThis isn't a sales call - just looking for your perspective.\nHappy to buy you lunch near your office at Pasir Panjang Road as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Pasir Panjang Road",
        "generated": true
      }
    },
    {
      "company_name": "SKLO",
      "contact_name": "Thoo Lee Ming",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at SKLO, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Lee Ming,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like SKLO.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Mandai Estate as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Mandai Estate",
        "generated": true
      }
    },
    {
      "company_name": "Bijon Corporation",
      "contact_name": "Domenic Ng",
      "contact_email": "N/A",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Domenic,\n\n\\n\\nWe're building an AI assistant that's always one step ahead for SG distributors.\\n\\nIt proactively checks in - running daily reconciliations of supplier invoices and POs, tracking outdated price lists and flagging discrepancies, or giving you morning updates on key component price changes - all without you having to ask.\\n\\n\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\\n\\n\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\\n\\n\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Bedok North if that's easier!\\n\\n\n\nBest,\\nSeth\\n\\n\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Bijon Corporation.",
        "ps_used": "document-specific AI training demo"
      },
      "email_2": {
        "subject": "Domenic <> Seth",
        "body": "Hi Domenic,\n\n\\n\\nI did some digging into Bijon Corporation and had a few ideas on where we could save time:\\n\\n- Extract 99% accurate data from diverse supplier price lists.\\n- Auto-update your ERP with audit-ready pricing, saving hours weekly.\\n- Flag critical price changes for Bijon Corporation that humans miss.\\n\\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\\n\\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\\n\\n\n\nBest,\\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from diverse supplier price lists.",
          "Auto-update your ERP with audit-ready pricing, saving hours weekly.",
          "Flag critical price changes for Bijon Corporation that humans miss."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Domenic,\n\n\\n\\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\\n\\nGiven your experience in distribution, I was hoping to get your opinion.\\n\\n\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\\n\\n\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\\n\\n\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\\n\\n\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and component specifications and get back all your supplier price list data as clean, ready to import Excel, would that be useful?\\n\\n\n\nWould you be open to a quick chat to point us in the right direction?\\n\\n\n\nBest,\\nSeth\\n\\n\n\nP.S. Happy to drop by your office at Bedok North if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and component specifications and get back all your supplier price list data as clean, ready to import Excel, would that be useful?",
        "value_line_source": "document_pain_analysis and company_profile"
      },
      "linkedin_message": {
        "message": "",
        "hook_used": "",
        "generated": false
      },
      "voice_note": {
        "script": "",
        "location_used": "",
        "generated": false
      }
    },
    {
      "company_name": "Woah Group",
      "contact_name": "Ashley Bai",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Woah Group, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Ashley,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Woah Group. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "none",
        "generated": true
      }
    },
    {
      "company_name": "Avani Resources Pte. Ltd.",
      "contact_name": "Ujjwal Jain",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Avani Resources, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Ujjwal,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Avani Resources.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Cecil Street as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Cecil Street",
        "generated": true
      }
    },
    {
      "company_name": "Bentz Jaz Group",
      "contact_name": "Allen Heng",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Bentz Jaz, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Allen,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Bentz Jaz.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Enterprise Hub as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Enterprise Hub",
        "generated": true
      }
    },
    {
      "company_name": "SP Muthiah & Sons",
      "contact_name": "Selvarathenam Muthiah",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading SP Muthiah & Sons, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Selvarathenam,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like SP Muthiah & Sons. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Eunos Technolink as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Eunos Technolink",
        "generated": true
      }
    },
    {
      "company_name": "Azurati Pte Ltd",
      "contact_name": "Kenneth Asuncion",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 11+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Kenneth,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Azurati.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Loyang Lane as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Loyang Lane",
        "generated": true
      }
    },
    {
      "company_name": "Megachem Limited",
      "contact_name": "Debbie Bowkett",
      "contact_email": "enquiry@uk.megachem.com",
      "email_1": {
        "subject": "quick question on chemical distribution",
        "body": "Hi Debbie,\n\nWe're building an AI assistant that's always one step ahead for SG chemical distributors.\n\nIt proactively checks in - running daily checks for outdated supplier pricing against sales orders, tracking missing price lists and sending automated reminders to suppliers, or giving you morning updates on new supplier price list versions - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what chemical distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tuas Link 1 if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Megachem Limited.",
        "ps_used": "Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Megachem Limited."
      },
      "email_2": {
        "subject": "Debbie <> Seth",
        "body": "Hi Debbie,\n\nI did some digging into Megachem Limited and had a few ideas on where we could save time:\n\n- Extract 99% accurate pricing from diverse supplier formats for Megachem.\n- Auto-update your ERP/pricing systems with audit-ready supplier changes.\n- Flag crucial price changes and exceptions that humans might miss.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing from diverse supplier formats for Megachem.",
          "Auto-update your ERP/pricing systems with audit-ready supplier changes.",
          "Flag crucial price changes and exceptions that humans might miss."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on chemical distribution",
        "body": "Hi Debbie,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back clean, ready to import supplier pricing data in Excel for your ERP, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Tuas Link 1 if that's easier!",
        "hook_used": "Fallback (from template)",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and get back clean, ready to import supplier pricing data in Excel for your ERP",
        "value_line_source": "Derived from Industry Context and classification_category"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "VOLTRIUM SYSTEMS PTE LTD",
      "contact_name": "Kenny Goh",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Voltrium Systems, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Kenny,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Voltrium Systems. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Win 5 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Win 5",
        "generated": true
      }
    },
    {
      "company_name": "Panasonic System Solutions Asia Pacific",
      "contact_name": "Hiroaki Sakamoto",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Panasonic System Solutions Asia Pacific, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Hiroaki,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Panasonic System Solutions Asia Pacific. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "none",
        "generated": true
      }
    },
    {
      "company_name": "Yappy Pets Pte Ltd",
      "contact_name": "Yap Seng Teck",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Yappy Pets, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Seng Teck,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Yappy Pets. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Loyang Way 1 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Loyang Way 1",
        "generated": true
      }
    },
    {
      "company_name": "Knight Auto Precision Engineering",
      "contact_name": "Fatt Chye Low",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Knight Auto Precision Engineering, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Fatt Chye,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Knight Auto Precision Engineering. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "None",
        "generated": true
      }
    },
    {
      "company_name": "Asaiki",
      "contact_name": "Benjamin Yap",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Asaiki, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Benjamin,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Asaiki. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Harvest @ Woodlands as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Harvest @ Woodlands",
        "generated": true
      }
    },
    {
      "company_name": "INOUT ENTERPRISE PTE LTD",
      "contact_name": "Jeffrey Heng",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Inout Enterprise, I was hoping to get your opinion. Sent you a voice note about our idea for a WhatsApp AI assistant that does back office work around the clock in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Jeffrey,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Inout Enterprise. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Harvest@Woodlands as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Harvest@Woodlands",
        "generated": true
      }
    },
    {
      "company_name": "Masstron",
      "contact_name": "Ng Kuo Wei Alain",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Masstron, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Kuo Wei Alain,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Masstron.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Fifth Lok Yang Road as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Fifth Lok Yang Road",
        "generated": true
      }
    },
    {
      "company_name": "Le Bono Collection",
      "contact_name": "Scott Larsen",
      "contact_email": "scottlarsen@gmail.com",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Scott,\n\nWe're building an AI assistant that's always one step ahead for SG distributors.\n\nIt proactively checks in - running daily reconciliation of supplier price lists against your master catalog, tracking missing supplier updates and sending automated follow-ups, or giving you morning updates on supplier price changes - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Aljunied Rd if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Le Bono Collection.",
        "ps_used": "Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Le Bono Collection."
      },
      "email_2": {
        "subject": "Scott <> Seth",
        "body": "Hi Scott,\n\nI did some digging into Le Bono Collection and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from your diverse supplier price lists.\n- Get audit-ready reconciliation of supplier invoices against purchase orders.\n- Flag price changes that humans miss across Le Bono Collection's catalog.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from your diverse supplier price lists.",
          "Get audit-ready reconciliation of supplier invoices against purchase orders.",
          "Flag price changes that humans miss across Le Bono Collection's catalog."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Scott,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your 31+ years in the industry, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back clean, ready to import pricing data in Excel, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Aljunied Rd if that's easier!",
        "hook_used": "10+ years",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back clean, ready to import pricing data in Excel, would that be useful?",
        "value_line_source": "document_pain_analysis and company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 31+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Scott,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Le Bono Collection.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Aljunied Rd as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Aljunied Rd",
        "generated": true
      }
    },
    {
      "company_name": "Sonepar Singapore",
      "contact_name": "Darren Koh",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Sonepar Singapore, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Darren,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Sonepar Singapore.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Eunos Ave 3 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Eunos Ave 3",
        "generated": true
      }
    },
    {
      "company_name": "ETONG Aluminium Engineering",
      "contact_name": "C CHEN LIXIN",
      "contact_email": "etong.chenlixin@gmail.com",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Lixin,\n\n We're building an AI assistant that's always one step ahead for SG building materials distributors. It proactively checks in - running daily reconciliation of supplier invoices against purchase orders, tracking pending change orders and flagging budget variances, or giving you morning updates on critical material price changes - all without you having to ask. \n\nYou just WhatsApp or email it instructions and it does your back office work around the clock. \n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference. \n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Enterprise Hub if that's easier! \n\nBest,\nSeth \n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for ETONG Aluminium Engineering.",
        "ps_used": "Before call, train AI on their docs (from Email 1 template in Generation Mode section)"
      },
      "email_2": {
        "subject": "Lixin <> Seth",
        "body": "Hi Lixin,\n\n I did some digging into ETONG Aluminium Engineering and had a few ideas on where we could save time: - Extract 99% accurate pricing from diverse supplier catalogs to prevent margin erosion. - Get audit-ready reconciliation of supplier invoices against POs for faster AP. - Flag discrepancies in change orders that humans miss for accurate project billing. Have you solved for keeping supplier pricing current across your catalog or is your team still doing it manually? If we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting? \n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing from diverse supplier catalogs to prevent margin erosion.",
          "Get audit-ready reconciliation of supplier invoices against POs for faster AP.",
          "Flag discrepancies in change orders that humans miss for accurate project billing."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Lixin,\n\n My co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes. Given your experience in distribution, I was hoping to get your opinion. \n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs. \n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference. \n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call. \n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean data in Excel ready to import into your ERP, would that be useful? \n\nWould you be open to a quick chat to point us in the right direction? \n\nBest,\nSeth \n\nP.S. Happy to drop by your office at Enterprise Hub if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean data in Excel ready to import into your ERP",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "HH Group",
      "contact_name": "Daniel Low",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at HH Group, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Daniel,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like HH Group.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Gul Crescent as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Gul Crescent",
        "generated": true
      }
    },
    {
      "company_name": "JJ-LAPP",
      "contact_name": "Marc von Grabowski",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 26+ years in the distribution industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Marc,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like JJ-LAPP.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Corporation Place as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Corporation Place",
        "generated": true
      }
    },
    {
      "company_name": "UCHEM TECHNOLOGIES PTE LTD",
      "contact_name": "Koh B.",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Uchem Technologies, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi B.,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Uchem Technologies. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Tuas Road as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tuas Road",
        "generated": true
      }
    },
    {
      "company_name": "Chip Guan Heng",
      "contact_name": "Kenneth Goh",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Chip Guan Heng, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Kenneth,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Chip Guan Heng.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Joo Chiat Place as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Joo Chiat Place",
        "generated": true
      }
    },
    {
      "company_name": "LEEPORT (SINGAPORE) PTE LTD",
      "contact_name": "Patrick Lee",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed Leeport Singapore announced a joint venture with Vaski Group to strengthen its global distribution network - figured you'd have perspective on how operations are scaling. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "News",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Patrick,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Leeport.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Sindo Building as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Sindo Building",
        "generated": true
      }
    },
    {
      "company_name": "Kowa Asia Pacific",
      "contact_name": "S Adachi",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Kowa Asia Pacific, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Adachi,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Kowa Asia Pacific. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Collyer Quay Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Collyer Quay Centre",
        "generated": true
      }
    },
    {
      "company_name": "Megachem",
      "contact_name": "Jeffrey Tan Bock Chia",
      "contact_email": "JYTAN@sg.megachem.com",
      "email_1": {
        "subject": "quick question on chemical distribution",
        "body": "Hi Jeffrey,\n\nWe're building an AI assistant that's always one step ahead for SG chemical distributors.\n\nIt proactively checks in - running daily reconciliation of supplier price lists against internal records, tracking missing MSDS updates and sending automated follow-ups, or giving you morning updates on critical chemical pricing changes - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what chemical distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tuas Link 1 if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your chemical price lists with specs so you can see exactly what we'd catch for Megachem.",
        "ps_used": "Before our call, I can train our AI on your chemical price lists with specs so you can see exactly what we'd catch for Megachem."
      },
      "email_2": {
        "subject": "Jeffrey <> Seth",
        "body": "Hi Jeffrey,\n\nI did some digging into Megachem and had a few ideas on where we could save time:\n\n- Extract 99% accurate pricing data from all supplier formats for Megachem.\n- Flag critical price changes and exceptions on supplier lists automatically.\n- Generate audit-ready reports on price history and trends for better negotiation.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing data from all supplier formats for Megachem.",
          "Flag critical price changes and exceptions on supplier lists automatically.",
          "Generate audit-ready reports on price history and trends for better negotiation."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on chemical distribution",
        "body": "Hi Jeffrey,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your 25+ years in the industry, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your chemical price lists and MSDS updates and get back an audit-ready reconciliation of all your supplier price lists in Excel, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Tuas Link 1 if that's easier!",
        "hook_used": "10+ years experience",
        "value_line": "just email or WhatsApp an AI assistant your chemical price lists and MSDS updates and get back an audit-ready reconciliation of all your supplier price lists in Excel",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 25+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years experience",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Jeffrey,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Megachem.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Tuas Link 1 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tuas Link 1",
        "generated": true
      }
    },
    {
      "company_name": "Only Olive Oil - Vas & Sav Trading",
      "contact_name": "Agus Rahardja",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Only Olive Oil - Vas & Sav Trading, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Agus,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Only Olive Oil - Vas & Sav Trading. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Tampines Ave 5 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tampines Ave 5",
        "generated": true
      }
    },
    {
      "company_name": "Uni-Stat Technology",
      "contact_name": "Peter Tang",
      "contact_email": "peter@unistat.com.sg",
      "email_1": {
        "subject": "quick question on industrial distribution",
        "body": "Hi Peter,\n\n We're building an AI assistant that's always one step ahead for SG industrial distribution companies. It proactively checks in - providing daily reconciliation of supplier price lists against current stock for accurate quotes, tracking discrepancies in modular workbench configurations for customer orders, or giving you morning updates on incoming supplier price changes - all without you having to ask. \n\nYou just WhatsApp or email it instructions and it does your back office work around the clock. \n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what industrial distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference. \n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tannery Lane if that's easier! \n\nBest,\nSeth \n\nP.S. Before our call, I can train our AI on your supplier price lists and product catalogs so you can see exactly what we'd catch for Uni-Stat Technology.",
        "ps_used": "Before our call, I can train our AI on your supplier price lists and product catalogs so you can see exactly what we'd catch for Uni-Stat Technology."
      },
      "email_2": {
        "subject": "Peter <> Seth",
        "body": "Hi Peter,\n\n I did some digging into Uni-Stat Technology and had a few ideas on where we could save time: - Extract 99% accurate data from all Uni-Stat's supplier price lists in minutes. - Get audit-ready reconciliation of supplier costs against ERP for better margins. - Flag discrepancies that humans miss in complex modular workbench BOMs. Have you solved for keeping supplier pricing current across your catalog or is your team still doing it manually? If we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting? \n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from all Uni-Stat's supplier price lists in minutes.",
          "Get audit-ready reconciliation of supplier costs against ERP for better margins.",
          "Flag discrepancies that humans miss in complex modular workbench BOMs."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on industrial distribution",
        "body": "Hi Peter,\n\n My co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes. Given your experience in distribution, I was hoping to get your opinion. \n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs. \n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference. \n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call. \n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back audit-ready pricing data in Excel, integrated into your systems, would that be useful? \n\nWould you be open to a quick chat to point us in the right direction? \n\nBest,\nSeth \n\nP.S. Happy to drop by your office at Tannery Lane if that's easier!",
        "hook_used": "Fallback",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back audit-ready pricing data in Excel, integrated into your systems, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "ACEPLAS PTE LTD",
      "contact_name": "Peter Koh",
      "contact_email": "*********@aceplas.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Peter,\n\nWe're building an AI assistant that's always one step ahead for SG distribution companies.\n\nIt proactively checks in - running daily reconciliation of supplier invoices against purchase orders, tracking missing price updates from key suppliers and following up, or giving you morning updates on critical product data needing validation - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Midview City if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Aceplas.",
        "ps_used": "Customized based on document_pain_analysis for supplier price lists"
      },
      "email_2": {
        "subject": "Peter <> Seth",
        "body": "Hi Peter,\n\nI did some digging into Aceplas and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from all your supplier price lists in any format.\n- Flag critical price changes and exceptions across all your SKUs for Aceplas.\n- Generate complete, ready-to-review margin reports based on the latest costs.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from all your supplier price lists in any format.",
          "Flag critical price changes and exceptions across all your SKUs for Aceplas.",
          "Generate complete, ready-to-review margin reports based on the latest costs."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Peter,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your 20+ years in the distribution industry, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate and normalized pricing data in Excel ready to update your ERP, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Midview City if that's easier!",
        "hook_used": "10+ years",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate and normalized pricing data in Excel ready to update your ERP",
        "value_line_source": "document_pain_analysis and company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "Vallen Asia",
      "contact_name": "Andrew Bennett",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed Vallen Asia's recent management buyout - figured you'd have perspective on how operations are scaling. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "News",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Andrew,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Vallen Asia. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Eunos as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Eunos",
        "generated": true
      }
    },
    {
      "company_name": "Edmund Optics Singapore",
      "contact_name": "Wilhelmus Messelink",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed Edmund Optics announced key executive appointments to drive growth, signalling scaling of operations - figured you'd have perspective on how operations are scaling. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "News",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Wilhelmus,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Edmund Optics. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Woodlands Loop as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Woodlands Loop",
        "generated": true
      }
    },
    {
      "company_name": "Seastarr International",
      "contact_name": "Masked Name",
      "contact_email": "****@seastarr.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Masked,\n\nWe're building an AI assistant that's always one step ahead for SG distribution companies.It proactively checks in - giving you morning updates on supplier price changes, tracking expiring price agreements and prompting renewals, or running weekly audits on catalog pricing accuracy - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at International Plaza if that's easier!\n\nBest,\nSeth\n\nP.S. With commodity prices moving weekly, I can show you how to get supplier updates into your system same-day instead of waiting for manual entry.",
        "ps_used": "commodity_exposure"
      },
      "email_2": {
        "subject": "Masked <> Seth",
        "body": "Hi Masked,\n\nI did some digging into Seastarr International and had a few ideas on where we could save time:- Get 99% accurate extraction from all your diverse supplier price list formats.- Flag all critical price changes from suppliers, catching what humans miss for Seastarr International.- Auto-update your internal systems so sales generates quotes with current, competitive pricing.Have you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?If we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Get 99% accurate extraction from all your diverse supplier price list formats.",
          "Flag all critical price changes from suppliers, catching what humans miss for Seastarr International.",
          "Auto-update your internal systems so sales generates quotes with current, competitive pricing."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Masked,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.Given your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate pricing data in Excel, ready for your ERP, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at International Plaza if that's easier!",
        "hook_used": "Fallback",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate pricing data in Excel, ready for your ERP, would that be useful?",
        "value_line_source": "document_pain_analysis and company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "Central-Midori International",
      "contact_name": "Joseph Juay",
      "contact_email": "joseph.juay@central-midori.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Joseph,\n\n We're building an AI assistant that's always one step ahead for SG electronics distributors. It proactively checks in - running daily reconciliation of supplier quotes against internal BOMs, tracking missing Certificates of Conformity and sending automated follow-ups, or giving you morning updates on critical engineering change notices awaiting approval - all without you having to ask. \n\nYou just WhatsApp or email it instructions and it does your back office work around the clock. \n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference. \n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Ayer Rajah Crescent if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your Certificates of Conformity so you can see exactly what we'd catch for Central-Midori International.",
        "ps_used": "Custom \n\nP.S. from Email 1 template"
      },
      "email_2": {
        "subject": "Joseph <> Seth",
        "body": "Hi Joseph,\n\nI did some digging into Central-Midori International and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from complex supplier component price lists in seconds.\n- Flag critical price changes that humans miss before they impact Central-Midori International's margins.\n- Get complete, ready-to-review reports on lead time updates consolidated from all suppliers.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from complex supplier component price lists in seconds.",
          "Flag critical price changes that humans miss before they impact Central-Midori International's margins.",
          "Get complete, ready-to-review reports on lead time updates consolidated from all suppliers."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Joseph,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier quotes and purchase orders and get back audit-ready reconciliation in Excel showing discrepancies and cost impacts, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Ayer Rajah Crescent if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier quotes and purchase orders and get back audit-ready reconciliation in Excel showing discrepancies and cost impacts, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "QT Instruments",
      "contact_name": "Hung Tran Ngoc",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at QT Instruments, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "Fallback",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Hung,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like QT Instruments. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Pasir Panjang as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Pasir Panjang",
        "generated": true
      }
    },
    {
      "company_name": "Snorre Food Pte Ltd",
      "contact_name": "Frank Arne Naesheim",
      "contact_email": "frank@snorrefood.com.sg",
      "email_1": {
        "subject": "quick question on F&B distribution",
        "body": "Hi Frank Arne,\n\nWe're building an AI assistant that's always one step ahead for SG F&B distributors.\n\nIt proactively checks in - running daily reconciliation of supplier price lists against your current catalog, tracking missing supplier price updates and sending follow-ups, or giving you morning updates on critical product pricing changes - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what F&B distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Fishery Port Road if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Snorre Food.",
        "ps_used": "Before the call, I can train our AI on your [their_doc_type] so you can see exactly what we'd catch for [company]. (Default option used due to lack of specific PS signals.)"
      },
      "email_2": {
        "subject": "Frank Arne <> Seth",
        "body": "Hi Frank Arne,\n\nI did some digging into Snorre Food and had a few ideas on where we could save time:\n\n- Extract 99% accurate pricing from Snorre Food's 50+ supplier price lists.\n- Auto-update your catalog and flag margin-eroding price changes.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing from Snorre Food's 50+ supplier price lists.",
          "Auto-update your catalog and flag margin-eroding price changes."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on F&B distribution",
        "body": "Hi Frank Arne,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nNoticed Snorre Food showcased at Seafood Expo Asia 2025 - figured you'd have perspective on how operations are scaling.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back audit-ready reconciliations in Excel showing current vs. old pricing, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Fishery Port Road if that's easier!",
        "hook_used": "News",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back audit-ready reconciliations in Excel showing current vs. old pricing, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "DEVICE ELECTRONICS PTE LTD",
      "contact_name": "Thomas Ng",
      "contact_email": "********@devicelect.com",
      "email_1": {
        "subject": "quick question on electronics distribution",
        "body": "Hi Thomas,\n\nWe're building an AI assistant that's always one step ahead for SG electronics distributors.\n\nIt proactively checks in - running daily reconciliations of supplier price lists against your internal catalog, tracking overdue supplier price updates and sending reminders, or giving you morning updates on new product additions from key suppliers - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what electronics distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at 8 Kaki Bukit Ave 1 if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Device Electronics.",
        "ps_used": "Derived from document_pain_analysis (supplier price lists)"
      },
      "email_2": {
        "subject": "Thomas <> Seth",
        "body": "Hi Thomas,\n\nI did some digging into Device Electronics and had a few ideas on where we could save time:\n\n- Get 99% accurate extraction of supplier price list data for Device Electronics.\n- Flag discrepancies in Panduit and Teledyne Relays pricing that impact margins.\n- Auto-update your online catalog with complete, ready-to-review new product details.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Get 99% accurate extraction of supplier price list data for Device Electronics.",
          "Flag discrepancies in Panduit and Teledyne Relays pricing that impact margins.",
          "Auto-update your online catalog with complete, ready-to-review new product details."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on electronics distribution",
        "body": "Hi Thomas,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back clean, ready to import pricing data into your catalog systems, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at 8 Kaki Bukit Ave 1 if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back clean, ready to import pricing data into your catalog systems, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Device Electronics, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Thomas,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Device Electronics.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at 8 Kaki Bukit Ave 1 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "8 Kaki Bukit Ave 1",
        "generated": true
      }
    },
    {
      "company_name": "Dashmesh Singapore",
      "contact_name": "Dawn",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Dashmesh Singapore, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Dawn,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Dashmesh Singapore. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Penjuru Lane as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Penjuru Lane",
        "generated": true
      }
    },
    {
      "company_name": "Ritchmen (S) Pte Ltd",
      "contact_name": "Jesse Guo",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Ritchmen, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Jesse,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Ritchmen.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Ang Mo Kio Street 62 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Ang Mo Kio Street 62",
        "generated": true
      }
    },
    {
      "company_name": "PHOENIX MECANO S.E.ASIA PTE LTD",
      "contact_name": "T. J. Ou",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Phoenix Mecano S.E. Asia, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi T. J.,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Phoenix Mecano S.E. Asia.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Travelite Building as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Travelite Building",
        "generated": true
      }
    },
    {
      "company_name": "AceCom Technologies",
      "contact_name": "Kee Lin Tan",
      "contact_email": "kee*******@acecom.com.sg",
      "email_1": {
        "subject": "quick question on electronics distribution",
        "body": "Hi Kee Lin,\n\nWe're building an AI assistant that's always one step ahead for SG electronics distributors.\n\nIt proactively checks in - running daily reconciliation of supplier invoices against purchase orders, tracking missing supplier price updates and sending follow-ups, or giving you morning updates on catalog price discrepancies - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what electronics distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at BHCC Space if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for AceCom Technologies.",
        "ps_used": "Before the call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for AceCom Technologies."
      },
      "email_2": {
        "subject": "Kee Lin <> Seth",
        "body": "Hi Kee Lin,\n\nI did some digging into AceCom Technologies and had a few ideas on where we could save time:\n\n- Extract 99% accurate pricing from all AceCom supplier formats to eliminate manual re-keying.\n- Auto-update 50,000+ SKU prices in your systems daily, saving days each month.\n- Flag price discrepancies that humans miss on incoming supplier invoices.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing from all AceCom supplier formats to eliminate manual re-keying.",
          "Auto-update 50,000+ SKU prices in your systems daily, saving days each month.",
          "Flag price discrepancies that humans miss on incoming supplier invoices."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on electronics distribution",
        "body": "Hi Kee Lin,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your 25+ years in the industry, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and catalogs and get back 99% accurate data in Excel ready to update your ERP systems, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at BHCC Space if that's easier!",
        "hook_used": "10+ years experience",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and catalogs and get back 99% accurate data in Excel ready to update your ERP systems, would that be useful?",
        "value_line_source": "document_pain_analysis/company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading AceCom Technologies, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Kee Lin,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like AceCom Technologies.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at BHCC Space as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "BHCC Space",
        "generated": true
      }
    },
    {
      "company_name": "Stainless Structurals Asia Pte Ltd",
      "contact_name": "Juerg Schweizer",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Stainless Structurals Asia, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Juerg,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Stainless Structurals Asia. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Tuas Avenue as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tuas Avenue",
        "generated": true
      }
    },
    {
      "company_name": "Air Liquide Singapore",
      "contact_name": "Xi",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Air Liquide Singapore, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Xi,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Air Liquide Singapore.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Vision Exchange as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Vision Exchange",
        "generated": true
      }
    },
    {
      "company_name": "Santak Electronics",
      "contact_name": "Weng Wei Ng",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Saw your recognition for the Senior Accredited Board Director badge by Singapore Institute of Directors - figured you'd have perspective on this. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "Awards",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Weng Wei,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Santak Electronics. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Clementi Loop as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Clementi Loop",
        "generated": true
      }
    },
    {
      "company_name": "Le Champ (South East Asia)",
      "contact_name": "Hirai",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Le Champ, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Hirai,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Le Champ.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Jalan Mesin as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Jalan Mesin",
        "generated": true
      }
    },
    {
      "company_name": "Snorre Food",
      "contact_name": "Valerie Kuah",
      "contact_email": "valerie@snorrefood.com.sg",
      "email_1": {
        "subject": "quick question on food & beverage distribution",
        "body": "Hi Valerie,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your 21+ years in the industry, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back audit-ready reconciliation of your supplier price changes in Excel, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Fishery Port Road if that's easier!",
        "ps_used": "Happy to drop by your office at {location} if that's easier! (from template, Fishery Port Road used for location)"
      },
      "email_2": {
        "subject": "Re: quick question on food & beverage distribution",
        "body": "Hi Valerie,\n\nJust wanted to check in again in case this missed your inbox.\n\nWe're building an AI assistant that's always one step ahead. It proactively checks in - giving you morning updates on critical price changes across your catalog, tracking missing quality certificates for incoming shipments and sending follow-ups, or running daily reconciliation of supplier price lists against current stock and customer orders - all without you having to ask.\n\nCurious whether teams in food & beverage distribution would actually use this from WhatsApp or email - would love your perspective if you have 15 mins.\n\nBest,\nSeth\n\nP.S. If you're juggling price lists from 50+ suppliers, I can show you how one distributor consolidated everything into a single update workflow.",
        "ideas_used": [
          "giving you morning updates on critical price changes across your catalog",
          "tracking missing quality certificates for incoming shipments and sending follow-ups",
          "running daily reconciliation of supplier price lists against current stock and customer orders"
        ]
      },
      "email_3": {
        "subject": "Valerie <> Seth",
        "body": "Hi Valerie,\n\nI did some digging into Snorre Food and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from your diverse supplier price lists.\n- Auto-update your catalog and flag price changes across thousands of SKUs.\n- Generate audit-ready quote sheets with real-time pricing for customers.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "hook_used": "10+ years experience",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back audit-ready reconciliation of your supplier price changes in Excel, would that be useful?",
        "value_line_source": "document_pain_analysis and company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 21+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years experience",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Valerie,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Snorre Food.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Fishery Port Road as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Fishery Port Road",
        "generated": true
      }
    },
    {
      "company_name": "Flexspeed Technology",
      "contact_name": "Hai Kiang",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 23+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Hai Kiang,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Flexspeed Technology.\nThis isn't a sales call - just looking for your perspective.\nHappy to buy you lunch near your office at Woodlands Industrial Xchange as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Woodlands Industrial Xchange",
        "generated": true
      }
    },
    {
      "company_name": "Pactumax International",
      "contact_name": "Joe Chik",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Pactumax International, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Joe,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Pactumax International. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Kaki Bukit as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Kaki Bukit",
        "generated": true
      }
    },
    {
      "company_name": "Beijer Ref Singapore",
      "contact_name": "William Ho",
      "contact_email": "w**@beijerref.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi William,\n\nWe're building an AI assistant that's always one step ahead for SG distributors.\n\nIt proactively checks in - running daily reconciliation of supplier invoices vs. orders, tracking missing supplier price updates and sending follow-ups, or giving you morning updates on refrigeration equipment price changes - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tagore Lane if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Beijer Ref Singapore.",
        "ps_used": "train AI on their_doc_type"
      },
      "email_2": {
        "subject": "William <> Seth",
        "body": "Hi William,\n\nI did some digging into Beijer Ref Singapore and had a few ideas on where we could save time:\n\n- Extract 99% accurate pricing data from Beijer Ref's diverse supplier lists.\n- Flag commodity price changes impacting your refrigeration component margins.\n- Auto-update your sales quoting system with current supplier pricing.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing data from Beijer Ref's diverse supplier lists.",
          "Flag commodity price changes impacting your refrigeration component margins.",
          "Auto-update your sales quoting system with current supplier pricing."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi William,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back audit-ready updates on price changes in Excel, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Tagore Lane if that's easier!",
        "hook_used": "Fallback (none)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back audit-ready updates on price changes in Excel, would that be useful?",
        "value_line_source": "document_pain_analysis + company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "Avani Resources Pte. Ltd.",
      "contact_name": "Garima P.",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Avani Resources, I was hoping to get your opinion. Connecting about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Garima,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Avani Resources. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Cecil Street as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Cecil Street",
        "generated": true
      }
    },
    {
      "company_name": "SM System Control",
      "contact_name": "Chris Pua",
      "contact_email": "*****@smsystem.com.sg",
      "email_1": {
        "subject": "quick question on electronics distribution",
        "body": "Hi Chris,\n\n We're building an AI assistant that's always one step ahead for SG electronics distributors. It proactively checks in - running daily reconciliation of supplier price lists against your catalog, tracking missing supplier price updates and sending follow-ups, or giving you morning updates on critical component price changes - all without you having to ask. \n\nYou just WhatsApp or email it instructions and it does your back office work around the clock. \n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what electronics distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference. \n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Woodlands Spectrum 1 if that's easier! \n\nBest,\nSeth \n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for SM System Control.",
        "ps_used": "Before the call, I can train our AI on your {their_doc_type} so you can see exactly what we'd catch for {company}. (using supplier price lists for their_doc_type and SM System Control for company). The \n\nP.S. is based on the logic provided in the email 1 section of the prompt, not the Email 2 \n\nP.S. options from the industry context file. The instruction '\n\nP.S. Before our call, I can train our AI on your [their_doc_type] so you can see exactly what we'd catch for [company].' is part of the Email 1 template, and then the [their_doc_type] and [company] variables are derived from research. Therefore, the most accurate label for 'ps_used' is the template itself, with variables filled from research as specified in the email 1 instructions. This is a slight ambiguity in the schema, but I've followed the Email 1 template's \n\nP.S. generation for 'email_1' and the Email 2 \n\nP.S. for 'email_2'. For 'ps_used' in the email_1 object, I am indicating the template from which it was generated with the derived variables. If the 'ps_used' was meant to refer to a specific \n\nP.S. option *like* the email 2's \n\nP.S. options, this would need further clarification in the schema for 'email_1'. Given the prompt's instructions for 'email_1', I will label it based on its direct derivation from the email 1 template."
      },
      "email_2": {
        "subject": "Chris <> Seth",
        "body": "Hi Chris,\n\n I did some digging into SM System Control and had a few ideas on where we could save time: - Extract 99% accurate data from supplier price lists for auto-updates. - Flag critical component price changes instantly to protect your margins. - Auto-update 50,000+ SKUs in your online store with current supplier costs. Have you solved for keeping supplier pricing current across your catalog or is your team still doing it manually? If we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting? \n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from supplier price lists for auto-updates.",
          "Flag critical component price changes instantly to protect your margins.",
          "Auto-update 50,000+ SKUs in your online store with current supplier costs."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on electronics distribution",
        "body": "Hi Chris,\n\n My co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes. Given your experience in distribution, I was hoping to get your opinion. \n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs. \n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference. \n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call. \n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back audit-ready reconciliations showing updated pricing for all SKUs in Excel, would that be useful? \n\nWould you be open to a quick chat to point us in the right direction? \n\nBest,\nSeth \n\nP.S. Happy to drop by your office at Woodlands Spectrum 1 if that's easier!",
        "hook_used": "Fallback (no specific signals)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back audit-ready reconciliations showing updated pricing for all SKUs in Excel, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at SM System Control, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Chris,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like SM System Control. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Woodlands Spectrum 1 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Woodlands Spectrum 1",
        "generated": true
      }
    },
    {
      "company_name": "Elect-Chemical & Electronics",
      "contact_name": "Paul Toh",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Elect-Chemical & Electronics, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Paul,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Elect-Chemical & Electronics. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Eunos Techpark as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Eunos Techpark",
        "generated": true
      }
    },
    {
      "company_name": "Acecom Technologies",
      "contact_name": "Jason Tan",
      "contact_email": "jas***@acecom.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Jason,\n\nWe're building an AI assistant that's always one step ahead for SG electronics distributors.\n\nIt proactively checks in - running daily reconciliation of supplier invoices against POs, tracking missing supplier price updates and sending follow-ups, or giving you morning updates on catalog discrepancies - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at BHCC Space if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Acecom Technologies.",
        "ps_used": "Document-specific value demo (from Email 1 template)"
      },
      "email_2": {
        "subject": "Jason <> Seth",
        "body": "Hi Jason,\n\nI did some digging into Acecom Technologies and had a few ideas on where we could save time:\n\n- Extract 99% accurate pricing data from any Acecom supplier format.\n- Flag price changes and discrepancies in your product catalogs for Acecom.\n- Auto-update Acecom's ERP/e-commerce systems with normalized price lists.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing data from any Acecom supplier format.",
          "Flag price changes and discrepancies in your product catalogs for Acecom.",
          "Auto-update Acecom's ERP/e-commerce systems with normalized price lists."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Jason,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back audit-ready reconciliation of pricing data in Excel, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at BHCC Space if that's easier!",
        "hook_used": "Fallback",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back audit-ready reconciliation of pricing data in Excel",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Acecom Technologies, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Jason,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Acecom Technologies.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at BHCC Space as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "BHCC Space",
        "generated": true
      }
    },
    {
      "company_name": "Tachibana Sales",
      "contact_name": "Kenny Tan",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Tachibana Sales, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Kenny,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Tachibana Sales.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at International Plaza as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "International Plaza",
        "generated": true
      }
    },
    {
      "company_name": "Kyowa Singapore",
      "contact_name": "S Stanley Lee",
      "contact_email": "stanley@kys.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Stanley,\n\nWe're building an AI assistant that's always one step ahead for SG electronics distributors.\n\nIt proactively checks in - running daily reconciliation of production orders against plating specifications, tracking pending Certificates of Conformity and sending reminders for completion, or giving you morning updates on customer RFQ progress and contract statuses - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tuas if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your Certificates of Conformity so you can see exactly what we'd catch for Kyowa Singapore.",
        "ps_used": "Document specific demo (Certificates of Conformity)"
      },
      "email_2": {
        "subject": "Stanley <> Seth",
        "body": "Hi Stanley,\n\nI did some digging into Kyowa Singapore and had a few ideas on where we could save time:\n\n- Extract 99% accurate component price data from supplier PDFs into clean Excel.\n- Flag critical price changes from key suppliers that could erode Kyowa Singapore's margins.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate component price data from supplier PDFs into clean Excel.",
          "Flag critical price changes from key suppliers that could erode Kyowa Singapore's margins."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Stanley,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your compliance documents and get back audit-ready traceability reports in Excel, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Tuas if that's easier!",
        "hook_used": "Fallback (no specific signals, based on industry experience)",
        "value_line": "If you could just email or WhatsApp an AI assistant your compliance documents and get back audit-ready traceability reports in Excel, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "Cadtronics Singapore",
      "contact_name": "Tan See Long",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 70+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi See Long,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Cadtronics Singapore. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Enterprise Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Enterprise Centre",
        "generated": true
      }
    },
    {
      "company_name": "ERIKS PRIVATE LTD",
      "contact_name": "Cindy Lim",
      "contact_email": "**********@eriks.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Cindy,\n\nWe're building an AI assistant that's always one step ahead for SG distribution companies.It proactively checks in - running daily reconciliations of supplier invoices against purchase orders, tracking pending supplier price list updates and flagging discrepancies, or giving you morning updates on catalog updates awaiting approval - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tuas Loop if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Eriks.",
        "ps_used": "document-specific value demo (supplier price lists)"
      },
      "email_2": {
        "subject": "Cindy <> Seth",
        "body": "Hi Cindy,\n\nI did some digging into ERIKS Singapore and had a few ideas on where we could save time:- Extract 99% accurate pricing from ERIKS' 50+ supplier formats for quick updates.- Automatically update ERP/pricing systems with audit-ready supplier data, reducing manual effort.- Flag critical price changes in your large catalog, catching what humans miss before quoting.Have you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?If we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing from ERIKS' 50+ supplier formats for quick updates.",
          "Automatically update ERP/pricing systems with audit-ready supplier data, reducing manual effort.",
          "Flag critical price changes in your large catalog, catching what humans miss before quoting."
        ]
      },
      "email_3": {
        "subject": "quick question on distribution",
        "body": "Hi Cindy,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.Given your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back 99% accurate, clean, ready to import data in Excel for your ERP/pricing system, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Tuas Loop if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back 99% accurate, clean, ready to import data in Excel for your ERP/pricing system",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "Central-Midori",
      "contact_name": "Tony Li",
      "contact_email": "tonyli@central-midori.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Tony,\n\n We're building an AI assistant that's always one step ahead for SG electronics distributors. It proactively checks in - providing daily reconciliation reports on supplier quotes against internal BOMs, tracking missing Certificates of Conformity and sending reminders, or giving you morning updates on critical engineering change notices - all without you having to ask. \n\nYou just WhatsApp or email it instructions and it does your back office work around the clock. \n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference. \n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Ayer Rajah Crescent if that's easier! \n\nBest,\nSeth \n\nP.S. Before our call, I can train our AI on your supplier quotes and purchase orders so you can see exactly what we'd catch for Central-Midori.",
        "ps_used": "Before our call, I can train our AI on your supplier quotes and purchase orders so you can see exactly what we'd catch for Central-Midori."
      },
      "email_2": {
        "subject": "Tony <> Seth",
        "body": "Hi Tony,\n\n I did some digging into Central-Midori and had a few ideas on where we could save time: - Extract 99% accurate pricing data from any supplier format for Central-Midori. - Get audit-ready reconciliation of supplier quotes against your internal BOMs. - Flag critical price changes that humans miss across your component catalog. Have you solved for keeping supplier pricing current across your catalog or is your team still doing it manually? If we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting? \n\nBest,\nSeth",
        "ideas_used": [
          "- Extract 99% accurate pricing data from any supplier format for Central-Midori.",
          "- Get audit-ready reconciliation of supplier quotes against your internal BOMs.",
          "- Flag critical price changes that humans miss across your component catalog."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Tony,\n\n My co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes. Given your experience in distribution, I was hoping to get your opinion. \n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs. \n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference. \n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call. \n\nIf you could just email or WhatsApp an AI assistant your supplier quotes and get back clean, ready to import data into your ERP, would that be useful? \n\nWould you be open to a quick chat to point us in the right direction? \n\nBest,\nSeth \n\nP.S. Happy to drop by your office at Ayer Rajah Crescent if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier quotes and get back clean, ready to import data into your ERP, would that be useful?",
        "value_line_source": "document_pain_analysis"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Central-Midori, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Tony,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Central-Midori. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Ayer Rajah Crescent as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Ayer Rajah Crescent",
        "generated": true
      }
    },
    {
      "company_name": "VF Fastening Systems",
      "contact_name": "Vincent Fong",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 34+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Vincent,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like VF Fastening Systems. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at North Link Building as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "North Link Building",
        "generated": true
      }
    },
    {
      "company_name": "Lionapex Equipment",
      "contact_name": "Michelle Ang",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Lionapex Equipment, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Michelle,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Lionapex Equipment.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Woodlands Industrial Park E1 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Woodlands Industrial Park E1",
        "generated": true
      }
    },
    {
      "company_name": "Megachem",
      "contact_name": "Francis Yau Thiam Hwa",
      "contact_email": "FSYAU@sg.megachem.com",
      "email_1": {
        "subject": "quick question on Chemicals Distributor",
        "body": "Hi Francis,\n\n We're building an AI assistant that's always one step ahead for SG chemical distributors. It proactively checks in - running daily reconciliation of supplier price lists to identify discrepancies, tracking pending supplier price updates and sending automated follow-ups, or giving you morning updates on critical chemical price fluctuations - all without you having to ask. \n\nYou just WhatsApp or email it instructions and it does your back office work around the clock. \n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what Chemicals Distributor teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference. \n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tuas Link 1 if that's easier! \n\nBest,\nSeth \n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Megachem.",
        "ps_used": "Specific document training"
      },
      "email_2": {
        "subject": "Francis <> Seth",
        "body": "Hi Francis,\n\n I did some digging into Megachem and had a few ideas on where we could save time: - Extract 99% accurate data from diverse chemical supplier price lists. - Auto-update ERP/pricing systems with clean, ready-to-import data. - Flag significant price changes to prevent margin erosion for Megachem. Have you solved for keeping supplier pricing current across your catalog or is your team still doing it manually? If we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting? \n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from diverse chemical supplier price lists.",
          "Auto-update ERP/pricing systems with clean, ready-to-import data.",
          "Flag significant price changes to prevent margin erosion for Megachem."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on Chemicals Distributor",
        "body": "Hi Francis,\n\n My co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes. Given your experience in distribution, I was hoping to get your opinion. \n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs. \n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference. \n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call. \n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean, ready-to-import pricing data in Excel, would that be useful? \n\nWould you be open to a quick chat to point us in the right direction? \n\nBest,\nSeth \n\nP.S. Happy to drop by your office at Tuas Link 1 if that's easier!",
        "hook_used": "Fallback",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean, ready-to-import pricing data in Excel, would that be useful?",
        "value_line_source": "Inferred from company profile and document pain"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "Measurement & Metrology",
      "contact_name": "Jimmy Tan",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Measurement & Metrology, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Jimmy,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Measurement & Metrology.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Sing Industrial Complex as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Sing Industrial Complex",
        "generated": true
      }
    },
    {
      "company_name": "YAMAICHI ELECTRONICS SINGAPORE PTE LTD",
      "contact_name": "Takahiro Amatatsu",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 14+ years in the distribution industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Takahiro,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Yamaichi Electronics. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Tai Seng Avenue as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tai Seng Avenue",
        "generated": true
      }
    },
    {
      "company_name": "Vital Vision Technology",
      "contact_name": "John Chan",
      "contact_email": "masked@v2tech.com.sg",
      "email_1": {
        "subject": "quick question on electronics distribution",
        "body": "Hi John,\n\nWe're building an AI assistant that's always one step ahead for SG electronics distributors.\n\nIt proactively checks in - running daily reconciliations of supplier price updates against your internal catalog, tracking missing supplier price lists and sending follow-ups, or giving you morning updates on critical price changes - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what electronics distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at AZ@Paya Lebar if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Vital Vision Technology.",
        "ps_used": "Document-specific value demo (supplier price lists)"
      },
      "email_2": {
        "subject": "John <> Seth",
        "body": "Hi John,\n\nI did some digging into Vital Vision Technology and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from all supplier price lists in seconds.\n- Auto-update Vital Vision Technology's ERP with clean, ready to import pricing.\n- Flag critical price changes and generate complete, ready to review quote sheets.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from all supplier price lists in seconds.",
          "Auto-update Vital Vision Technology's ERP with clean, ready to import pricing.",
          "Flag critical price changes and generate complete, ready to review quote sheets."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on electronics distribution",
        "body": "Hi John,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back 99% accurate pricing data in Excel, ready to update your systems, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at AZ@Paya Lebar if that's easier!",
        "hook_used": "Fallback (no specific signal)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back 99% accurate pricing data in Excel, ready to update your systems, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Vital Vision Technology, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi John,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Vital Vision Technology. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at AZ@Paya Lebar as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "AZ@Paya Lebar",
        "generated": true
      }
    },
    {
      "company_name": "J.P. Electronics",
      "contact_name": "Manprit Singh",
      "contact_email": "manprit@jpegroup.com",
      "email_1": {
        "subject": "quick question on Electronics Distributor",
        "body": "Hi Manprit,\n\nWe're building an AI assistant that's always one step ahead for SG electronics distributors.\n\nIt proactively checks in - running daily reconciliations of supplier price list changes, tracking outdated product catalogs and sending alerts, or giving you morning updates on critical component price fluctuations - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what Electronics Distributor teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tai Seng Avenue if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for J.P. Electronics.",
        "ps_used": "Before the call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for J.P. Electronics."
      },
      "email_2": {
        "subject": "Manprit <> Seth",
        "body": "Hi Manprit,\n\nI did some digging into J.P. Electronics and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from J.P. Electronics' diverse supplier price lists.\n- Get audit-ready updates of component pricing into your ERP automatically.\n- Flag critical price changes that humans miss across your 50+ suppliers.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from J.P. Electronics' diverse supplier price lists.",
          "Get audit-ready updates of component pricing into your ERP automatically.",
          "Flag critical price changes that humans miss across your 50+ suppliers."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on Electronics Distributor",
        "body": "Hi Manprit,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back unified, 99% accurate data in Excel ready for your ERP system, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Tai Seng Avenue if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back unified, 99% accurate data in Excel ready for your ERP system, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at J.P. Electronics, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Manprit,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like J.P. Electronics.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Tai Seng Avenue as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tai Seng Avenue",
        "generated": true
      }
    },
    {
      "company_name": "Device Electronics",
      "contact_name": "Yen",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Device Electronics, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Yen,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Device Electronics.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Kaki Bukit as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Kaki Bukit",
        "generated": true
      }
    },
    {
      "company_name": "Alkemal Singapore Pte Ltd",
      "contact_name": "Puneeta Singh Wasan",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 10+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Puneeta,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Alkemal.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Shenton House as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Shenton House",
        "generated": true
      }
    },
    {
      "company_name": "Camwell Industries",
      "contact_name": "Roger Lee",
      "contact_email": "********@camwell.com.sg",
      "email_1": {
        "subject": "quick question on electronics distribution",
        "body": "Hi Roger,\n\nWe're building an AI assistant that's always one step ahead for SG electronics distributors.\n\nIt proactively checks in - running daily reconciliation of supplier price lists against internal systems, tracking outdated product catalogs and prompting for updates, or giving you morning updates on new supplier pricing data - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what electronics distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Bizlink Centre if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Camwell Industries.",
        "ps_used": "Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Camwell Industries."
      },
      "email_2": {
        "subject": "Roger <> Seth",
        "body": "Hi Roger,\n\nI did some digging into Camwell Industries and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from 50+ supplier price lists into Excel.\n- Get audit-ready reconciliation of new pricing directly into your ERP for Camwell.\n- Flag critical price changes or discrepancies that humans miss on product catalogs.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from 50+ supplier price lists into Excel.",
          "Get audit-ready reconciliation of new pricing directly into your ERP for Camwell.",
          "Flag critical price changes or discrepancies that humans miss on product catalogs."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on electronics distribution",
        "body": "Hi Roger,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, unified price lists in Excel, ready for your ERP, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Bizlink Centre if that's easier!",
        "hook_used": "Fallback (no specific signals)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, unified price lists in Excel, ready for your ERP, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "Kim Ann Engineering",
      "contact_name": "Eric Lim",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed Kim Ann Engineering is participating in the Singapore Airshow 2026 - figured you'd have perspective on how operations are scaling. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "News",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Eric,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Kim Ann Engineering. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Joo Koon Circle as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Joo Koon Circle",
        "generated": true
      }
    },
    {
      "company_name": "Wemark Techno Engineering",
      "contact_name": "Zyron Goh",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 28+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Zyron,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Wemark Techno Engineering.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Tuas Basin as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tuas Basin",
        "generated": true
      }
    },
    {
      "company_name": "Megachem",
      "contact_name": "Sidney Chew Choon Tee",
      "contact_email": "SYCHEW@sg.megachem.com",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Sidney,\n\nWe're building an AI assistant that's always one step ahead for SG chemical distributors.\n\nIt proactively checks in - running daily reconciliation of supplier price lists against your ERP, tracking overdue supplier updates and sending automated reminders, or giving you morning updates on new price changes in your catalog - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what chemical distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tuas Link 1 if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Megachem.",
        "ps_used": "Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Megachem."
      },
      "email_2": {
        "subject": "Sidney <> Seth",
        "body": "Hi Sidney,\n\nI did some digging into Megachem and had a few ideas on where we could save time:\n\n- Extract 99% accurate chemical price data from diverse supplier formats.\n- Auto-update Megachem's ERP with normalized pricing, removing manual entry.\n- Flag critical price changes in supplier contracts that humans miss.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate chemical price data from diverse supplier formats.",
          "Auto-update Megachem's ERP with normalized pricing, removing manual entry.",
          "Flag critical price changes in supplier contracts that humans miss."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Sidney,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nNoticed Megachem reported its recent earnings, figured you'd have perspective on how operations are scaling.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate supplier price data in Excel, ready to update your catalog, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Tuas Link 1 if that's easier!",
        "hook_used": "News",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate supplier price data in Excel, ready to update your catalog",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "MASS TECHNOLOGIES PTE LTD",
      "contact_name": "Clyde Gan",
      "contact_email": "*****@masstech.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Clyde,\n\n We're building an AI assistant that's always one step ahead for SG distributors. It proactively checks in - running daily reconciliations of supplier price lists against your catalog, tracking missing price updates from key suppliers and sending reminders, or giving you morning updates on new product additions or discontinuations - all without you having to ask. \n\nYou just WhatsApp or email it instructions and it does your back office work around the clock. \n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference. \n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Bukit Batok if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Mass Technologies.",
        "ps_used": "Before our call, I can train our AI on your [their_doc_type] so you can see exactly what we'd catch for [company]."
      },
      "email_2": {
        "subject": "Clyde <> Seth",
        "body": "Hi Clyde,\n\n I did some digging into Mass Technologies and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from diverse supplier price lists for Mass Technologies.\n- Auto-update your ERP with audit-ready pricing from all 3M and other suppliers.\n- Flag critical price changes that humans miss, protecting your margins.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from diverse supplier price lists for Mass Technologies.",
          "Auto-update your ERP with audit-ready pricing from all 3M and other suppliers.",
          "Flag critical price changes that humans miss, protecting your margins."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Clyde,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean, and audit-ready pricing data in Excel for your catalog and quotes, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Bukit Batok if that's easier!",
        "hook_used": "Fallback",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean, and audit-ready pricing data in Excel for your catalog and quotes, would that be useful?",
        "value_line_source": "document_pain_analysis"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "Foresight Metal Engineering",
      "contact_name": "Vivien Ngo",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Foresight Metal Engineering, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Vivien,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Foresight Metal Engineering. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Eco-Tech as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Eco-Tech",
        "generated": true
      }
    },
    {
      "company_name": "Beijer Ref Singapore",
      "contact_name": "Dickson Lee",
      "contact_email": "dle@beijerref.com.sg",
      "email_1": {
        "subject": "quick question on industrial distribution",
        "body": "Hi Dickson,\n\nWe're building an AI assistant that's always one step ahead for SG industrial distributors.\n\nIt proactively checks in - running daily reconciliation of supplier price lists against current stock, tracking outstanding price updates from key manufacturers and sending follow-ups, or giving you morning updates on new product announcements and associated pricing changes - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what industrial distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tagore Lane if that's easier!\n\nBest,\nSeth\n\nP.S. If you're juggling price lists from 50+ suppliers, I can show you how one distributor consolidated everything into a single update workflow.",
        "ps_used": "multiple_suppliers"
      },
      "email_2": {
        "subject": "Dickson <> Seth",
        "body": "Hi Dickson,\n\nI did some digging into Beijer Ref Singapore and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from complex supplier price lists in minutes.\n- Flag critical price changes and exceptions that impact margins automatically.\n- Generate quote sheets for Beijer Ref Singapore with real-time, current pricing.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from complex supplier price lists in minutes.",
          "Flag critical price changes and exceptions that impact margins automatically.",
          "Generate quote sheets for Beijer Ref Singapore with real-time, current pricing."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on industrial distribution",
        "body": "Hi Dickson,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in industrial distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean data in Excel ready for your ERP system, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Tagore Lane if that's easier!",
        "hook_used": "Fallback",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean data in Excel ready for your ERP system, would that be useful?",
        "value_line_source": "document_pain_analysis + company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "Snorre Food",
      "contact_name": "Michael PK How",
      "contact_email": "michael@snorrefood.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Michael,\n\nWe're building an AI assistant that's always one step ahead for SG food & beverage distributors.It proactively checks in - running daily reconciliation of supplier price lists against current inventory, tracking missing product catalogs and sending follow-ups to suppliers, or giving you morning updates on invoices awaiting approval from your suppliers - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Fishery Port Road if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Snorre Food.",
        "ps_used": "Before our call, I can train our AI on your {their_doc_type} so you can see exactly what we'd catch for {company}."
      },
      "email_2": {
        "subject": "Michael <> Seth",
        "body": "Hi Michael,\n\nI did some digging into Snorre Food and had a few ideas on where we could save time:- Extract 99% accurate pricing from your varied supplier lists.- Get audit-ready reconciliation of incoming supplier invoices.- Flag discrepancies in product catalogs for improved accuracy.Have you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?If we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing from your varied supplier lists.",
          "Get audit-ready reconciliation of incoming supplier invoices.",
          "Flag discrepancies in product catalogs for improved accuracy."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Michael,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.Given your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean data in Excel, ready for your ERP updates, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Fishery Port Road if that's easier!",
        "hook_used": "Fallback",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean data in Excel, ready for your ERP updates, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Snorre Food, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Michael,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Snorre Food.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Fishery Port Road as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Fishery Port Road",
        "generated": true
      }
    },
    {
      "company_name": "Hoffmann Quality Tools Asia Pacific",
      "contact_name": "Leslie Goh",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Hoffmann Quality Tools Asia Pacific, I was hoping to get your opinion. I'm building a WhatsApp AI assistant that does back office work around the clock - sending a voice note too with more context!",
        "hook_used": "Fallback (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Leslie,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Hoffmann Quality Tools Asia Pacific. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at German Centre Singapore as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "German Centre Singapore",
        "generated": true
      }
    },
    {
      "company_name": "Techfield Supply",
      "contact_name": "Mervin Boon",
      "contact_email": "mervin@techfield.com.sg",
      "email_1": {
        "subject": "quick question on Industrial/MRO Distribution",
        "body": "Hi Mervin,\n\n We're building an AI assistant that's always one step ahead for SG Industrial/MRO distributors. It proactively checks in - running daily reconciliations of supplier price lists, tracking missing updates to product catalogs and sending follow-ups, or giving you morning updates on pricing changes across your SKUs - all without you having to ask. \n\nYou just WhatsApp or email it instructions and it does your back office work around the clock. \n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what Industrial/MRO Distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference. \n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at KB Industrial Building if that's easier! \n\nBest,\nSeth \n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Techfield Supply.",
        "ps_used": "Document-specific value demo (supplier price lists)"
      },
      "email_2": {
        "subject": "Mervin <> Seth",
        "body": "Hi Mervin,\n\n I did some digging into Techfield Supply and had a few ideas on where we could save time: - Extract 99% accurate data from diverse supplier price lists for Techfield Supply. - Auto-update ERP systems with audit-ready, reconciled supplier pricing. - Flag critical price changes that humans miss across your extensive product catalog. Have you solved for keeping supplier pricing current across your catalog or is your team still doing it manually? If we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting? \n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from diverse supplier price lists for Techfield Supply.",
          "Auto-update ERP systems with audit-ready, reconciled supplier pricing.",
          "Flag critical price changes that humans miss across your extensive product catalog."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on Industrial/MRO Distribution",
        "body": "Hi Mervin,\n\n My co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes. Given your experience in distribution, I was hoping to get your opinion. \n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs. \n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference. \n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call. \n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back 99% accurate, clean data in Excel, ready to import, would that be useful? \n\nWould you be open to a quick chat to point us in the right direction? \n\nBest,\nSeth \n\nP.S. Happy to drop by your office at KB Industrial Building if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and product catalogs and get back 99% accurate, clean data in Excel, ready to import, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Techfield Supply, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Mervin,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Techfield Supply. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at KB Industrial Building as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "KB Industrial Building",
        "generated": true
      }
    },
    {
      "company_name": "Aries Fresh Pte Ltd",
      "contact_name": "Shally Chin",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 33+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Shally,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Aries Fresh. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Pasir Panjang Wholesale Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Pasir Panjang Wholesale Centre",
        "generated": true
      }
    },
    {
      "company_name": "Yappy Pets",
      "contact_name": "Jasmine Tan",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Yappy Pets, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Jasmine,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Yappy Pets. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Loyang Way 1 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Loyang Way 1",
        "generated": true
      }
    },
    {
      "company_name": "CHH Construction System",
      "contact_name": "Nelson Tee",
      "contact_email": "nelsontee@chhsys.com",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Nelson,\n\n We're building an AI assistant that's always one step ahead for SG electronics distributors. It proactively checks in - running daily reconciliation of supplier price lists against current project BOMs, tracking outstanding supplier quotes and sending follow-ups, or giving you morning updates on new supplier price list versions - all without you having to ask. \n\nYou just WhatsApp or email it instructions and it does your back office work around the clock. \n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference. \n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at LHK2 Building if that's easier! \n\nBest,\nSeth \n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for CHH Construction System.",
        "ps_used": "Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for CHH Construction System."
      },
      "email_2": {
        "subject": "Nelson <> Seth",
        "body": "Hi Nelson,\n\n I did some digging into CHH Construction System and had a few ideas on where we could save time: - Extract 99% accurate pricing from construction and security supplier catalogs. - Flag discrepancies between POs and supplier invoices that humans miss. - Auto-update project BOMs and ERP with clean, ready-to-import pricing data. Have you solved for keeping supplier pricing current across your catalog or is your team still doing it manually? If we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting? \n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing from construction and security supplier catalogs.",
          "Flag discrepancies between POs and supplier invoices that humans miss.",
          "Auto-update project BOMs and ERP with clean, ready-to-import pricing data."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Nelson,\n\n My co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes. Given your experience leading CHH Construction System, I was hoping to get your opinion. \n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs. \n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference. \n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call. \n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and BOMs and get back an audit-ready reconciliation in Excel showing mispriced lines across your projects, would that be useful? \n\nWould you be open to a quick chat to point us in the right direction? \n\nBest,\nSeth \n\nP.S. Happy to drop by your office at LHK2 Building if that's easier!",
        "hook_used": "C-suite",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and BOMs and get back an audit-ready reconciliation in Excel showing mispriced lines across your projects, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile, classification_category"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading CHH Construction System, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Nelson,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like CHH Construction System. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Playfair Road as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Playfair Road",
        "generated": true
      }
    },
    {
      "company_name": "S E Electronics",
      "contact_name": "Ling",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading S E Electronics, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Ling,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like S E Electronics.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Sim Lim Tower as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Sim Lim Tower",
        "generated": true
      }
    },
    {
      "company_name": "Hoiho Pcb",
      "contact_name": "MT Leung",
      "contact_email": "mt-leung@hoiho-pcb.com",
      "email_1": {
        "subject": "quick question on electronics distribution",
        "body": "Hi MT,\n\nWe're building an AI assistant that's always one step ahead for SG electronics distributors.\n\nIt proactively checks in - running daily reconciliation of component price lists against your internal catalog, tracking MOQ changes and flagging critical lead time updates, or giving you morning updates on new supplier price adjustments - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at The Plaza if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your component price lists so you can see exactly what we'd catch for Hoiho Pcb.",
        "ps_used": "P.S. Before our call, I can train our AI on your component price lists so you can see exactly what we'd catch for Hoiho Pcb."
      },
      "email_2": {
        "subject": "MT <> Seth",
        "body": "Hi MT,\n\nI did some digging into Hoiho Pcb and had a few ideas on where we could save time:\n\n- Extract 99% accurate component pricing from diverse supplier formats.\n- Get audit-ready reconciliation of new price lists against your catalog at Hoiho Pcb.\n- Auto-update your ERP with clean, ready to import MOQ and lead time changes.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate component pricing from diverse supplier formats.",
          "Get audit-ready reconciliation of new price lists against your catalog at Hoiho Pcb.",
          "Auto-update your ERP with clean, ready to import MOQ and lead time changes."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi MT,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your component price lists and get back 99% accurate pricing data in Excel, ready to import, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at The Plaza if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "just email or WhatsApp an AI assistant your component price lists and get back 99% accurate pricing data in Excel, ready to import",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "Adtec Enterprise",
      "contact_name": "Anthony Sim",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Adtec Enterprise, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Anthony,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Adtec Enterprise.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at EastTech as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "EastTech",
        "generated": true
      }
    },
    {
      "company_name": "P.L. Global Impex Pte. Ltd.",
      "contact_name": "Vivek Dinodiya",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 32+ years in the distribution industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Vivek,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like PL Global Impex. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Tong Eng Building as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tong Eng Building",
        "generated": true
      }
    },
    {
      "company_name": "Mesh",
      "contact_name": "Andrew Wu",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Saw you went to ACS too - the best is yet to be. Given your experience in distribution, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "ACS Alumni",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Andrew,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Mesh. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Pixel Red as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Pixel Red",
        "generated": true
      }
    },
    {
      "company_name": "Acecom Technologies",
      "contact_name": "Mei Loh",
      "contact_email": "mei***@acecom.com.sg",
      "email_1": {
        "subject": "quick question on electronics distribution",
        "body": "Hi Mei,\n\n We're building an AI assistant that's always one step ahead for SG electronics distribution companies. It proactively checks in - running daily reconciliation of supplier invoices against purchase orders, tracking missing price lists and sending follow-ups to vendors, or giving you morning updates on pricing changes across your catalog - all without you having to ask. \n\nYou just WhatsApp or email it instructions and it does your back office work around the clock. \n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what electronics distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference. \n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at BHCC Space if that's easier! \n\nBest,\nSeth \n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Acecom Technologies.",
        "ps_used": "train our AI on your [their_doc_type]"
      },
      "email_2": {
        "subject": "Mei <> Seth",
        "body": "Hi Mei,\n\n I did some digging into Acecom Technologies and had a few ideas on where we could save time: - Extract 99% accurate data from diverse supplier price lists for Acecom - Flag critical price changes and update your ERP automatically - Generate complete, ready-to-review quotes with current catalog pricing Have you solved for keeping supplier pricing current across your catalog or is your team still doing it manually? If we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting? \n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from diverse supplier price lists for Acecom",
          "Flag critical price changes and update your ERP automatically",
          "Generate complete, ready-to-review quotes with current catalog pricing"
        ]
      },
      "email_3": {
        "subject": "Re: quick question on electronics distribution",
        "body": "Hi Mei,\n\n My co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes. Given your experience in distribution, I was hoping to get your opinion. \n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs. \n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference. \n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call. \n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back clean, ready to import normalized price data in Excel ready for your ERP, would that be useful? \n\nWould you be open to a quick chat to point us in the right direction? \n\nBest,\nSeth \n\nP.S. Happy to drop by your office at BHCC Space if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and get back clean, ready to import normalized price data in Excel ready for your ERP",
        "value_line_source": "document_pain_analysis + company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "Link 2 Link Asia Pacific",
      "contact_name": "Patrick Chua",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 49+ years in the distribution industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Patrick,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Link 2 Link Asia Pacific. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Clementi Loop as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Clementi Loop",
        "generated": true
      }
    },
    {
      "company_name": "Vital Vision Technology",
      "contact_name": "Allison Cheong",
      "contact_email": "masked@v2tech.com.sg",
      "email_1": {
        "subject": "quick question on electronics distribution",
        "body": "Hi Allison,\n\n \u041c\u044b \u0441 \u043c\u043e\u0438\u043c \u0441\u043e\u0443\u0447\u0440\u0435\u0434\u0438\u0442\u0435\u043b\u0435\u043c \u0441\u0442\u0440\u043e\u0438\u043c \u0441\u0442\u0430\u0440\u0442\u0430\u043f \u0432 \u0421\u0438\u043d\u0433\u0430\u043f\u0443\u0440\u0435, \u0447\u0442\u043e\u0431\u044b \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0430\u0442\u044c \u043c\u0435\u0441\u0442\u043d\u044b\u0439 \u0431\u0438\u0437\u043d\u0435\u0441, \u0438 \u043c\u044b \u0445\u043e\u0442\u0435\u043b\u0438 \u0441\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f \u0441 \u0432\u0430\u043c\u0438, \u043f\u043e\u0442\u043e\u043c\u0443 \u0447\u0442\u043e \u0432\u0430\u0448 \u043e\u043f\u044b\u0442 \u043c\u043e\u0433 \u0431\u044b \u0441\u043f\u0430\u0441\u0442\u0438 \u043d\u0430\u0441 \u043e\u0442 \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u0430 \u043e\u0448\u0438\u0431\u043e\u043a.\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your 25+ years in the industry, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate pricing data in Excel, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at AZ@Paya Lebar if that's easier!",
        "ps_used": "multiple_suppliers"
      },
      "email_2": {
        "subject": "Allison <> Seth",
        "body": "Hi Allison,\n\nI did some digging into Vital Vision Technology and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from LMI Gocator price lists in seconds.\n- Flag margin-eroding price changes from suppliers that humans miss.\n- Get audit-ready reconciliation of supplier invoices to purchase orders for Vital Vision.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from LMI Gocator price lists in seconds.",
          "Flag margin-eroding price changes from suppliers that humans miss.",
          "Get audit-ready reconciliation of supplier invoices to purchase orders for Vital Vision."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on electronics distribution",
        "body": "Hi Allison,\n\nJust wanted to check in again in case this missed your inbox.\n\nWe're building an AI assistant that's always one step ahead. It proactively checks in - running daily reconciliations of supplier invoices to purchase orders, tracking missing purchase orders and sending follow-ups to suppliers, or giving you morning updates on key component price changes - without you having to ask.\n\nCurious whether teams in electronics distribution would actually use this from WhatsApp or email - would love your perspective if you have 15 mins.\n\nBest,\nSeth\n\nP.S. If you're juggling price lists from 50+ suppliers, I can show you how one distributor consolidated everything into a single update workflow.",
        "hook_used": "10+ years",
        "value_line": "just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate pricing data in Excel",
        "value_line_source": "document_pain_analysis"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 25+ years in the distribution industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Allison,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Vital Vision Technology. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at AZ@Paya Lebar as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "AZ@Paya Lebar",
        "generated": true
      }
    },
    {
      "company_name": "Hoffmann Quality Tools Asia Pacific",
      "contact_name": "Wai Meng",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 19+ years in the distribution industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Wai Meng,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Hoffmann Quality Tools Asia Pacific. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at German Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "German Centre",
        "generated": true
      }
    },
    {
      "company_name": "Beijer Ref Singapore",
      "contact_name": "Joyce Choy",
      "contact_email": "jcy@beijerref.com.sg",
      "email_1": {
        "subject": "quick question on industrial distribution",
        "body": "Hi Joyce,\n\nWe're building an AI assistant that's always one step ahead for SG industrial distributors.\n\nIt proactively checks in - running daily reconciliation of supplier price lists against your catalog, tracking pending price updates and following up with suppliers, or giving you morning updates on new product pricing or superseded parts - all without you having to ask.\n\nYou just WhatsApp or email it instructions and it does your back office work around the clock.\n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what industrial distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference.\n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Tagore Lane if that's easier!\n\nBest,\nSeth\n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Beijer Ref.",
        "ps_used": "value_demo_ps_for_supplier_price_lists"
      },
      "email_2": {
        "subject": "Joyce <> Seth",
        "body": "Hi Joyce,\n\nI did some digging into Beijer Ref Singapore and had a few ideas on where we could save time:\n\n- Extract 99% accurate data from complex component price lists for quicker updates.\n- Flag critical price changes from suppliers that could impact Beijer Ref's margins.\n- Auto-update your internal systems with normalized supplier pricing, saving manual entry time.\n\nHave you solved for keeping supplier pricing current across your catalog or is your team still doing it manually?\n\nIf we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting?\n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate data from complex component price lists for quicker updates.",
          "Flag critical price changes from suppliers that could impact Beijer Ref's margins.",
          "Auto-update your internal systems with normalized supplier pricing, saving manual entry time."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on industrial distribution",
        "body": "Hi Joyce,\n\nMy co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes.\n\nGiven your experience in distribution, I was hoping to get your opinion.\n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs.\n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference.\n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call.\n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate supplier price list data in Excel ready for system import, would that be useful?\n\nWould you be open to a quick chat to point us in the right direction?\n\nBest,\nSeth\n\nP.S. Happy to drop by your office at Tagore Lane if that's easier!",
        "hook_used": "Fallback (Given your experience in {industry_short})",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate supplier price list data in Excel ready for system import, would that be useful?",
        "value_line_source": "document_pain_analysis"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Beijer Ref Singapore, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Joyce,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Beijer Ref.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Tagore Lane as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Tagore Lane",
        "generated": true
      }
    },
    {
      "company_name": "mesh",
      "contact_name": "Arsen Batagov",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading mesh, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Arsen,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like mesh.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Pixel Red as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Pixel Red",
        "generated": true
      }
    },
    {
      "company_name": "Almech Steel",
      "contact_name": "Tan Hock Guan",
      "contact_email": "sales@almech.com.sg",
      "email_1": {
        "subject": "quick question on distribution",
        "body": "Hi Hock Guan,\n\n We're building an AI assistant that's always one step ahead for SG hardware wholesale distributors. It proactively checks in - running daily reconciliation of supplier invoices against purchase orders, tracking overdue supplier price list updates and sending follow-ups, or giving you morning updates on new price lists awaiting processing - all without you having to ask. \n\nYou just WhatsApp or email it instructions and it does your back office work around the clock. \n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference. \n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Benoi Crescent if that's easier! \n\nBest,\nSeth \n\nP.S. If you're juggling price lists from 50+ suppliers, I can show you how one distributor consolidated everything into a single update workflow.",
        "ps_used": "multiple_suppliers"
      },
      "email_2": {
        "subject": "Hock Guan <> Seth",
        "body": "Hi Hock Guan,\n\n I did some digging into Almech Steel and had a few ideas on where we could save time: - Extract 99% accurate pricing data from all your supplier price lists. - Auto-update your ERP/pricing systems with current steel commodity prices. - Flag discrepancies on supplier invoices that humans might miss for Almech Steel. Have you solved for keeping supplier pricing current across your catalog or is your team still doing it manually? If we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting? \n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing data from all your supplier price lists.",
          "Auto-update your ERP/pricing systems with current steel commodity prices.",
          "Flag discrepancies on supplier invoices that humans might miss for Almech Steel."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on distribution",
        "body": "Hi Hock Guan,\n\n My co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes. Given your experience in distribution, I was hoping to get your opinion. \n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs. \n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference. \n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call. \n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back a clean, ready to import master price list in Excel, would that be useful? \n\nWould you be open to a quick chat to point us in the right direction? \n\nBest,\nSeth \n\nP.S. Happy to drop by your office at Benoi Crescent if that's easier!",
        "hook_used": "Fallback (no signals)",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back a clean, ready to import master price list in Excel, would that be useful?",
        "value_line_source": "document_pain_analysis and company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    },
    {
      "company_name": "Kawata Pacific",
      "contact_name": "Jeremy Khoo",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Kawata Pacific, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Jeremy,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Kawata Pacific. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Kaki Bukit Road 2 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Kaki Bukit Road 2",
        "generated": true
      }
    },
    {
      "company_name": "Istar Trading Pte Ltd",
      "contact_name": "Alex Choo",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Istar Trading, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "Fallback (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Alex,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Istar Trading.\n\nThis isn't a sales call - just looking for your perspective.\n\nHappy to buy you lunch near your office at Toh Guan Road East as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Toh Guan Road East",
        "generated": true
      }
    },
    {
      "company_name": "LONG SHINE EQUIPMENT & SUPPLIES PTE LTD",
      "contact_name": "Ivan Cheah",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Long Shine Equipment & Supplies, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Ivan,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Long Shine Equipment & Supplies. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at MacTaggart Building as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "MacTaggart Building",
        "generated": true
      }
    },
    {
      "company_name": "Masstron",
      "contact_name": "Margaret Ng",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Masstron, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Margaret,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Masstron. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Fifth Lok Yang Rd as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Fifth Lok Yang Rd",
        "generated": true
      }
    },
    {
      "company_name": "Gernise Global Pte Ltd",
      "contact_name": "Vanessa Ong",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your 40+ years in the industry, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "10+ years",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Vanessa,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Gernise Global. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Pioneer Junction as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Pioneer Junction",
        "generated": true
      }
    },
    {
      "company_name": "ENGENIUS NETWORKS SINGAPORE PTE LTD",
      "contact_name": "Nancy Bang",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Noticed EnGenius Networks Singapore unveiled Cloud-Managed Wi-Fi 7 Enterprise AP with 24/7 AirGuard Security - figured you'd have perspective on how operations are scaling. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "News",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Nancy,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation.\n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like EnGenius Networks Singapore.This isn't a sales call - just looking for your perspective.Happy to buy you lunch near your office at Pacific Tech Centre as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Pacific Tech Centre",
        "generated": true
      }
    },
    {
      "company_name": "Farlee Pte Ltd",
      "contact_name": "Low Lee Yong",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Farlee, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Lee Yong,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Farlee. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Woodlands Close as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Woodlands Close",
        "generated": true
      }
    },
    {
      "company_name": "Pacific-Tec Scientific",
      "contact_name": "Patrick Fernandez",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience at Pacific-Tec Scientific, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "FALLBACK (no signals)",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Patrick,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Pacific-Tec Scientific. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office at Ubi Ave 3 as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "Ubi Ave 3",
        "generated": true
      }
    },
    {
      "company_name": "Panasonic System Solutions Asia Pacific",
      "contact_name": "Yuki Sakamoto",
      "contact_email": "N/A",
      "email_1": {
        "subject": "N/A",
        "body": "N/A",
        "ps_used": "N/A"
      },
      "email_2": {
        "subject": "N/A",
        "body": "N/A",
        "ideas_used": []
      },
      "email_3": {
        "subject": "N/A",
        "body": "N/A",
        "hook_used": "N/A",
        "value_line": "N/A",
        "value_line_source": "N/A"
      },
      "linkedin_message": {
        "message": "Seth here. Given your experience leading Panasonic System Solutions Asia Pacific, I was hoping to get your opinion. Emailed you about our idea for a WhatsApp AI assistant that does back office work around the clock - sending a voice note too in case it missed you!",
        "hook_used": "C-suite",
        "generated": true
      },
      "voice_note": {
        "script": "Hi Yuki,\n\n I'm building an AI startup in Singapore focused on automating heavy back-office paperwork - a gap recently highlighted to us by government leaders in Smart Nation. \n\nWe're a Cambridge-led team with a working prototype, and I'd love 20 minutes of your time to ensure we're solving the right pain points for firms like Panasonic System Solutions Asia Pacific. This isn't a sales call - just looking for your perspective. Happy to buy you lunch near your office as a thank you. \n\nWould you be open to a quick chat?",
        "location_used": "none",
        "generated": true
      }
    },
    {
      "company_name": "Unique Hardware Co.",
      "contact_name": "Teo Yeow Pin",
      "contact_email": "ypteo@unique.com.sg",
      "email_1": {
        "subject": "quick question on Industrial/MRO distribution",
        "body": "Hi Yeow Pin,\n\n We're building an AI assistant that's always one step ahead for SG Industrial/MRO distributors. It proactively checks in - running daily reconciliations of supplier invoices against purchase orders, tracking overdue supplier price lists and sending automated reminders, or giving you morning updates on critical price changes across your catalog - all without you having to ask. \n\nYou just WhatsApp or email it instructions and it does your back office work around the clock. \n\nWe're a Cambridge-backed group with a working prototype to demo, but this isn't a sales call. We're trying to learn what Industrial/MRO distribution teams actually find useful, what pain points keep coming up, and how you're thinking about future-proofing the business. 30 minutes of your time would make a big difference. \n\nI know you're busy, so let me know what time is best for a call or I can drop by your office at Kranji Loop if that's easier! \n\nBest,\nSeth \n\nP.S. Before our call, I can train our AI on your supplier price lists so you can see exactly what we'd catch for Unique Hardware Co.",
        "ps_used": "fixed_template_ps"
      },
      "email_2": {
        "subject": "Yeow Pin <> Seth",
        "body": "Hi Yeow Pin,\n\n I did some digging into Unique Hardware Co. and had a few ideas on where we could save time: - Extract 99% accurate pricing data from Unique Hardware Co.'s diverse supplier formats. - Auto-update your ERP/e-commerce with clean, ready to import price lists. - Flag margin-eroding price changes instantly across your entire catalog. Have you solved for keeping supplier pricing current across your catalog or is your team still doing it manually? If we could help you do the same and save 10+ hours a week, automatically from WhatsApp, email or any chat app you already use, would that be interesting? \n\nBest,\nSeth",
        "ideas_used": [
          "Extract 99% accurate pricing data from Unique Hardware Co.'s diverse supplier formats.",
          "Auto-update your ERP/e-commerce with clean, ready to import price lists.",
          "Flag margin-eroding price changes instantly across your entire catalog."
        ]
      },
      "email_3": {
        "subject": "Re: quick question on Industrial/MRO distribution",
        "body": "Hi Yeow Pin,\n\n My co-founder and I are building a startup in Singapore to support local businesses and we wanted to reach out because your expertise could save us a ton of mistakes. Given your experience in distribution, I was hoping to get your opinion. \n\nFor some background, we spoke with senior government leaders last week at Smart Nation - they shared that SMEs in underserved areas stand to gain the most from AI compared to MNCs. \n\nWe're now looking to figure out which are the biggest pain points distributors face and 30 minutes of your time would make a huge difference. \n\nWe're a Cambridge led group, based in SG, and have a prototype, but this is in no way a sales call. \n\nIf you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean, ready to import pricing in Excel, would that be useful? \n\nWould you be open to a quick chat to point us in the right direction? \n\nBest,\nSeth \n\nP.S. Happy to drop by your office at Kranji Loop if that's easier!",
        "hook_used": "Fallback",
        "value_line": "If you could just email or WhatsApp an AI assistant your supplier price lists and get back 99% accurate, clean, ready to import pricing in Excel, would that be useful?",
        "value_line_source": "document_pain_analysis, company_profile"
      },
      "linkedin_message": {
        "message": "N/A",
        "hook_used": "none",
        "generated": false
      },
      "voice_note": {
        "script": "N/A",
        "location_used": "none",
        "generated": false
      }
    }
  ]
}
```
