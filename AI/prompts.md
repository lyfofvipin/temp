Prompt structure is the way you organize instructions and context so an LLM can produce the result you want.

How to write a prompt:
```
WHO should the model be?
↓
WHAT should it do?
↓
WHAT information does it need?
↓
WHAT rules must it follow?
↓
HOW should the answer look?
```


Weak
```
Write something about databases.
```

Strong
```
You are a database instructor.

Explain SQL vs NoSQL.

Audience:
Beginner developers.

Requirements:
- Use simple language
- Include real-world examples
- Provide a comparison table

Length:
500 words maximum
```

Structure:
```
Role
Task
Context
Constraints
Output Format
```

Example:

`Explain binary search.`


```
Role:
You are a Python tutor.

Task:
Explain binary search.

Context:
The student knows loops and arrays.

Constraints:
Avoid advanced math.

Output Format:
Use simple examples and bullet points.
```


The Hierarchy the Model Sees:
```
System Instructions
↓
Developer Instructions
↓
User Prompt
↓
Conversation History
```

## Few-Shot Prompting

Instead of describing the pattern, show examples.

Example:
```
Input: Cat
Output: Animal

Input: Rose
Output: Plant

Input: Eagle
Output: Object
```

## Zero-Shot Prompting

Example:
```
Classify the following word as Animal, Plant, or Object:
Eagle
```

## Chain-of-Thought Prompting

Example:
`Solve this problem step by step.`

For many applications, asking for:
assumptions,
intermediate reasoning,
calculations,


## Delimiter Technique

Example:
```
Summarize the text between <article> tags.

<article>
...
</article>
```

And:

```
Text:
"""

content here

"""
```

A good Example:
```
Role:
You are a senior product manager.

Task:
Create a feature specification.

Context:
We are building a food delivery app.

Requirements:
- Include user stories
- Include edge cases
- Include acceptance criteria

Output:
Markdown document
```

