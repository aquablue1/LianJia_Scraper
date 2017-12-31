"""
" Contains some useful informations for house class and its successors.
" Contains Three main types of info: BasicInfo, TradeInfo, OtherInfo.
" Defined by Zhengping on 2017/12/30
"""

class BasicInfo:
    """
    " Basic information for a house
    """
    def __init__(self, house_type, house_overallArea, house_insideArea, house_direction, is_elevator, house_level,
                 house_structure, construct_type, construct_structure, elevator_average, property_year ):
        self.house_type = house_type               # 房屋户型

        self.house_overallArea = house_overallArea # 建筑总面积

        self.house_insideArea = house_insideArea   # 套内面积

        self.house_direction = house_direction     # 房屋朝向

        self.declaration = house_direction         # 装修情况

        self.is_elevator =  is_elevator            # 配备电梯?

        self.house_level =  house_level            # 所在楼层

        self.house_structure = house_structure     # 户型结构（平层/

        self.construct_type = construct_type       # 建筑类型

        self.construct_structure = construct_structure # 建筑结构

        self.elevator_average = elevator_average   # 梯户比例

        self.property_year = property_year         # 产权年限



class TradeInfo:
    """
    " Trade information for a house
    """