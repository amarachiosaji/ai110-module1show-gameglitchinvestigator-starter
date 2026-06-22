# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The first time I ran it, the game loaded fine and looked polished- title, guess box, attempts counter, a debug panel. But playing it, things were off. I figured out that something was off when I opened the Developer Debug Info panel, saw the actual secret was 83, and noticed the hints pointed the wrong way.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  Reversed hints- Secret 83, guessed 23 → "Go LOWER"; guessed 99 → "Go HIGHER" (backwards)
  Scrambled difficulty tiers- Range + Attempts don't follow Easy→Normal→Hard logic

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guessed 23 when secret was 83 (seen in Debug panel) | Hint should say "Go HIGHER" since 23 < 83 | Hint said "Go LOWER"- direction reversed | none |
| Guessed 87 then 99 when secret was 83 (seen in Debug panel) | Score should stay at 0 or above | Score dropped from 0 to −5 to −10 with each wrong guess | none |
| Opened Settings sidebar, compared Easy / Normal / Hard | Harder difficulty should mean a bigger range and/or fewer attempts | Normal's range (1–100) is bigger than Hard's (1–50), and Easy gives fewer attempts (6) than Normal (8) | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
