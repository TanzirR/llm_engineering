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
google.generativeai.configure(api_key=google_api_key)
gemini = google.generativeai.GenerativeModel(
    model_name='gemini-2.0-flash',
    system_instruction="system_prompt"
)
response = gemini.generate_content("user_prompt")
print(response.text)

```
