#David Justice
#12-14-16
#crop graphic class

from graphic_field_item_class import *

class CropGraphicsPixmapItem(FieldItemGraphicsPixmapItem):
    """this class provides a pixmap item with a preset image for the crop"""

    #constructor
    def __init__(self, graphics_list):
        super().__init__(graphics_list)

        self.crop = None

    def update_status(self):
        if self.crop._status == "Seed":
            self.setPixmap(QPixmap(self.available_graphics[0]).scaledToWidth(50,1))
        elif self.crop._status == "Seedling":
            self.setPixmap(QPixmap(self.available_graphics[1]).scaledToWidth(50,1))
        elif self.crop._status == "Young":
            self.setPixmap(QPixmap(self.available_graphics[2]).scaledToWidth(50,1))
        elif self.crop._status == "Mature":
            self.setPixmap(QPixmap(self.available_graphics[3]).scaledToWidth(50,1))
        elif self.crop._status == "Old":
            self.setPixmap(QPixmap(self.available_graphics[4]).scaledToWidth(50,1))
            
