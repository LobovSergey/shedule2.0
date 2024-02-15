from lgc.logic.prcs import process
from lgc.source.wrap import check_time


@check_time
def main():
    process()


if __name__ == "__main__":
    main()
