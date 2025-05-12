import Lab2


def test_find_min_max():
    expected_result=(1.0, 12.0)
    testlist = [2.0, 3.0, 4.0, 1.0, 12.0, 5.0]
    test_result = Lab2.find_min_max(testlist)
    assert(test_result == expected_result)



def test_calc_average():
    expected_result=4.5
    testlist = [2.0, 3.0, 4.0, 1.0, 12.0, 5.0]
    test_result = Lab2.calc_average(testlist)
    assert(test_result == expected_result)    


def test_calc_median_temperature():
    expected_result=3.5
    testlist = [2.0, 3.0, 4.0, 1.0, 12.0, 5.0]
    test_result = Lab2.calc_median_temperature(testlist)
    assert(test_result == expected_result)    

