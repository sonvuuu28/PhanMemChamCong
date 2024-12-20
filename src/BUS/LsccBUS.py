import os
import sys

# Assuming you're in the 'BUS' folder, make sure to import from the correct path
current_dir = os.path.dirname(os.path.abspath(__file__))
dto_dir = os.path.join(current_dir, '../DTO')
sys.path.append(dto_dir)
from LsccDTO import LsccDTO  # Make sure LsccDTO is imported here
current_dir = os.path.dirname(os.path.abspath(__file__))
dao_dir = os.path.join(current_dir, '../DAO')
sys.path.append(dao_dir)
from LsccDAO import LsccDAO  # Make sure LsccDTO is imported here

class LsccBUS:
    def __init__(self):
        pass
    
    @staticmethod
    def getInstance():
        return LsccBUS()
    
    def getall(self):
        ls_dao = LsccDAO.getInstance()
        data = ls_dao.get_all()  # Assuming get_all() fetches data correctly
        return None if len(data) == 0 else data

    def update_shift(self, dataUpdate):
        ls_dao = LsccDAO.getInstance()
        # Assuming you have the update method in LsccDAO
        result = ls_dao.update(dataUpdate)
        return result
    def getbydate(self, date):
        ls_dao = LsccDAO.getInstance()
        # Assuming you have the update method in LsccDAO
        result = ls_dao.get_by_date(date)
        return result
