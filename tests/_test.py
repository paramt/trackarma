from src import collect_data
from src import generate_chart


def test():
    collect_data.main(False, "hypnotic-hippo")
    generate_chart.main()

    collect_data.main(False, "GallowBoob")
    generate_chart.main()
