# Copyright (C) 2024 Spandan Barve
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pygame


def scale_image_maintain_ratio(img, w=None, h=None):
    o_w, o_h = img.get_size()
    m_w, m_h = o_w, o_h

    if w is not None and h is None:
        m_h = w * (o_h / o_w)
        return pygame.transform.scale(img, (int(w), int(m_h)))

    if h is not None and w is None:
        m_w = h * (o_w / o_h)
        return pygame.transform.scale(img, (int(m_w), int(h)))

    if w is None and h is None:
        return img


def array_has_no_none(arr):
    return all(element is not None for element in arr)


def compare_arrays_unordered(*arrays):
    sets = [set(arr) for arr in arrays]
    return all(s == sets[0] for s in sets)


def rotate_by_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(center=(x, y)).center)
    return rotated_image, new_rect
