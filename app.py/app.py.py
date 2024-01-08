import openai
# pass the api key

openai.api_key = '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'

# define prompt
message = {'role': 'user', 'content': 'why is my website down?'}
messages = []
messages.append(message)

# make an api call
response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages)

#print the response
print(response.choices[0].message.content)