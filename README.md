# J.A.R.V.I.S for Windows

Same Flutter J.A.R.V.I.S app as Android — **Windows desktop EXE** via GitHub Actions.

## Build

1. New GitHub repo → upload these files to the **root**.
2. Push `main` → **Actions → Build Windows EXE**.
3. Download artifact **`jarvis-windows`** → unzip.

## Run

Unzip and run **`jarvis_assistant.exe`** (name may match project).

**Keep the whole folder together** (exe + `.dll` files). The exe alone will not start.

## Same features

- OpenAI / Grok / Claude
- Voice (mic permission on Windows)
- Local code workspace on disk
- GitHub tools, Discord **bot**, txAdmin, Pterodactyl, MySQL mind
- HUD UI

## Not identical to Android (OS limits)

| Feature | Windows |
|--------|---------|
| Discord **notification** auto-reply | No (use Discord bot) |
| Android notification access | No |
| Always-on FGS like phone | Limited |

## Layout

```
lib/main.dart
pubspec.yaml
tool/patch_windows.py
.github/workflows/build.yml
```
