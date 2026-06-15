## The Core Goal of an LLM

An LLM is fundamentally a next-token prediction machine.

Given:

"The capital of France is"

the model estimates probabilities:
| Token  | Probability |
| ------ | ----------- |
| Paris  | 95%         |
| London | 2%          |
| Berlin | 1%          |

Example:
```
Input:
"The capital of France is"

Output token:
" Paris"

New input:
"The capital of France is Paris"
```

## Context Window

The model sees a sequence of tokens called the context.

Example:

User: My dog's name is Max.
...
User: What's my dog's name?

Because "Max" is inside the context window, the model can use it.

The context window is essentially the model's working memory during inference.


## Attention

Attention answers:
Which previous words should I focus on right now?

Example:
```
John put the book on the table.
He picked it up later.
```

When processing "it", attention helps the model connect "it" to "book".
Conceptually:
```
Current token
      ↓
Look at all previous tokens
      ↓
Assign importance scores
      ↓
Combine relevant information
```

## Parameters
Parameters are the learned numbers inside the model.
A parameter is roughly a learned weight that influences predictions.
Training adjusts these weights to reduce prediction error.


## Training

Training consists of:

Take text.
Hide the next token.
Predict it.
Measure error.
Update weights.

Example:
```
Input:
"The sky is"

Target:
" blue"
```

The model predicts: Green
Error is calculated.
Weights are adjusted.
This process is repeated trillions of times.


## Loss Function
Lower loss means better predictions.
During training:
```
High loss
↓
Medium loss
↓
Low loss
```

How it's done:
```
Make prediction
↓
Calculate error
↓
Determine which weights caused it
↓
Adjust weights slightly
↓
Repeat
```

### Pretraining

Pretraining is where the model learns language itself.
Data may include:
Books
Websites
Articles
Documentation
Code

The objective remains:
Predict the next token.
No human labels are required.


## Fine-Tuning

After pretraining, models are often specialized.
Examples:
Coding assistants
Medical assistants
Legal assistants
Customer support bots
Fine-tuning teaches the model behaviors and domain knowledge beyond general language modeling.

## RLHF ( Reinforcement Learning from Human Feedback )

```
Model generates answers
↓
Humans rank answers
↓
Reward model learns preferences
↓
Model is optimized toward preferred behavior
```

## Hallucinations

LLMs do not store facts the way databases do.
They generate text that is statistically likely.
Sometimes this produces incorrect but plausible-sounding outputs, called hallucinations.
This happens because the model is optimizing for likely continuations, not guaranteed truth.

## Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation (RAG) is an architecture in natural language processing that combines document retrieval with text generation. It enables large language models to access and incorporate external knowledge sources dynamically, improving factual accuracy and grounding responses in verifiable information.

```
Question
↓
Search knowledge base
↓
Retrieve relevant documents
↓
Provide documents to LLM
↓
Generate answer
```

