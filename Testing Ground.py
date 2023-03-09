import openai
openai.api_key =

print(openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a story about a mouse.",
  max_tokens=100,
  temperature=0
))
