# Zhao OrderOps Call Notes

## Core Ask

Build a phase-one workflow tool that makes night-shift order capture less manual and less error-prone without replacing the existing ERP.

The immediate goal is not a full ERP. The goal is to capture customer WhatsApp orders accurately enough that morning operations can draw inventory with fewer corrections.

## Main Pain

- Current workflow is time-consuming, tedious, manual, and dependent on human context.
- Night-shift staff need to interpret vague customer orders, dialect, Singlish, accents, and customer-specific shorthand.
- The hard part is not basic text capture; the hard part is mapping vague product language to the exact SKU/spec.
- Example: "pork 5 kilos" could map to many possible inventory items, so the system needs customer history and product rules.

## Source Of Truth

- Existing ERP remains in place.
- ERP history only keeps roughly three months of customer order validity/history.
- WhatsApp group descriptions may contain customer-specific product specs maintained by sales.
- Sales updates are usually stable, but changes like thickness/spec can create ambiguity.
- ERP API access is uncertain and may be difficult because the ERP was built by an external team.

## Practical MVP

- Start with exported SKU lists and customer order history rather than deep ERP integration.
- Refresh exports weekly or fortnightly if real-time integration is not available.
- Use those exports plus WhatsApp group context as the matching layer.
- Match incoming orders against customer-specific order history and product lists.
- Flag ambiguous, missing, unusual, or new items for manual review.
- Let normal, repeatable orders pass through with a soft confirmation.
- Allow admin/manual updates for missing customer-product history or first-time products.

## Confirmation Flow

- Send a soft confirmation after capture: the order has been understood as X, and the team will follow up.
- Final confirmation still happens through invoice/stock availability.
- This gives the customer a chance to correct wrong specs early without pretending stock is guaranteed.

## Data Needed

- SKU/product master list.
- Customer-specific historical order lists.
- WhatsApp group/product description examples.
- Examples of ambiguous orders and how staff resolve them today.
- Any ERP export format that is available.

## Commercial Notes

- Zhao does not want a competitor-owned F&B platform because of customer and order-history data exposure.
- A privately hosted/self-owned deployment is a meaningful trust point.
- Scope should be fixed, simple, and useful first.
- Future upgrades should be treated as separate scopes once the first phase works.

## Implementation Direction

- Keep phase one narrow.
- Avoid building a full ERP.
- Build around data ingestion, matching, exception review, and soft confirmation.
- Treat ERP integration as optional later work unless exports are easy and reliable.
