# dnd_vendor

This script checks the stats of all items of interest that a vendor sells, then purchases the item if the stats are good. (Craftables)

The script checks a list of vendors for a list of items. Template matching is used to find the items.
The mouse moves to the coordinates where the item is located.
Image pre-processing and contour matching is used to find a region where item stats occur.
OCR is performed on image to extract stats.
Stats are used to create an object that will determine whether or not the item is worth purchasing.

** ITEM STATS ARE NO LONGER VISIBLE BEFORE PURCHASE RENDERING THIS USELESS **
