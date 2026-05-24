---
title: strawberry, the agentic browser
date: 2026-05-24 20:55:00 +0100
categories: [til, product, tech]
summary: an agentic browser comibining the concepts of second brain, skills, and a genuine working agent loop
---

til there exists an agentic browser called [strawberry](https://strawberrybrowser.com/) and it has absolutely blown my mind!

let me clarify one thing - i knew it existed before today, because charles maddock and a part of his team have been coming up on my linkedin feed in one way or another but it's only today that i gave into the hype and really tried it for myself. and boy, was it impressive!

i went in expecting yet another "Chat GPT style sidebar bolted onto chromium" style experience ([Comet](https://www.perplexity.ai/comet), looking at you here) and came out convinced this might be the first browser that actually deserves the title *agentic*.

what makes it different is that it isn't just trying to be a chat window with a browser attached. it's a browser with three things stitched together at the core:

1. **a second brain** - it remembers what you've looked at, what you cared about, and the threads you've been pulling on. so when you come back later and ask it something vague, it actually has the real context to answer like a colleague (or even you, yourself) would.

    ![strawberry's second brain]({{ site.baseurl }}/assets/images/2026-05-24-strawberry/strawberry-brain.jpg)

2. **skills** - reusable little capabilities you (or it) can compose. this is the bit that feels closest to how i've been using [claude code skills](https://www.anthropic.com/news/skills), except now they live inside the thing i already spend 80% of my day in.

    ![strawberry skills]({{ site.baseurl }}/assets/images/2026-05-24-strawberry/strawberry-skills.jpg)

3. **a genuine agent loop** - not "summarise this YT video" parlour (yes Google that's a dig at you) tricks, but a system that can plan, take actions across tabs, and actually finish a real task. or tasks, rather. and the reason this loop actually runs is that the workflows have clearly been researched to death and ship out of the box, so you're not building them yourself (you could do if you wanted to) from a blank canvas.

    ![strawberry workflows]({{ site.baseurl }}/assets/images/2026-05-24-strawberry/strawberry-workflows.jpg)

the architecture above (brain + skills + workflows) is what lets all three stitched-together pieces work in concert. and even if you want to argue it isn't *really* agentic under the hood - honestly, it doesn't matter. it feels like it is, and that's the bit that counts and led to my my "holy shit" moment

it isn't simply calling a model on every keystroke - it's pulling from personalised memory, connecting the right tools (Slack, Mail, CRMs etc.), dispatching the *right* skill, and only invoking heavyweight reasoning when it actually needs to; that's the same architectural insight that makes agents feel snappy instead of laggy, and i've never seen it applied to a browser before.

and honestly? for the kind of research-y, multi-tab, "i need to research into this industry/topic and then absorb all I can about it" workflow i do as a PM all day, this might already be replacing [perplexity](https://www.perplexity.ai/) or Google for me. 

see, perplexity is brilliant as a search-answer engine, but it lives in its own walled garden. 
strawberry is meeting me where i already am - in the browser, on real pages, with *real* context about me as an individual - and just gets on with it.

i'll come back to this once the honeymoon wears off and write a more sober take but right now, i'm fully in the "where has this been all my life" phase.

hats off to you Charles Maddock and team 🫡

p.s. what i said on linked in still stands - even on a 16 GB M4, I immediately experienced slowdown and dare i say, a lag?, during just the onboarding phase...might be something you guys want to look into!