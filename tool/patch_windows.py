#!/usr/bin/env python3
from pathlib import Path
import re

def patch_cmake() -> None:
    for path in Path("windows").rglob("CMakeLists.txt"):
        t = path.read_text(encoding="utf-8", errors="ignore")
        if "_SILENCE_EXPERIMENTAL_COROUTINE" in t:
            continue
        # Add definition near top after cmake_minimum_required if present
        add = """
# Silence MSVC experimental coroutine deprecation (older Flutter plugins)
add_compile_definitions(_SILENCE_EXPERIMENTAL_COROUTINE_DEPRECATION_WARNINGS)
"""
        if "cmake_minimum_required" in t:
            t = re.sub(
                r"(cmake_minimum_required\([^\)]*\))",
                r"\1\n" + add,
                t,
                count=1,
            )
        else:
            t = add + t
        path.write_text(t, encoding="utf-8")
        print(f"Patched CMake: {path}")

def patch_runner() -> None:
    main_cpp = Path("windows/runner/main.cpp")
    if main_cpp.exists():
        t = main_cpp.read_text(encoding="utf-8", errors="ignore")
        t2 = re.sub(r'L"[^"]*jarvis[^"]*"', 'L"J.A.R.V.I.S"', t, flags=re.I)
        t2 = t2.replace("jarvis_assistant", "J.A.R.V.I.S")
        if t2 != t:
            main_cpp.write_text(t2, encoding="utf-8")
            print("Patched main.cpp")

def main() -> None:
    patch_cmake()
    patch_runner()
    print("patch_windows.py done")

if __name__ == "__main__":
    main()
