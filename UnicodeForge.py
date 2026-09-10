import random
import unicodedata
from pathlib import Path


# ============================================================
# Unicode Pattern Generator
# ============================================================

# حروف Unicode مشابه نمونه‌ی اصلی
CHARS = "𝙟𝙚𝙙𝙧𝙣𝙨𝙞𝙎"


def normalize_text(text: str) -> str:
    """
    تبدیل حروف Unicode فانتزی به حروف معمولی در صورت امکان.
    """
    return unicodedata.normalize("NFKC", text)


def generate_random(length: int) -> str:
    """
    ساخت رشته کاملاً تصادفی.
    """
    return "".join(random.choice(CHARS) for _ in range(length))


def generate_pattern(pattern: str, repeat: int) -> str:
    """
    تکرار یک الگوی مشخص.
    """
    return pattern * repeat


def generate_pattern_with_variation(
    pattern: str,
    repeat: int,
    variation: float = 0.15
) -> str:
    """
    الگوی اصلی را چند بار تکرار می‌کند،
    اما درصد کمی از کاراکترها را تغییر می‌دهد.

    variation:
        0.0  = بدون تغییر
        0.15 = حدود 15 درصد تغییر
        1.0  = کاملاً متغیر
    """

    result = []

    for _ in range(repeat):

        for char in pattern:

            if random.random() < variation:
                result.append(random.choice(CHARS))
            else:
                result.append(char)

    return "".join(result)


def save_to_file(text: str, filename: str = "generated.txt"):
    """
    ذخیره خروجی در فایل.
    """

    path = Path(filename)

    path.write_text(
        text,
        encoding="utf-8"
    )

    print(f"\n[+] فایل ذخیره شد: {path.absolute()}")


def show_stats(text: str):
    """
    نمایش اطلاعات رشته.
    """

    print("\n" + "=" * 50)
    print("STATS")
    print("=" * 50)

    print(f"Unicode characters : {len(text)}")
    print(f"Unique characters  : {len(set(text))}")

    print("\nCharacter frequency:")

    counter = {}

    for char in text:
        counter[char] = counter.get(char, 0) + 1

    for char, count in sorted(
        counter.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        print(f"{char} : {count}")


def menu():
    """
    منوی اصلی برنامه.
    """

    while True:

        print("\n")
        print("=" * 60)
        print("        Unicode Pattern Generator")
        print("=" * 60)

        print("""
1. ساخت رشته تصادفی
2. تکرار یک Pattern
3. Pattern + تغییرات تصادفی
4. نمایش حروف استفاده‌شده
5. خروج
""")

        choice = input("انتخاب: ").strip()

        # ----------------------------------------------------
        # Random
        # ----------------------------------------------------

        if choice == "1":

            try:
                length = int(
                    input("طول رشته: ")
                )

                if length <= 0:
                    print("طول باید بیشتر از صفر باشد.")
                    continue

                result = generate_random(length)

                print("\nOUTPUT:")
                print(result)

                show_stats(result)

                save = input(
                    "\nذخیره در فایل؟ (y/n): "
                ).lower()

                if save == "y":
                    filename = input(
                        "نام فایل [generated.txt]: "
                    ).strip()

                    if not filename:
                        filename = "generated.txt"

                    save_to_file(result, filename)

            except ValueError:
                print("عدد معتبر وارد کن.")

        # ----------------------------------------------------
        # Pattern
        # ----------------------------------------------------

        elif choice == "2":

            pattern = input(
                "\nPattern را وارد کن: "
            )

            if not pattern:
                print("Pattern خالی است.")
                continue

            try:
                repeat = int(
                    input("تعداد تکرار: ")
                )

                if repeat <= 0:
                    print("تعداد تکرار باید بیشتر از صفر باشد.")
                    continue

                result = generate_pattern(
                    pattern,
                    repeat
                )

                print("\nOUTPUT:")
                print(result)

                show_stats(result)

                save = input(
                    "\nذخیره در فایل؟ (y/n): "
                ).lower()

                if save == "y":
                    filename = input(
                        "نام فایل [generated.txt]: "
                    ).strip()

                    if not filename:
                        filename = "generated.txt"

                    save_to_file(result, filename)

            except ValueError:
                print("عدد معتبر وارد کن.")

        # ----------------------------------------------------
        # Pattern Variation
        # ----------------------------------------------------

        elif choice == "3":

            pattern = input(
                "\nPattern را وارد کن: "
            )

            if not pattern:
                print("Pattern خالی است.")
                continue

            try:

                repeat = int(
                    input("تعداد تکرار: ")
                )

                variation = float(
                    input(
                        "میزان تغییر (0 تا 1) [0.15]: "
                    ) or "0.15"
                )

                if repeat <= 0:
                    print("تعداد تکرار نامعتبر است.")
                    continue

                if not 0 <= variation <= 1:
                    print(
                        "مقدار variation باید بین 0 و 1 باشد."
                    )
                    continue

                result = generate_pattern_with_variation(
                    pattern,
                    repeat,
                    variation
                )

                print("\nOUTPUT:")
                print(result)

                show_stats(result)

                save = input(
                    "\nذخیره در فایل؟ (y/n): "
                ).lower()

                if save == "y":

                    filename = input(
                        "نام فایل [generated.txt]: "
                    ).strip()

                    if not filename:
                        filename = "generated.txt"

                    save_to_file(
                        result,
                        filename
                    )

            except ValueError:
                print("مقدار نامعتبر.")

        # ----------------------------------------------------
        # Characters
        # ----------------------------------------------------

        elif choice == "4":

            print("\nCharacters:")
            print(CHARS)

            print("\nNormal form:")

            for char in CHARS:
                print(
                    f"{char} -> "
                    f"{normalize_text(char)}"
                )

        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------

        elif choice == "5":

            print("\nBye!")
            break

        else:

            print("گزینه نامعتبر است.")


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    menu()
