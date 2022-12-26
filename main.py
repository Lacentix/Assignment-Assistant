from gets import get_name, get_id
from checkers import check_name, check_id

first_name, last_name = get_name()
check_name(first_name)
check_name(last_name)

user_id = get_id()
check_id(user_id)
