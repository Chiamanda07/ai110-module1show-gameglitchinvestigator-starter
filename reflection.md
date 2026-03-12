# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
It looked ok, but I need to go through the interface to understand it better
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. The input box tells me to press enter to apply, but it doesn't work
  2. The hint only says go lower, when it is supposed to be going higher
  3. It shows me the answer when I still have one attempt left
  4. New game resets the attemps part of the code, but it does not do anything esle to make me be able to play again;  i.e the history is still filled up.
  5. Easy - Hard range is weird. Needs to be corrected
  6. Even when the difficulty level changed, the instruction did not change.


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude for this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
It helped correct the initial message error for check_guess() function by turning "guess > secret → "📉 Go LOWER!"
guess < secret → "📈 Go HIGHER!"". This was then verified through a code that was used for testing.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When correcting the input boxes using forms fir the submit button, it also rearranged the "show hint" button and put it above the other buttons. I verified my result by just cross checking what the code was before and what it was now after AI made the change and discovered the error.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I first looked over the test file that Claude had made, and understood it ran. I then ran it, fixed its errors and ran the app again to see if it worked.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  When I ran the test file, it had simple errors like not assigning some output of the functions to a variable. I then fixed those errors.
- Did AI help you design or understand any tests? How?
Yes. 
I didn't know how to test the second changes I made, so I asked Claude. It exaplained that the second changes I amde was less of a coding problem and more of a UI problem, So the most effective way to test it is by runniing the streamlit program. Although it gave a few coding tests.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
