# -*- coding: utf-8 -*-
from typing import Tuple, List


class Pixel:

    def __init__(self, color: Tuple[int, int, int]):
        self.color = color

    def __str__(self):
        return f'{self.color}'


class Picture:

    def __init__(self, pixels: List[List[Pixel]]):
        self.pixels = pixels

    def __add__(self, other):
        if not isinstance(other, Picture):
            raise TypeError('Error')
        picxe_l = self.pixels[0][0].color
        result = []
        for i in range(len(picxe_l)):
            if picxe_l[i] >= 0 and picxe_l[i] <= 255:
                sum_a = picxe_l[i] + other.pixels[0][0].color[i]
                if sum_a >= 255:
                    result.append(255)
                elif sum_a <= 0:
                    result.append(0)
                else:
                    result.append(sum_a)

        new_pixel = Pixel((result[0], result[1], result[2]))
        new_pixels = [[new_pixel]]
        return self.__class__(new_pixels)


    def __sub__(self, other):
        if not isinstance(other, Picture):
            raise TypeError('Error')
        picxe_l = self.pixels[0][0].color
        result = []
        for i in range(len(picxe_l)):
            if picxe_l[i] >= 0 and picxe_l[i] <= 255:
                sum_a = picxe_l[i] - other.pixels[0][0].color[i]
                if sum_a >= 255:
                    result.append(255)
                elif sum_a <= 0:
                    result.append(0)
                else:
                    result.append(sum_a)

        new_pixel = Pixel((result[0], result[1], result[2]))
        new_pixels = [[new_pixel]]
        return self.__class__(new_pixels)



if __name__ == '__main__':
    pxls = [
        [Pixel((0, 25, 255))]
    ]

    # assert Picture(pxls) + Picture(pxls) == Picture([[Pixel((0, 50, 255))]])
    # assert Picture(pxls) - Picture(pxls) == Picture([[Pixel((0, 0, 0))]])

    # print(type(Picture(pxls)))
    print(Picture(pxls) + Picture(pxls))
