+++
date = "2025-05-24"
linktitle = "Vibe coding To-Do app with Cursor"
type = ["post", "posts"]
title = "Vibe coding To-Do app with Cursor"
weight = "11"
series = ["AI", "LLM", "Vibe Coding", "Cursor"]
[ author ]
  name = "Harshit Joshi"
+++

In the ever-evolving landscape of software development, the tools we use can significantly impact our productivity and coding experience. One such tool that has been making waves in the developer community is Cursor - an AI-powered code editor that's redefining how we write and interact with code. In this post, I'll share my experience with Cursor and how it's transformed my coding workflow.

## What are we doing in this article? 

In this article we will explore how did cursor do when asked to create a simple To-Do application locally using React. I personally have very limited experience with React and majority of front-end technologies. So I was using Cursor to help me create a simple To-Do application. I started with a basic prompt mentioned below and fine-tuned my responses as Cursor generated the code. 

Entire screen recording is also available for you to watch. 

{{< youtube k3h_jew1b38 >}}

## Experience Rating

Here's my personal rating of Cursor's performance across different aspects while building the To-Do application:

| Aspect | Rating (out of 10) | Emoji Rating | Comments |
|--------|-------------------|--------------|----------|
| One shot utterance outcome | 6/10 | ✅ | Basic functionality was working. However it had few bugs. |
| First run | 2/10 | ❌ | First ever run after setting up dependency and packages had errors. |
| Setting Up Projects | 9/10 | 🏆 | Excellent at project initialization, dependency management, and creating the basic structure. Almost perfect for React setup. |
| Debugging and Problem Solving | 8/10 | ⭐ | Very good at identifying and fixing common React errors. Sometimes needed additional context for complex state management issues. |
| Code Review and Refactoring | 7/10 | 👍 | Looking at generated it is of descent quality. I had specifically asked to add comments in my first prompt. |
| Design and Layout | 5/10 | ❌ | Basic CSS suggestions were helpful, but needed more guidance for complex layouts and responsive design. I could not get it to fix the background structure. |
| Functional Competency | 8/10 | ⭐ | It correctly implemented basic CRUD operations on to-do items. |
| Surprise Factor | 7/10 | 👍 | It added these features without me asking 1) Enter is add 2) Made design responsive 3) Chose checkbox to mark it complete instead of button (single click) |

While Cursor is powerful, it's important to:
- Review generated code carefully
- Understand the suggestions before implementing
- Use it as a tool, not a replacement for learning
- Keep security considerations in mind


## High level workflow 

### 1) First prompt 

```
Create a simple to-do application using react. The application should allow users to add, remove, edit and mark tasks as complete. Make sure user interface is intuitive and visually appealing. Include code comments to explain the funationality of each component and the overall structure of the code easy to understand. Also, provide brief overview of the statemegement how it is handled. Id database is required, create in-memory database as needed. 
```

This prompt resulted into entire project setup with React and basic functionality with in-memory database. 

1.A ) after this when I ran the server, it had mismatched versions and missing imports. 
1.B ) After fixing above, it ran but browser was empty nothing was there.

Post that, it was able to fix and it worked. 

### 2) Testing first working version

2.A) When I refresh the page after adding To-Dos, app was not persisting them. Asked Cursor to fix it 
2.B) Next I Asked it to do following: 

```
I see 3 issues. 1) Home page design is not good. 2) deleted to-dos should move to deleted section. 3)  there is no button to mark task as complete.
```

2.C) Asked one more requirement 

```
One more issue - once all the tasks are marked complete - count in "Active Task" should be 0 but it still shows count of all the to-dos created ever. 
```

At this point - functionality stand point it had all the basic to-do app features working. 

### 3) Improving desing 

It improved the design but I was not able to remove the balck portion at the bottom of the page. I tried following prompts 

```
improve the home page design even more. Remove black and white background and keep 1 consistent background. 
```

```
Bottons are better. However there is still while background which changes the size depending on number of to-dos. Remove that and keep just 1 box in entire page. Remove black part from the bottom. 
```

## Resources

- [Cursor Official Website](https://cursor.sh)
- [Cursor Documentation](https://cursor.sh/docs)
- [Cursor GitHub Repository](https://github.com/getcursor/cursor)

---

*Have you tried Cursor? Share your experiences and tips in the comments below!*