import openai
openai.api_key = "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"

print(openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a story about a mouse.",
  max_tokens=100,
  temperature=0
))
