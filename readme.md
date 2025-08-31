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
