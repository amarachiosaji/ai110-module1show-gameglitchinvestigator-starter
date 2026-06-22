# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- Describe the game's purpose: A number guessing game where the player guesses a secret number between a range, getting higher/lower hints until they win or run out of attempts
- Detail which bugs you found: Reversed hints, negative/fluctuating score, scrambled difficulty tiers
- Explain what fixes you applied: Corrected the swapped hint messages in check_guess; rewrote update_score to subtract 5 per wrong guess floored at 0, starting score at 100; refactored logic into logic_utils.py

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:


1. User opens the app and sees "Guess a number between 1 and 100. Attempts left: 8"
2. User enters a guess of 40 → game returns "Too Low 📈 Go HIGHER!"
3. User enters a guess of 90 → game returns "Too High 📉 Go LOWER!"
4. Score starts at 100 and drops by 5 on each wrong guess (and never goes below 0)
5. User guesses the correct number → "🎉 Correct! You won!" and the score stays at its current value



## 🧪 Test Results

```
tests\test_game_logic.py .....                    [100%]
===== 5 passed in 0.08s =====
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
