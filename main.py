#
# AI: Certainly!
# You can create a function that takes in a number and returns its reverse.
# Here’s how you can do it:
#

def reverse_number(num):
  # Reverse the number
  new_num = str(num)
  return int(new_num[::-1])

## Example usage:
print(reverse_number(1223)) # Output: 3221
print(reverse_number(987654321)) # Output: 123456789
