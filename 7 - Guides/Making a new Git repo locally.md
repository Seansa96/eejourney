
1. Go to the directory you want to push
2. Open the cmd prompt in that directory
3. `git init -b main`
4. This will make the .git dir in the cwd.  At this point you can `git commit -m "my first push"` and then
5. `git remote add origin https:github.com/USERNAME/REPO.git`
6. Check it with `git remote -v` and then `git push origin main`


# gitignore

You can add a .gitignore file in the root of the repo, NOT INSIDE THE .git DIR.  Then, use relative pathing (absolute pathing does not work) to blacklist certain directories or files as needed from being pushed.