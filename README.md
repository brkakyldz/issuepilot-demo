# shelf

A tiny reading-list CLI: it keeps your books in `books.json` and lists them a page
at a time.

```bash
python -m shelf list            # page 1, ten books per page
python -m shelf list --page 2
python -m shelf list --per-page 5 --page 3
```

> **Demo repository.** `shelf` exists to show [IssuePilot](https://github.com/brkakyldz/IssuePilot)
> at work: new issues here are investigated by IssuePilot, which posts one comment with
> the likely cause, the code it points to and a suggested fix. The bugs in this
> repository are planted on purpose.
