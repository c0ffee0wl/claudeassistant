# Multi-Agent Workflows

Run multiple Claude agents simultaneously, each with its own context and working directory.

## Agents

Traditionally, one `claude` session is bound to one `agent`.  If you want to work on multiple things, you create multiple `claude` sessions in multiple terminals.

With Claude Assistant, you type `/agent some-new-name` and a new agent starts running in your session with access to all the same files.  You can switch back and forth between these agents easily.

-  Many agents in parallel
-  Agents persist in normal Claude storage
-  Agents can run in different directories
-  Agents can start other agents
-  Agents can ask questions of other agents

### Example: Review

**Situation:** you've done lots of work and want a fresh agent to review this
work (not the one who helped you in the first place)

!!! user ""
    /agent reviewer

!!! user ""
    Please review the ongoing work in this branch with a critical eye.

    Tell the other agent running what you think when you're done.

When you call `/agent` you create a new agent and the UI immediately moves you
there.  That agent is in the same directory and can see all of your work, but
isn't biased by the context of your previous agent.

### Example: Review (automatic)

!!! user ""
    Start a new reviewing agent and have it review our work.  Ask it what it thinks

Claude Assistant comes with a small MCP server that gives Claude the ability to use
the `/agent` and related commands.

## Agent Commands

| Command | Description |
|---------|-------------|
| `/agent` | List all running agents |
| `/agent <name>` | Create new agent in current directory |
| `/agent <name> <path>` | Create new agent in specified directory |
| `/agent close` | Close the current agent |
| `/agent close <name>` | Close agent by name |

You can also switch between agents or close them by clicking in the sidebar.

## Concurrent development

Using multiple agents makes it trivial to have many ongoing threads of work.  You can start a new thread any time and then leave it for days.  You can bounce between agents as they're busy or idle as you like.

In practice this also helps with agent context, creating many agents, each with a small task avoids context bloat and, anecdotally, may improve agent focus and performance.

## Example: Deep Review and Many Tasks

**Situation:** You ask Claude to do a deep review on your project and it
generates a lot of work.  You spawn all of that work in separate agents.

!!! user ""
    Do an in-depth review of this project, paying particular attention to
    organization and cleanliness.  Think hard and propose improvements

!!! claude ""
    This project is great, but has many issues.  Here are some:

    1.  ...
    2.  ...
    3.  ...
    4.  ...

!!! user ""
    Thank you, start agents for tasks 1, 2, and 4.

Then several new streams of work are created and you can engage with them
individually as they progress.

## Resuming work

When you restart Claude Assistant, your agents will be listed in the sidebar.  All of your state is, as always, stored in Claude state in `~/.claude/projects/`, just like any other Claude session.

In practice this means you can start work freely without worrying about
finishing it soon (or ever).  It is free to keep agents around.
You can close your session and open it up again next week and all your agents
will be ready for you.

## Example: Chess

*Just for fun, you can ask Claude to play Chess against itself using multiple agents:*

<video src="https://github.com/user-attachments/assets/735ebc91-335e-4476-8fde-f49ce1df056a" autoplay loop muted playsinline style="max-width: 100%"></video>

## FAQ

??? question "How does this relate to normal SubAgents or Tasks?"

    Claude normally can launch subagents or tasks for parallel work .  These let Claude delegate work to other claude agents in parallel before bringing their summary back to the main agent.  This helps to parallelize and avoid context bloat.

    Claude Assistant's use of agents differs in three ways:

    1.  You can interact with the agents as they do work
    2.  They can interact with each other
    3.  You can start and stop agents as you like, rather than always use a broadcast/collect pattern.

    In general Claude Assistant gives you access to full agents, while SubAgents are somewhat limited.

??? question "What kinds of multi-agent workflows do you recommend?"

    This is green field.  We encourage you to play and find out.  Common patterns (reviewing, parallel research) are in this doc.
