#!/usr/bin/env python3
"""Minor Windows runner tweaks after flutter create."""
from pathlib import Path
import re

ROOT = Path("windows/runner")
MAIN_CPP = ROOT / "main.cpp"
RC = ROOT / "Runner.rc"

def main() -> None:
    if MAIN_CPP.exists():
        t = MAIN_CPP.read_text(encoding="utf-8", errors="ignore")
        t2 = t.replace("jarvis_assistant", "J.A.R.V.I.S")
        # window title string often L"jarvis_assistant"
        t2 = re.sub(r'L"[^"]*jarvis[^"]*"', 'L"J.A.R.V.I.S"', t2, flags=re.I)
        if t2 != t:
            MAIN_CPP.write_text(t2, encoding="utf-8")
            print("Patched main.cpp title")
        else:
            print("main.cpp: no title change needed or pattern differs")
    else:
        print("main.cpp missing (ok if create failed)")

    if RC.exists():
        t = RC.read_text(encoding="utf-8", errors="ignore")
        t2 = re.sub(
            r'(VALUE "FileDescription",\s*)"[^"]*"',
            r'\1"J.A.R.V.I.S Assistant"',
            t,
        )
        t2 = re.sub(
            r'(VALUE "ProductName",\s*)"[^"]*"',
            r'\1"J.A.R.V.I.S"',
            t2,
        )
        if t2 != t:
            RC.write_text(t2, encoding="utf-8")
            print("Patched Runner.rc")
    print("patch_windows.py done")

if __name__ == "__main__":
    main()
