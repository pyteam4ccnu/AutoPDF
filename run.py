from app import run_app
from mergePDF import run_merge
from view import run_view
import time

if __name__ == "__main__":
    t0 = time.time()
    run_view(run_app)
    print("Start merge PDF.")
    run_merge()
    print("\n --------\n -Cost: %.3fs\n --------" % (time.time() - t0))
