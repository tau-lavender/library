from src.simulation import run_simulation


def main() -> None:
    """
    Заппрашивает seed и steps. Запускает симуляцию
    :return: None
    """
    seed = input("Введите seed (ENTER для случайного): ")
    str_steps:str = input("Введите кол-во шагов (ENTER для 20): ")
    if str_steps == "":
        steps = 20
    else:
        steps = int(str_steps)
    run_simulation(steps=steps, seed=seed)


if __name__ == "__main__":
    main()
