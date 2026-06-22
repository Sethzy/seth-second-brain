---
type: raw_capture
source_type: x
url: https://x.com/P3b7_/status/2062807526463205876
original_url: https://x.com/P3b7_/status/2062807526463205876
author: "Charles Guillemet"
handle: P3b7_
status_id: 2062807526463205876
captured_at: 2026-06-20T00:13:17+08:00
published_at: "Fri Jun 05 08:03:34 +0000 2026"
capture_quality: complete
status: raw
trust_lane: intentional
metrics:
  replies: 315
  reposts: 213
  likes: 1028
---

# X post by @P3b7_

## Source

- Original: [https://x.com/P3b7_/status/2062807526463205876](https://x.com/P3b7_/status/2062807526463205876)
- Canonical: [https://x.com/P3b7_/status/2062807526463205876](https://x.com/P3b7_/status/2062807526463205876)
- Author: Charles Guillemet (@P3b7_)

## Verbatim Text

👉For 4 years, 1 day, and 10 hours, anyone who understood the Orchard circuit could have minted ZEC out of thin air, silently, with no on-chain signature. The bug was disclosed this week. It was found by an AI-driven audit running Opus 4.8, not by an attacker.

1. Call the bug what it is
Two lines in halo2's variable-base scalar multiplication gadget used assign_advice() where copy_advice() was required. As a result, the diversified-address integrity check pk_d = [ivk]·g_d could be satisfied for arbitrary inputs. A malicious prover could spend the same note multiple times with different nullifiers, i.e. counterfeit ZEC inside the Orchard pool, undetectable on-chain because the privacy of the ZK proof hides exactly the inputs that would reveal the attack.

We do not know whether it was exploited. We will probably never know.

2. Four years. Multiple audits. Top-tier reviewers.
Orchard was reviewed by some of the strongest cryptographers in the field before activation. They missed it. Earlier automated audits with Opus 4.7 missed it. Opus 4.8 catches it in roughly 1 in 4 runs when prompted generically. The bug is hard.

And ZK inflation bugs are not new. Zcash itself shipped a counterfeiting vulnerability in Sprout (BCTV14) that survived years before being silently neutralized during Sapling. Similar soundness issues have appeared in circom, halo2, and rollup verifiers since. The pattern is consistent: when the protocol is private, exploitation is undetectable. You patch the bug and hope.

3. What Zcash did right
This was a textbook decentralized incident response:

▶️Audit: a full AI-assisted soundness audit of halo2 + Orchard, scoped end-to-end.
▶️Discover: the agent flagged the missing constraint and worked out the algebra to turn it into an exploit. A working RPC-level PoC in ~6 hours, mostly waiting on tokens.
▶️Coordinate: a soft fork disabling Orchard, prepared and distributed without leaking the bug, activated 2 days and 15 hours after acknowledgement. Coordinating a soft fork across miners, exchanges, and nodes without disclosing why is genuinely hard. They did it.
▶️Disclose: timeline, code lines, math, open questions. No spin.
Worth naming explicitly: Zcash's turnstile invariant caps the value that can ever leave a shielded pool by the value that entered it. Privacy and verifiability inside the same protocol. That is not an accident. That is good engineering, and it is what kept the worst case bounded.

4. The economics of security just changed
AI does not change whether bugs like this exist. It changes the cost of finding them. I wrote about this https://t.co/AeurraJXhB: a missing constraint in a 4-year-old production ZK circuit used to require a top-tier cryptographer with months of context. It now requires a few tokens, an API key, and a well-framed prompt.

The defender benefits. The attacker benefits more, they only need to find it once, and they never disclose.

Orchard is the optimistic version of this story: defense got there first. The pessimistic version is the one we cannot rule out, because the chain is private by design.

5. The only real exit
You do not patch your way out of this asymmetry. You raise the floor.

Formal verification of consensus-critical circuits, every assign_advice audited by SAT solvers and AI for under-constraint, as the reporter himself recommends. Proof-grade engineering that used to be too expensive is now cheap enough to be mandatory.
Hardware roots of trust, secure enclaves, certified secure elements, WYSIWYS. Cryptographic guarantees the user can actually verify, not promises a host can lie about.
Continuous AI-assisted audit of every consensus-critical commit, re-run immediately on the release of any new frontier model.
Zcash didn't just patch a bug. They demonstrated the new defensive playbook: AI-driven audits, decentralized coordination, radical transparency, verifiable invariants. That is the direction the rest of the industry needs to follow. 

And those who don't raise the bar for security will be rekt in this new world.

Stay safe. Stay honest about your trust assumptions.

## Quoted Post

- URL: https://x.com/zooko/status/2062644925590900980
- Author: zooko🛡🦓🦓🦓 ⓩ (@zooko)

The Orchard Counterfeiting Vulnerability — and next steps

By Zooko Wilcox, Jason McGee, and Taylor Hornby

Update! This article is about the problem. See https://x.com/zooko/status/2063262293442678830 about the solution.

# Summary

On May 29, 2026, Taylor Hornby discovered a critical counterfeiting vulnerability in Zcash’s Orchard pool.

Taylor disclosed the vulnerability to Zcash Open Development Lab (ZODL), who coordinated an ecosystem-wide emergency response to fix the vulnerability, which was completed on June 2.

After reviewing Taylor's report and discussing the implications of the vulnerability internally, Shielded Labs believes it is important to provide additional context.

The vulnerability could have been exploited to undetectably create an unlimited amount of counterfeit ZEC within Orchard. Because of the privacy properties of Orchard, there is no way to cryptographically prove whether the vulnerability was exploited before it was remediated. However, a network upgrade can be deployed to protect users and prove the integrity of the Zcash supply.

# Background

In April 2026, Shielded Labs engaged Taylor Hornby to conduct ongoing security research focused on the Zcash protocol. Taylor is an experienced security engineer with a deep understanding of Zcash.

The goal of this work was simple: identify vulnerabilities before malicious actors do. Taylor immediately began evaluating Zcash using the latest AI-assisted security auditing techniques alongside traditional security research methods.

Shortly after the release of Anthropic's Opus 4.8 model on May 28, Taylor used it as part of a highly targeted review of the Orchard circuit. On May 29, Taylor discovered the vulnerability in the Orchard circuit and immediately disclosed it to ZODL engineers. ZODL engineers and others from the Zcash ecosystem acted quickly and skillfully to close the window of vulnerability within days.

# What We Know and What We Don’t Know

The vulnerability was real and exploitable. Taylor, with the help of Opus 4.8, wrote a complete exploit which, when he tested it in a local regtest environment, generated unlimited, undetectable counterfeit ZEC. If he had run the same tool on Zcash mainnet it would have generated unlimited, undetectable counterfeit ZEC in his mainnet Zcash wallet.

The vulnerability has to do with an under-constrained element of the Orchard circuit, because of which it was possible to put arbitrary false inputs into an elliptic curve multiplication and still have the multiplication check pass. See Taylor’s full [report and work log](https://drive.google.com/file/d/1SVK41y-ip3Vw9eB69E9QRy-Qn3idTOwV/view?usp=drivesdk) for details.

The vulnerability was present from Orchard's activation in May 2022 until the emergency fix was deployed on June 1, 2026.

What makes this particularly challenging is that, due to the privacy properties of Orchard and the nature of the bug, there is no definitive way to determine using only cryptography whether such exploitation occurred before the vulnerability was discovered and fixed. We believe it is important to be transparent about that uncertainty.

# Assessment: Prior Exploitation Of This Orchard Vulnerability Seems Unlikely

There are several reasons we are not overly concerned that counterfeiting occurred before this vulnerability was remediated.

First, the vulnerability had evaded years of scrutiny by many of the world’s best cryptographers.

Second, Shielded Labs specifically engaged Taylor Hornby for this purpose. The discovery was not accidental—it was the result of a deliberate effort to identify vulnerabilities of this kind before malicious actors could. Taylor is one of the most skilled people in the world at this. He used the most recent AI tools, available only to white-hat security researchers, along with a sophisticated custom-built AI harness and prompts, and worked hard to outrace the attackers. We think he probably succeeded.

Once the vulnerability was discovered, the window of opportunity for attack was sharply limited by the speed with which ZODL and the Zcash ecosystem executed the remediation.

Taken together, these factors suggest to us that there were few people who had the capability and opportunity to discover and exploit this vulnerability prior to it being fixed.

# Proving the Integrity of the Zcash Supply

Our assessment is that exploitation of this vulnerability was unlikely. However, we do not believe that users should rely on our assessment, or anyone else’s. Shielded Labs is exploring —with the help of other Zcash developers—a proposed Network Upgrade to allow anyone to verify the integrity of the Zcash supply and to prove the non-existence of counterfeit Zcash in the Orchard pool. The proposal involves deploying a new shielded pool and enforcing turnstile accounting on all coins from the Orchard pool.

We plan to publish a follow-up post next week that explains the proposal in greater detail, including how it would work and the tradeoffs involved. Like all major network upgrades, it would require support from Zcash users and need to go through the standard governance process before it could be activated.

# Accelerating Our Security Work

At the same time, we are doubling down on proactive security research, including using state-of-the-art AI tools, to find problems before the bad guys do. We have already begun the next stage of that, with the help of Taylor Hornby and Anthropic, and we’ll keep you updated.

In addition, Shielded Labs is initiating a project to formally verify the Orchard circuit—an attempt to write a mathematical proof that there are no more undiscovered bugs in it.

Shielded Labs is opening a search for a Head of Security and a Cryptographer to help deepen our security efforts. If you're interested, or know someone who may be a good fit, please reach out.

# Conclusion

This was a serious vulnerability, and we believe it's important to be transparent about what it means for Zcash users.

We hired Taylor to find any vulnerabilities before the attackers, and that's exactly what he did. We're grateful for his work, the quick response from ZODL and the Zcash Foundation, as well as the many ecosystem participants who helped remediate the issue.

While no one wants to discover a vulnerability like this, we're confident that Zcash is well positioned to recover. We stand ready to continue to help the other Zcash development groups and the Zcash community as a whole in how they want to move forward.

# Acknowledgements

Thanks to Sean Bowe, Dev Ohja, David Campbell, Alex Bornstein, Nate Wilcox, Kris Nuttycombe, and Vitalik Buterin for review and feedback.

Appendix A: [Taylor’s work log PDF](https://drive.google.com/file/d/1SVK41y-ip3Vw9eB69E9QRy-Qn3idTOwV/view?usp=drivesdk) – the dramatic story of the discovery of the vuln!

## Media

- photo: https://pbs.twimg.com/media/HKCPArbWMAAT2O-.png

## Capture Note

TweetDetail returned complete normal-post text.
