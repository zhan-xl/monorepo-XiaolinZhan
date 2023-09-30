# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item], *, Max_Quality=50, Min_Quality = 0):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
        # Adding keyword attributes for min, max quality and legendary quality.
        self._Max_Quality = Max_Quality
        self._Min_Quality = Min_Quality

    def update_quality(self):
        for item in self.items:
            if "Aged Brie" in item.name:
                self.update_aged_brie(item)
            elif "Sulfuras" in item.name:
                self.update_sulfuras(item)
            elif "Backstage passes" in item.name:
                self.update_backstage_passes(item)
            elif "Conjured" in item.name:
                self.update_conjured(item)
            else:
                self.update_default(item)

# update general items
    def update_default(self, item):
        item.sell_in -= 1
        if item.quality >= self._Max_Quality:
            return
        else:
            item.quality -= 1
    
    def update_aged_brie(self, item):
        item.sell_in -= 1
        if item.quality >= self._Max_Quality:
            return
        if item.sell_in < 0:
            item.quality += 2
        else :
            item.quality += 1
            item

    def update_sulfuras(self, item):
        pass

    def update_backstage_passes(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
            return
        
        if 10 >= item.sell_in > 5:
            item.quality += 2
        elif 5 >= item.sell_in > 0:
            item.quality = item.quality + 3
        elif item.sell_in <= 0:
            item.quality = 0
        else:
            item.quality = item.quality + 1

        item.quality = min(item.quality, self._Max_Quality)

    def update_conjured(self, item):
        item.sell_in -= 1
        item.quality = max(item.quality - 2, self._Min_Quality)