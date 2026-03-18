def main():
    # --- Personalized values based on my ID ---
    d1 = 7  # last digit of 6309037
    d2 = 3  # second-last digit of 6309037

    k = (d1 + d2) % 4 + 2
    shift = d1 - d2
    rows_keep = (d1 % 2) + 2

    print("\n--- Personal Values ---")
    print("d1 =", d1)
    print("d2 =", d2)
    print("k =", k)
    print("shift =", shift)
    print("rows_keep =", rows_keep)

    # --- Component A: Collect readings ---
    n = int(input("\nHow many readings will you enter? "))
    readings = []

    for i in range(n):
        value = float(input(f"Enter reading {i+1}: "))
        readings.append(value)

    print("\n--- Original List ---")
    print("Full list:", readings)

    if len(readings) > 0:
        print("First reading:", readings[0])
        print("Last reading:", readings[-1])
    else:
        print("The list is empty.")

    if len(readings) >= 4:
        print("Slice from index 1 to index 3:", readings[1:4])
    else:
        print("Slice [1:4] not available (list too short)")

    print("Sum of readings:", sum(readings))

    # --- Component B: ID-based modifications ---
    shifted_list = [x + shift for x in readings]
    multiplied_list = [x * k for x in readings]
    elementwise_sum = [a + b for a, b in zip(readings, shifted_list)]

    print("\n--- Modified Lists ---")
    print("Shifted list (+shift):", shifted_list)
    print("Multiplied list (*k):", multiplied_list)
    print("Element-wise sum (original + shifted):", elementwise_sum)
if __name__ == "__main__":
    main()