from app import run_app
from mergePDF import run_merge

if __name__ == "__main__":
    run_app()
    print("Start merge PDF.")
    run_merge()
