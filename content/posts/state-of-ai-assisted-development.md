+++
date = "2026-02-11"
linktitle = "Re-wiring rules of SDLC: AI Through a Senior Engineer’s Lens"
type = ["post", "posts"]
title = "Re-wiring rules of SDLC: AI Through a Senior Engineer’s Lens"
weight = "10"
series = ["AI", "LLM", "Vibe Coding", "Software Development"]
[ author ]
  name = "Harshit Joshi"
+++

With new large language models improving almost every day, I can’t help but feel excited. It reminds me of about ten years ago, when every new cloud tool or managed platform felt like a small dopamine hit. Back then, the excitement was about spinning up infrastructure in seconds and offloading undifferentiated heavy lifting to managed services. Today, that same feeling is back—but this time, the shift is happening in the way we actually build software. It feels less like an incremental improvement and more like a re-wiring of development processes that have been mostly unchanged for over a decade.

---

### Coding Was Never the Bottleneck

In traditional software development, coding was rarely the slowest part of the job. The real time sink was always figuring out what to build and how to build it. Design discussions, trade-offs, system constraints, and long-term impact consumed most of the engineering cycles. Once those decisions were made, implementation was relatively straightforward—even before AI assistance existed.

Now, with the rise of what people call “vibe coding,” that reality is even more obvious. When an LLM can produce functional code in seconds, the bottleneck shifts almost entirely to problem definition and system thinking. Knowing exactly what you want to build, why you’re building it, and how it should behave becomes the primary skill. The clearer the intent, the better the prompt. And the better the prompt, the faster you move.

---

### Where AI Is Changing the Daily Workflow

In my day-to-day work, I’ve noticed that AI is not just speeding up coding—it’s changing how entire parts of the development cycle feel.

**Ideation and trade-off analysis** are much faster. Instead of thinking in isolation, I can bounce ideas off an LLM, explore alternative architectures, and quickly surface pros, cons, and edge cases. It feels like having a technical sounding board available at all times.

Another big shift comes from **connecting agents to tools through MCP-style integrations**. A lot of the operational work that used to involve logging into multiple dashboards can now happen directly from the command line. Agents can run queries, fetch metrics, inspect logs, and execute workflows without me context-switching across half a dozen tools. The development environment starts to feel more like a unified control panel.

**On-call debugging** is where this change becomes very tangible. With the right access, an agent can log into the appropriate environment, run queries against logs, wait for results, analyze the output, and report back. While one agent is doing that, another can be drafting a fix, writing tests, or preparing a patch. It starts to feel like having two additional senior engineers working in parallel, while I focus on the higher-level decisions and coordination.

When it comes to **coding itself**, I’ve naturally started operating in two different modes. For well-defined tasks, I use spec-driven development. Clear requirements and interfaces lead to predictable, high-quality generated code. For exploratory work or smaller features, I lean into a more vibe-driven approach, where speed and iteration matter more than perfection. Both approaches have their place, and choosing the right one is part of the new workflow.

One of the most practical improvements is how quickly I can **onboard to a new codebase**. Instead of spending days navigating unfamiliar repositories, I can ask the LLM to map out the project structure, explain code paths, and trace requests through the system. Questions like “where does this logic live?” or “what calls this function?” get answered in seconds. That alone can compress onboarding time significantly.

---

### What Still Isn’t Perfect

This new way of working is not without its rough edges.

**Context management** is still a real challenge. When the context window overflows, the model may forget earlier instructions or produce inconsistent results for the same prompt. Long sessions require careful structuring, otherwise things start to drift.

Another limitation is that **LLMs still tend to operate in silos**. They usually reason about one file, one service, or one module at a time. They don’t naturally understand the full system context—like upstream dependencies, downstream consumers, or the long-term architectural impact of a change. This is where experienced engineers remain essential. System thinking and domain knowledge are still very human strengths.

**Code review has also become more important, not less.** Generated code often comes with unnecessary abstractions or designs for hypothetical future use cases. It feels a lot like reviewing code from an enthusiastic engineer who wants to over-engineer everything. As a senior engineer, part of the job now is to guide the output by refining prompts and enforcing principles like KISS, DRY, and YAGNI. The review process becomes less about syntax and more about architectural discipline.

---

### Context Switching Becomes a Superpower

Working with coding agents also changes what kind of working style becomes an advantage. Agents naturally encourage parallel work streams and constant context switching. If you’re someone who is comfortable juggling multiple threads at once, that might actually become your superpower.

While one agent is running queries, another is generating code, and a third is preparing a fix, you’re coordinating all of them in parallel. Instead of doing one task at a time, you’re effectively delivering multiple outcomes simultaneously by managing and switching context efficiently. In this new workflow, the ability to orchestrate several moving parts can be just as valuable as deep technical expertise.

---

### The Role of the Senior Engineer Is Evolving

All of this points to a bigger shift in the role of the senior engineer. A decade ago, productivity was closely tied to how quickly and accurately you could write code. Today, the leverage comes from defining problems clearly, orchestrating tools and agents, and reviewing generated solutions at scale. The role starts to look less like a code producer and more like a system designer, technical strategist, and agent orchestrator.

It really does feel like the early days of cloud computing again—but instead of abstracting servers and infrastructure, we’re abstracting parts of the development process itself. The tools are evolving fast, the feedback loops are getting shorter, and the leverage per engineer is increasing. For those willing to adapt, it’s an incredibly exciting time. The last decade of software development practices is being quietly re-wired in real time.

![test!](/images/sdlc.png "SDLC")
