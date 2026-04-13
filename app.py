from src.cli import args
from src.services import do_the_heavy_lifting


def main():
    file_path = args.instruction_set
    heavy_lifter_version = args.heavy_lifter
    # If error occurs I let the user see the Exception traceback
    output = do_the_heavy_lifting(file_path, heavy_lifter_version)
    # Logging can be used as well
    print(output)
    

if __name__ == '__main__':
    main()
