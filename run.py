import os
from src import cok as yy

if __name__ == "__main__":
    os.system("git pull");os.system("rm -rf results/OK/...");os.system("rm -rf results/CP/...")
    yy.cek_server()
