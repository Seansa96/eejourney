# Vim Commands Cheat Sheet

A beginner reference for basic movement, editing, and saving files.

## Navigation

- [[#Start here]]
- [[#Modes]]
- [[#Basic movement]]
- [[#Insert text]]
- [[#Delete, copy, and paste]]
- [[#Undo and redo]]
- [[#Find text]]
- [[#Save and quit]]
- [[#A simple editing workflow]]

## Start here

Open a file from your terminal with `vim filename.txt`.

**When unsure, press `Esc` to return to Normal mode.** Most commands below work in Normal mode. Keys are case-sensitive: `g` and `G` are different.

- `dd` means press `d` twice in sequence.
- `Ctrl+r` means hold `Ctrl` and press `r`.
- Commands beginning with `:` and searches beginning with `/` need `Enter` to run.

## Modes

| Mode         | What it does                               | How to enter                  |
| ------------ | ------------------------------------------ | ----------------------------- |
| Normal       | Move around and run editing commands.      | Press `Esc`. Vim starts here. |
| Insert       | Type text into the file.                   | Press `i` from Normal mode.   |
| Visual       | Select text to copy or delete.             | Press `v` from Normal mode.   |
| Command-line | Enter commands such as saving or quitting. | Press `:` from Normal mode.   |

## Basic movement

Use these in **Normal mode**. Arrow keys also work for basic movement.

| Key                | Movement                                    |
| ------------------ | ------------------------------------------- |
| `h`                | Left one character.                         |
| `j`                | Down one line.                              |
| `k`                | Up one line.                                |
| `l`                | Right one character.                        |
| `w`                | Forward to the start of the next word.      |
| `b`                | Back to the start of a word.                |
| `e`                | Forward to the end of a word.               |
| `0`                | Start of the line. This is the number zero. |
| `^`                | First nonblank character on the line.       |
| `$`                | End of the line.                            |
| `gg`               | First line of the file.                     |
| `G`                | Last line of the file.                      |
| `:25` then `Enter` | Jump to line 25; use any line number.       |
| `Ctrl+d`           | Scroll down about half a screen.            |
| `Ctrl+u`           | Scroll up about half a screen.              |

Put a number before a movement to repeat it: `5j` moves down five lines, and `3w` moves forward three words.

## Insert text

Use these from **Normal mode**, then type your text. Press `Esc` when finished.

| Key | Action                                              |
| --- | --------------------------------------------------- |
| `i` | Insert before the cursor.                           |
| `a` | Insert after the cursor.                            |
| `I` | Insert at the first nonblank character on the line. |
| `A` | Insert at the end of the line.                      |
| `o` | Create a new line below and start typing.           |
| `O` | Create a new line above and start typing.           |

## Delete, copy, and paste

Use these in **Normal mode**, unless a selection is mentioned. Vim calls copying **yanking**.

| Key                         | Action                                                           |
| --------------------------- | ---------------------------------------------------------------- |
| `x`                         | Delete the character under the cursor.                           |
| `dd`                        | Delete the current line.                                         |
| `D`                         | Delete from the cursor to the end of the line.                   |
| `yy`                        | Copy the current line.                                           |
| `p`                         | Paste after the cursor; copied lines go below the current line.  |
| `P`                         | Paste before the cursor; copied lines go above the current line. |
| `r` followed by a character | Replace the character under the cursor with that character.      |
| `v`, move, then `y`         | Select characters and copy them.                                 |
| `v`, move, then `d`         | Select characters and delete them.                               |
| `V`, move, then `y` or `d`  | Select whole lines, then copy or delete them.                    |

Counts also work here: `3dd` deletes three lines, and `3yy` copies three lines.

Deleted text can be pasted with `p`, so `dd` followed by movement and `p` is a simple way to move a line. A later deletion or yank can replace what an ordinary `p` will paste.

These commands use Vim's internal registers; they do not necessarily use your system clipboard.

## Undo and redo

| Key      | Action in Normal mode                              |
| -------- | -------------------------------------------------- |
| `u`      | Undo the last change. Repeat to undo more changes. |
| `Ctrl+r` | Redo an undone change.                             |
| `.`      | Repeat the last editing change.                    |

## Find text

Start in **Normal mode**.

| Command              | Action                                          |
| -------------------- | ----------------------------------------------- |
| `/text` then `Enter` | Search forward for `text`.                      |
| `?text` then `Enter` | Search backward for `text`.                     |
| `n`                  | Go to the next match in the search direction.   |
| `N`                  | Go to the next match in the opposite direction. |
| `:noh` then `Enter`  | Clear the current search highlighting.          |

Search patterns can treat punctuation as special. For a literal search, start with `\V`, such as `/\Vfile.txt`.

## Save and quit

Press `Esc` first, type the command, then press `Enter`.

| Command           | Action                                                       |
| ----------------- | ------------------------------------------------------------ |
| `:w`              | Save the file.                                               |
| `:w filename.txt` | Write the current contents to the given filename.            |
| `:q`              | Quit. Vim refuses if there are unsaved changes.              |
| `:wq`             | Save and quit.                                               |
| `:q!`             | Quit and discard unsaved changes.                            |
| `:set number`     | Show line numbers.                                           |
| `:set nonumber`   | Hide line numbers.                                           |
| `:help`           | Open Vim's built-in help. Use `:q` to close the help window. |

## A simple editing workflow

1. Open a file: `vim notes.txt`.
2. Move with `h`, `j`, `k`, `l`, or the arrow keys.
3. Press `i` and type your changes.
4. Press `Esc` to return to Normal mode.
5. If you made a mistake, press `u` to undo it.
6. Type `:wq` and press `Enter` to save and quit.

**First commands to memorize:** `Esc`, `i`, `h j k l`, `w`, `b`, `dd`, `yy`, `p`, `u`, `:w`, and `:q`.
