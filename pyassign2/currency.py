"""currency.py:
Module for currency exchange
This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
__author__ = 'Friedrich Foo'
__pkuid__ = '1800011746'
__email__ = '1800011746@pku.edu.cn'
"""

# Part A: Breaking Up Strings
def before_space(s):
    """Returns: Substring of s; up to, but not including, the first space"""
    m = s.partition(' ')
    num = m[0]
    return num

def test_before_space():
    # Test case 1
    result = before_space("hello patty")
    assert ("hello" == result)
    # Test case 2
    result = before_space(" hello patty")
    assert ("" == result)    

# Part B: Processing a JSON String
def get_to(json):
    """The TO value in the response to a currency query."""
    m = json.split('"')
    nxtcur = m[7]
    return nxtcur

def test_get_to():
    # Test case 1
    assert  (get_to('"from" : "2.5 United States Dollars", "to" \
                    : "2.24075 Euros", "success" : true, "error" : "" ')
             == '2.24075 Euros')
    # Test case 2
    assert (get_to('"from":"","to":"","success":false,"error"\
                   :"Source currency code is invalid."') == '')
    
def has_noerror(json):
    """True if the query has no error; False otherwise."""
    replaceuno = json.replace('false','False')
    replacedos = replaceuno.replace('true','True')
    dic = eval(replacedos)
    if dic["success"] == True:
        return True
    else:
        return False

def test_has_noerror():
    # Test case 1
    result = has_noerror('{"from" : "2.5 United States Dollars", "to" : \
                         "2.24075 Euros", "success" : true, "error" : "" }')
    assert  (result == True)
    # Test case 2
    result = has_noerror('{"from":"","to":"","success":false,"error":\
                        "Source currency code is invalid."}')
    assert (result == False)

def isfloat(s):
    """True if string s can be transformed into class float"""
    try:
        x = float(s)
    except TypeError:
        return False
    except ValueError:
        return False
    except Exception as e:
        return False
    else:
        return True  
    
def test_isfloat():
    # Test case 1
    assert (isfloat("1.4") == True)
    # Test case 2
    assert (isfloat("2") == True)
    # Test case 3
    assert (isfloat("string") == False)
    # Test case 4
    assert (isfloat("5 strings") == False)
    
# Part C: Currency Query
def currency_response(currency_from, currency_to, amount_from):
    """Returns: a JSON string that is a response to a currency query."""
    from urllib.request import urlopen
    stramt = str(amount_from)
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='
                  +currency_from+'&to='+currency_to+'&amt='+stramt)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr

def test_currency_response():
    # Test case 1
    result1 = ('{ "from" : "2.5 United States Dollars", "to" : \
"2.1589225 Euros", "success" : true, "error" : "" }')
    assert (currency_response("USD","EUR",2.5) == result1)
    # Test case 2
    result2 = '{ "from" : "", "to" : "", "success" : false, "er\
ror" : "Source currency code is invalid." }'
    assert (currency_response("USA","EUR",2.5) == result2)
    # Test case 3
    result3 = '{ "from" : "1.6 Venezuelan Bol\\u00edvares Fuertes", \
"to" : "0.00020905107719705 Uruguayan Pesos", "success" : true, "error" : "" }'
    assert (currency_response("VEF","UYU",1.6) == result3)
    # Test case 4
    result4 = '{ "from" : "1.6 Iranian Rials", "to" : \
"0.0040597211275802 Icelandic Kr\\u00f3nur", "success" : true, "error" : "" }'
    assert (currency_response("IRR","ISK",1.6) == result4)
    
# Part D: Currency Exchange
def iscurrency(currency):
    """True if currency is a valid (3 letter code for a) currency. """
    strout = currency_response("USD", currency, 1)
    boolnum = has_noerror(strout)
    return boolnum

def test_iscurrency():
    # Test case 1
    assert (iscurrency("HKD") == True)
    # Test case 2
    assert (iscurrency("IDKK") == False)
    # Test case 3
    assert (iscurrency("TND") == True)
    # Test case 4
    assert (iscurrency("III") == False)
    
def exchange(currency_from,currency_to,amount_from):
    """Returns: amount of currency received in the given exchange."""
    strfin = currency_response(currency_from,currency_to,amount_from)
    nxtcur = get_to(strfin)        
    finalamt1 = before_space(nxtcur)
    finalamt = float(finalamt1)
    return finalamt

def test_exchange():
    # Test case 1
    assert (exchange("USD","HKD",8.0) == 62.798)
    # Test case 2
    assert (exchange("USD","CNY",2.5) == 17.13025)
    # Test case 3
    assert (exchange("CNY","THB",3.3) == 15.798333051181)
    # Test case 4
    assert (exchange("EUR","GEL",1.5) == 4.3144647387759)

# Part Extra: Testing All functions mentioned above
def testALL():
    test_get_to()
    test_has_noerror()
    test_isfloat()
    test_currency_response()
    test_iscurrency()
    test_exchange()
    print("All tests passed")     
        
# Main process
def main():
    currency_from = input("type down currency you want to exchange from: ")
    currency_to = input("type down currency you want to exchange to: ")
    amount_from = input("type down amount of money you want to exchange: ")
    if iscurrency(currency_from) == False or iscurrency(currency_to) == False:
        print("invalid currency type")
    elif isfloat(amount_from) == False:
        print("invalid amount type")
    else:
        testALL()
        stramt = str(exchange(currency_from, currency_to, amount_from))
        print("amount of money exchanged to is: "+stramt)

if __name__ == "__main__":
    main()
