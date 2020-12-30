# Static Personal Site

#### Components
- Developed using [Hugo](https://gohugo.io/)
- Using open sourced [theme](https://github.com/rhazdon/hugo-theme-hello-friend-ng)

#### Current Setup
- Hugo Code + HTML Code at [harshit_site](https://github.com/hpj1992/harshit_site)
- HTML code for Github Hosting at [hpj1992.github.io](https://github.com/hpj1992/hpj1992.github.io)
- [harshit_site](https://github.com/hpj1992/harshit_site) has 2 git submodules. Submodules are link to another github repository from one. 
  - Sub module 1: [hpj1992.github.io](https://github.com/hpj1992/hpj1992.github.io) at public folder
  - Sub module 2: [](https://github.com/rhazdon/hugo-theme-hello-friend-ng) at themes/hello-friend-ng
- Both sub modules point to head of master branch. Which means if master is broken, submodules will point to broken sub modules.
- Both sub modules are configured at [.gitmodules](https://github.com/hpj1992/harshit_site/blob/master/.gitmodules)
- [Portfolio](https://github.com/hpj1992/Portfolio) repository is of no use. Make no changes to it.

#### Make changes to website
Any new changes (new blogs, about me update etc) should follow below procedure.
- Make changes locally in `harshit_site` 
- `hugo` - this will build site locally
- `hugo server` - this will start hugo server. Once running successfully, verify changes locally
- At this point you have uncommited changes ready to deploy
- from root of `harshit_site`, execute `./deploy.sh "{commit-message}"`  - This will deploy your new changes at [hpj1992.github.io](https://github.com/hpj1992/hpj1992.github.io)
- Note `./deploy.sh` will not make any changes to `harshit_site` repository.
- To verify above changes, hit http://hpj1992.github.io/ -> this will redirect you to http://joshiharshit.com/ 
- You will not see your new changes yet - make sure to hit refresh or visit it on incognito mode to see new changes
- New changes should reflect now
- At this point you are done, but it is important to push these new changes to [harshit_site](https://github.com/hpj1992/harshit_site) as well. Otherwise, you can lose your local changes and harshit_site includes changes till second last commit, not the latest one.
- It is critical to keep [hpj1992.github.io](https://github.com/hpj1992/hpj1992.github.io) and [harshit_site](https://github.com/hpj1992/harshit_site) at same commits
- To achieve that, stay at root level of `harshit_site`
- `git add .` 
- `git commit -m "{commit-message}"`
- `git push` 
- Done.

TODO: Update `./deploy.sh` to push changes to both repository
