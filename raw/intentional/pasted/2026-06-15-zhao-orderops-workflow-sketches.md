---
type: raw_capture
source_type: pasted
title: "Zhao OrderOps workflow sketches"
url: "local-files:///Users/sethlim/Desktop/Zhao%201; local-files:///Users/sethlim/Desktop/Zhao%202.jpg"
collected_at: 2026-06-15T08:35:05Z
published_at: Unknown
capture_quality: complete
status: raw
trust_lane: intentional
---

# Zhao OrderOps workflow sketches

Source: local image files supplied by Seth.

## Canonical Raw Attachments

The copied image snapshots are the raw evidence. The transcription below is interpretive and should be checked against the images before treating details as final requirements.

- [Zhao sketch 1](attachments/zhao-orderops-2026-06-15/zhao-1.jpg)
  - Original path: `/Users/sethlim/Desktop/Zhao 1`
  - SHA256: `339ef42b7ad1d3645026cff5e58554137cf80cc90164cfc5bd4686f20e13d171`
- [Zhao sketch 2](attachments/zhao-orderops-2026-06-15/zhao-2.jpg)
  - Original path: `/Users/sethlim/Desktop/Zhao 2.jpg`
  - SHA256: `c0afd4c2a829ac71c13953efc9159e8e63d870583d45e27d4fa66fda13b5d19`

## Interpreted Transcription

The sketches appear to describe a food or frozen-goods distribution workflow with customers ordering through multiple informal channels, then staff converting those orders into warehouse picklists, driver route sheets, and invoices.

Visible customer/channel examples:

- Customer A appears to order through WhatsApp, with one note suggesting WhatsApp is more than 50% or about 65% of volume.
- Customer B appears to order through WeChat or a similar text channel, roughly 30% in one sketch.
- Customer C appears to order through SMS.
- Customer D appears to order through voice call or hotline, around 10-15%.
- Notes say all channels are viable, customer service can be automated, and all languages are accepted.

Visible product/order examples:

- "Belly slice" with variants such as thickness and pack weight, including possible readings like 1.5mm per piece, 1cm per piece, 4.5kg per packet, 2kg per packet, and 10kg belly slice.
- "Dory" by cartons.
- "Nugget" by packets.
- Customer phrases and product nicknames must be mapped to the correct internal inventory item.

Visible operations:

- A "black box" or plugin built to phone captures orders from channels.
- It auto-generates picklists for route drivers and warehouse.
- It auto-generates in-sequence order lists for drivers.
- Route/loading logic includes first-to-deliver versus last-to-deliver ordering; the loading sequence appears to require last delivery loaded first and first delivery loaded last.
- Admin reviews and sends information toward invoice/customer flow.
- A 04:00-04:30 warehouse preparation window is visible.
- There is a handoff between driver and warehouse and a note about drawing/picking packets.
- There is mention of mapping to ERP system data.

Visible pain points:

- Complicated mapping from customer order wording to the correct part/SKU/inventory item.
- Time consuming manual work.
- HR issue: hard to employ long-term night-shift staff.
- Miscommunication risk between WhatsApp/phone/customer wording and ERP records, including possible date/order mismatches.

Uncertain readings:

- Some location/customer labels are unclear, including possible "Bugis," "Tuas," "Yishun," and other customer names or route zones.
- Some channel labels are unclear, especially whether "W.E" means WeChat or another channel.
- Several product names, abbreviations, and units are ambiguous and should be clarified with Zhao before implementation.
