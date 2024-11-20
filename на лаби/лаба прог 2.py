#true ^
#false -
#ascending агремент
def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (arr[j] > arr[j + 1] and ascending) or (arr[j] < arr[j + 1] and not ascending):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    список = [34, 7, 23, 32, 5, 62]
    print("Оригінальний список:", список)

    відсортований_за_зростанням = bubble_sort(список.copy(), ascending=True)
    print("Список за зростанням:", відсортований_за_зростанням)

    відсортований_за_спаданням = bubble_sort(список.copy(), ascending=False)
    print("Список за спаданням:", відсортований_за_спаданням)
