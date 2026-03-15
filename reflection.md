# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

- Hint keepts it kept telling us to go higher
- Once we guess correctly, it stops letting us play
- The history doesnt continue adding values
- the difficulty doesn't seem to make sense
- the score doesn't seem to restart at new game
- switching mid game doesn't reset the game

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used claude code and copilot.
It helped me figure out how different functions were related to each other as we'll it understood where thcleare bug was
One the suggestion was to move the developer debug thing down, but it didn't solve the attempt start problem.
Copilot was helpful in auto-filling some of comments.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

- I tested it manually and then added pytest tests to make sure to catch the edge cases
- one of the test I ran was to ensure that the input of the function was a string becasue we do typecasting in the function to fix of the bugs
- Yes, I helped me with the boilerplate syntax and some edge cases

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

Its not that the secret wasn't stable, it was that the hints we not correct, and some of functionality didnt make sense.
Streamlit "reruns" are a fresh new start to the app and the varibles reset to what they were originally.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - Using the #context, to add context to the prompts
  - Asking AI to refactor code
- What is one thing you would do differently next time you work with AI on a coding task?
  - I would commit more often so I can roll back when I need to.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - It definitely makes it a little less intimating. Using AI to code is often scary because if you dont use it carefully it may output code buggy code that you dont understand. And since you cant understand it you cant fix it and you end up spending more time debugging then you saved by generating.
