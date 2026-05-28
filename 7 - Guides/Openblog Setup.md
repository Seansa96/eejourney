2024-08-14 18:28

Status: #baby 

Tags: [[guide]] [[webdev]] 



## Openblog Setup: Fresh Install

On a fresh system, you'll need a few things:

- [x] Nginx
- [x] git
- [x] node
- [x] npm
- [x] pnpm

So, here's the order you can run it in:

1. sudo apt update
2. sudo apt upgrade
3. sudo apt install nginx
4. sudo apt install git
5. sudo apt install curl (you download node this way from the latest Node repo)

`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash`

^above script can be found at nvm github docs https://github.com/nvm-sh/nvm?tab=readme-ov-file#install--update-script.

To install pnpm:

`npm install -g pnpm`


Edit the src/data/config.ts with necessary metadata. This would be site name, author, description, and pagination number.

Then, go to the astro.confing.mjs at the project root dir to add your domain to the `site` listing.

Do the same thing at `root/public/robots.txt`

#### Building the application

To do so, we just need to first install all the dependencies, which you can do with

`pnpm install`

Once this is done, if you want to mess around (this would be on the local setup) and see what it looks like, you can do:

`pnpm run dev`

This will launch a dev server on the configured server (4321 by default).
TinaCMS will also launch at the same time, allowing you to edit it easily. 

#### Hooking it up to the Webserver


Now, we'll need to do the nginx config to serve it.

We'll first remove the default symbolic link at `/etc/nginx/sites-enabled/` for the default config file.

Next, we'll go `vi` into `/etc/nginx/sites-available/<yourdomainname>` (as in, you'll do this command to generate the file).

You can just remove everything not related to the `server` block.  Make especially sure to get rid of the `default_server` block.

Set `root` to the root project directory. **DON'T USE YOUR GIT REPO DIRECTORY FOR THIS. CAUSES BIG PROBLEMS.** Just use default nginx.

Set `server_name` to your domain name
You can leave location alone for now
Add two logging statements: `access_log /var/log/nginx/<domainname_access.log` and `error_log /var/log/nginx/<domainname_error.log`

Now, save and exit. Add a symbolic link in `sites-enabled` to this file. You can do this with:
`sudo ln -s /etc/nginx/sites-available/<domainname> /etc/nginx/sites-enabled`

If nginx isn't running, start it and run a `sudo nginx -t`. If it is running, do a `sudo systemctl reload nginx` then do `sudo nginx -t`. This is to test the config and see it is ok.

Now just go to the browser and test.  

### Typical Issues

Permissions. Nginx may not own or have the necessary permissions to use the files in your project directory. Use `chown` and `chmod` to resolve this.

Incorrect syntax in the `sites-available` config.  Make especially sure your configuration isn't commented out...I'd totally never do that.

Issues with nginx cache

I've also encountered build issues when there's an existing dist/ folder in the git repo. Running either (or both) `npm cache clean --force ` and an rm -rf on the dist/ folder will fix it. Avoid user superuser when building.



## Official Node Docs

# installs nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash

# download and install Node.js (you may need to restart the terminal)
nvm install 18

# verifies the right Node.js version is in the environment
node -v # should print `v18.20.4`

# verifies the right npm version is in the environment
npm -v # should print `10.7.0`
## References:
https://github.com/danielcgilibert/blog-template