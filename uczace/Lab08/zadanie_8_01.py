import numpy
import random
from PIL import Image


def png_read(filepath):
    img = Image.open(filepath)
    assert len(img.size) == 2  # skala szarosci, nie RGB
    return (numpy.array(img) / 255).reshape(img.size[1], img.size[0])


def png_write(img, filepath):
    img = Image.fromarray((numpy.array(img) * 255).astype(numpy.int8), "L")
    img.save(filepath)


def print_min_max(A):
    print("MIN:", numpy.min(A))
    print("MAX", numpy.max(A))


def rozjasnianie(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i, j] += random.uniform(-1.0, 1.0)

            if A[i, j] < -1.0:
                A[i, j] = -1.0
            elif A[i, j] > 1.0:
                A[i, j] = 1.0
    png_write(A, "output_rozjasnianie.png")


def negatyw(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i, j] = 1.0 - A[i, j]

    png_write(A, "output_negatyw.png")


def konwersja(A):
    p = random.uniform(0.0, 1.0)

    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i, j] = 1.0 if A[i, j] > p else 0.0

    png_write(A, "output_konwersja.png")


def rozciaganie_kontrastu(A):
    theta = random.uniform(1.0, 100.0)
    f = lambda x: 1 / (1 + numpy.e ** (-theta * (x - 0.5)))

    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i, j] = f(A[i, j])

    png_write(A, "output_rozciaganie.png")


def convolution(A, B, k):
    C = numpy.zeros(A.shape)
    k = (B.shape[0] - 1) // 2

    for i in range(C.shape[0]):
        for j in range(C.shape[1]):

            C[i, j] = sum(
                [
                    sum(
                        [
                            A[i + u, j + v] * B[u + k + 1, v + k + 1]
                            if i + u < A.shape[0] and j + v < A.shape[1]
                            else 0.0
                            for v in range(-k, k)
                        ]
                    )
                    for u in range(-k, k)
                ]
            )

    png_write(C, f"output_convolution_{k}.png")


def generate_kernel(k):
    return numpy.full((k, k), 1 / k**2)


def main():
    A = png_read("skimage_astronaut.png")
    print_min_max(A)

    rozjasnianie(A.copy())
    negatyw(A.copy())
    konwersja(A.copy())
    rozciaganie_kontrastu(A.copy())

    for k in [3, 5, 15]:
        B = generate_kernel(k)
        convolution(A.copy(), B, k)


if __name__ == "__main__":
    main()
