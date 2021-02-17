---
author:
  name: "Harshit Joshi"
date: 2021-02-15
linktitle: Professional Programmer - The Clean Coder
type:
- post
- posts
title: Professional Programmer - The Clean Coder
weight: 10
series:
- Books
---

 In [The Clean Coder: A Code of Conduct for Professional Programmers](https://www.amazon.com/dp/0137081073/ref=cm_sw_em_r_mt_dp_40RD8RQ0KB2XD4A5BFHM), legendary software expert Robert C. Martin introduces the disciplines, techniques, tools, and practices of true software craftsmanship. This book is packed with practical advice–about everything from estimating and coding to refactoring and testing. It covers much more than technique: It is about attitude.

In this article, I have tried to summarize key insights from the book, carefully picking key advices from each chapter.

## 1 Minute Summary
If you do not have time to read detailed summary below, just try to apply below points on your software engineering life:


> You can not take pride and honor in something that you can not be held accountable for. Any code you are not certain about is a faulty code.

> When the cost of failure is so high that survival of your company depends upon it, you must be absolutely determined to give your managers the best information you can. and that often means saying no.

> There are three parts of saying yes. You *say* that you will do it. You *mean* it. And you actually *do* it.

> Programing is hard. The younger you are the less you believe this. You have to carefully partition the system into small understandable units that have as little to do with each other as possible - and *that is hard*.

> It is often difficult to test a function if that function calls other functions. In other words, the need to test first forces you to think about good design.

> When performance matters, professionals practice. Doing anything quickly requires practice. 

> To make good on the goal that "QA should find nothing", development teams need to work hand in hand with QA to define testing strategies.

> Software professionals keep their options open by keeping an open mind about alternate solutions. They never become so vested in a solution that they can not abandon it.

> Most software is created by teams. Teams are most effective when the team members collaborate professionally. 

> Teams are harder to build than projects.

> School can teach the theory of computer programming, but school does not and can not teach the discipline, practice, and skill of being craftsman.

## Let's Understand More

### Professionalism 
Professionals take responsibilities. You can not take pride and honor in something that you can not be held accountable for. Take responsibility to complete the clean code on time, and if not possible, take responsibility to communicate early. Shipping incomplete/faulty code/build is bound to fail. Any code you are not certain about is a faulty code. Only way to avoid it is to test, test and test. QA should find nothing. And if it is hard to test, refactor/rewrite. They key thing is to keep your hands dirty in code all the time. The more changes you make, the more you know the code, the more you test and the better estimates. Repeat this cycle all the time.

### Saying NO
When your manager tells you that X module has to be ready by tomorrow, he is pursuing and defending one of his objectives. He is doing his job. If you know full well that getting model X by tomorrow is impossible, then you are not doing your job if you say "Ok, I will try. I might work extra hours". The only way to do your job, at that point, is to say "No, that is impossible." Your manager is counting on your to defend your objectives as aggressively as he defends his. That is how the two of you are going to get to the best possible outcome. 

~~~~
The most important time to say no is when the stakes are highest. The higher the stakes, the more valuable no becomes.
~~~~

Temptation to jump start and "solve the problem" is huge. What we all have to realize is that saying yes to dropping our professional discipline is not the way to solve problems. Dropping those disciplines is the way you create problems. Despite years of constant reminders that every feature a client/manager asks for will always be more complex to write than it is to explain. As a developers, we are going to be asked/told to write twice the code in half the time if we are not careful.

### Saying YES
Professionals are not required to say yes to everything that is asked of them. However, they should work hard to find creative ways to make "yes" possible. When professionals say yes, they use language of commitment so that there is no doubt about what they have promised. There are three parts of saying yes:
- You *say* you will do it
- You *mean* it
- You *actual do* it

You can only commit to things that you have full control of. If the end goal depends on someone else, you should commit to specific actions that bring you to the end goal. If it can not be done, you can still commit to actions that will bring you close to the target. And sometimes, it just will not work. That happens, something unexpected might happen, and that is fine. But you still want to live up to expectations. In 
that case, it is time to change the expectations, as soon as possible. If you can not make your commitment, the most important thing is to raise a red flag as soon as possible to stake holders.

### Coding
Programing is hard. The younger you are the less you believe this. After all, it is just a bunch of `if` and `while` statements. But as you gain experience you begin to realize that the way you combine those `if` and `while` statements is critically important. You can't just slather them together and hope fo the best. Rather, you have to carefully partition the system into small understandable units that have as little to do with each other as possible - and *that is hard*.

Software development is a marathon, not a sprint. You can't win the race by trying to run as fast as you can from the outset. You win by conserving your resources and pacing yourself. A marathon runner takes care of her body both before and during the race. Professional programmers conserve their energy and creativity with the same care. Coding is an intellectually challenging and exhausting activity. It requires you to balance:
- First, your code must work.
- Your code must solve the problem set for you by the customer.
- Your code must fit well into existing system. It should not increase the rigidity, fragility, or opacity of that system.
- Your code must be readable by other programmers.

Juggling all above concerns is hard. It is physiologically difficult to maintain the required concentration and focus for long periods of time. If you are tired or distracted, *do not code*. Some of the best advices are:
- Make sure that your sleep, health and lifestyle are tunes so that you can put in eight good hours per day.
- Non work related worries affect your work. Partition the time. Rather than forcing yourself to code while the background worry is nagging you, spend dedicated block of time, handling the worry.
- Like me, many engineers love [the flow zone](https://en.wikipedia.org/wiki/Flow_(psychology)). Reality is, you lose some of the big picture while you are in the Zone, so you will likely make decisions that you will later have to go back and reverse.
- *Disengagement* from work allows your mind to hunt for solutions in a different and more creative way.

Even after following all best practices mentioned above, we might fall short while coding. We will be late. It happens to the best of us. The trick to managing lateness is early detection and transparency. Top recommendations to avoid running late on work:
- Do not *hope* that you can get it all done in ten days. Hope is a project killer.
- Do not rush. The poor developer might buckle up and agrees to try to make the deadline. That developer will start taking shortcuts and working extra hours with the *hope* of working a miracle.
- Do not agree to work overtime unless
  - You can personally afford it
  - It is short term, two weeks or less
  - Your boss has a fallback plan in case overtime effort fails

### TDD - Test Driven Development
I personally have not used TDD in a professional environment, however after reading this chapter of a book I can not wait to use it professionally.

The unit tests are documents The describe the lowest level design of the system. They are unambiguous, accurate, written in a language that audience understands.The problem with testing code is that you have to isolate that code. It is often difficult to test a function if that function calls other functions. In other words, the need to test first forces you to think about good design.

The three laws of TDD
- You are not allowed to write any production code until you have first written a failing unit test
- You are not allowed to write more of a unit test than is sufficient to fail.
- You are not allowed to write more production code that is sufficient to pass the currently failing unit test.

Round and round the cycle you go. Adding a bit to the test code. Adding a bit to the production code.

### Practicing
When performance matters, professionals practice. Doing anything quickly requires practice. Spinning around code/test loop quickly requires you to make very quick decisions. Making decisions quickly means being able to recognize a vast number of situations and problem and simply know what to do to address them.

There are various ways developer can keep practicing, weekly/monthly sessions to solve some of the well known problems. [Kata programming](https://en.wikipedia.org/wiki/Kata_(programming)) is an exercise in programming which helps programmers hone their skills through practice and repetition.

In one way or another, all professionals practice. They do this because they care about doing the best job they possibly can. They practice on their own time because it is their responsibility - and not their employer's - to keep their skills sharp.

### Acceptance Testing
Both business and programmers are tempted to fall into the trap of *premature precision*. Business people want to know exactly what they are going to get before they authorize a project. Developers wan to know exactly what they are supposed to deliver before they estimate the project. Both sides want a precision that simply can not be achieved, and are often willing to waste a fortune trying to attain it. The solution to premature precision is to defer precision as long as possible. Professional developers do not flesh out a requirement until they are just about to develop it. However, it can lead to another problem: *late ambiguity*. Late ambiguity is a term which represents some requirements missed or discovered late in the development cycle. This type of late ambiguity can result into missing dates or delivering imperfect product. Solution to both those problems is to define **Acceptance Tests**. Acceptance tests are not QA tests, these are tests written by a collaboration of the stakeholders and the programmers in order to define when a requirement is done.

Purpose of acceptance test is communication, clarity, and precision. By agreeing to them, the developers, stakeholders, and tests all understand what the plan for the system behavior is.

### Testing Strategies
Professional developers test their code, but testing is not simply a matter of writing a few unit tests or integration tests. What every team needs is a good testing strategy.

![test!](/images/tests-pyramid.png "Pyramid Tests")
Image by [Codingjourneyman](https://www.google.com/url?sa=i&url=https%3A%2F%2Fcodingjourneyman.com%2F2014%2F09%2F24%2Fthe-clean-coder-testing-strategies%2F&psig=AOvVaw0yiHP_hoeBuhQ66bDIaJXR&ust=1613544169334000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCOD7gs3m7e4CFQAAAAAdAAAAABAD)

- #### Unit tests: At the bottom of the pyramid are the unit tests. These tests are written by programmers, for programmers. The intent is to specify system at the lowest level.
- #### Component Tests: These are written against individual components of the system. IT encapsulates the business rules.
- #### Integration Tests: These tests only have meaning for larger systems that have many components. Integration tests are choreography tests. They do not test business rules, rather, they test how well assembly of components dance together.
- #### System/API tests: These are automated tests that execute against the entire integrated system. We can expect to see throughput and performance tests in this suite.
- #### Manual Exploratory Tests: This is where humans put their hands on. The intent of these tests is to explore the system for unexpected behaviors while confirming expected behaviors.

TDD is a powerful discipline, but they are only part of a total testing strategy. To make good on the goal that "QA should find nothing", development teams need to work hand in hand with QA to define testing strategies.

### Time Management
Software professionals are diligent in the management of their time and their focus. They understand the temptations of [priority inversion](https://en.wikipedia.org/wiki/Priority_inversion) and fight it as a matter of honor. They keep their options open by keeping an open mind about alternate solutions. They never become so vested in a solution that they can not abandon it. And they are always on the lookout for growing messes, and they clean them as soon as they are recognized. There is no sadder sight than a team of developers fruitlessly slogging through an ever deepening bog.

Time management Tips:
- Meetings cost about $200 per hour per attendee, considering salaries, benefit, facilities etc. Professions are aware of the high cost and aware of their time, so they actively resist attending meetings that they do not have an immediate and significant benefit.
- You have an obligation to manage your time well. If you find yourself stuck in a meeting that is not a good use of your time, you need to find a way to politely exit that meeting.
- To use the participants' time wisely, the meeting should have a clear agenda with times for each topic and stated goal.
- Standup meeting should not take more 1 minute for each participant.
- Sprint/Iteration planning should not take more than 5% of total duration of entire sprint. ie 2 hours for 40 hour sprint planning.
- Any argument that can not be settled in five minutes, can not be settled by arguing.

Focus management Tips:
- Focus is a scarce resource, after you have expended your focus, you have to recharge by doing unfocussed activities. 
- A good long walk, a conversation with friends, a time of just looking outside window can help you pump the focus back up.
- You will get most focus after good night's sleep.
- Muscle focus can help you recharge mental focus. ie martial arts, tai-chi, yoga, meditation.

### Collaboration
Most software is created by teams. Teams are most effective when the team members collaborate professionally. It is unprofessional to be a loner or a recluse on a team.
The first responsibility of the professional programmer is to meet the needs of his or her employer. that means collaborating with your managers, business analysis, testers and other team members to deeply understand the business goals.It means that you need to understand why you are writing the code you are writing, and how the business that employs you will benefit from it.

One of the worst symptoms of a dysfunctional team is when each programmer builds a wall around his code and refuses to let other programmers touch it. I personally have not faced any such situations. Today's world is at least able to collaborate good. It is far better to break down all walls of code ownership and have the team own all the code.

### Teams And Projects
Teams are harder to build than projects. Therefore, it is better to form persistent teams that move together from one project to the next and can take on more than one project at a time. the goal in forming a team is to give that team enough time to gel, and the keep it together as an engine for getting many projects done.

Professional development organization allocate projects to existing gelled teams, the do not form teams around projects. A gelled team can accept many projects simultaneously and will distribute the work according to their own opinions, skills and abilities.

### Craftsmanship

School can teach the theory of computer programming, but school does not and can not teach the discipline, practice, and skill of being craftsman. A craftsman is someone who works quickly, but without rushing, who provides reasonable estimates and meets commitments. A craftsman knows when to say no, but tries hard to say yes. A craftsman is a professional.

Craftsmanship is the mindset held by craftsman. It is handed from one person to another. It is taught by elders to the young. It is exchanged between peers. Observed and learned. You can not convince people to be craftsman. You act as a role model. You become a craftsman first, and let your craftsmanship show.

Reinforcing my learning, was refreshing to document the book insights here.

Thank you.
