class Solution(object):
   def defangIPaddr(self, address):
      address = address.split(".")
      return "[.]".join(address)
ob1 = Solution()
print(ob1.defangIPaddr("192.168.4.1"))
