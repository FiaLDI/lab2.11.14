#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def search_area(type = 0):
    '''
    Функция вычисления плозади.
    '''
    def triangle(a, h):
        '''
        Функция вычисления площади треугольника.
        '''
        return 1 / 2 * a * h

    def rectangle(a, b):
        '''
        Функция вычисления площади прямоугольника.
        '''
        return a * b
    
    if type == 0:
        return triangle
    else:
        return rectangle


def main():
    '''
    Главная функция программы.
    '''
    print(search_area(0)(1, 2))
    print(search_area(1)(1, 2))


if __name__ == "__main__":
    main()