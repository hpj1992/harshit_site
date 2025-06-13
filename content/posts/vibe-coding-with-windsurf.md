+++
date = "2025-06-08"
linktitle = "Vibe coding To-Do app with Windsurf"
type = ["post", "posts"]
title = "Vibe coding To-Do app with Windsurf"
weight = "11"
series = ["AI", "LLM", "Vibe Coding", "Windsurf"]
[ author ]
  name = "Harshit Joshi"
+++

## What are we doing in this article? 

In this article we will explore how did Winsdurf do when asked to create a simple To-Do application locally using React. I personally have very limited experience with React and majority of front-end technologies. So I was using Windsurf to help me create a simple To-Do application. I started with a basic prompt mentioned below and fine-tuned my responses as Windsurf generated the code. 

Entire screen recording is also available for you to watch. 

{{< youtube rMTkj-p746Y >}}

## Experience Rating

Here's my personal rating of Windsurf's performance across different aspects while building the To-Do application:

| Aspect | Rating (out of 10) | Emoji Rating | Comments |
|--------|-------------------|--------------|----------|
| One shot utterance outcome | 7/10 | ⭐ | Basic functionality was working with good looking UI. However it had few bugs related to permissions and functionality. |
| First run | 8/10 | ⭐ | First ever run had it working in browser with add, edit, mark complete and delete. However it still had bugs related to not persistent items upon refresh. |
| Setting Up Projects | 9/10 | 🏆 | Excellent at project initialization, dependency management, and creating the basic structure. Almost perfect for React setup. |
| Debugging and Problem Solving | 8/10 | ⭐ | Very good at identifying and fixing common React errors. |
| Code Review and Refactoring | 7/10 | 👍 | Looking at generated it is of descent quality. I had specifically asked to add comments in my first prompt. |
| Design and Layout | 8/10 | ❌ | Initial CSS and components it came up with was really nice looking with good color combination and responsive. |
| Functional Competency | 8/10 | ⭐ | It correctly implemented basic CRUD operations on to-do items. |
| Surprise Factor | 8/10 | 👍 | It added these features without me asking 1) Enter is add 2) Made design responsive 3) Chose checkbox to mark it complete instead of button (single click) 4) Buttons and icons  |


## High level workflow 

### 1) First prompt 

```
Create a simple to-do application using react. The application should allow users to add, remove, edit and mark tasks as complete. Make sure user interface is intuitive and visually appealing. Include code comments to explain the funationality of each component and the overall structure of the code easy to understand. Also, provide brief overview of the statemegement how it is handled. Id database is required, create in-memory database as needed. 
```

This prompt resulted into entire project setup with React and basic functionality with in-memory database. 

1.A ) while creating files, it needed to make it public. Without that all the file creations were failing. You can see this in video at 1:11. 

Post that, it `npm install` and `npm start` started the server with basic Task manager app. It was able to 1) Add new to-do 2) Delete to-do 3) Edit previously created todo. You can see this in action beginning 3:00 in the video linked above. 

### 2) Testing first working version


2.A) Initially it had no button to mark todo as complete. So I prompted it to fix it. However, based on response looked like just clicking on it will mark it complete. Which was not very intuitive in the beginning. I asked it to update it and add separate sections for previously completed items. 

```
Found 2 bugs: 
1) No feature to mark item as complete 
2) No feature which shows deleted or previously completed items 
```

Windsurf was able to update the code based on my prompt. Now updated UI had separate compoenets for All, Active and Completed. 

2.C) Asked one more requirement 

I noticed it was not persisting the counts of to-do/tasks when I refresh the page. This suggested it was not persisting the tasks in the local db and not fetching at the load time. 

```
Found one more bug. When page is refreshed - data is lost 
```

Initially it suggested logic is correct and went on and suggested to debug in the browser. Immediaately it also agreed that it was critical bug and went on to fixing in the app.js . It had missed adding else block if it was not array. It fixed with following logic 

```
else {
          // If parsedTodos is valid JSON but not an array (e.g., "null", "true", "123", "{}")
          console.warn('Stored todos is valid JSON but not an array. Resetting. Found:', parsedTodos);
          setTodos([]);
        }
```

Even after above fix it was not working, I had to prompt again with below at 13:09. 

```
issue still persists. Once I add a task and refresh a page - it is lost 
```

At this point - functionality stand point it had all the basic to-do app features working.

### 3) Improving desing 

```
Improve color scheme. Add some more animations. Improve the layout and make it responsive. 
```

I did not push further as design was neat and clean. You can see final design and UI beginning 15:45 in the video linked above.

![Final version](/images/vibe-code-windsurf-to-do.png)

---

*Have you tried Windsurf? Share your experiences and tips in the comments below!*git submodule update --recursive
