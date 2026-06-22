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
I used two AI tools on this project: Claude chat— for planning/understanding bugs, and Claude Code in VS Code— for proposing the actual fixes.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One AI suggestion that was correct: when I fixed the scoring bug, I asked Claude Code to: "In app.py, the update_score function (marked with a FIXME) has broken scoring. I want to replace the logic with these rules: a wrong guess — whether "Too High" or "Too Low" — subtracts 5 points, and the score must never go below 0 (floor at 0). On a "Win", return the score unchanged. Please rewrite update_score to do exactly this and nothing more. Separately, the score is initialized to 0 in session_state — I want it to start at 100 instead". It suggested: "def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        return current_score

    if outcome == "Too High" or outcome == "Too Low":
        return max(0, current_score - 5)

    return current_score
And the session_state score initialization change (around line 99-100):

if "score" not in st.session_state:
    st.session_state.score = 100". I verified it by tracing the math by hand: 100→95→90, checking 0 stays at 0, then confirming it live in the running game.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Honestly I didn't get one. I think that's because of how I worked: specific prompts, and only one bug per chat. Most importantly, instead of auto-applying the AI's code, I asked to view it first, reviewed it myself, then pasted it in manually. So even during the riskiest change— the refactor, where the AI could have silently rewritten my fixed functions — I checked the diff/code to confirm my hint and score fixes survived.

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
