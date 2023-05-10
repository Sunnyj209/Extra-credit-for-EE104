import openai
openai.api_key = "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"
response = openai.Completion.create(engine="davinci", prompt="Hello, world!")
print(response.choices[0].text)
print(f"OpenAI API Key: {openai.api_key}")