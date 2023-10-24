import openai

openai.api_key = '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'

messages = []
content = "코끼리가 뭐야?"
messages.append({"role": "user", "content": content})
print(messages)

completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = messages
)
com = completion
res = completion.choices[0].message.content
print(com.usage)

messages.append({"role": "assistant", "content": res})
print(messages)