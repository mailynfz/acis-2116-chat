# CostGPT

I am a GPT4-powered chat assistant to answer your questions about ACIS 2116 at Virginia Tech. Ask me anything about your managerial accounting class. I am trained on your class materials, and can answer questions from your class syllabus, course lecture notes, and exam review sheets. I can help you study important course concepts and explain how to solve problems. Because I\'m AI, I don\'t need sleep, so I am here 24/7 to help you study for your upcoming final exam. Go Hokies! 😎

# Caveat Emptor
While AI chat assistants performing information retrieval from a knowledge base (known as retrieval augmented generation, or RAG) tend to perform more accurately, there's still a possibility of hallucination. That is, it will literally make stuff up. In additional to RAG using OpenAI's latest `gpt-4-1106-preview` model, I have also enabled OpenAI's code interpreter, which handles the calculations in its responses using Python. While I'm very excited with CostGPT's accuracy and performance explaining accounting concepts and answering accounting questions/problems from the class, it's still just a language model...it's NOT a math model, NOT an accounting model. Just as you might be a bit skeptical about accounting advice from an English teach, you should verify CostGPT's responses with your course materials. If you encounter any egregious or unexpected errors, please let me know by filling out [this short feedback form](https://forms.gle/3DfPAG86RyepVXMo8).

# Get started
To use CostGPT, you must use your own OpenAI API key to pay for your own usage. If you don\'t have an API key, go to [openai.com](openai.com) to create a new one ([here is a quick tutorial](https://youtu.be/UO_i1GhjElQ?si=7VvfWK8AXQG6vdcn)).

I would love nothing more than to find a rich benefactor to pay for the API costs related to running this app, but unfortunately I haven't found an accountingGPT sugar daddy yet, so we're stuck paying our own way here. However, OpenAI gives new users $5 in API credits for the first 90 days of an account (if you have an existing ChatGPT account, you might need to setup a new account to get the $5 credit) and the overall cost per user should be relatively inexpensive. This app uses the `gpt-4-1106-preview` model, which costs \$0.01/1K tokens for input and \$0.03/1K tokens for output (response). For reference, 1K tokens is equivalent to approximately 750 words. In addition to your prompt, the app will take as input its predefined instructions (~350 tokens) and any information it retrieves from its knowledge base (i.e., the class materials that I uploaded). To retain context, the app will also resubmit the entire conversation (i.e., thread), which increases the number of input tokens per prompt. You can reduce the number of input tokens by starting a new thread if the conversation gets too long--just click the "Start New Chat" button again. Learn more about [OpenAI's pricing here](https://openai.com/pricing). 

**Note:** Unlike the ChatGPT interface that you might be used to, this app does not retain your conversation history. Once you start a new chat or exit the page, your chats are gone forever, and there's no guarantee that it will every reproduce the same exact response again. Therefore, if you find the information in your chats useful, consider copy-pasting the thread into your prefered text editor or note-taking app so that you can refer to it later.

## Prompting Advice for Students
- In general, you should be as specific as possible for the bot to respond with helpful answers.

- If it's having trouble recognizing your questions as part of the course content, start your prompt by asking it to refer to its knowledge base. 
    - For instance, "According to your lecture notes, what is chapter 7 about?" or "according to your files, what is IRR?"
- Ask it to refer to specific chapters
    - "According to the Chapter 14 lecture notes, what is the IRR?"

- When asking it for help solving a specific problem, ask it to use step-by-step reasoning. For instance, you can copy-paste a question into the chat box then add the text "Explain your reasoning step-by-step" to the end of your prompt.
    - It also helps to tell it what chapter the question comes from.
    - The template that I have been using to ask it for help solving sample questoins look something like this:
> Here is an example problem from Chapter 14. <br>
> Casey Nelson is a divisional manager for Pigeon Company. His annual pay raises are largely determined by his division’s return on investment (ROI), which has been above 20% each of the last three years. Casey is considering a capital budgeting project that would         require a $3,500,000 investment in equipment with a useful life of five years and no salvage value. Pigeon Company’s discount rate is 16%. The project would provide net operating income each year for five years is $400,000, which is reported net of $700,000              depreciation expense. What is the project's IRR? <br>
> Please explain your reasoning step-by-step.

- I don't know whether to say this first or last, but in general you should be polite to the AI. There's research shows kids who learn to speak with a voice assistant in their home, like Alexa or Google Assistant, grow up to be less polite to humans, in part because they grew up barking orders at a bot, without practicing how to say please or thank you. You will go on to correspond in writing in your professional lives and you don't want the way you communicate with AI to change the way you communicate with other humans. Also, just in case AI does ever become sentient, it's probably not bad for it to remember that you were one of the nice humans. 😂

