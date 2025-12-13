from src.simulation import run_simulation


def main() -> None:
    seed = input("Введите seed (ENTER для случайного): ")
    run_simulation(seed=seed)


if __name__ == "__main__":
    main()
