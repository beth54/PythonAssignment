def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
 
    while repetitions > 0:
        outtext = text[-repetitions:]
        repetitions = repetitions - 1
        print(outtext)

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))