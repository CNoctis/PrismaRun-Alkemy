def print_met(select: str):
    """Prints the selected transport method
    transport: means of transport
    select: selected option
    """
    print(select)


def select_met(transport: list) -> int:
    """Allows the user to select the method of transport
    return: selected option
    """
    print("Select a transportation option")
    for i in range(len(transport)):
        print(f"{i+1}. {transport[i]}")
    try:
        select = int(input("\nenter option\n"))
        try:
            # Verification of the range of the list
            assert (select <= len(transport) and select > 0)
        except AssertionError:
            print(f"""\nNegative number or outside the range of the list is not
            allowed ({len(transport)} options)""")
            select_met(transport)
        return transport[select-1]
    except ValueError:
        print("\nEntering characters is not allowed, only numbers")
        select_met(transport)


def main():
    medios_transporte = ['auto', 'avión', 'barco', 'bicicleta', 'ómnibus']
    select = select_met(medios_transporte)
    print_met(select)


if __name__ == '__main__':
    main()
