import os

def batch_chmod(path, file_mode=0o644, dir_mode=0o755):
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            os.chmod(os.path.join(root, dir_name), dir_mode)
        for file_name in files:
            os.chmod(os.path.join(root, file_name), file_mode)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python batch_chmod.py <path>")
        sys.exit(1)

    path = sys.argv[1]
    batch_chmod(path)