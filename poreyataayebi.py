import random

print("================================")
print("      بازی حدس اعداد")
print("================================")

while True:
    number = random.randint(1, 100)
    max_attempts = 5
    attempts = 0
    won = False

    print("\nیک عدد بین 1 تا 100 انتخاب کردم!")
    print("شما 5 فرصت برای حدس زدن دارید.")

    while attempts < max_attempts:
        try:
            guess = int(input("\nعدد مورد نظر را وارد کن: "))

            if guess < 1 or guess > 100:
                print("خطا! عدد باید بین 1 تا 100 باشد.")
                continue

        except ValueError:
            print("خطا! لطفاً فقط عدد صحیح وارد کن.")
            continue

        attempts += 1
        remaining = max_attempts - attempts

        print(f"\nتلاش {attempts} از {max_attempts}")
        print(f"جان باقی‌مانده: {remaining}")

        if guess == number:
            won = True
            print("\nآفرین! عدد را درست حدس زدی.")

            if attempts == 1:
                print("رتبه: نمونه‌ای!")
            elif attempts == 2:
                print("رتبه: بسیار خوبی!")
            elif attempts == 3:
                print("رتبه: خوب!")
            elif attempts == 4:
                print("رتبه: قبول!")
            else:
                print("رتبه: با شانس بردی!")

            break

        difference = abs(guess - number)

        if difference <= 5:
            print("خیلی نزدیکی!")
        elif difference <= 15:
            print("نزدیکی، ولی هنوز فاصله داری!")
        else:
            print("خیلی دوری!")

        if guess > number:
            print("عدد مخفی کوچک‌تر است.")
        else:
            print("عدد مخفی بزرگ‌تر است.")

    if not won:
        print("\nمتأسفانه باختی!")
        print(f"عدد مخفی برابر بود با: {number}")

    while True:
        again = input(
            "\nآیا می‌خواهی دوباره بازی کنی؟ (بله/خیر): "
        ).strip().lower()

        if again in ["بله", "بلی", "آره", "اره", "yes", "y"]:
            break
        elif again in ["خیر", "نه", "no", "n"]:
            print("\nممنون که بازی کردی! خداحافظ.")
            exit()
        else:
            print("لطفاً بله یا خیر وارد کن.")