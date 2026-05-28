
2024-08-16 17:08

Status: #baby 

Tags: [[guide]] [[git]]



Setting Git up for Pushing Commits

You'll need to set up an SSH key, which you can refer to [[SSH Key Gen]] for.

Once that's done, you need to paste the public key to the https://github.com/settings/keys section by making a new key.

Now, while in the repo you intend to set up for commits/pushing, run:

`git remote -v`
to check the current URL. If it's https, you need to change it using:

`git remote set-url origin git@github.com:<username>/<repo-name>.git` filling in the tagged fields with the requisite info.

You may also need to do a `git config --global --edit` but likely not.

Now, you should be fine to stage and push commits.





## References:
