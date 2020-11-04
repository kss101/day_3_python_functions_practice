def return_10():
    return 10

def add( num1, num2 ):
    return num1 + num2

def subtract( num1, num2 ):
    return num1 - num2

def multiply( num1, num2 ):
    return num1 * num2

def divide( num1, num2 ):
    return num1 / num2

def length_of_string( test_string ):
    return len(test_string)

def join_string( string_1, string_2 ):
    return string_1 + string_2

def add_string_as_number( string_1, string_2 ):
    return int(string_1) + int(string_2)

def number_to_full_month_name( month_num ):
	import datetime
	get_month_name = datetime.datetime(2020, month_num, 1)
	return(get_month_name.strftime("%B"))

def number_to_short_month_name( month_num ):
    import datetime
    get_month_short_name = datetime.datetime(2020, month_num, 1)
    return(get_month_short_name.strftime("%b"))

