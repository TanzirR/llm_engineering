```py
#OPENAI API

 response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "system_prompt"},
            {"role": "user", "content": "user_prompt"}
      ],
        response_format={"type": "json_object"}
    )
 result = response.choices[0].message.content
 json.loads(result)

```

```py
# Claude 4.0 Sonnet
# API needs system message provided separately from user prompt
# Also adding max_tokens

message = claude.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=200,
    temperature=0.7,
    system=system_message,
    messages=[
        {"role": "user", "content": user_prompt},
    ],
)

print(message.content[0].text)
```

```py
# Google released endpoints that means you can use Gemini via the client libraries for OpenAI
gemini_via_openai_client = OpenAI(
    api_key=google_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = gemini_via_openai_client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=prompts
)
print(response.choices[0].message.content)
```
