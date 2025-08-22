try:
    import tkinter as tk
    from tkinter import messagebox
    TK_AVAILABLE = True
except Exception:
    TK_AVAILABLE = False
    tk = None
    messagebox = None

_root = None

def _get_root():
    global _root
    if not TK_AVAILABLE:
        return None
    if _root is None:
        _root = tk.Tk()
        _root.withdraw()
    return _root

def show_info(titolo: str, messaggio: str):
    if TK_AVAILABLE:
        root = _get_root()
        messagebox.showinfo(titolo, messaggio, parent=root)
    else:
        print(f"[{titolo}] {messaggio}")

def show_error(titolo: str, messaggio: str):
    if TK_AVAILABLE:
        root = _get_root()
        messagebox.showerror(titolo, messaggio, parent=root)
    else:
        print(f"[{titolo}] {messaggio}")

def show_warning(titolo: str, messaggio: str):
    if TK_AVAILABLE:
        root = _get_root()
        messagebox.showwarning(titolo, messaggio, parent=root)
    else:
        print(f"[{titolo}] {messaggio}")