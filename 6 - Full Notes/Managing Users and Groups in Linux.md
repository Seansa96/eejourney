2024-08-06 12:57

Status: #child

Tags: [[linux]] [[red-hat]] [[3 - Tags/cli]] [[bash]]

# Managing Users and Groups in Linux

A user who creates a file owns it, and is also the group owner of that file.
Only root can change who owns the file. The user who owns it cannot do this. ONLY ROOT
Access permissions (read, write, execute) can be modified by the file owner and root.
A user who owns the file can however change the group that owns it.

So:

`ls -l testfile.txt`

`-rwxr--r-- testfile.txt` has file owner rwx perms, group perms are read only, other group is read only.

The file owner cannot change the user who OWNS the file, but he can change the group that owns it (thus, the scope of the 2nd set of bits.

Every user has a UID (user ID) and each group has an associated GID (group ID).

Users within a group share rwx perms.

It is important to note that in unix and unix-like operating systems, file permissions are assigned based on the first available security bit match. This is referred to officially as Discretionary Access Control.  There is no official term for each triplet of the total permission bit structure (although the overall structure is referred to as the "mode"). But since each permission bit is indeed a value from 0 to 8, then you can refer to each bit as a triplet, much in the same vein that each portion of an IP address is an octet, since its binary-to-decimal value ranges from 0-255.

RHEL reservers UIDs and GIDs below 1000 for system users and groups.  The reserved UIDs and GIDs are available locally in the setup packinage, at /usr/share/doc/setup, with each profile having a /uidgid sub-directory.

Thus, to view them all, you can run the command cat /usr/share/doc/setup*/uidgid, and probably pipe that to more or perform other filtering commands upon that output.

RHEL officially recommends starting any new IDs and GIDs at 5000 to future proof your systems, but this is of course not a hard rule. You are free to do as you please.

You can set a lower bound for new users to start at by default by modifying the login.defs file in /etc/, adjusting the UID_MIN and GID_MIN parameters.

In case you are wondering--no, this does not apply retroactively.


**User Private Groups (UPG)** - In RHEL, there is a special group created whenever a new user is added to the system.  This private group has the same name as the user (so, if user Shawnzx is made, a UPG named Shawnzx is simultaneously created).

**--Demonstration here--** https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/identity_management_guide/user-private-groups

It is important to note that it is atypical for system/service users to have an accompanying UPG.  While there is no definite way to prove this, here are a few ways you can use to mostly confirm whether or not there is a UPG assigned to a user.

getent group <username> will show you: <user>:password bit:gid
grep '<username>' /etc/group will produce similar as above
grep '<username> /etc/passwd will display <user>:password bit:uid:gid::<user home dir>:<login shell/whether or not the user can use an interactive terminal session>
id <username> The gid name here would generally match the uid name. Format is - uid=<actual uid.(username) gid=<actual gid>(primary group name) groups=<gids>(names of all groups user is part of).

To demonstrate this further, here is:

`groupadd testgroup1`
`groupadd testgroup2`

usermod -aG testgroup1, testgroup2 shawnzx

getent group
id shawnzx

Note that you can prevent this behavior (that of assigning a UPG to a user at creation) with the -N/--no-user-group flag. This will instead cause the useradd command to set the primary group of the new user to the value specified by the GROUP variable in /etc/default/useradd, or 100 by default.

And here are the basic commands to manipulate users, while we're at it.

id - displays user and group IDs and related info

useradd - allows you to create a user acc. Add options for greater specificity. Syntax is useradd <username>.
Useful options are -G (to add a user to specific groups at its inception). -g/--gid to specify an initial gid value.
-N as referred previously. -c/--comment to adda  short description to the user. -e/--expire-date to set a date at which the user will expire. -f/--inactive to set a date when the user's account will become permanently disabled after their password expires. This is dependent upon the INACTIVE variable in /etc/default/useradd.

-u/--uid to set the initial UID. Must be unique unless the -o option is used.
-U/--user-group if you have disabled default UPGs, to essentially create a UPG on creation. -Z/--selinux-user. Outside of the scope of this lesson but bear it in mind.

usermod - allows you to modify a specified user account. Syntax is usermod <option> username. 
Useful options are: -a/--append. Use only with the -G option as you need to define supplementary groups to append the user to. -G/--groups to list the groups that you wish to perform an action against with the user's account.
Many of the same options as useradd, so I won't discuss many further. One significant different option is the -L/--lock option, which lock's a user's password. To lock the user's account, you would need to set the EXPIRE_DATE to 1.You can do this with the -e/--expire-date flag. Format is specified in the YYYY-MM-DD style.  An empty value here disables expiration. This also requires an /etc/shadow file. The command wiil create one if none exists.



passwd - updates the user's authentication tokens using the Linux-PAM, an API/framework suite to interact with user accounts and authentication of said accounts. Syntax is passwd <option> example-user

-l/--lock, (root only) note the lowercase here as opposed to usermod's uppercase L.  Like usermod, this will lock the account's password, making it accessible only by means other than the password, like ssh authentication keys.

-u/--unlock (root only). Self-explanatory.

-d/--delete (root only). Deletes the password, essentially unlocking the account. Useful hack in some situations.

-e/--expire (root only). User will be forced to set a new password after their next login.

-S/--status - Provides various useful information about the user's password. Locked password=LK, No password=NP, usable password=PS.


On deleting users:
userdel <username>. However, this is inelegant and does not fully purge the user's files.
userdel -r <username> will delete their home dir, mail spool and skel directories, but any files outside of these directories they own will not be affected. You will require a more focused approach or granular scripting or custom service/package. Ansible has plenty of features for automating the cleanup of user resources.



# Reference:

https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/managing-users-and-groups_configuring-basic-system-settings

https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/identity_management_guide/user-private-groups

https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/linux_domain_identity_authentication_and_policy_guide/idm-domain