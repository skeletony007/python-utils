## > To find your equivalent DPI in your new resolution you need to divide the new resolution with the old resolution for eg:- 1440/1080=1.33 and multiply it with your old DPI 1.33*800=1064. 1064dpi in 1440p will be equivalent to 800dpi in 1080p.
## 
## <https://dorkyclicks.com/guide-to-mouse-dpi-for-1080p1440p-and-4k-etc/>

#def find_equivelant_dpi(new_res, old_res, old_dpi):
#  new_dpi = (new_res / old_res) * old_dpi
#  return new_dpi
#
#find_equivelant_dpi(1440, 1080, 800)

## refining this:

class computer:
  def __init__(self,new_res,new_dpi):
    self.res=new_res
    self.dpi=new_dpi
  def round_num(self,num,sf):
    num=str(num)
    if(num[sf]=="."):
      
  def scale_dpi(self,new_res,old_res,old_dpi):
      monitor_distance_coefficient=self.round_num(100*(new_res/old_res))/100
      new_dpi=monitor_distance_coefficient*old_dpi
      return new_dpi
  def set_res(self,new_res):
    self.dpi=self.scale_dpi(new_res,self.res,self.dpi)
    self.res=new_res
  def set_dpi(self,new_dpi):
    self.dpi=new_dpi
  def get_res(self):
    return self.res
  def get_dpi(self):
    return self.dpi

## example
my_computer=computer(1080,800)
my_computer.set_res(1440)
my_computer.get_dpi()
my_computer.set_res(720)
my_computer.set_res(1080)
my_computer.get_dpi()

