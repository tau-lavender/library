from src.simulation import run_simulation


def main() -> None:
    """
    Заппрашивает seed и steps. Запускает симуляцию
    :return: None
    """
    seed = input("Введите seed (ENTER для случайного): ")
    steps = int(input("Введите кол-во шагов (ENTER для 20): "))
    run_simulation(steps=steps, seed=seed)


if __name__ == "__main__":
    main()
