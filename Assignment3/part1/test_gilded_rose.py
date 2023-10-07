# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_default_item(self):
        item = Item("Chair", 5, 10)
        items = [item]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEquals(4, item.sell_in)
        self.assertEquals(9, item.quality)

    def test_aged_brie(self):
        item = Item("Aged Brie something", 5, 10)
        items = [item]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEquals(4, item.sell_in)
        self.assertEquals(11, item.quality)

    def test_sulfuras(self):
        item = Item("Sulfuras", 5, 80)
        items = [item]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEquals(5, item.sell_in)
        self.assertEquals(80, item.quality)

    def test_backstage_passes(self):
        item = Item("Backstage passes something", 9, 10)
        items = [item]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEquals(8, item.sell_in)
        self.assertEquals(12, item.quality)

    def test_conjured(self):
        item = Item("Conjured something", 9, 10)
        items = [item]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEquals(8, item.sell_in)
        self.assertEquals(8, item.quality)


if __name__ == "__main__":
    unittest.main()
