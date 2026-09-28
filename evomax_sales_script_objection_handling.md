# Vector Compute - Sales Script & Objection Handling Guide

## 1. The Sales Script (The "Sovereign Compute" Pitch)

**Context:** This script is designed for a 15-30 minute discovery/introductory call with a Chief Digital Officer (CDO), CTO, or Head of AI following up on the outbound email.

### Step 1: The Opening & Pattern Interrupt
**You:** "Hi [Name], thanks for taking the time. I know you’re leading the GenAI rollout at [Company Name]. Typically, when I speak with leaders in your position at [similar companies, e.g., Maybank/Singtel], they are caught between a rock and a hard place: the board wants AI efficiency, but compliance and security say you can’t send your best data to OpenAI or Azure. Is that a tension you’re navigating right now?"

*(Let them answer. They will almost always agree. This establishes you understand their core problem immediately.)*

### Step 2: The Diagnosis (Validating the Pain)
**You:** "Exactly. What we've found is that the default solution—using public APIs—is a direct violation of data sovereignty. Even if they promise not to train on your data, the moment your internal documents leave your server’s RAM and hit a US-based cache, you’ve lost control. On top of that, your teams are probably experiencing what we call 'token bloat'—wasting 30-40% of your API budget on redundant context. Sound familiar?"

### Step 3: The Pitch (The Zero-Retention Doctrine)
**You:** "That’s why we built EvoMax. Think of EvoMax as a sovereign security checkpoint that sits entirely inside your firewall. 

Before any prompt leaves your network, EvoMax mathematically compresses it—scrubbing PII, removing 40% of redundant tokens, and ensuring that your data never touches a persistent disk. We call this the **Zero-Retention Doctrine**. 

The result for [Company Name] is threefold:
1. **Total Compliance:** You satisfy [RMiT/PDPA/etc.] because sensitive data never leaves your sovereign control.
2. **Instant ROI:** You cut your LLM API bill by up to 40% overnight.
3. **Speed:** We drastically reduce latency for your end-user applications."

### Step 4: The Call to Action (The Audit)
**You:** "We aren’t asking you to rip out your existing models. EvoMax runs parallel to your current stack. What we’d like to do is set up a **free 30-day token audit**. We’ll run a sample of your non-sensitive prompts through our local engine to show you exactly how much token bloat you have and how much money you'll save. If the math makes sense, we can talk about a pilot. How does your schedule look next week for a brief technical walkthrough with our engineering team?"

---

## 2. Objection Handling Guide

### Objection 1: "We already have an Enterprise Agreement with Microsoft Azure / AWS, and they promise data privacy."
**The Reality:** They promise not to *train* on the data, but it is still subject to the US CLOUD Act, and data is still being logged in their telemetry.
**Your Rebuttal:** "Azure and AWS are great platforms, and EvoMax actually works perfectly *with* them. The issue isn't whether they train on your data; the issue is data sovereignty and cost. Under the US CLOUD Act, they can be compelled to hand over data. Furthermore, Microsoft doesn't compress your prompts—they charge you for every single token you send. EvoMax sits *between* you and Azure, ensuring no PII ever reaches their servers and cutting your Azure OpenAI bill by 40% before it even gets there."

### Objection 2: "We are building our own Private Cloud / running Llama 3 locally."
**The Reality:** On-prem hardware for LLMs is incredibly expensive to buy, maintain, and power. 
**Your Rebuttal:** "That’s a highly secure route, but as I'm sure your finance team has noticed, provisioning H100 GPUs locally is a massive CapEx burden, and managing the infrastructure is a nightmare. EvoMax gives you the security of an on-prem deployment (zero retention, on-shore processing) but allows you to leverage the intelligence of frontier models without the CapEx. You get the best of both worlds."

### Objection 3: "We just don't have the budget for another enterprise software tool right now."
**The Reality:** EvoMax is designed to pay for itself immediately through API savings.
**Your Rebuttal:** "I completely understand budget constraints. That's actually why we lead with EvoMax. It’s not a net-new expense; it’s a cost-recovery tool. Our current clients are seeing a 30-40% reduction in their LLM API costs. EvoMax pays for its own license within the first quarter of deployment. That’s why we offer the 30-day token audit—we will prove the ROI before you spend a dime."

### Objection 4: "Our AI usage is still too experimental; we aren't spending enough on tokens to justify this."
**The Reality:** They will be soon. 
**Your Rebuttal:** "That makes this the perfect time to talk. It is much harder to retroactively secure and optimize an AI architecture once hundreds of agents are in production. By placing EvoMax at the gateway now, you future-proof your compliance and ensure that as your usage scales, your costs scale linearly, not exponentially. Let's do a quick architecture review to ensure you're setting up for safe scaling."

### Objection 5: "Is your compression actually lossless? Will the AI still understand the prompt?"
**The Reality:** Lexical and semantic compression removes filler words, not meaning.
**Your Rebuttal:** "It is functionally lossless for the LLM. LLMs don't need perfect grammar to understand intent. Our ML classifiers strip out 'filler' tokens and redundant context that humans need but machines don't. We maintain the semantic integrity of the prompt. During the token audit, we will show you a side-by-side comparison of the original output vs. the EvoMax compressed output to prove there is zero degradation in quality."
