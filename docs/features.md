# Features

Beyond multi-agent and styling, Claude Assistant includes several quality-of-life features.

## Shell Access

Run shell commands without leaving the UI:

```bash
!git status          # Quick inline command
!ls -la              # Output displayed in chat
```

```bash
!nvim README.md      # Interactive command
!git log             # Drops into native shell
```

<video src="https://github.com/user-attachments/assets/85f3dbe0-9a88-436e-aa9d-c1ba012c1f0e" autoplay loop muted playsinline></video>

Or use the explicit form:

```bash
/shell git diff      # Same as !git diff
/shell -i htop       # Interactive mode (suspends TUI)
/shell               # Opens interactive shell
```

**Inline mode** captures output and displays it in the chat. **Interactive mode** (`-i` flag or no command) suspends the TUI and gives you a real terminal—useful for commands that need interactivity like `vim`, `htop`, or `git rebase -i`.

## Vim Mode

Toggle vi-style keybindings for the input area:

```bash
/vim                 # Toggle vim mode on/off
```

When enabled, the input supports vi normal/insert modes. Setting persists across sessions.

## Background Processes

Claude sometimes runs long-running commands (builds, tests, servers). Track them:

```bash
/processes           # Show modal with all background processes
```

The process panel in the sidebar shows active processes. Click to view details or kill runaway processes.
