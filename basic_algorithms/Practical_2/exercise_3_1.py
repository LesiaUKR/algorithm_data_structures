from pathlib import Path
import argparse
import shutil

def parse_args():
    parser = argparse.ArgumentParser(description="Копіювання файлів з сортуванням за розширеннями.")
    parser.add_argument("--source", type=Path, required=True, help="Шлях до вихідної директорії")
    parser.add_argument("--dest", type=Path, default=Path("dist"), help="Шлях до директорії призначення")
    return parser.parse_args()

# source/
#     test/
#         test.txt
#     a.py


# dist/
#     txt/
#         test.txt
#     py/
#         a.py

# dist/txt/

def copy_files(src, dst):
    try:
        for item in src.iterdir():
            print(item)
            if item.is_dir():
                # Рекурсивний виклик для піддиректорії
            else:
                # Копіювання файлу
    except Exception as e:
        print(f"Помилка при копіюванні файлів: {e}")

def main():
    args = parse_args()
    print(args.source, args.dest)
    args.dest.mkdir(parents=True, exist_ok=True)  # Створюємо директорію призначення, якщо вона не існує
    copy_files(args.source, args.dest)


if __name__ == "__main__":
    main()